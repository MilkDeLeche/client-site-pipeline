---
name: launch-audit
description: Pre-launch / ship-readiness audit for any website before it goes live — checks technical hygiene AND legal/liability items. Verifies non-empty view-source (real SSR content, not a JS shell), a custom 404 page, unique per-page titles, an OG image, structured data (JSON-LD), canonical tags, a robots.txt that ALLOWS AI crawlers (AEO/GEO), a sitemap, the html lang attribute, image alt text, no exposed source maps, and no exposed secrets/keys or public storage. On the legal side it checks for a privacy policy that discloses data collection, AI usage, and third-party data processors, and confirms testimonials are real (not fabricated). Use before shipping or launching a site, or when the user asks for a "launch checklist", "pre-launch audit", "is this ready to go live", "legal/compliance review", "what could get us sued", or "make sure we're not missing anything before launch". Runs per-project and pairs with the `seo` skill (deeper SEO/GEO practice).
---

# Launch Audit

**Pipeline step 4 of 5** (`client-site-pipeline`). Previous: `clone-workflow`. Next: `seo`. Run on the production build, not the dev server. Do not treat this as SEO — that is the next skill, after launch.

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
4. **OG image** — `og:image` (+ `twitter:image`) present with an **absolute** URL, ideally a purpose-built 1200×630 asset.
5. **Structured data** — JSON-LD present and valid for the site type (LocalBusiness / Organization / Product / Article), plus breadcrumbs and per-page types. Validate with Google's Rich Results Test.
6. **Canonical** — every page emits `<link rel="canonical">` with the absolute URL. Requires the framework's `site`/base URL to be set.
7. **robots.txt allows AI** — exists AND does not block AI crawlers. For AEO/GEO you WANT `GPTBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-Web`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended` allowed. Include the `Sitemap:` line.
8. **Sitemap** — `sitemap-index.xml` / `sitemap.xml` generated and referenced from robots.txt.
9. **Lang attribute** — `<html lang="…">` set to the correct language.
10. **Alt text** — every `<img>` has `alt` (decorative images → `alt=""`). Count imgs vs imgs-with-alt.
11. **No exposed source maps** — no `.map` files in the build output; they leak your original source. Turn off the bundler's production sourcemap option (Vite `build.sourcemap: false`, etc.).
12. **No exposed secrets / public storage** — no `.env`, service-account keys (`*key*.json`), tokens, or credentials in the build output or in `public/` (which ships verbatim). Confirm any cloud storage bucket is not publicly listing or serving private files. Secrets live in env vars, never web-served.

## Legal checklist — don't get sued

13. **Privacy policy page exists** (`/privacy`) and is linked in the footer.
14. **Data-collection disclosure** — if you collect ANY data (even cookieless analytics, or a contact form), disclose what, why, and how long.
15. **AI disclosure** — if the site uses AI (generated imagery, chatbots, AI copy tools), disclose it. For a business showing "results," AI-generated images MUST be labeled illustrative / not real outcomes — otherwise it's misleading advertising (FTC risk), especially in regulated fields (medical, finance, legal).
16. **Third-party data collectors** — list every third party that can see the visitor: analytics, map embeds, font CDNs (Google Fonts, onlinewebfonts), embedded booking/checkout, tag managers, chat/social widgets. Each usually logs the visitor's IP.
17. **No fake testimonials** — every review must be real and attributable (source it: Google, Yelp, the POS/booking API). Fabricated reviews plus `aggregateRating` schema = FTC violation + Google manual action. Confirm the source and get permission to republish named reviews.

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
Client-blocked: <real domain, asset/font licensing, real reviews, real photos>
```

Fix the ❌s you can; keep client-blocked items in their own list so the user knows what to request.

## Pairs with

- **`seo`** skill — deeper SEO / GEO / AEO (keyword & content strategy, Google Business Profile, Core Web Vitals, internal links, indexing). This skill is the pre-launch **gate**; `seo` is the ongoing practice. Run this first, then hand off to `seo` for growth.
