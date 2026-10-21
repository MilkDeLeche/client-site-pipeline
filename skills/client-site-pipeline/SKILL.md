---
name: client-site-pipeline
description: Ordered end-to-end workflow for a client site clone — brand discovery (creative direction), client setup-list, architecture plan, clone intake, clone/build, launch audit, then SEO, then a client handoff. Use when starting a client website (including from a seed PRD that is just the client's current site link, or as a near-final pitch built before the sale), cloning a template, choosing hosting/database/auth, or when the user mentions brand-discovery, clone-intake, clone-workflow, client-web-delivery, launch-audit, or seo together. Required order; do not skip ahead.
---

# Client site pipeline

Six skills, steps 0–5. Run them **in this order**. Each one produces an artifact the next one needs. If that artifact is missing, stop and do the earlier skill — do not improvise.

| Step | Skill | When | Done when |
|---|---|---|---|
| 0 | `brand-discovery` | Start of the job, before the PRD and before a template is settled | Vibe read written; every link sorted into template or reference brand; the ask-first list asked (or carried to the pitch meeting); two or three directions offered; `creative-direction.md` saved with its approval type |
| 1 | `client-web-delivery` | Start of the job | `PRD.md` read (if supplied) or drafted, and approved, with the site's intent: who buys, what they must believe, the one action that makes money; setup-list exists; client facts live in **one** `src/data/` file; `architecture-plan.md` exists with a reason for every service; no invented phone/reviews/prices or infrastructure |
| 2 | `clone-intake` | Before any clone build | Template vetted against `creative-direction.md`; live template URL + repo `.txt` dumps (scrolled to the section) + motion video |
| 3 | `clone-workflow` | After intake passes | Template cloned at fidelity (Phase A), then rebranded from the data file only, mapped to the PRD's intent and the approved creative direction section by section by the senior room, from a media-truth inventory, until the first screen speaks to the target buyer with real proof (Phase B), then only the functionality named in `architecture-plan.md` is connected (Phase C), **including the live showcase standard** |
| 4 | `launch-audit` | After build, **before** public launch | Production build audited; privacy / 404 / titles / no fake testimonials; remaining asks stay on the setup-list |
| 5 | `seo` | After it is live (or on a rebuild, snapshot URLs **before** step 3) | Crawlable HTML, GBP/NAP if local, no `noindex` left on, redirects if replacing an old site |

Do not run 1 on a new client without 0 (`reference-only` skips 0). Do not run 3 without 2. Do not run 4 on the dev server — it needs `npm run build`. Do not run 5 as a substitute for 4. DESIGN.md / TypeUI files are tokens only; they are not a step, and they encode a chosen direction without choosing it.

## Required companion skills (check before step 0)

The pipeline needs two outside skill packs. Check that they are installed before doing anything else; they are not optional.

| Skill | From | Used for |
|---|---|---|
| `copywriting` | `coreyhaines31/marketingskills` | Phase B copywriter: the hook bank, headlines, CTAs, in both site languages |
| `antislop` (core) + `antislop-copywriting`, `antislop-ui`, `antislop-layoutmobile`, `antislop-human` | `miqdadbadjuber/anti-slop` | The slop filter on every line of copy and every UI addition; the redline; the launch audit's contrast and delivery checks |

**If any is missing, stop.** Name the missing skills and give the user these commands (global install, recommended; drop `-g` for one project only):

```bash
npx skills add coreyhaines31/marketingskills --skill copywriting -g
npx skills add miqdadbadjuber/anti-slop -g
```

Then tell them to start a new session: skills load when a session starts. Do not continue the job without them, and do not fetch or write skill files yourself.

**How the pipeline uses them, and what wins:**
- **Phase B writes with these skills, in antislop's DURING mode.** The copywriter drafts every line through `copywriting` and `antislop-copywriting`, and the UX lead builds every addition through `antislop-ui`, `antislop-layoutmobile` and `antislop-human`, from the first draft. They are how Phase B writes, not a cleanup pass afterward. antislop asks once per session; answer *during* for pipeline work, and follow its own mode and pointer-block rules. Phase B ends with antislop's Delivery Gate report.
- antislop wants design direction (`DESIGN.md`). In this pipeline **`creative-direction.md` is the strategy and the cloned template is how it looks**: point antislop at both, the chosen direction and the design-grammar inventory in `section-purpose-map.md`. antislop filters what we add and write. It never restyles the Phase A clone; a finding against the inherited template goes into the rebrand plan as a proposal, not an edit.
- `copywriting` drafts; `antislop-copywriting` filters. Neither overrides the ban on invented facts: reviews, prices, contact details and results still come only from the facts file.

## Live showcase standard (every site, Phase C)

Most of these sites go up before the client pays, as a **near-final pitch**: it must read as about 99% done. Nothing on it says preview, prototype, demo or coming soon, and every form really captures what is submitted (signups to `/api/subscribe`, the primary inquiry form to `/api/inquiries`). Every site ships with: a signup popup + inline signup that really save to D1 through `/api/subscribe`, a cookie banner that really gates analytics, a privacy page that matches, and a second language (Spanish for RGV / Texas clients) on every page, form and popup. The signup hook fits the business (juice bar → new drinks, seasonal specials, birthday treats; home builder → new-home alerts). Details and the hook table are in `client-web-delivery` → “Live showcase standard”. Put the promise and the email-tool choice on the setup-list. Showcase deploys go to `*.workers.dev` first, with `noindex`. Removing `noindex` belongs to step 5, after the client buys and the real domain is on.

## What each later skill actually is

**`launch-audit`** — ship / don’t-get-sued gate. Privacy policy on `/privacy` (what you collect including newsletter fields, cookie/analytics choice, AI use, font/analytics third parties), a signup that saves a row, a banner that gates analytics, real testimonials only, view-source not empty, custom 404, unique titles, OG image, schema, canonical, robots that allow AI crawlers, sitemap, alt text, no secrets in the build.

**`seo`** — growth after launch. Classic search, Google Business Profile / “near me,” and getting cited by AI assistants. Never invent keyword volumes. If this is a rebuild of a live site, snapshot old URLs and rankings **before** step 3.

## Agent rule

On a new client clone, read this skill first and run the **Required companion skills** check, then start at step 0 and open **only the current step’s** skill. Name the step out loud (“step 2, clone-intake”). When architecture is being chosen, say “Current step: Architecture / Setup”. When the user jumps ahead (“do SEO”), say which step they skipped and what is missing.

## PRD gate

Step 1 is not done without a `PRD.md` (template: `client-web-delivery` → `assets/prd-template.md`).

- **PRD supplied** (file, doc, link): read it first, keep its decisions, add a labeled supplement for gaps. Never overwrite it.
- **Seed PRD** (a text file whose content is only the client's current website link, or that link plus a few notes): a seed even when the file is named `PRD.md`. It is not a brief and not approved. Keep its bytes (if it is named `PRD.md`, copy it unchanged to `PRD.seed.md` first). Open the site and their public profiles, put publishable facts in `src/data/`, save their photos and logo to `reference/` with rights noted, snapshot the old URLs for redirects (`seo`), then write the full `PRD.md` at status `draft`.
- **No PRD:** say it is required for a client rebrand, draft it from what is known, mark `UNKNOWN`s, and get approval (the builder approves a near-final pitch; the client approves production).
- **`reference-only`:** a light PRD lets Phase A run; client-facing Phase B/C waits for the full brief.
- The PRD holds intent; `src/data/` stays canonical for publishable facts. Conflicts between them are surfaced, not silently resolved.
- The PRD never changes Phase A.

## Creative direction gate

Step 0 is not done without a `creative-direction.md` (template: `brand-discovery` → `assets/creative-direction-template.md`).

- Client-facing Phase B needs an approved PRD **and** an approved creative direction: the client's approval for production, the builder's (labeled a guess) for a near-final pitch. A draft blocks settling the look as final, not the research, the media inventory or the rebrand plan.
- `reference-only` skips step 0; Phase A runs as a pure fidelity clone.
- The PRD is canonical for the business, `creative-direction.md` for how it comes across. Conflicts between them become questions, never silent overwrites.
- A template the user loves is not an approved direction. `clone-intake` checks the fit before Phase A; the direction never changes Phase A.

## Sources of truth

| What | Where |
|---|---|
| How the business should come across: impression, voice, look, motion, what to avoid | `creative-direction.md` |
| Business intent and strategy | `PRD.md` |
| Client facts | one `src/data/` file |
| Architecture | `architecture-plan.md` |
| Missing client facts | the setup-list |
| Visual reference | clone-intake evidence |
| What each client file actually shows | `media-inventory.md` (Phase B) |
| Why each section says what it says | `section-purpose-map.md` (Phase B) |
| Proof that conversions work | `conversion-acceptance.md` (launch-audit) |
| What actually shipped | the source and the production build |
| What the client is told | `deliverables/client-handoff.md` |

Do not invent a fact to fill the data file, and do not invent a service to fill the architecture plan. If a business answer would change the architecture and cannot be inferred, put that question on the setup-list in business language (“Should a booked time disappear for everyone else immediately?”), not as a vendor quiz (“Supabase or Convex?”).

## Architecture gate

Do not start Phase C, and do not provision a database, auth, object storage, or a server runtime, unless `architecture-plan.md` exists and names that system with a reason. Astro stays the framework unless the user explicitly overrides it. Cloudflare Workers is the standard host for every project; a site already live elsewhere moves over as a named step in the plan, with the old URL redirected. A static marketing site stays static: no login, no R2, no server-rendered pages, just because those exist. The only standing exception is the capture API Worker + D1 from the live showcase standard: a `subscribers` table, plus an `inquiries` table when the PRD's `primary_action` is a form.

## After step 5

Return to `client-web-delivery` for the client handoff (`deliverables/client-handoff.md`, then the visual prompt). That is not a step you can run instead of the audit or SEO. The handoff describes only what production actually has.
