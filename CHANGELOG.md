# Changelog

All notable changes to this pipeline are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] — 2026-09-07

Initial release. Six skills:

- `client-site-pipeline` — orchestrator; enforces the five-step order and refuses to skip ahead.
- `client-web-delivery` — intake, the client setup-list, pre-launch gate, deploy. Includes `assets/setup-list-template.md`.
- `clone-intake` — the checklist that gates cloning: live URL + repo `.txt` DOM dumps + motion video.
- `clone-workflow` — the non-negotiable Phase A (verbatim clone, verified against the screenshot/video) → Phase B (content-only rebrand) gate; `ffmpeg` motion-reading; content-integrity rules.
- `launch-audit` — technical + legal ship-readiness on the production build. Includes `scripts/audit.sh`.
- `seo` — SEO / local / GEO-AEO practice with seven reference docs and `scripts/google-index.js`.
