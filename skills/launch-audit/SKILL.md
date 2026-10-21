---
name: launch-audit
description: Pre-launch / ship-readiness audit for any website before it goes live — checks technical hygiene AND legal/liability items. Verifies non-empty view-source (real SSR content, not a JS shell), a custom 404 page, unique per-page titles, an OG image, structured data (JSON-LD), canonical tags, a robots.txt that ALLOWS AI crawlers (AEO/GEO), a sitemap, the html lang attribute, image alt text, no exposed source maps, and no exposed secrets/keys or public storage. On the legal side it checks for a privacy policy that discloses data collection, AI usage, and third-party data processors, and confirms testimonials are real (not fabricated). Use before shipping or launching a site, or when the user asks for a "launch checklist", "pre-launch audit", "is this ready to go live", "legal/compliance review", "what could get us sued", or "make sure we're not missing anything before launch". Runs per-project and pairs with the `seo` skill (deeper SEO/GEO practice).
---

# Launch Audit

**Pipeline step 4** (`client-site-pipeline`, steps 0–5). Previous: `clone-workflow`. Next: `seo`. Run on the production build, not the dev server. Do not treat this as SEO — that is the next skill, after launch.

Run this before any website goes live. It has two halves: **technical ship-readiness** and **legal / don't-get-sued**. Do not eyeball the source — **build the site and inspect the actual shipped output** (`dist/`, `build/`, `out/`, `.output/public/`, or `.vercel/output/static`), then verify the legal items in the codebase, then report pass/fail with concrete fixes.

## Workflow

