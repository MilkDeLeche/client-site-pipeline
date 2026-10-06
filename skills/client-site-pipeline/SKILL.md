---
name: client-site-pipeline
description: Ordered end-to-end workflow for a client site clone — client setup-list, architecture plan, clone intake, clone/build, launch audit, then SEO, then a client handoff. Use when starting a client website, cloning a template, choosing hosting/database/auth, or when the user mentions clone-intake, clone-workflow, client-web-delivery, launch-audit, or seo together. Required order; do not skip ahead.
---

# Client site pipeline

Five skills. Run them **in this order**. Each one produces an artifact the next one needs. If that artifact is missing, stop and do the earlier skill — do not improvise.

| Step | Skill | When | Done when |
|---|---|---|---|
| 1 | `client-web-delivery` | Start of the job | Setup-list exists; client facts live in **one** `src/data/` file; `architecture-plan.md` exists with a reason for every service; no invented phone/reviews/prices or infrastructure |
| 2 | `clone-intake` | Before any clone build | Live template URL + repo `.txt` dumps (scrolled to the section) + motion video |
| 3 | `clone-workflow` | After intake passes | Template cloned at fidelity (Phase A), then rebranded from the data file only (Phase B), then only the functionality named in `architecture-plan.md` is connected (Phase C) |
| 4 | `launch-audit` | After build, **before** public launch | Production build audited; privacy / 404 / titles / no fake testimonials; remaining asks stay on the setup-list |
| 5 | `seo` | After it is live (or on a rebuild, snapshot URLs **before** step 3) | Crawlable HTML, GBP/NAP if local, no `noindex` left on, redirects if replacing an old site |

Do not run 3 without 2. Do not run 4 on the dev server — it needs `npm run build`. Do not run 5 as a substitute for 4. DESIGN.md / TypeUI files are tokens only; they are not a step.

## What each later skill actually is

**`launch-audit`** — ship / don’t-get-sued gate. Privacy policy on `/privacy` (what you collect, AI use, font/analytics third parties), real testimonials only, view-source not empty, custom 404, unique titles, OG image, schema, canonical, robots that allow AI crawlers, sitemap, alt text, no secrets in the build.

**`seo`** — growth after launch. Classic search, Google Business Profile / “near me,” and getting cited by AI assistants. Never invent keyword volumes. If this is a rebuild of a live site, snapshot old URLs and rankings **before** step 3.

## Agent rule

On a new client clone, read this skill first, then open **only the current step’s** skill. Name the step out loud (“step 2, clone-intake”). When architecture is being chosen, say “Current step: Architecture / Setup”. When the user jumps ahead (“do SEO”), say which step they skipped and what is missing.

## Sources of truth

| What | Where |
|---|---|
| Client facts | one `src/data/` file |
| Architecture | `architecture-plan.md` |
| Missing client facts | the setup-list |
| Visual reference | clone-intake evidence |
| What actually shipped | the source and the production build |
| What the client is told | `deliverables/client-handoff.md` |

Do not invent a fact to fill the data file, and do not invent a service to fill the architecture plan. If a business answer would change the architecture and cannot be inferred, put that question on the setup-list in business language (“Should a booked time disappear for everyone else immediately?”), not as a vendor quiz (“Supabase or Convex?”).

## Architecture gate

Do not start Phase C, and do not provision a database, auth, object storage, or a server runtime, unless `architecture-plan.md` exists and names that system with a reason. Astro stays the framework unless the user explicitly overrides it. New projects default to Cloudflare Workers. A static marketing site stays static: no database, no login, no R2, no Worker runtime, just because those exist.

## After step 5

Return to `client-web-delivery` for the client handoff (`deliverables/client-handoff.md`, then the visual prompt). That is not a step you can run instead of the audit or SEO. The handoff describes only what production actually has.
