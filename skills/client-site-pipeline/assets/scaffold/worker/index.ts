// API Worker (Cloudflare "static + API Worker" mode). Pages are static assets;
// this runs only for /api/* (`assets.run_worker_first` in wrangler.jsonc).
//
//   POST /api/inquiries  request form -> D1 `inquiries`, then email via Resend
//                                        when RESEND_API_KEY + LEAD_NOTIFY_EMAIL
//                                        are set as Worker secrets
//   POST /api/subscribe  email list   -> D1 `subscribers` (upsert on email)
//
// Every request is stored first, so nothing is lost before the inbox is wired.
// The request form is designed per client: `name`, `email`, `phone`, `message`,
// `locale` and `source` are columns, and every other field the form sends is
// kept together as JSON in `fields`.
import schema from "../migrations/0001_init.sql";

interface Env {
  DB: D1Database;
  ASSETS: Fetcher;
  BRAND_NAME?: string;
  RESEND_API_KEY?: string;
  LEAD_NOTIFY_EMAIL?: string;
  RESEND_FROM_EMAIL?: string;
}

const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });

const clip = (v: File | string | null, max: number) => String(v ?? "").trim().slice(0, max);
const isEmail = (v: string) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
const isPhone = (v: string) => v.replace(/\D/g, "").length >= 7;

const statements = (sql: string) =>
  String(sql)
    .split(";")
    .map((s) => s.replace(/--.*$/gm, "").trim())
    .filter(Boolean);

let schemaReady: Promise<unknown> | null = null;
function ensureSchema(db: D1Database) {
  schemaReady ??= db.batch(statements(schema).map((s) => db.prepare(s))).catch((err) => {
    schemaReady = null;
    throw err;
  });
  return schemaReady;
}

function sameOrigin(request: Request) {
  const origin = request.headers.get("Origin");
  return !origin || origin === new URL(request.url).origin;
}

const CORE = new Set(["name", "email", "phone", "message", "locale", "source", "website"]);

async function notify(env: Env, lead: Record<string, string>, extra: Record<string, string>) {
  if (!env.RESEND_API_KEY || !env.LEAD_NOTIFY_EMAIL) return false;
  const brand = env.BRAND_NAME || "Website";
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: env.RESEND_FROM_EMAIL || `${brand} <onboarding@resend.dev>`,
      to: env.LEAD_NOTIFY_EMAIL,
      ...(lead.email ? { reply_to: lead.email } : {}),
      subject: `New request: ${lead.name}`,
      text: [
        `Name: ${lead.name}`,
        `Email: ${lead.email || "not given"}`,
        `Phone: ${lead.phone || "not given"}`,
        ...Object.entries(extra).map(([key, value]) => `${key}: ${value}`),
        `Language: ${lead.locale} · from: ${lead.source}`,
        "",
        lead.message,
      ].join("\n"),
    }),
  });
  return res.ok;
}

async function inquiries(request: Request, env: Env, ctx: ExecutionContext) {
  const form = await request.formData();
  if (clip(form.get("website"), 200)) return json({ ok: true }); // honeypot: pretend success
  const lead = {
    name: clip(form.get("name"), 120),
    email: clip(form.get("email"), 200),
    phone: clip(form.get("phone"), 40),
    message: clip(form.get("message"), 4000),
    locale: clip(form.get("locale"), 5) || "en",
    source: clip(form.get("source"), 40) || "request-form",
  };
  // One way to reach them is enough, and they choose which.
  const reachable = (lead.email && isEmail(lead.email)) || (lead.phone && isPhone(lead.phone));
  if (!lead.name || !reachable || (lead.email && !isEmail(lead.email))) return json({ ok: false, error: "invalid" }, 400);

  const extra: Record<string, string> = {};
  for (const [key, value] of form.entries()) {
    if (CORE.has(key) || typeof value !== "string" || Object.keys(extra).length >= 20) continue;
    const text = value.trim().slice(0, 500);
    if (text) extra[key.slice(0, 40)] = text;
  }

  await ensureSchema(env.DB);
  const row = await env.DB.prepare(
    "INSERT INTO inquiries (created_at, name, email, phone, message, fields, locale, source) VALUES (?, ?, ?, ?, ?, ?, ?, ?) RETURNING id",
  )
    .bind(new Date().toISOString(), lead.name, lead.email || null, lead.phone || null, lead.message || null,
      Object.keys(extra).length ? JSON.stringify(extra) : null, lead.locale, lead.source)
    .first<{ id: number }>();

  ctx.waitUntil(
    (async () => {
      const sent = await notify(env, lead, extra);
      if (sent && row) await env.DB.prepare("UPDATE inquiries SET delivered_at = ? WHERE id = ?").bind(new Date().toISOString(), row.id).run();
    })().catch(() => {}),
  );
  return json({ ok: true });
}

async function subscribe(request: Request, env: Env) {
  const form = await request.formData();
  if (clip(form.get("website"), 200)) return json({ ok: true });
  const email = clip(form.get("email"), 200).toLowerCase();
  if (!isEmail(email)) return json({ ok: false, error: "invalid" }, 400);
  const firstName = clip(form.get("first_name"), 80) || null;
  const locale = clip(form.get("locale"), 5) || "en";
  const source = clip(form.get("source"), 40) || "inline";

  await ensureSchema(env.DB);
  const now = new Date().toISOString();
  await env.DB.prepare(
    `INSERT INTO subscribers (email, first_name, locale, source, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?)
     ON CONFLICT(email) DO UPDATE SET
       first_name = COALESCE(excluded.first_name, subscribers.first_name),
       locale = excluded.locale,
       updated_at = excluded.updated_at`,
  )
    .bind(email, firstName, locale, source, now, now)
    .run();
  return json({ ok: true });
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const { pathname } = new URL(request.url);
    if (!pathname.startsWith("/api/")) return env.ASSETS.fetch(request);
    if (request.method !== "POST") return json({ ok: false, error: "method" }, 405);
    if (!sameOrigin(request)) return json({ ok: false, error: "origin" }, 403);
    try {
      if (pathname === "/api/inquiries") return await inquiries(request, env, ctx);
      if (pathname === "/api/subscribe") return await subscribe(request, env);
      return json({ ok: false, error: "not-found" }, 404);
    } catch (err) {
      console.error(pathname, err);
      return json({ ok: false, error: "server" }, 500);
    }
  },
} satisfies ExportedHandler<Env>;
