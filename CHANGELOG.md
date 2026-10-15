# Changelog

All notable changes to this pipeline are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
