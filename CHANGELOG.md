# Changelog

All notable changes to this pipeline are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.6.0] — 2026-10-18

Lessons from shipping the Timeless Media pitch.

- `clone-workflow` Phase B adds **hook voice: finesse, not corn**. The payoff half of a hook is the owner's outcome in an everyday phrase (about five words), section headings are confident labels, and there's no forced slang, stunt lines or instructions as headings. Includes the real before/after rewrites the client chose, and offering two or three options when a hook carries the page.
- `client-web-delivery`: add-ons such as an AI sales chat are opt-in per client, never part of the standard offer; renamed or deleted media keep their old URLs alive through `public/_redirects`; the share image is recaptured whenever hero copy changes (1200x630, under ~300 KB, cache-busted).
- `launch-audit`: the OG check confirms the share image shows the current hero and stays under ~300 KB.

## [1.5.0] — 2026-10-17

- **Required companion skills.** `client-site-pipeline` now checks, before step 1, for `copywriting` (`coreyhaines31/marketingskills`) and the `antislop` pack (`miqdadbadjuber/anti-slop`). If either is missing it stops, names them, and gives the install commands. `install.sh` / `install.ps1` print the same reminder.
- Phase B's copywriter drafts with `copywriting` and filters every line, in both languages, through `antislop-copywriting`; the redline uses `antislop-ui`, `antislop-layoutmobile` and `antislop-human` as the checklist for what Phase B/C added.
- The cloned template is antislop's design direction: it filters additions and never restyles the Phase A clone (findings against the template become rebrand-plan proposals). Neither skill overrides the ban on invented facts.
- `launch-audit` runs antislop's contrast checker and Delivery Gate.
- Phase B runs antislop in **DURING** mode: the copywriter and UX lead write with these skills from the first draft, and Phase B closes with the Delivery Gate report. They are not an after-the-fact rewrite.

## [1.4.0] — 2026-10-15

Phase B is judged by the buyer, not by the slots. Found running v1.3.1 on an agency pitch (Timeless Media): every image and heading was replaced, the page still spoke to nobody, and real client reels sat in a folder while AI mood images held the hero and the service cards.

