# Technical SEO

Ordered by consequence. A page that can't be crawled doesn't benefit from a better title tag.

## 1. Crawlability

**robots.txt** at the domain root.
- Not blocking CSS or JS — Google needs them to render the page
- No accidental `Disallow: /` (the classic: a staging file promoted to production)
- Sitemap referenced: `Sitemap: https://example.com/sitemap.xml`
- AI crawlers handled deliberately — see `geo-aeo.md`

**XML sitemap.**
- Only canonical, indexable, 200-status URLs. No redirects, no `noindex`, no 404s.
- Accurate `<lastmod>`. A file claiming everything changed today is ignored.
- Under 50,000 URLs and 50MB per file; use a sitemap index above that.
- Astro: `@astrojs/sitemap`, and set `site` in `astro.config.mjs` or the URLs come out wrong.

**Crawl directives — check for conflicts.** `noindex` plus a canonical pointing elsewhere is contradictory and Google resolves it unpredictably. Check both `<meta name="robots">` and the `X-Robots-Tag` header; the header wins and is easy to forget.

## 2. Indexation

**Status codes.** 200 for live pages. 301 (not 302) for permanent moves. 410 for intentionally removed content — it de-indexes faster than 404. No redirect chains, no loops, no 5xx.

**Canonicals.** Self-referencing on every page. Absolute URLs. One canonical per page. Pick one host (`www` or bare) and one protocol and redirect the rest in a single hop.

**Duplicate content.** Trailing-slash variants, uppercase URLs, query-parameter versions, print views, paginated archives. Each needs a canonical or a redirect.

**`noindex` on staging and mockups.** Correct while pitching, launch-blocking afterwards. Grep before launch:

```bash
grep -rn "noindex" src/ dist/
```

## 3. Rendering — check this early

Fetch the raw HTML and confirm the content is in it:

```bash
curl -sL https://example.com/page | grep -c "distinctive sentence from the page"
```

Zero means client-side rendering. Google will usually get there eventually; AI crawlers usually won't, and it delays indexing regardless. Astro static output passes. SPA routing does not.

## 4. Core Web Vitals

Thresholds, at the 75th percentile of real users:

| Metric | Good | Needs work | Poor |
|---|---|---|---|
| LCP — Largest Contentful Paint | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| INP — Interaction to Next Paint | ≤ 200ms | ≤ 500ms | > 500ms |
| CLS — Cumulative Layout Shift | ≤ 0.1 | ≤ 0.25 | > 0.25 |

Field data (CrUX, in Search Console) beats lab data (Lighthouse). Lighthouse tells you *why*; CrUX tells you *whether*.

**LCP** — usually the hero image or a web font. Serve modern formats, size correctly, `fetchpriority="high"` on the hero, and never lazy-load it. Preconnect to font origins; `font-display: swap`. Get TTFB under 200ms, which for a static site means a CDN.

**INP** — main-thread work. Defer third-party scripts. Break up long tasks. Chat widgets, analytics and tag managers are the usual culprits; load them last.

**CLS** — always dimensions. `width`/`height` on every image, reserved space for embeds and ads, no content injected above existing content, `font-display: swap` with a metric-matched fallback to limit the reflow.

**Astro specifics.** Ship zero JS by default — only hydrate what needs it, and prefer `client:visible` over `client:load`. `<Image />` from `astro:assets` handles dimensions and formats. Astro inlines small stylesheets and scripts into the HTML rather than emitting separate files — don't conclude an asset is missing because `dist/_astro/` looks empty; grep the HTML.

## 5. Meta and head

- **Title** — 50–60 characters, unique per page, primary term early, brand at the end. Google rewrites about half of them; write it well anyway.
- **Meta description** — 150–160 characters. Not a ranking factor; it is a click-through factor.
- **Open Graph and Twitter Card** — `og:title`, `og:description`, `og:image` (1200×630, absolute URL), `og:url`, `twitter:card`. Controls how the link looks when shared, which is where a lot of first impressions happen.
- **Viewport** — `width=device-width, initial-scale=1`.
- **`lang`** on `<html>`, and `hreflang` if multilingual.

## 6. Structure and content signals

One `<h1>` per page. No skipped heading levels. Descriptive alt text on meaningful images, empty `alt=""` on decorative ones. Clean lowercase hyphenated URLs, shallow depth. Internal links with real anchor text — see `links.md`.

## 7. Security and delivery

HTTPS everywhere, no mixed content, HTTP→HTTPS in one hop, HSTS. Brotli or gzip. HTTP/2 or HTTP/3. Cache headers on static assets. No exposed `.env` or `.git`.

---

## Fast indexing

For new or substantially changed pages. This skill ships a script that submits to Google's Indexing API. Run it from the skill directory — the working directory is the user's project, not here:

```bash
node ~/.claude/skills/seo/scripts/google-index.js https://example.com/new-page
```

One-time setup: create a Google Cloud project, enable the **Web Search Indexing API**, create a service account, download the JSON key to `.google-indexing-key.json` (and gitignore it — it is a credential), then add the service account's `client_email` as an **Owner** in Search Console for that property.

Quota is 200 URLs/day per project. Submit new and changed pages only; resubmitting unchanged URLs wastes quota and does nothing.

Errors: `403` means the service account isn't an Owner in Search Console. `400` means the URL doesn't match the verified property. `429` means quota exhausted.

Note that Google officially supports this API for `JobPosting` and `BroadcastEvent` only. It works more broadly in practice, but it is not a guarantee, and it is not a substitute for a correct sitemap.

---

## Reporting findings

Per issue: **what → evidence → fix → effort**. Evidence means a file:line, a URL, or a measured number — not an assertion.

Order by impact. If you give a score, say what produced it. Never invent one.