1. Build for production (`npm run build` or the project's equivalent). Audit the build output, **not** the dev server — some issues only appear in the real shipped HTML.
2. Run the automated checks: `bash scripts/audit.sh <build-dir>` (defaults to `dist`). Or run them by hand from the checklist below.
3. Verify the legal items (privacy policy contents, AI + third-party disclosure, real testimonials) by reading the code.
4. Report each item as ✅ pass / ⚠️ note / ❌ fail with the exact fix. Fix the ❌s you can; separate client-blocked items (domain, font/asset licensing, real reviews, real photos) clearly.

## Technical checklist — inspect the BUILD output

1. **View source not empty** — shipped HTML must contain real content, not just a JS shell. SSG/SSR (Astro, Next, SvelteKit) render content server-side; a pure client-rendered SPA may ship an empty `<div id="root">` — bad for SEO and AI crawlers. Grep the built index for known body text.
2. **404 page** — a custom `404.html` exists, uses the site layout, and offers a path back (home / primary CTA).
3. **Unique titles** — every page has its own `<title>`; none share the layout default. List them and diff.
4. **OG image** — `og:image` (+ `twitter:image`) present with an **absolute** URL, ideally a purpose-built 1200×630 asset under ~300 KB, that shows the **current** hero (a screenshot of an older version is the first thing a shared link shows).
5. **Structured data** — JSON-LD present and valid for the site type (LocalBusiness / Organization / Product / Article), plus breadcrumbs and per-page types. Validate with Google's Rich Results Test.
6. **Canonical** — every page emits `<link rel="canonical">` with the absolute URL. Requires the framework's `site`/base URL to be set.
7. **robots.txt allows AI** — exists AND does not block AI crawlers. For AEO/GEO you WANT `GPTBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-Web`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended` allowed. Include the `Sitemap:` line.
8. **Sitemap** — `sitemap-index.xml` / `sitemap.xml` generated and referenced from robots.txt.
9. **Lang attribute** — `<html lang="…">` set to the correct language on every page of every locale, with `hreflang` alternates (plus `x-default`) between the language versions.
10. **Alt text** — every `<img>` has `alt` (decorative images → `alt=""`). Count imgs vs imgs-with-alt.
11. **No exposed source maps** — no `.map` files in the build output; they leak your original source. Turn off the bundler's production sourcemap option (Vite `build.sourcemap: false`, etc.).
12. **No exposed secrets / public storage** — no `.env`, service-account keys (`*key*.json`), tokens, or credentials in the build output or in `public/` (which ships verbatim). Confirm any cloud storage bucket is not publicly listing or serving private files. Secrets live in env vars, never web-served.

**Companion checks** — run `antislop-human`'s contrast checker on the built pages, and antislop's Delivery Gate on everything Phase B/C added. Both skills are required by `client-site-pipeline`; if they're missing, stop and give the install commands from there.

## Legal checklist — don't get sued

13. **Privacy policy page exists** (`/privacy`) and is linked in the footer.
14. **Data-collection disclosure** — if you collect ANY data (even cookieless analytics, or a contact form), disclose what, why, and how long.
15. **AI disclosure** — if the site uses AI (generated imagery, chatbots, AI copy tools), disclose it. For a business showing "results," AI-generated images MUST be labeled illustrative / not real outcomes — otherwise it's misleading advertising (FTC risk), especially in regulated fields (medical, finance, legal).
16. **Third-party data collectors** — list every third party that can see the visitor: analytics, map embeds, font CDNs (Google Fonts, onlinewebfonts), embedded booking/checkout, tag managers, chat/social widgets. Each usually logs the visitor's IP.
17. **No fake testimonials** — every review must be real and attributable (source it: Google, Yelp, the POS/booking API). Fabricated reviews plus `aggregateRating` schema = FTC violation + Google manual action. Confirm the source and get permission to republish named reviews.

## Architecture-aware checks

The lists above always run. Then read `architecture-plan.md` and check **only the systems it selected**. Do not fail a static site for lacking a database, and do not skip a check for a system the plan turned on.

- **Cloudflare static** — production assets and the custom domain resolve, the custom 404 works, the intended pages are actually there, and no server runtime was added.
- **Worker runtime** — API/server routes work in production, bindings/env are set, no dev-only URLs, errors do not leak secrets.
- **R2** — the bucket/binding exists, upload and download work, private files are not public, and database metadata points at real objects.
- **Auth** — login, logout, expired session, protected routes, and a logged-out visitor. Secrets stay server-side.
- **Supabase** — production project and env vars, service-role key not in the client bundle, exposed data has an RLS/authorization story, production create/read/update paths work.
- **Convex** — production deployment, queries/mutations work, protected functions enforce auth. If the plan’s reason was realtime, prove it: window A shows a slot, window B books it, window A updates. “The booking saved” is not that test.

## Conversion journey checks (conditional)

Static checks can't prove a lead lands. For each conversion the PRD and architecture plan turned on (signup, inquiry/estimate/insight form, booking, order), run the real journey in a real browser (headless Chrome or Playwright): type, submit, then prove the outcome. Record it in `conversion-acceptance.md`. If the site has no conversion feature, write "not applicable" rather than inventing a test.

- **Capture (near-final pitch):** submit on the URL being shipped, then check the row in that same database: `wrangler dev` → `wrangler d1 execute <db> --local`; `*.workers.dev` → `wrangler d1 execute <db> --remote`. The success message says only that it was received. No "preview", "prototype", "demo" or "coming soon" wording appears anywhere in the build (grep the output).
- **Not a form:** a `tel:` link, a map link or an external order/booking URL is proved by following it. Don't add a form just to have something to submit.
- **Live delivery:** the message actually arrives (the agreed inbox, the email tool's send log, the CRM record), not just a success message. A booking or order shows up in the real third-party or backend system. On a near-final pitch, pending delivery is expected: don't fail the audit because the inbox or email tool isn't connected yet.
- **Failure path:** invalid input is blocked, a server error shows the error state, and the honeypot is in place. Check a challenge (e.g. Turnstile) only if the plan names one.
- **Ownership:** a named person receives each conversion. Without one, the site may capture, but don't call it live.
- **Measurement:** count completed conversions server-side by default (D1 rows, send logs). Cloudflare Web Analytics is pageview-based; propose an events tool only if the PRD needs one, and get approval. Never send form contents to analytics.
- **Consent + access:** the cookie banner gates analytics, forms work by keyboard, and errors are announced.

Legacy output paths (including `.vercel/output/static`) still count as a build directory when the architecture plan names that host. New projects are audited from the Cloudflare/Astro output (`dist/` unless the plan says otherwise).

## Privacy policy — minimum contents

Draft it, and mark it a **template the client/lawyer must review before publishing**. Cover:

- Business identity + contact (legal name, address, email).
- What data IS collected (analytics events, form fields) and what is NOT — e.g. on a marketing site, no health/PHI or payment data is collected here; that lives in the external booking/POS system under **its** policy, so HIPAA/PCI don't attach to the marketing site.
- Cookies / tracking technologies.
- The **named** third-party processors (hosting, analytics, maps, fonts, booking hand-off).
- AI usage + the illustrative-image note.
- How bookings/payments hand off to the external system (link to that system's policy).
- User rights (access / correction / deletion) and how to request them; note state privacy laws where relevant (e.g. Texas TDPSA, CCPA, GDPR).
- Retention, children (not directed at minors if adult-only), security, changes + effective date, governing law (business's state).

## Report format

```
Launch audit — <site>  (build: <dir>)
Technical:  1 ✅ · 2 ✅ · … · 11 ✅ · 12 ⚠️ <note>
Legal:      13 ❌ <fix> · 14 ❌ · 15 ⚠️ · 16 ❌ · 17 ✅
Conversions: signup ✅ row stored · estimate form ✅ captured, delivery ⏳ client inbox · (or: not applicable)
Client-blocked: <real domain, asset/font licensing, real reviews, real photos>
```

Fix the ❌s you can; keep client-blocked items in their own list so the user knows what to request.

## Pairs with

- **`seo`** skill — deeper SEO / GEO / AEO (keyword & content strategy, Google Business Profile, Core Web Vitals, internal links, indexing). This skill is the pre-launch **gate**; `seo` is the ongoing practice. Run this first, then hand off to `seo` for growth.
