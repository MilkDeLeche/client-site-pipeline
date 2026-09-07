---
name: client-web-delivery
description: A safe, repeatable workflow for delivering a client website end-to-end — intake, build, the "what we need from the client" setup-list, the pre-launch gate, and deploy. Use when starting or finishing a client website project, when the user asks "what do I need from the client", wants a client setup / onboarding list or handoff document, wants to hand a project off, or wants a professional / safe / repeatable workflow for shipping client sites. Produces a per-project setup-list (from assets/setup-list-template.md) tailored to whatever external systems the site connects to (payments/POS, booking, CMS, email, maps, analytics, fonts, chat). Ties in the `launch-audit` skill (the pre-launch gate) and the `seo` skill (post-launch growth). Runs per-project.
---

# Client Web Delivery

**Pipeline step 1 of 5** (`client-site-pipeline`). Next: `clone-intake`. Do not clone a template until this step has a setup-list and a single `src/data/` file for client facts.

A repeatable, professional workflow for shipping a client website without surprises. Five stages. The signature artifact is the **setup-list**: one page of everything you need FROM the client, so you never chase them for it piecemeal.

## Stage 1 — Intake (before building)

Pin down, in writing:

- Business identity, target market, and the ONE goal of the site (book / call / buy / lead).
- **Where the money and the data live:** which external systems will this site connect to or hand off to? (POS / payments, booking / scheduling, CMS, email / CRM, maps, analytics, chat.) This single question determines the whole setup-list.
- Brand assets on hand vs. missing (logo, photos, fonts, copy, reviews).
- Domain: owned or to buy.

## Stage 2 — Build

Build the site. Keep every client-supplied fact in ONE data file so it's swappable. **Do not invent facts** (prices, reviews, credentials, results) — leave a clear placeholder and add the real item to the setup-list.

## Stage 3 — The setup-list (what you need FROM the client)

Copy `assets/setup-list-template.md` into the project, fill it in for THIS client, and send it. What you request depends on what the site connects to — use the map below. Golden rule: **collect everything once, in one document.**

### Integration → what to request

| The site connects to… | Ask the client for… |
| --- | --- |
| **Clover** (payments/menu) | Hosted-checkout private token + Merchant ID; a second API token scoped Inventory/Orders/Merchant. |
| **Stripe / Square** | Publishable + restricted/secret keys — or connect through their own dashboard / OAuth. |
| **GlossGenius / external booking** | Usually **nothing** — booking and payment happen there; just confirm the booking URL(s). |
| **A CMS (Sanity, Contentful, Keystatic…)** | Project ID / dataset / a read token, or an invite to the space. |
| **Email / newsletter / contact forms** | The destination inbox; an API key if using a form service. |
| **Google Maps / Business Profile** | Confirm the exact NAP (name, address, phone); claim/verify the GBP. |
| **Analytics** | Which tool; any consent/cookie requirements for their region. |
| **A licensed font or stock asset** | Proof of license — or approval to swap for a free equivalent. |

Always also request: **domain**, **public phone + email to publish**, **team/staff photos + bios**, **real reviews + permission to use names**, **factual/medical/legal sign-off** on any regulated copy, and **rights to any AI or stock imagery**.

## Stage 4 — Pre-launch gate

Before shipping, **invoke the `launch-audit` skill** and clear its checklist: non-empty view-source, 404, unique titles, OG image, structured data, canonical, robots-allows-AI, sitemap, lang, alt text, no exposed source maps or secrets, and the legal items (a privacy policy disclosing data collection + AI usage + third-party processors, and real testimonials). Fix the ❌s you can; keep client-blocked items on the setup-list.

## Stage 5 — Deploy + verify

- Get a **green production build locally first**.
- Ship: `git push` to the deploy branch (Vercel/Netlify auto-deploy) or the platform's deploy command.
- **Verify the live URL, not just the build** — load the real pages and confirm the deploy went green in the host dashboard.
- Set the real **domain** and the framework's **site/base URL** so canonical, OG, and sitemap point at production.

## After launch → growth

Hand off to the **`seo`** skill for Google Business Profile, keyword/content strategy, internal links, Core Web Vitals, and AI-assistant visibility (GEO/AEO).

## Safety rules (the "professional" part)

- One data file for client facts; one setup-list for client asks.
- **Never receive secrets or keys over chat/DM.** The client pastes them into their own dashboard or a secure vault; your code references env vars.
- Don't fabricate prices, reviews, credentials, or results — placeholder + request.
- Disclose AI usage; label AI/stock imagery as illustrative, not real outcomes.
- Green build → push → verify live. Never "push and hope."
