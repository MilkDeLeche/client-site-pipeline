---
name: seo
description: Full SEO, local SEO and GEO/AEO practice — audit, fix, rank, and get cited by AI assistants. Use for any search-visibility work: "SEO audit", "why aren't we ranking", "technical SEO", "Core Web Vitals", "robots/sitemap/canonical", "schema markup", "meta tags", "keyword research", "content strategy", "internal links", "broken links", "backlinks", "Google Business Profile", "local pack", "rank near me", "NAP", "get recommended by ChatGPT", "AI visibility", "GEO", "AEO", "llms.txt", "index this page", or launching/migrating a site without losing rankings.
---

# SEO

**Pipeline step 5 of 5** (`client-site-pipeline`). Previous: `launch-audit`. Do not skip the launch audit. If this is a rebuild of a live site, snapshot old URLs and rankings before `clone-workflow`.

Search visibility across three surfaces that now matter equally:

| Surface | Won by | Reference |
|---|---|---|
| **Classic search** — ten blue links | Crawlability, content, links | `references/technical.md`, `references/content.md`, `references/links.md` |
| **The map pack** — "near me", local intent | Google Business Profile, NAP consistency, reviews | `references/local.md` |
| **AI answers** — ChatGPT, AI Overviews, Perplexity | Being the extractable primary source about yourself | `references/geo-aeo.md` |

**For a local business, the map pack outranks everything else in revenue terms.** A juice bar does not need a blog. It needs a claimed Google Business Profile, consistent NAP, review velocity, and `LocalBusiness` schema. Start at `references/local.md` and don't let a content calendar distract from it.

---

## Before anything: the two rules

**1. Never invent a number.** No search volumes, no keyword difficulty, no traffic estimates, no "SEO score: 73/100" unless a real tool produced it. If you have no data, say so and state what you'd need. A fabricated audit score is worse than no audit — the client acts on it.

**2. Measure, don't assume.** Fetch the robots.txt. Read the rendered HTML. Run the Lighthouse pass. Check the actual status code. Almost every SEO claim is cheaply verifiable, so verify it. Where you infer rather than measure, label it: `measured` / `inferred` / `assumption`.

---

## Route the request

Most asks are one job, not the whole program. Match and jump:

| They said | Go to |
|---|---|
| "audit my site" / "why aren't we ranking" | **Audit** below, then the phased program |
| "we're launching / rebuilding / changing domain" | **Migration** below — do this *before* launch |
| "rank for "near me"" / "show up on the map" | `references/local.md` |
| "get recommended by ChatGPT" | `references/geo-aeo.md` |
| "add schema" | `references/schema.md` |
| "what should we write about" | `references/content.md` |
| "fix our links" / "orphan pages" / "404s" | `references/links.md` |
| "index this now" | `scripts/google-index.js` — setup and usage in `references/technical.md` |
| "is it working" / monthly report | `references/measurement.md` |

For a full engagement, run the phased program. Otherwise do the one job well and mention what else you saw.

---

## Audit

One audit, not three. Work top-down — a page that can't be crawled doesn't need its title tag optimized.

1. **Can it be reached?** robots.txt, sitemap, status codes, redirect chains, `noindex`, canonicals.
2. **Can it be read?** Fetch the raw HTML, not the rendered DOM. Is the body copy in the source, or does it need JavaScript? This is the single most common silent killer on JS-framework sites, and it breaks AI citation completely.
3. **Is it fast enough?** LCP < 2.5s, INP < 200ms, CLS < 0.1. Field data (CrUX) over lab data where available.
4. **Is it understandable?** One H1, sane heading order, unique titles and descriptions, alt text, schema.
5. **Is it connected?** Orphan pages, click depth, anchor text, broken links.
6. **Is it findable locally?** (local business only) GBP claimed, NAP consistent, categories right.
7. **Is it citable?** (see `references/geo-aeo.md`) Facts stated plainly, AI crawlers allowed.

