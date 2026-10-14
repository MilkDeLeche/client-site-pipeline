---
name: client-site-pipeline
description: Ordered end-to-end workflow for a client site clone — client setup-list, architecture plan, clone intake, clone/build, launch audit, then SEO, then a client handoff. Use when starting a client website, cloning a template, choosing hosting/database/auth, or when the user mentions clone-intake, clone-workflow, client-web-delivery, launch-audit, or seo together. Required order; do not skip ahead.
---

# Client site pipeline

Five skills. Run them **in this order**. Each one produces an artifact the next one needs. If that artifact is missing, stop and do the earlier skill — do not improvise.

| Step | Skill | When | Done when |
|---|---|---|---|
| 1 | `client-web-delivery` | Start of the job | `PRD.md` read (if supplied) or drafted, and approved, with the site's intent: who buys, what they must believe, the one action that makes money; setup-list exists; client facts live in **one** `src/data/` file; `architecture-plan.md` exists with a reason for every service; no invented phone/reviews/prices or infrastructure |
| 2 | `clone-intake` | Before any clone build | Live template URL + repo `.txt` dumps (scrolled to the section) + motion video |
| 3 | `clone-workflow` | After intake passes | Template cloned at fidelity (Phase A), then rebranded from the data file only, mapped to the PRD's intent section by section (Phase B), then only the functionality named in `architecture-plan.md` is connected (Phase C), **including the live showcase standard** |
| 4 | `launch-audit` | After build, **before** public launch | Production build audited; privacy / 404 / titles / no fake testimonials; remaining asks stay on the setup-list |
| 5 | `seo` | After it is live (or on a rebuild, snapshot URLs **before** step 3) | Crawlable HTML, GBP/NAP if local, no `noindex` left on, redirects if replacing an old site |

Do not run 3 without 2. Do not run 4 on the dev server — it needs `npm run build`. Do not run 5 as a substitute for 4. DESIGN.md / TypeUI files are tokens only; they are not a step.

## Live showcase standard (every site, Phase C)

Most of these sites go up before the client pays, as a **near-final pitch**: it must read as about 99% done. Nothing on it says preview, prototype or demo, and every form really captures what is submitted. Every site ships with: a signup popup + inline signup that really save to D1 through `/api/subscribe`, a cookie banner that really gates analytics, and a privacy page that matches. The signup hook fits the business (juice bar → new drinks, seasonal specials, birthday treats; home builder → new-home alerts). Details and the hook table are in `client-web-delivery` → “Live showcase standard”. Put the promise and the email-tool choice on the setup-list. Showcase deploys go to `*.workers.dev` first.

## What each later skill actually is

**`launch-audit`** — ship / don’t-get-sued gate. Privacy policy on `/privacy` (what you collect including newsletter fields, cookie/analytics choice, AI use, font/analytics third parties), a signup that saves a row, a banner that gates analytics, real testimonials only, view-source not empty, custom 404, unique titles, OG image, schema, canonical, robots that allow AI crawlers, sitemap, alt text, no secrets in the build.

**`seo`** — growth after launch. Classic search, Google Business Profile / “near me,” and getting cited by AI assistants. Never invent keyword volumes. If this is a rebuild of a live site, snapshot old URLs and rankings **before** step 3.

## Agent rule

On a new client clone, read this skill first, then open **only the current step’s** skill. Name the step out loud (“step 2, clone-intake”). When architecture is being chosen, say “Current step: Architecture / Setup”. When the user jumps ahead (“do SEO”), say which step they skipped and what is missing.

## PRD gate

Step 1 is not done without a `PRD.md` (template: `client-web-delivery` → `assets/prd-template.md`).

- **PRD supplied** (file, doc, link): read it first, keep its decisions, add a labeled supplement for gaps. Never overwrite it.
- **Seed PRD** (a text file holding only the client's current website link, or a few lines): it is the starting point, not the brief. Open the site and their public profiles, put publishable facts in `src/data/`, save their photos and logo to `reference/` with rights noted, snapshot the old URLs for redirects (`seo`), then draft the full `PRD.md` around it. Leave the seed file as it was.
- **No PRD:** say it is required for a client rebrand, draft it from what is known, mark `UNKNOWN`s, and get approval (the builder approves a near-final pitch; the client approves production).
- **`reference-only`:** a light PRD lets Phase A run; client-facing Phase B/C waits for the full brief.
- The PRD holds intent; `src/data/` stays canonical for publishable facts. Conflicts between them are surfaced, not silently resolved.
- The PRD never changes Phase A.

## Sources of truth

| What | Where |
|---|---|
| Business intent and strategy | `PRD.md` |
| Client facts | one `src/data/` file |
| Architecture | `architecture-plan.md` |
| Missing client facts | the setup-list |
| Visual reference | clone-intake evidence |
| Why each section says what it says | `section-purpose-map.md` (Phase B) |
| Proof that conversions work | `conversion-acceptance.md` (launch-audit) |
| What actually shipped | the source and the production build |
| What the client is told | `deliverables/client-handoff.md` |

Do not invent a fact to fill the data file, and do not invent a service to fill the architecture plan. If a business answer would change the architecture and cannot be inferred, put that question on the setup-list in business language (“Should a booked time disappear for everyone else immediately?”), not as a vendor quiz (“Supabase or Convex?”).

## Architecture gate

Do not start Phase C, and do not provision a database, auth, object storage, or a server runtime, unless `architecture-plan.md` exists and names that system with a reason. Astro stays the framework unless the user explicitly overrides it. New projects default to Cloudflare Workers. A static marketing site stays static: no login, no R2, no server-rendered pages, just because those exist. The only standing exception is the email-capture API Worker + D1 subscribers table from the live showcase standard.

## After step 5

Return to `client-web-delivery` for the client handoff (`deliverables/client-handoff.md`, then the visual prompt). That is not a step you can run instead of the audit or SEO. The handoff describes only what production actually has.