- `clone-workflow` Phase B (`references/intent-aware-rebrand.md`) defines **done**: someone in the target buyer group sees, on the first screen, that the site is for them, what they'd get, and real proof. Swapping content is the method, not the goal.
- **The room:** Phase B runs as four senior roles, each writing its part before the build: strategist/analyst (buyers by situation, research), copywriter (a hook bank in the buyer's words), art director (media truth and slot assignment), UX/front-end lead (grammar, funnel gaps, build). After the build, each role **redlines** the running page and the misses get fixed.
- **Media-truth inventory** (`media-inventory.md`): every client file is opened and logged by what's actually in frame, its origin (real, AI-generated, stock) and the slots it may enter. Filenames are not evidence. Claim slots (hero, services, proof) take real work whenever it exists; AI images fill true gaps only.
- **Headlines name the buyer's situation** ("Got a bar?"); service titles named after departments are a failed Phase B. Punchy lines are fine; invented reviews, prices, contact details and results are still banned.
- Research has a floor: three peer sites, the industry guidance, the client's best-performing posts, and, for agencies, their buyers' industries.
- The rebrand plan must answer what the page still fails to do and whether an existing section pattern should be duplicated to do it.
- A **draft** PRD blocks an invented positioning, not the research, the media inventory or the plan.
- **Lead capture is a Phase B decision per site type:** the money action (call, order, booking, directions or a form), qualifying fields only where the owner uses them, D1 capture so no lead is lost, and a failure message that hands the visitor a working channel instead of a dead end.
- **Cloudflare Workers is the standard host for every project.** A site already on Vercel or Netlify moves over as a named step with its old URL redirected, never silently.
- **Every site ships a second language** as part of the live showcase standard (Spanish for RGV / Texas clients): `/<code>/` via Astro i18n, one copy file per locale over the same facts, written natively (not translated word for word), `hreflang` + `x-default`, locale stored with each signup and inquiry, and a fluent client review on the setup-list. The PRD, architecture-plan and setup-list templates and the launch audit's lang check follow.
- New gates and anti-patterns to match. **Phase A, the grammar limits and the ban on fake proof are unchanged.**

## [1.3.1] — 2026-10-15

Fixes found by running v1.3 on a real near-final pitch (Kasocri Construction).

- `launch-audit/scripts/audit.sh` checks every built page whichever layout the build uses. With Astro `build.format: "file"` (`dist/about.html`, the static + API Worker default) it used to see only `index.html`/`404.html`, report false duplicate titles and miss `/privacy`. Check [13] now also counts the pages that link to `/privacy`.
- `clone-workflow` Phase B (`references/intent-aware-rebrand.md`): re-measure the fixed header after the logo swap; a taller client logo hides inner-page headings under the template's hardcoded offset.
- `client-web-delivery`: moving a project off the Astro Cloudflare adapter, delete the stale `.wrangler/deploy/config.json`.

## [1.3.0] — 2026-10-14

Intent-aware rebranding. Phase A is unchanged; Phase B now knows what the business needs the site to do.

- `client-site-pipeline` adds a **PRD gate** to step 1: read a supplied PRD and never overwrite it, or draft and approve one. A **seed PRD** (just the client's current website link in a text file) is researched and expanded into the full PRD, never mistaken for one. `reference-only` PRDs allow Phase A only. `PRD.md`, `section-purpose-map.md` and `conversion-acceptance.md` join the sources of truth. Unsold showcase sites are now **near-final pitches**: about 99% done, nothing labeled preview or prototype, every form really captures.
- `client-web-delivery` starts Stage 1 from the PRD (intent: audience, proof, the action that makes money, who answers it) and reconciles the architecture plan with it. The standing D1 exception adds an `inquiries` table when the primary action is a form. New `assets/prd-template.md`.
- `clone-workflow` adds a Phase B strategy gate and the on-demand `references/intent-aware-rebrand.md`: a design-grammar inventory (only the template's buttons, where it places them; its fonts, spacing and section patterns), a section-purpose map, editorial media rules (Krea images as labeled illustrative fill only), funnels by business type, and a **first-screen test** (on phone and desktop the first screen must say what is sold, where, why trust them, and what to do next), one label for the primary CTA everywhere, and the near-final pitch standard. The "PRD first" step now reads a supplied PRD instead of rewriting it. **No Phase A text changed.**
- `launch-audit` adds conditional **conversion journey checks**: a real browser submission, proof the submission was stored or delivered, failure paths, a named owner, server-side conversion counts, and `conversion-acceptance.md`. The existing 17 checks are unchanged.
- `architecture-plan-template.md` records `primary_action`, `completion_route` and `destination_owner` from the PRD (the PRD template uses the same names).
- Inquiry capture is fully specified: `POST /api/inquiries` (columns, honeypot, same-origin, honest success message) joins `/api/subscribe` behind the API Worker, which now serves `/api/*`. The setup-list asks who receives new inquiries, and its numbering is fixed.
- Near-final pitches deploy to `*.workers.dev` with `noindex`; it is removed in step 5 after the sale. A missing fact is hidden, never shown as a placeholder. Fonts stay the template's unless the user directs a brand font.
- Conversion checks read the database the form actually wrote to (local for `wrangler dev`, remote for `workers.dev`), prove `tel:` and external order/booking links by following them, accept pending delivery on a pitch, and check a challenge only when the plan names one.

## [1.2.0] — 2026-10-14

Live showcase standard: client sites are often built before the client pays, so every site ships feeling live.

- `client-site-pipeline` adds the live showcase standard to Phase C and to the launch-audit summary. The architecture gate keeps static sites static, with one standing exception: the email-capture API Worker + D1 subscribers table.
- `client-web-delivery` adds a third Cloudflare mode, **static + API Worker** (`run_worker_first: ["/api/*"]`, no Astro adapter, `build.format: "file"`). It also defines the standard: a signup popup + inline signup saved to D1 via `/api/subscribe`, a cookie banner that actually gates analytics, and a privacy page that matches. It includes a signup-hook table by business type, D1 deploy steps (no `database_id`, schema run by the Worker, clean-clone dry run) and Git-connected Workers deploy settings.
- `architecture-plan-template.md` records `api_worker`, the D1 subscribers table, consent-gated analytics, and the newsletter/cookie feature flags.
- `setup-list-template.md` asks what the signup promises and which email tool will send it, and the privacy item now covers newsletter data, the cookie banner and AI-made images.

## [1.1.0] — 2026-10-06

Architecture planning, without changing the five-step order or the clone gates.

- `client-web-delivery` writes `architecture-plan.md` at intake and `deliverables/client-handoff.md` after SEO. New projects default to Astro on Cloudflare Workers. Database is none, Supabase, or Convex, each with a reason. D1 and KV are not auto-selected. R2 is only for files uploaded after launch.
- `clone-workflow` adds Phase C after the existing Phase A verify and Phase B rebrand. Phase C connects only what the architecture plan selected and does not redesign layout.
- `launch-audit` keeps the existing technical and legal checklists, then checks only the systems the plan turned on (including a two-window test when Convex was chosen for realtime).
- `seo` states that a content strategy is required and a blog is not. The existing “a juice bar does not need a blog” rule stays.
- Legacy hosts (Vercel, Netlify) remain valid when the architecture plan names them. They are no longer the default for a new project.

## [1.0.0] — 2026-09-07

Initial release. Six skills:

- `client-site-pipeline` — orchestrator; enforces the five-step order and refuses to skip ahead.
- `client-web-delivery` — intake, the client setup-list, pre-launch gate, deploy. Includes `assets/setup-list-template.md`.
- `clone-intake` — the checklist that gates cloning: live URL + repo `.txt` DOM dumps + motion video.
- `clone-workflow` — the non-negotiable Phase A (verbatim clone, verified against the screenshot/video) → Phase B (content-only rebrand) gate; `ffmpeg` motion-reading; content-integrity rules.
- `launch-audit` — technical + legal ship-readiness on the production build. Includes `scripts/audit.sh`.
- `seo` — SEO / local / GEO-AEO practice with seven reference docs and `scripts/google-index.js`.
