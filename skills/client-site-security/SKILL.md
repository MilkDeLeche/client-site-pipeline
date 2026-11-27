---
name: client-site-security
description: Security gate for a client site after launch-audit and before SEO (pipeline step 4b). Proves on the live host and in the database that a stranger and a malicious staff member cannot do what the screens say they cannot. Covers public keys, RLS, column grants, security-definer functions, triggers, rate limits, uploads and signed URLs, headers/CSP, third-party scripts, auth settings and dependencies. Use when the user asks for a pentest, security review, "is this safe", "no quiero fallas", "is this safe to hand to the client", or when client-site-pipeline reaches step 4b.
---

# Client site security

**Pipeline step 4b** (`client-site-pipeline`). Previous: `launch-audit`. Next: `seo`. Launch-audit checks the build, the privacy page and secrets in the bundle. This skill checks whether a stranger and a malicious staff member can do what the screens claim they cannot.

Static marketing sites with no database, login, uploads or server routes only need **The host that answers** and **Dependencies**. Everything else applies when `architecture-plan.md` turned on a database, auth, storage or a Worker.

## Rules of engagement

- Prove each control with the smallest request that cannot create or change a row: a shop slug that does not exist, a zero uuid, a missing signature, an `alg: none` token. Stop when the status code answers the question. No exploit scripts, payloads or how-tos.
- Insider tests run inside a transaction that ends in `raise exception 'RESULTADO: …'`, so every write rolls back (pattern below). Never test against real customer rows outside that.
- If a tool refuses a statement (the Supabase MCP declines SQL containing `DELETE`), do not work around it. Test with a non-delete equivalent, or give the user the SQL to run themselves.
- A previous report, a Cursor/Claude note, a committed migration or a passing UI is a **claim**. Re-test it. On one job a "pentest closed" migration had never been applied: it failed on `CHECK ... DEFERRABLE` (Postgres does not allow it), so production was still the old database.
- Never ask for or paste secret keys in chat. The user sets them with `wrangler secret put` in their own terminal.

## 1. The host that answers

Resolve the live domain first: `curl -sI https://<domain>/` and `/api/<health>`. Note `Server` and whether `/api/` returns JSON or the HTML app.

