# GEO / AEO — getting cited by AI

Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO) are the same job: being the source an AI assistant reaches for. ChatGPT, Google AI Overviews, Perplexity, Claude and Copilot increasingly answer the question instead of listing links, and the business that gets named in the answer wins the customer the ten blue links used to deliver.

## What's actually happening

Two different mechanisms, and they need different work:

**Retrieval at answer time.** ChatGPT search, Perplexity and AI Overviews fetch live pages and cite them. This is winnable now and behaves like SEO — you need to be crawlable, extractable, and the clearest answer available.

**Training data.** What the model "knows" without searching. Set months or years ago, not directly editable. You influence it by being consistently and accurately described across the open web, and you wait.

Optimize for retrieval. Let training data accrue.

**Say this to clients plainly:** you can make a brand the clearest, most quotable source about itself; you cannot make a model recommend it. Anyone selling guaranteed AI mentions is selling nothing.

---

## Let the crawlers in

The first thing to check, and frequently the whole problem. Fetch `/robots.txt` and look for:

| Bot | Belongs to | Blocking it means |
|---|---|---|
| `GPTBot` | OpenAI, training | Not in future training data |
| `OAI-SearchBot` | OpenAI, ChatGPT search | **Not citable in ChatGPT** |
| `ChatGPT-User` | OpenAI, user-triggered fetch | Can't be fetched when a user asks |
| `Google-Extended` | Google, Gemini/AI training | Excluded from Gemini grounding |
| `PerplexityBot` | Perplexity | Not citable in Perplexity |
| `ClaudeBot` / `Claude-SearchBot` | Anthropic | Not citable in Claude |
| `Bingbot` | Microsoft | Powers Copilot — **also normal Bing search** |

Many sites block these by accident, inheriting a template or a hosting default. If the client wants AI traffic, allow them.

A real trade-off worth stating rather than deciding for them: allowing `GPTBot` and `Google-Extended` means the content contributes to training with no attribution and no click. For a local business, that's an easy yes — being known is the entire goal. For a publisher whose product *is* the content, it's a genuine decision.

## Server-render the content

Fetch the raw HTML — `curl` it, or read the network response, not the DOM inspector. If the body copy isn't in the source, most AI crawlers will never see it. They are far less patient than Googlebot about executing JavaScript.

```bash
curl -sL https://example.com/page | grep -c "a distinctive sentence from the page"
```

Zero means the content is client-rendered and invisible. Astro static output passes this by default. Client-side React and SPA routing frequently fail it.

## llms.txt

A plain-Markdown file at `/llms.txt` describing the site for language models. Not an established standard and not honored by everyone — but it costs fifteen minutes and it forces you to write down the facts you want repeated.

```markdown
# Feel Good

> Cold-pressed juice bar, açaí bowls and waffles in Brownsville, Texas.
> Local, women-owned, open since 2020. Everything is plant-based,
> dairy-free, gluten-free and made without refined sugar or refined flour.

## Key facts
- Address: 800 N. Expressway 77/83, Suite 17, Brownsville, TX 78521
- Phone: (956) 667-5300
- Hours: Mon–Fri 10am–6pm, Sat 10am–2pm, closed Sunday
- Juice is cold-pressed twice daily in a hydraulic press; unpasteurized,
  non-HPP, never frozen, bottled in glass.

## Pages
- [Menu](https://example.com/menu): full menu with prices
- [Visit](https://example.com/visit): address, hours, directions
- [Our story](https://example.com/story): how the shop started
```

---

## Write to be extracted

An AI needs a self-contained, liftable passage. Most web content buries the answer under three paragraphs of preamble, which makes it unquotable.

**Answer first.** The direct answer in the first two or three sentences, before context, before story. If a model can only take one paragraph, that paragraph must be the answer.

**Question-shaped headings.** `## How long does cold-pressed juice last?` rather than `## Shelf life`. It matches the query and marks a self-contained block.

**Self-contained passages.** Each section should make sense lifted out alone. "As mentioned above" breaks extraction.

**State facts flatly.** "Feel Good is a women-owned juice bar in Brownsville, Texas, open since 2020." Not "we're passionate about wellness." Models repeat facts; they discard atmosphere.

**FAQ blocks.** Real questions, 40–60 word answers, each standing alone, with `FAQPage` schema. The single highest-yield AEO format.

**Structure the comparable.** Tables get lifted whole. Prices, hours, specs, options.

**Dates and authorship.** Visible publish and updated dates, a real named author with credentials. Freshness and attribution both weigh on whether a passage gets used.

**Be the primary source about yourself.** Everything about the business — hours, address, story, what's in the food, why it's made that way — should exist in plain text on the site. If the only description lives on DoorDash, DoorDash gets cited.

---

## Off-site: where AI answers actually come from

For local and consumer questions, models lean heavily on aggregators and communities, not the brand's own site. Being right on your own site is necessary, not sufficient.

- **Reddit** — enormously influential in current model behavior. Not astroturfing: genuine participation where the audience already asks.
- **Review platforms** — Google, Yelp, Tripadvisor. Their content is training data and retrieval fodder.
- **Wikipedia / Wikidata** — if genuinely notable. Wikidata has a much lower bar than Wikipedia and is machine-read.
- **"Best of" roundups and local press** — being in the list is what gets a business named when someone asks for a recommendation.
- **Industry directories** and, for a restaurant, the delivery platforms.

Consistency across all of them is what makes a model confident enough to state something. Contradictory hours across five listings produce a hedged non-answer.

---

## Baseline and measurement

There is no Search Console for this. Test manually and keep the log.

Build a query set of 10–20 real questions a customer would ask — "best açaí bowl in Brownsville", "vegan gluten-free breakfast near me", "where to get cold-pressed juice in the Rio Grande Valley", plus branded ones. Run them across ChatGPT, Perplexity, Google AI Overviews and Claude. Record:

| Query | Platform | Mentioned? | Position | Accurate? | Who was cited instead |
|---|---|---|---|---|---|

Re-run monthly, same queries, same wording. The competitor column is the useful one — it tells you which sources the models trust for this category, and those sources become the target list.

Two cautions. Results vary between runs and between users; treat one test as a sample, not a fact. And check accuracy, not just presence — a confident wrong answer about your hours is worse than absence, and the fix for it is usually a stale third-party listing.