Report findings as: **issue → evidence → fix → effort**. Order by impact, not by category. Nobody needs a 40-item list where item 1 is "add a trailing slash" — lead with what changes rankings.

Full checklists: `references/technical.md`.

---

## Migration — do this before the rebuild launches

The most expensive SEO mistake is relaunching a site and silently dropping every ranking. If a site is being rebuilt or moved, this comes first, before design and before content.

1. **Inventory every live URL** — crawl it. Save URL, title, H1, type.
2. **Snapshot rankings** — ask for the Search Console performance export, last 3–6 months. Record top pages by clicks and every keyword in positions 1–20. Without this you cannot prove what you lost or kept.
3. **Snapshot backlinks** — which pages have earned links. Those URLs must survive or redirect.
4. **Build the redirect map** — old URL → new URL, 301, one hop, no chains. Mark unknowns `[TBD]` and resolve every one before launch.
5. **Verify after launch** — fetch each old URL, confirm a single 301 to the right place. Not a 302. Not a chain. Not the homepage — a URL redirected to the homepage is treated as a soft 404 and loses its equity.

A common trap in this repo's own stack: mockups ship `<meta name="robots" content="noindex, nofollow">` deliberately. **Flipping that on launch day is a launch-blocking checklist item.** Grep for it before going live.

---

## The phased program

For a full engagement. Track state in `SEO-PROGRESS.md` at the project root so any session can resume. Phases can be entered directly if earlier ones are already done — don't force a client through Phase 00 for a schema question.

| # | Phase | Output |
|---|---|---|
| 00 | **Baseline** | Audit, Core Web Vitals, rankings snapshot, competitor set, AI-citation baseline. Nothing is fixed yet — this is the before photo, and without it nothing later can be proven. |
| 01 | **Technical** | Redirects verified, robots/sitemap/canonicals correct, CWV fixes, titles and descriptions rewritten, Organization + LocalBusiness schema live. |
| 02 | **Local** | *(local business)* GBP claimed and complete, NAP fixed everywhere, categories, photos, review system running. Usually the highest-ROI phase — do it before content. |
| 03 | **Keywords** | Clustered keyword map, one cluster per page, mapped against existing pages, cannibalization flagged. |
| 04 | **AEO structure** | Answer-first intros, question headings, FAQ blocks + schema, author bios, dates. |
| 05 | **Content** | Pillar and cluster pages produced against briefs. |
| 06 | **Entity** | Consistent brand description everywhere, directory and citation coverage, press page, Wikidata if eligible. |
| 07 | **Schema & AI access** | Full schema coverage, AI crawlers allowed, `llms.txt`, server-rendering confirmed. |
| 08 | **Links** | Unlinked mention reclaim, broken-link replacement, digital PR, prospect list. |
| 09 | **CTR & UX** | High-impression / low-CTR pages rewritten, engagement fixed, CTAs matched to intent. |
| 10 | **Measurement** | Before/after against the Phase 00 baseline. Monthly report template. |

Working style: one task at a time, show the result, then continue. Ask for the client's own data (Search Console, GA4, GBP Insights) rather than guessing at it. If something is broken, fix it before moving on.

---

## Honesty about SEO

State these plainly when they come up. They protect the client and they protect you.

- **Timelines.** Technical fixes show up in weeks. Content and links take months. Local pack movement can be fast — a well-optimized GBP can move in days. Anyone promising rankings by a date is guessing.
- **No guarantees.** You control inputs, not Google's ranking output. Sell the work, not a position.
- **AI citation is influence, not a lever.** You can make a brand the clearest, most extractable source about itself. You cannot make a model say it. Models also update on their own schedule — expect months, not days.
- **Don't buy links.** It's a manual-action risk and it wastes money. Earn them or do digital PR.
- **Review gating is illegal in the US** (FTC) and against Google's policy. Ask every customer, not just the happy ones.
- **Never fabricate reviews, testimonials, press logos or credentials.** If the client hasn't earned it, don't render it. Substitute something true.
