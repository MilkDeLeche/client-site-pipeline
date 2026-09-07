# Links — internal, broken, and earned

## Internal linking

The most controllable ranking lever there is. No outreach, no waiting, no budget — and most sites do it badly.

It does three things: helps crawlers discover pages, passes authority from strong pages to weak ones, and tells Google which pages are related and which matter.

### What to look for

**Orphan pages** — nothing links to them. Effectively invisible; often the entire reason a page never ranked. Find them by diffing the sitemap against every internal link target.

**Click depth** — how many clicks from the homepage. Anything past three is treated as unimportant. Money pages should be one or two.

**Dead ends** — pages that link nowhere. The reader stops, and so does the crawler.

**Weak anchor text** — "click here", "read more", "learn more". The anchor tells Google what the target page is about; generic anchors throw that away.

**Over-linking** — 100+ links on one page dilutes each one. Navigation and footer links count.

**Missing reciprocity within a cluster** — pillar links down, cluster pages should link back up and sideways to siblings.

### Fixing it

Hub and spoke: pillar links to every cluster page, each cluster page links back to the pillar and to two or three siblings. Contextual in-body links beat sidebars and footers — Google weights position.

Anchor text should describe the destination and vary naturally. Identical anchors on every link to one page reads as manipulation.

Footer links are the weakest kind. Use them for genuinely important evergreen pages only, not as a keyword dumping ground.

---

## Broken links

**Internal 404s** waste crawl budget and strand readers. Find them by cross-referencing every `href` against the actual route list — in a codebase this is fully automatable and worth scripting.

**External 404s** accumulate on their own as other sites change. Audit periodically.

**Backlink 404s** are the expensive ones: another site links to a page of yours that no longer exists, and all of that authority evaporates. Find them in Search Console under Pages → Not found (404), sorted by referring links, then 301 each to the closest relevant live page.

**Redirect chains.** A → B → C loses value at each hop and slows the page. Update the source link to point at the final destination. Three or more hops and Google may stop following.

Redirect to a *relevant* page. A redirect to the homepage is treated as a soft 404 and passes nothing.

---

## Earning links

Slow, hard, and the thing that separates sites that rank from sites that merely have good pages. There is no shortcut. Do not buy links — it's a manual-action risk and the money is wasted.

Roughly in order of effort-to-return:

**Unlinked mentions.** Someone already wrote about the business without linking. Search the brand name, find them, ask. Highest conversion rate of any outreach because the relationship already exists.

**Local links** — for a local business, by far the easiest wins. Chamber of commerce, tourism board, local press, sponsorships, nearby non-competing businesses, "best of" roundups. Detail in `local.md`.

**Broken link replacement.** Find a dead page in the niche that has inbound links, offer yours as the replacement. Genuinely useful to the person you're emailing, which is why it works.

**Digital PR.** Original data, a survey, a local story with a human angle. Journalists need something to write about; a press release does not qualify.

**Linkable assets.** A tool, a calculator, a genuinely definitive guide, original research. Things people cite because they need to.

**Guest posts** on real publications with real audiences. Not guest-post farms — those are a footprint Google already recognizes.

### Outreach

Short. Four sentences. Say what you found, why it's relevant to their page, and what you're asking for. Personalized to that page — if the email would work unchanged for a hundred sites, it will convert on none of them.

### Assessing a link

Relevance to the topic first, then genuine authority, then whether real people read it, then whether it's editorially given rather than paid or dropped in a comment. One relevant link from a local news site beats fifty directory listings.

### Toxic links

Mostly a non-issue now — Google ignores most junk automatically. Disavow only for a manual action or an obvious negative-SEO attack. Routine disavowing does more harm than good.