- If the repo's Worker, CSP or rate limit is not on that host (the domain still points at the old Netlify/Vercel site), those controls are absent in production. Say so. Do not describe them as shipped.
- Grep the **live HTML**, not `index.html` in the repo, for third-party scripts. Template editors (Lovable's `gptengineer.js`), tag managers and chat widgets on the origin can read a staff session in `localStorage`. Remove what the site does not need.
- Security headers count only on the document response: `Content-Security-Policy` (list exactly the map, fonts, images and API hosts the site loads, then load each page and confirm nothing is blocked), `X-Content-Type-Options: nosniff`, `X-Frame-Options` or `frame-ancestors`, `Referrer-Policy`, HSTS.
- Pages whose URL carries a secret token (order tracking, history links): `Referrer-Policy: no-referrer` and `noindex`. The staff panel: `X-Frame-Options: DENY`, `noindex`, and out of `robots.txt` crawl paths.
- Cloudflare `_headers`: a `/taller/*` rule does not match `/taller`; add both. A path matched by two rules sends duplicate headers unless the later rule detaches with `! Header-Name`.
- `/.env`, `/.dev.vars`, source maps and secret `/api/` paths: a `200` that is the SPA shell is not a leak; a `200` with the file is.

## 2. Outside, with the public key

The publishable/anon key is in the shipped JavaScript. Using it is the test.

1. `GET /rest/v1/<table>?select=*&limit=1` for **every** business table. Pass: `401`/permission denied, or `[]` because RLS returned nothing. Any customer, payment or staff row is a fail. Best baseline: `revoke all on all tables in schema public from anon`, then grant back only what is public.
2. Each staff function with the public key and a zero uuid. Pass: permission denied. A function that runs (even to say "not found") is granted too widely.
3. Each public write (booking, quote accept, contact) **on the database URL**, not through the website. If it executes, the Worker's rate limit, origin check and honeypot are bypassed. Fix: revoke `EXECUTE` from `anon`/`authenticated`/`public`, grant it to `service_role`, and have the Worker call it with the secret key. Also cap bursts in the database itself (a trigger that refuses more than N web bookings per minute per shop), because a per-IP limit does not stop many IPs.
4. An unsigned token (`alg: none`) to the database and to the Worker's authenticated routes. Pass: rejection. Do not forge a signed token.
5. `GET /auth/v1/settings`: `disable_signup: true` unless the product is a public registration. Accounts come only from an admin screen or the dashboard, and an account with no membership row sees nothing.
6. GraphQL (`/graphql/v1`) introspection with the public key should not list business tables.

## 3. Insider, in the database

The screen's `esAdmin` flag is not a control. For every sensitive write, find the RLS policy, the column grant and the trigger that enforce it.

- **Roles.** Deletes and money edits (payments, expenses, sale cancels, discounts) admin-only with `as restrictive` policies, so they AND with the permissive ones. A staff member cannot make themselves admin, add members, edit the shop row or move a client to another shop. A deactivated member sees nothing.
- **Computed columns.** `revoke update on <table> from authenticated`, then `grant update (<safe columns>)`. Supabase's default privileges grant ALL on every new table to `anon` and `authenticated`, so a column grant on a new table does nothing until you `revoke all` first. Check with `has_column_privilege('authenticated', '<table>', '<col>', 'UPDATE')` after every new table. Do this for totals, paid amounts, stock, folios and state. `REVOKE UPDATE` does not stop `INSERT` of that column, and it does not stop a trigger that writes the column as the table owner: a payment row that bumps "amount paid" is the same hole as writing the column.
- **State machines.** A state that lives only in a function is skipped by a direct `update ... set estado`. The role loses the column; the function that still writes it is `security definer` and checks membership itself. `security invoker` cannot update a column the role cannot update.
- **Definer functions** bypass RLS. Every one needs an explicit membership or token check, `set search_path = ''`, and `revoke execute ... from public, anon`. Revoke `EXECUTE` on trigger functions too.
- **Tenant checks on triggers.** A definer trigger that touches a row by id must check that row has the same `taller_id`/tenant as the incoming row (product, order, sale, service). One shop today does not make the missing check safe for the second shop.
- **Parent and child.** Admin-only on the parent row is not admin-only on the child. If a trigger recomputes the parent from the child, lock the child too (revoke insert/update/delete) and let the official definer function be the only writer.
- **Constraints, not UI.** A check must make the illegal total impossible (`descuento >= 0 and descuento <= subtotal`). CHECK constraints cannot be deferrable; when lines can lower the subtotal, clamp the discount in the subtotal trigger.
- **Every new feature gets a role decision.** A new table or screen starts as "any active member can write" unless someone decides otherwise. For each feature that writes (uploads, public content, settings), ask the builder which roles may write, then enforce it in three places: a restrictive policy with a definer helper that checks role and `activo`, the Worker route (403 before it touches storage), and the screen (hide the controls, explain why). Test each role in the rolled-back block: one allowed role writes; another role reads but gets 0 rows on update; a deactivated member sees nothing.
- **RLS fails silently on update and delete.** A filtered `update` or `delete` returns no error and 0 rows. Any server code that does something after the write (deletes the storage object, sends an email, charges) must check the affected rows (`.delete().eq(...).select('id')`) and stop when none came back. Otherwise a refused delete still removes the file, and the site shows a broken image.
- **Public responses.** A public function returns only what that page needs (first name, not phone). It must not include a second secret: an order token that also returns the bike's permanent token turns one repair link into the whole history. Staff need a way to rotate a leaked link.

### Rolled-back insider test

```sql
do $$
declare r text := ''; u uuid; o uuid;
begin
  -- setup as owner (fixture rows, a temporary membership for a real auth user)
  perform set_config('request.jwt.claims', json_build_object('sub', u, 'role', 'authenticated')::text, true);
  execute 'set local role authenticated';
  begin
    update public.ordenes set estado = 'lista' where id = o;
    r := r || ' estado_directo=PERMITIDO';
  exception when others then r := r || ' estado_directo=bloqueado'; end;
  -- … one begin/exception block per control; report row_count when 0 rows could hide RLS
  execute 'reset role';
  raise exception 'RESULTADO: %', r;   -- rolls everything back
end $$;
```

Also check privileges directly: `has_function_privilege('anon', '<fn(args)>', 'execute')`, `has_column_privilege('authenticated', '<table>', '<col>', 'UPDATE')`, `has_table_privilege(...)`. Read `pg_policies` for restrictive policies.

## 4. Worker, uploads and signed URLs

- A limit that returns early when its binding is missing fails open; the database cap still has to exist. Cloudflare's rate-limit binding is approximate: test with paced requests (30 over a minute), not a burst of 9.
- Public POSTs: same-origin check against the real domain and `www`, plus a honeypot field.
- Trust the body size you read, not `Content-Length`. Cap images and count per order.
- Object storage (R2) is private. Files are served through short-lived HMAC-signed URLs; a fake, expired or path-traversal (`..`) key is refused. Sign only keys under that shop's prefix (`t/<taller_id>/…`), and filter public responses to that prefix, or a staff member who can insert a row can mint a signature for a key they typed.
- SVG and HTML uploads (logos) are served with `nosniff` and `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; sandbox` on **that** response.
- The secret key lives only in Worker secrets. `grep` the build output for `service_role`, `sb_secret_`, `SUPABASE_SECRET`.
- Errors return a plain message, never a stack or a key.
- Public pages use a database client that does not persist a session, so a broken staff session in `localStorage` cannot break or ride along on them.

## 5. Platform settings (the user does these in dashboards)

Supabase → Authentication: signups off, minimum password 8, leaked-password protection if the plan allows, Site URL and redirect URLs on the real domain. Run the Supabase security advisors (`get_advisors`) and explain each remaining warning. Cloudflare: Always Use HTTPS, `www` → apex redirect, optional WAF rate rule on the booking route, optional Turnstile on public forms. Give click-by-click steps; the user does not read dashboards fluently.

## 6. Dependencies

`npm audit` on the production tree. Separate dev-only issues (Vite, esbuild, sucrase, glob) from code the browser runs, and say whether each remaining one is reachable. Do not copy a count from an old note. Remove packages the code does not use.

"Not reachable" explains a warning; it doesn't close it. When the builder agrees, do the upgrade, including the major version, instead of leaving it for later:
1. Read the library's breaking changes.
2. Grep the code for the patterns they touch (for a router: relative links inside splat routes, removed APIs).
3. Upgrade with an exact version, then run the typecheck and the build (the prerender exercises every public page).
4. Click through every route in a real browser: links, back, second language, 404, token pages, the staff login.
5. Deploy, and repeat the smoke test on the live domain.

Keep a copy of `package.json` and the lockfile to roll back, and finish at `found 0 vulnerabilities` or name what is left and why.

## Report

Plain language first, for the builder and the owner: what a stranger can do, what a staff member can still do, what the last report got wrong, what was fixed, what only the user can do in a dashboard. Each fail names the control that was supposed to stop it and whether the live host actually has it. Give the counts ("60 outside checks, 59 pass") and say how the one miss was handled. No payloads. Fix what the user asked you to fix, apply migrations yourself, then confirm with `list_migrations` and a re-test. Record the result in the project's setup-list. Then make the owner's update brochure (`client-web-delivery` → `references/update-brochure.md`): the protections and the pass counts in plain words, in the client's design kit, never how an attack works.

## Done when

- The live domain is served by the code you audited, with a CSP that allows only what the pages load and no editor/analytics script the repo removed.
- The public key cannot read business tables or call staff functions, and public writes are not callable with it (or the database refuses a burst).
- Signups are off; an account without membership, or a deactivated one, sees nothing.
- Staff cannot change order state, sale lines, paid totals, stock or folios except through the function that enforces the rule; deletes and money edits are admin-only.
- A mismatched id from a second shop is refused by every trigger and definer function.
- Uploads and signed URLs are scoped to the shop, private by default, and SVG is sandboxed.
- Every migration is **applied** (checked with `list_migrations`), not only committed, and re-tested after applying.
