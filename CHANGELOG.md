# Changelog

All notable changes to this pipeline are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
