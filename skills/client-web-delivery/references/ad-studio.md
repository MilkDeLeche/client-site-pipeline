# Weekly ads with Krea Ad Studio

A standing routine, not a step: a few finished static ads every week, for the builder's own agency (its own marketing) and, when a client's plan includes marketing, for that client. Krea's Ad Studio makes each ad from a brand kit and a product: it picks the layout, the copy and the art direction. The routine's job is to feed it only true material, keep the lines researched, check every ad before anyone sees it, and remember when the next batch is due.

## Two ways to run it

Ad Studio has two buttons: **Generate in Krea** (the builder, in the app) and **Generate in Claude** (an agent, through the Krea tools). Same brand kit, same products. Whichever runs it, the pipeline leaves a **kit sheet** in `deliverables/ads/ad-studio-kit.md` (template: `assets/ad-studio-kit-template.md`): every box on Ad Studio's "Setup Brand Kit" page filled with approved values, the weekly steps, and this week's five lines with their instructions ready to paste. It is written when a brand's ads start (the builder's own agency, or a client whose plan includes marketing) and updated each batch, so the workflow is never lost between weeks.

Once a site is live with only cleared content, its address can go into "Fill from yourbrand.com" to build the kit; then fix anything that looks off from the sheet.

## The brand kit, once per brand

Build it by hand with `ad_studio_create_brand_kit`, from facts the owner already approved. Ad Studio can also research a kit from a website (`ad_studio_research_brand_kit`), but that pulls whatever the site shows, including client names, prices and claims nobody has cleared. Use research only for a site whose every word is approved, then read the kit back and correct it.

| Field | Where it comes from |
|---|---|
| Name, logo, colors, fonts | `brand-kit.md`, or the brand board's found values |
| Tagline | A line the owner picked (`language-bank.md` section 7) |
| Description, audience | `PRD.md`: what they do, for whom, where |
| Tone | The owner's voice rules (`language-bank.md` section 4, the copy-voice notes) |
| Aesthetic | The chosen direction (`creative-direction.md` section 7), plus "no stock people, no invented faces" |
| Selling points | Things the business really does, in plain words. No results, no numbers |
| Products | One per service or plan, with its approved description and **real images**: the client's own work, real screenshots of the site, and the Instagram mockups (`mockups.md`). Leave the price empty until the owner says the site shows prices |

Images must be public URLs or uploads (`get_upload_url`, then a POST of the file). Before uploading a mockup, check what its screen shows: nothing the owner hasn't cleared (client names, prices) may be legible, because the ad can enlarge it.

Record the kit's ID and each product's ID in the builder profile (`ads.brands`) and in the brand's ads log.

## Each week: one batch

The builder's default is five ads a week per brand (`ads.per_week` in the profile).

1. **Trend check, ten minutes.** Pinterest, Reddit and Meta's Ad Library, dated, in the log: which formats, hooks and ratios are working for this kind of business right now, and what local competitors are running. Take the structure, never a line. Reddit can be hard to reach from an agent: say so in the log rather than calling a thin search a trend check.
2. **Plan the batch** in the log before generating. Each ad gets a product, a ratio, and a line:
   - Rotate products so every service gets a turn, and rotate ratios: 9:16 for Reels and Stories, 4:5 for the feed (Meta's recommended feed shape), 1:1 now and then.
   - **Lines come from niche ad research, not from the website.** A hero line welcomes someone who already came; an ad has to stop an owner scrolling past. Each ad speaks to one niche: who it's for (a small call-out line), the problem they haven't put into words, then the payoff in an everyday phrase. Take them from the trade's "Ad hooks by niche" in `copy-bank` (`industries/`), and add to it every batch: the buyers' own words, what competitors in the area are running now in Meta's Ad Library (facebook.com/ads/library: it shows any page's live ads), and the formats working this week. Write at least five candidates per niche, filter them the `copy-bank` way, and log new ones back. Owner-picked hero lines are a fallback, not the plan. No line repeats within four weeks.
   - **One product, one kind of photo.** A product whose images show different things (a house and an engine) lets Ad Studio pick the wrong one. Split it.
   - **Ask for a native-post look:** the real photo big, the line in bold type, little else. Ads that look like ads get scrolled past.
3. **Generate once each** with `ad_studio_generate_ad`, one call per ad. Pass the line as an exact headline and the guardrails as instructions: no prices, no numbers or statistics, no reviews, quotes or star ratings, no people's faces, and the only other words are the brand name and a short call to action. Generate the first ad alone and compare the balance before and after, so the batch's cost is known, and stop if it would pass the profile's credit budget.
4. **Download every ad** into `deliverables/ads/<YYYY>-w<NN>/` (the gitignored deliverables folder) with a name that says the product and the ratio.
5. **Look at each one and gate it.** Ad Studio writes its own copy, so read every word on the image:
   - A claim the business can't back (a number, "best in the Valley", a guarantee, a review), a price, a face, another company's logo, or misspelled text fails.
   - Their real work must still be recognizable as theirs.
   - A failed ad is marked `failed` in the log with the reason. It is not regenerated unless the builder asks, and a retake costs the same again. Small faults (a stray word in a corner) can be fixed in code: crop, mask, or set the type again.
6. **Log the batch** and set the next due date (seven days on).
7. **Hand over:** the folder, which ads passed, and a caption for each (researched, through `copywriting` and `antislop-copywriting`, with the place tags from the market read). The builder or the owner posts. The agent never posts, and never runs paid ads: spending money on a placement is the builder's call, made in the platform.

## The ads log

`deliverables/ads/ads-log.md` in the brand's project (template: `assets/ads-log-template.md`). It holds the kit and product IDs, every batch with its date, trend note, lines, cost and results, the lines already used, and the **next batch due** date.

## Coming back

At the start of any session, check each brand in the profile's `ads.brands`: if its log's next due date has passed, say so before anything else, in one line, with the week number:

> It's week 2 for Timeless Media: run five more? (Last batch 2026-11-13, about N credits.)

On a yes, run the week from step 1. On a no, move the due date and note why. When a client's plan stops including marketing, mark the brand `paused` in the profile.

## What it isn't

- Not proof of results. Never put an ad's reach, clicks or sales on a deliverable unless the owner shows the numbers from the platform.
- Not the hype set. Hype cards sell the website to the owner; weekly ads sell the business to its customers.
- Not a replacement for real footage. When the client sends new work, add it to the products before the next batch.

## Done when (each week)

- [ ] Trend note dated in the log
- [ ] Batch planned: products, ratios, lines with their sources
- [ ] First ad's cost measured; the batch stayed inside the budget
- [ ] Every ad downloaded, read word for word, and marked passed or failed with a reason
- [ ] Captions written for the passed ads
- [ ] Next due date set, and the builder told where the folder is
