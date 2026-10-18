---
name: client-web-delivery
description: A safe, repeatable workflow for delivering a client website end-to-end — intake (starting from a PRD, or drafting one from a seed link to the client's current site), an architecture plan, build, the "what we need from the client" setup-list, the pre-launch gate, deploy, and a final client handoff. Use when starting or finishing a client website project, when the user asks "what do I need from the client", wants a client setup / onboarding list or handoff document, wants to choose hosting, database, auth, or storage, wants to hand a project off, or wants a professional / safe / repeatable workflow for shipping client sites. Produces a per-project setup-list (from assets/setup-list-template.md) and architecture-plan (from assets/architecture-plan-template.md) tailored to whatever external systems the site connects to (payments/POS, booking, CMS, email, maps, analytics, fonts, chat). Ties in the `launch-audit` skill (the pre-launch gate) and the `seo` skill (post-launch growth). Runs per-project.
---

# Client Web Delivery

**Pipeline step 1 of 5** (`client-site-pipeline`). Next: `clone-intake`. Do not clone a template until this step has a `PRD.md` (a `reference-only` one is enough for Phase A), a setup-list, a single `src/data/` file for client facts, and an `architecture-plan.md`.

A repeatable, professional workflow for shipping a client website without surprises. Five stages. The signature artifact is the **setup-list**: one page of everything you need FROM the client, so you never chase them for it piecemeal.

## Stage 1 — Intake (before building)

Pin down, in writing:

- **`PRD.md` first.** If the user supplied a PRD (file, doc, link), read it and keep its decisions; add a labeled supplement for gaps and never overwrite it. If it is only a seed (the client's website link in a text file, even one named `PRD.md`), keep its bytes (copy a `PRD.md` seed to `PRD.seed.md`), research that site and their public profiles, extract facts to `src/data/`, and write the full `PRD.md` at status `draft`. Otherwise draft one from `assets/prd-template.md`. A PRD is **intent**, not contact details: what the business sells and to whom, where visitors come from, what they must believe, the one action that makes the business money, what completes it, and who answers it. Get it approved (client for production, builder for a near-final pitch). Publishable facts still go in the one `src/data/` file.
- Business identity, target market, and the ONE goal of the site (book / call / buy / lead), taken from the PRD.
- **Where the money and the data live:** which external systems will this site connect to or hand off to? (POS / payments, booking / scheduling, CMS, email / CRM, maps, analytics, chat.) This single question determines the whole setup-list.
- Brand assets on hand vs. missing (logo, photos, fonts, copy, reviews).
- Domain: owned or to buy.
- Write `architecture-plan.md` from the requirements you already have (template: `assets/architecture-plan-template.md`), reconciled with the PRD's functional needs and primary conversion. Infer the smallest stack. Do not stop to ask “Supabase or Convex?” when the brief is a brochure site.

## Architecture plan

Infrastructure is selected because a requirement needs it, never because the technology is available. Astro stays the framework unless the user explicitly overrides it. **Cloudflare Workers is the standard host for every project.** Use another host only when the user explicitly says so. A project already live elsewhere (a legacy Vercel or Netlify site) moves to Cloudflare as a named step in the plan: new Worker, D1 capture, then the old URL redirected or retired. Never migrate in silence, and never leave a shared link dead.

Three Cloudflare modes:

- **Static** (`rendering: static`, `server_runtime_required: false`) — marketing, portfolio, restaurant, contractor, brochure, developer-published blog. `astro build` → `dist/` → Workers static assets. Do not add a Worker runtime because Workers can run code.
- **Static + API Worker** (`rendering: static`, `api_worker: true`) — the default for client showcase sites, because every site captures emails (see "Live showcase standard"). Pages stay static assets; `wrangler.jsonc` has `main: worker/index.ts` and `assets.run_worker_first: ["/api/*"]`, so the Worker runs only for `/api/*`: `/api/subscribe`, plus `/api/inquiries` when the primary action is a form. No Astro adapter. Set Astro `build.format: "file"` so `/menu` is served without a trailing-slash redirect. Moving an existing project off the adapter: delete `.wrangler/deploy/config.json`, which still redirects Wrangler to `dist/server/wrangler.json` and breaks `wrangler dev` and `deploy`.
- **Server** (`rendering: server`, `server_runtime_required: true`) — auth handlers, protected routes, API endpoints, signed file URLs, server-rendered app behavior. Use the Astro Cloudflare adapter only in this mode.

Database is one of `none`, `supabase`, or `convex` for business data. Never both “just in case.” The one standing exception is capture: a D1 `subscribers` table (email, optional first name, optional birthday month/day, source, timestamps) behind the API Worker, until the client picks an email platform, plus an `inquiries` table when the PRD's primary action is a form (estimate, insight form), until the client's inbox or CRM is connected. `POST /api/inquiries` stores `created_at`, `name`, `email`, `phone`, `message`, `source`, and only the qualifying fields the PRD names (e.g. company, website, goal, budget range, timeline). Same honeypot, same-origin check and error states as `/api/subscribe`. The success message says only that the message was received, never that someone will reply. Do not put anything else in D1 without its own reason, and do not auto-select KV.

| Need | Choice |
|---|---|
| No persistent app data (pages, gallery, hours, a repo-published blog, a contact form that only emails) | `database: none`. A contact form is not a database. The word “appointment” is not Convex. |
| Relational business data: customers, invoices, orders, inventory, CRM, reporting, SQL | `supabase`. Auth default: `supabase-auth` when the app uses Supabase’s Data API / RLS. Better Auth only with a written reason. |
| Live shared state is the product: slots disappearing for everyone else, live order status, chat, queues, a dashboard that updates without refresh | `convex`, `realtime_required: true`. Auth default when login is required: `better-auth`, via the supported Convex integration — do not invent a bridge. |
| “We might want realtime someday” with no behavior named | Not enough. Stay on `none` or Supabase. |

Auth is `none` unless something must be protected (accounts, staff/admin, private downloads, a client-run CMS). Do not put “Powered by Supabase” or “Powered by Better Auth” on the login screen. The client’s logo and copy are the UI.

Storage: logos and photos that change only by deploy stay in Astro static assets. R2 is for files uploaded **after** launch (PDFs, contracts, customer documents, a gallery the staff manages). The database stores the file’s metadata; R2 stores the bytes. Private files are not a public bucket.

Analytics default for a suitable new project: Cloudflare Web Analytics, one system, disclosed in the privacy policy. If the client already named another tool, use that instead.

Every selected service needs a `reason`. Add-ons are opt-in per client, never standard: an AI sales/lead chat, for example, goes only on sites whose owner wants it and is never listed as part of the base offer. Missing business facts stay on the setup-list. Content strategy is required; a blog is not. A dead blog of generic articles is not an SEO asset. Client-editable publishing needs auth and persistent storage; developer-committed Markdown does not.

Copy `assets/architecture-plan-template.md`, fill it, and keep it as the source of truth for Phase C and the launch audit.

## Live showcase standard (every client site)

These sites are often built **before** the client has paid, as a **near-final pitch** that wins the job: it must read as about 99% done. Nothing on the site says preview, prototype, demo or coming soon, and every form genuinely captures what is submitted (the primary inquiry form saves to the `inquiries` table until the client's inbox or CRM is connected). The remaining 1% is the client's own: email tool, real photos, domain. Build them to feel fully live. Every site gets all four of these, tuned to the business. They are not optional and do not need a separate request.

1. **Email capture that actually saves.** A newsletter / alert popup (once per visitor, after the cookie choice and ~12s or ~45% scroll, snoozed 14 days when closed, never again after signup) **and** an always-visible inline signup section. Fields: email (required), first name and birthday month/day (optional) when the business can use them. Honeypot field, same-origin check, `ON CONFLICT(email)` upsert. Working endpoint `/api/subscribe` → D1. Test it with `wrangler dev` before deploy (`wrangler d1 migrations apply <name> --local`).
2. **Cookie consent banner.** Accept / Decline, links to `/privacy#cookies`, remembers the choice in localStorage, and **actually gates** analytics: the analytics script loads only after Accept. Banner copy says what is really stored. Never claim cookies the site doesn't use.
3. **Privacy policy that matches.** `/privacy` lists exactly what the signup keeps, where it is stored (Cloudflare), how to unsubscribe or delete, the cookie/analytics choice, and that AI imagery is illustrative.
4. **A second language.** Every site ships in its primary language plus one secondary language, picked in the PRD from who actually buys (Rio Grande Valley and most of Texas → Spanish). The primary stays at `/`, the secondary at `/<code>/` through Astro's `i18n` config (`defaultLocale`, `locales`, `routing.prefixDefaultLocale: false`). Rules:
   - One copy file per locale (`src/data/<client>.ts`, `src/data/<client>.<code>.ts`) importing the **same** facts, so names, prices, hours and phone numbers can't drift between languages.
   - Write the second language natively for that audience (how a local owner actually talks, including regional usage), not word for word. Hooks get rewritten, not translated.
   - Both languages get every page, the forms, the popup, the banner, the privacy page and the 404. `<html lang>` per page, `hreflang` alternates plus `x-default`, and a language switch built from the template's own nav-link style.
   - The API stores the visitor's `locale` with each signup and inquiry.
   - A fluent person on the client's side reviews the second-language copy; that goes on the setup-list.

Pick the signup hook from what the business sells. Promise only what the client will send, and put the promise on the setup-list for confirmation:

| Business | Signup hook (title / what they get) |
| --- | --- |
| Juice bar, café, restaurant, bakery | “Sign up to our newsletter” — new drinks/dishes first, seasonal specials, birthday treats; rewards/points only if a real program exists (e.g. Clover Rewards) |
| Home builder, construction, real estate | “Get new-home alerts” — new homes and lots as they list, open houses, price changes; optional fields: area, budget range, beds |
| Salon, barber, spa, clinic | “Get first dibs” — open appointment slots, seasonal services, birthday offers |
| Gym, studio, coach | “Join the list” — new classes, challenges, schedule changes, member offers |
| Retail / boutique | “Be first to know” — new arrivals, restocks, sales, birthday discounts |
| Service trades (HVAC, plumbing, landscaping, cleaning) | “Seasonal tune-up reminders” — maintenance reminders, seasonal specials |
| Events, venues | “Get the lineup” — upcoming events, presales |

Blog: not part of this standard yet. A client-editable blog needs an admin login and storage; decide it per client.

## Stage 2 — Build

Build the site. Keep every client-supplied fact in ONE data file so it's swappable. **Do not invent facts** (prices, reviews, credentials, results) — leave a clear placeholder and add the real item to the setup-list (in a near-final pitch, omit the fact or hide its section instead of showing a placeholder).

## Stage 3 — The setup-list (what you need FROM the client)

Copy `assets/setup-list-template.md` into the project, fill it in for THIS client, and send it. What you request depends on what the site connects to — use the map below. Golden rule: **collect everything once, in one document.**

### Integration → what to request

| The site connects to… | Ask the client for… |
| --- | --- |
| **Clover** (payments/menu) | Hosted-checkout private token + Merchant ID; a second API token scoped Inventory/Orders/Merchant. |
| **Stripe / Square** | Publishable + restricted/secret keys — or connect through their own dashboard / OAuth. |
| **GlossGenius / external booking** | Usually **nothing** — booking and payment happen there; just confirm the booking URL(s). |
| **A CMS (Sanity, Contentful, Keystatic…)** | Project ID / dataset / a read token, or an invite to the space. |
| **Email / newsletter / contact forms** | Which email tool sends the newsletter (Brevo, Mailchimp, Klaviyo, the POS's marketing tool) and confirmation of what subscribers are promised (birthday treat, alerts). Until then signups live in D1. The tool's API key goes in a Worker secret (`wrangler secret put`), never in chat. |
| **Google Maps / Business Profile** | Confirm the exact NAP (name, address, phone); claim/verify the GBP. |
| **Analytics** | Which tool; any consent/cookie requirements for their region. |
| **A licensed font or stock asset** | Proof of license — or approval to swap for a free equivalent. |

Always also request: **who reviews the second-language copy**, **what the signup promises** (and which email tool sends it), **domain**, **public phone + email to publish**, **team/staff photos + bios**, **real reviews + permission to use names**, **factual/medical/legal sign-off** on any regulated copy, and **rights to any AI or stock imagery**.

## Stage 4 — Pre-launch gate

Before shipping, **invoke the `launch-audit` skill** and clear its checklist: non-empty view-source, 404, unique titles, OG image, structured data, canonical, robots-allows-AI, sitemap, lang, alt text, no exposed source maps or secrets, and the legal items (a privacy policy disclosing data collection + AI usage + third-party processors, and real testimonials). Also confirm the live showcase standard works: the banner gates analytics, the popup and inline signup save a row (check with `wrangler d1 execute <name> --local`), and the privacy page matches. Fix the ❌s you can; keep client-blocked items on the setup-list.

## Stage 5 — Deploy + verify

- Get a **green production build locally first**.
- For the API Worker: leave `database_id` **out** of the D1 binding (only `binding` + `database_name`); the first `wrangler deploy` provisions the database. Wrangler does not run migrations on deploy, so the Worker runs the schema (`CREATE TABLE IF NOT EXISTS`, imported from the migration `.sql`) before its first insert. Pin Node with `.node-version` (`22`) and `engines`. Prove it the way Cloudflare will build it: clone the repo into a clean folder, `npm ci`, `npm run build`, `wrangler deploy --dry-run`, then `wrangler dev` against an empty local D1 and post a signup.
- Renaming or deleting files in `public/` (re-encoded video, swapped images): keep the old URLs alive with a `public/_redirects` entry (`/video/old/* /video/new/:splat 301`). A page already open or cached on a phone still points at the old paths, and media that 404s just sits still.
- Hero copy changed? Recapture the share image (`og:image`) from the live hero at 1200x630, keep it under about 300 KB (WhatsApp drops larger previews), and bump its cache-busting version so apps refetch it.
- Git-connected deploy (no local login needed): Workers & Pages → Import a repository; build command `npm run build`, deploy command `npx wrangler deploy`, project name = `name` in `wrangler.jsonc`. Write these settings into the project README. Showcase sites deploy to the `*.workers.dev` address first, with `noindex` on; the client's domain is attached, and `noindex` removed, after they say yes.
- Ship to the host named in `architecture-plan.md`. New projects: Cloudflare Workers (static assets unless `server_runtime_required: true`). Legacy projects: the provider the plan already recorded (Vercel, Netlify, or otherwise).
- **Verify the live URL, not just the build** — load the real pages and confirm the deploy went green in the host dashboard.
- Set the real **domain** and the framework's **site/base URL** so canonical, OG, and sitemap point at production.

## After launch → growth

Hand off to the **`seo`** skill for Google Business Profile, keyword/content strategy, internal links, Core Web Vitals, and AI-assistant visibility (GEO/AEO). SEO chooses a content strategy. It does not require a blog.

## Final handoff (after SEO)

Run this skill again only to explain what shipped. Canonical file: `deliverables/client-handoff.md` (template: `assets/client-handoff-template.md`). Then `deliverables/client-handoff-visual-prompt.md` (template: `assets/client-handoff-visual-prompt-template.md`) so a presentation tool can make a booklet later. The Markdown file is the source of truth. A PDF is optional and is not a dependency of this skill.

Write only what production actually has: client data, `architecture-plan.md`, the build, real integrations, SEO output, verified brand assets. No invented features, rankings, certifications, backups, or testimonials. Omit empty sections. Explain each technology in one plain sentence (what it does for this client), and keep a short technical appendix for the developer.

## Safety rules (the "professional" part)

- One data file for client facts; one setup-list for client asks; one `architecture-plan.md` for infrastructure.
- **Never receive secrets or keys over chat/DM.** The client pastes them into their own dashboard or a secure vault; your code references env vars. The setup-list says *where* a credential goes. It never asks them to paste the secret into chat.
- Don't fabricate prices, reviews, credentials, or results — placeholder + request.
- Disclose AI usage; label AI/stock imagery as illustrative, not real outcomes.
- Green build → push → verify live. Never "push and hope."
