# The builder's toolkit: how this work gets done, on any computer

This page is for setting up a new computer, or coming back after a break. `scripts/setup.mjs` checks and installs what can be installed. The rest are accounts and sites the builder signs into once. Agents read this page and the builder profile (`~/.client-site-pipeline/builder.json`, private, outside every repo) and don't ask what they already answer.

## The way of working (builder's standing preference, Nov 2026)

- **Everything through the terminal.** The builder doesn't paste API keys around dashboards. A key is created once in the service's own dashboard, then put where it lives with one command (`npx wrangler secret put NAME`), and the agent does the rest: setup endpoints, scripts, deploys, checks. When a dashboard step can't be avoided, the agent gives it one screen at a time.
- **Cloudflare first** (`client-web-delivery` → `references/cloudflare-stack.md`): domain, DNS, site, API, secrets, storage and scheduled jobs on Cloudflare; outside services only for what Cloudflare doesn't do, always through the Worker.
- **Copy from research, never from the model's imagination.** Brand discovery, the market read and Reddit/forum research collect how real buyers talk; `copy-bank` turns that into headlines, tags and hooks; `humanizer` / antislop filter it. The same for brochures, billables and emails.
- **Templates come from the builder's libraries** and are adapted to the client's brand: site templates from Envato, MotionSites, Land-book, Lapa Ninja or Awwwards references; email templates from Copymail.

## Installed by the setup script

Run `node ~/.claude/skills/client-site-pipeline/scripts/setup.mjs`. It checks and installs:

| Tool | For |
|---|---|
| Node 18+ (LTS) | builds, scripts, `npx wrangler` |
| Companion skills: `copywriting`, `antislop` | writing and the slop filter |
| ffmpeg | reading motion out of template videos |
| Google Chrome, Python 3.9+ and the pitch kit packages | pitch kit renders, QR |
| Playwright Chromium + WebKit | the responsive audit (Safari's engine) |
| Wrangler sign-in (`npx wrangler login`) | deploys, secrets, D1, R2 |
| Git and the GitHub CLI (`gh`) | pushing the pipeline repo and client repos |

Wrangler itself runs through `npx` from each project, so it isn't installed globally.

## Accounts to sign into once (the script can't install these)

| Account | What it's for | Where the key goes |
|---|---|---|
| Cloudflare | every site, DNS, Workers, D1, R2 | `npx wrangler login` (browser sign-in) |
| Resend | all email: transactional, automations, newsletters | a full access key per client project, `npx wrangler secret put RESEND_API_KEY` |
| Supabase | the database when a client needs logins and records | connected as an MCP in Claude; the secret key with `wrangler secret put` |
| GitHub | the pipeline repo (public: no client names or keys) and client repos | `gh auth login` |
| Krea | generated images and video (one generation each, quote first) | connected as an MCP in Claude |
| Copymail (lifetime premium) | email template library | browser only: pick a template, share the link or a screenshot |
| MotionSites, Envato | site templates (subscriptions) | browser only |
| Land-book, Lapa Ninja, Awwwards | reference sites for the design scout | browser only |
| Claude in Chrome | reading sites that block plain fetches, checking live pages | the browser extension |

## Claude connectors to turn on (claude.ai → Settings → Connectors)

Supabase, Krea, and Claude in Chrome. Others (Canva, Figma, Google Drive) are optional.

## After a break

Open the project, then read in this order: `pipeline-state.md`, `deliverables/pending-items-of-the-skill.md`, `setup-list.md`. Ask the agent: "what's pending?" and it answers from those.
