---
name: client-web-delivery
description: A safe, repeatable workflow for delivering a client website end-to-end — intake, an architecture plan, build, the "what we need from the client" setup-list, the pre-launch gate, deploy, and a final client handoff. Use when starting or finishing a client website project, when the user asks "what do I need from the client", wants a client setup / onboarding list or handoff document, wants to choose hosting, database, auth, or storage, wants to hand a project off, or wants a professional / safe / repeatable workflow for shipping client sites. Produces a per-project setup-list (from assets/setup-list-template.md) and architecture-plan (from assets/architecture-plan-template.md) tailored to whatever external systems the site connects to (payments/POS, booking, CMS, email, maps, analytics, fonts, chat). Ties in the `launch-audit` skill (the pre-launch gate) and the `seo` skill (post-launch growth). Runs per-project.
---

# Client Web Delivery

**Pipeline step 1 of 5** (`client-site-pipeline`). Next: `clone-intake`. Do not clone a template until this step has a setup-list, a single `src/data/` file for client facts, and an `architecture-plan.md`.

A repeatable, professional workflow for shipping a client website without surprises. Five stages. The signature artifact is the **setup-list**: one page of everything you need FROM the client, so you never chase them for it piecemeal.

## Stage 1 — Intake (before building)

Pin down, in writing:

- Business identity, target market, and the ONE goal of the site (book / call / buy / lead).
- **Where the money and the data live:** which external systems will this site connect to or hand off to? (POS / payments, booking / scheduling, CMS, email / CRM, maps, analytics, chat.) This single question determines the whole setup-list.
- Brand assets on hand vs. missing (logo, photos, fonts, copy, reviews).
- Domain: owned or to buy.
- Write `architecture-plan.md` from the requirements you already have (template: `assets/architecture-plan-template.md`). Infer the smallest stack. Do not stop to ask “Supabase or Convex?” when the brief is a brochure site.

## Architecture plan

Infrastructure is selected because a requirement needs it, never because the technology is available. Astro stays the framework unless the user explicitly overrides it. **New projects default to Cloudflare Workers.** If the plan identifies an existing host (a legacy Vercel or Netlify site), name that provider explicitly and keep it — do not migrate it in silence.

Two Cloudflare modes:

- **Static** (`rendering: static`, `server_runtime_required: false`) — marketing, portfolio, restaurant, contractor, brochure, developer-published blog. `astro build` → `dist/` → Workers static assets. Do not add a Worker runtime because Workers can run code.
- **Server** (`rendering: server`, `server_runtime_required: true`) — auth handlers, protected routes, API endpoints, signed file URLs, server-rendered app behavior. Use the Astro Cloudflare adapter only in this mode.

Database is one of `none`, `supabase`, or `convex`. Never both “just in case.” Do not auto-select Cloudflare D1 or KV.

| Need | Choice |
|---|---|
| No persistent app data (pages, gallery, hours, a repo-published blog, a contact form that only emails) | `database: none`. A contact form is not a database. The word “appointment” is not Convex. |
| Relational business data: customers, invoices, orders, inventory, CRM, reporting, SQL | `supabase`. Auth default: `supabase-auth` when the app uses Supabase’s Data API / RLS. Better Auth only with a written reason. |
| Live shared state is the product: slots disappearing for everyone else, live order status, chat, queues, a dashboard that updates without refresh | `convex`, `realtime_required: true`. Auth default when login is required: `better-auth`, via the supported Convex integration — do not invent a bridge. |
| “We might want realtime someday” with no behavior named | Not enough. Stay on `none` or Supabase. |

Auth is `none` unless something must be protected (accounts, staff/admin, private downloads, a client-run CMS). Do not put “Powered by Supabase” or “Powered by Better Auth” on the login screen. The client’s logo and copy are the UI.

Storage: logos and photos that change only by deploy stay in Astro static assets. R2 is for files uploaded **after** launch (PDFs, contracts, customer documents, a gallery the staff manages). The database stores the file’s metadata; R2 stores the bytes. Private files are not a public bucket.

Analytics default for a suitable new project: Cloudflare Web Analytics, one system, disclosed in the privacy policy. If the client already named another tool, use that instead.

Every selected service needs a `reason`. Missing business facts stay on the setup-list. Content strategy is required; a blog is not. A dead blog of generic articles is not an SEO asset. Client-editable publishing needs auth and persistent storage; developer-committed Markdown does not.

Copy `assets/architecture-plan-template.md`, fill it, and keep it as the source of truth for Phase C and the launch audit.

## Stage 2 — Build

Build the site. Keep every client-supplied fact in ONE data file so it's swappable. **Do not invent facts** (prices, reviews, credentials, results) — leave a clear placeholder and add the real item to the setup-list.

## Stage 3 — The setup-list (what you need FROM the client)

Copy `assets/setup-list-template.md` into the project, fill it in for THIS client, and send it. What you request depends on what the site connects to — use the map below. Golden rule: **collect everything once, in one document.**

### Integration → what to request

| The site connects to… | Ask the client for… |
| --- | --- |
| **Clover** (payments/menu) | Hosted-checkout private token + Merchant ID; a second API token scoped Inventory/Orders/Merchant. |
| **Stripe / Square** | Publishable + restricted/secret keys — or connect through their own dashboard / OAuth. |
| **GlossGenius / external booking** | Usually **nothing** — booking and payment happen there; just confirm the booking URL(s). |
| **A CMS (Sanity, Contentful, Keystatic…)** | Project ID / dataset / a read token, or an invite to the space. |
| **Email / newsletter / contact forms** | The destination inbox; an API key if using a form service. |
| **Google Maps / Business Profile** | Confirm the exact NAP (name, address, phone); claim/verify the GBP. |
| **Analytics** | Which tool; any consent/cookie requirements for their region. |
| **A licensed font or stock asset** | Proof of license — or approval to swap for a free equivalent. |

Always also request: **domain**, **public phone + email to publish**, **team/staff photos + bios**, **real reviews + permission to use names**, **factual/medical/legal sign-off** on any regulated copy, and **rights to any AI or stock imagery**.

## Stage 4 — Pre-launch gate

Before shipping, **invoke the `launch-audit` skill** and clear its checklist: non-empty view-source, 404, unique titles, OG image, structured data, canonical, robots-allows-AI, sitemap, lang, alt text, no exposed source maps or secrets, and the legal items (a privacy policy disclosing data collection + AI usage + third-party processors, and real testimonials). Fix the ❌s you can; keep client-blocked items on the setup-list.

## Stage 5 — Deploy + verify

- Get a **green production build locally first**.
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
