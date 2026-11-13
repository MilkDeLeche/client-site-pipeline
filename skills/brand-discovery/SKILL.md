---
name: brand-discovery
description: Pipeline step 0. Find how the client should come across before the PRD and template are settled. Starts with Yes / Skip for now (a skip saves a resumable state). Produces a vibe read from their site, socials or seed link; a market read (the place, competitors, how buyers search, tags, what heroes work); a design scout with a template search brief (reference sites, Land-book filters); an ask-first list and the owner sheet (one fillable PDF: plans, design veto, open facts); what leads and its evidence; named directions with one recommended; a brand kit when they have no real logo; and creative-direction.md with an alignment statement. Sorts every link into template or reference. Use at the start of a client site or pitch, when the user says "start the pipeline", shares a client link, seed PRD or reference sites, when a pitch becomes paid work, or when a client pushes back ("make it simpler", "not my vibe"), sends a competitor's site, goes quiet or won't pick, which goes to feedback diagnosis before any rebuild.
---

# Brand discovery

**Pipeline step 0** (`client-site-pipeline`, steps 0–5). Next: `client-web-delivery`. Produces `creative-direction.md` (template: `assets/creative-direction-template.md`).

A site can be correct, fast and good-looking and still be wrong for the owner. On an agency pitch the build followed the owner's trendy social edits. The owner wanted something much simpler: a site his non-technical buyers could follow, sized to the amount of work he actually had, instead of a "maxed out" agency site. Nobody had asked him. This step asks.

The PRD owns the business: what is sold, to whom, the money action, the proof. This step owns how the business comes across: the impression, voice, look, density, motion, what leads, what to avoid, and which template can carry that. It never repeats PRD fields; it points to them.

| File | Use |
|---|---|
| `references/market-read.md` | The research that stands in for asking: the business, the place, the competition, how buyers search, tags, heroes |
| `references/design-scout.md` | Reference sites for the niche and the template search brief (Land-book filters, Awwwards categories, neighbor trades) |
| `references/brand-kit.md` | Step 0b, only when the owner has no real logo or colors: what exists, a wordmark in type, a symbol with the builder's yes, `brand-kit.md`, the brand board |
| `references/question-bank.md` | Core decisions, showcase emphasis, reference decoding, industry add-ons, Spanish notes |
| `references/feedback-diagnosis.md` | When a client rejects or questions a design |
| `assets/creative-direction-template.md` | The record this step produces |
| `references/owner-sheet.md` | The owner sheet: its three parts, the rules, the commands |
| `scripts/discovery_pdf.py` + `assets/*.example.json` | Builds and reads the owner sheet and the questions-only PDF |

## Two ways a job starts

- **Outbound pitch (the usual one).** The builder goes to the owner with a site already built. Nobody can be asked first, so research does what asking would: the market read and the design scout are how the guess gets close. The builder picks the direction and the template, and builds as many options as they like; templates from a subscription the builder already has (Envato, MotionSites) cost nothing to try. The owner sheet goes out with the pitch or right after it, as the way to steer: "If this isn't it yet, fill this in and we'll get you there."
- **Inbound client.** The owner came to the builder, or has paid. Ask first: the owner sheet goes out before the build.

Either way, when the owner pushes back, find which decision was wrong before rebuilding (section 7).

## Start: run it now, or skip for now

Offer the operator one choice before the homework:

- **Yes:** run the step now.
- **Skip for now:** the usual pick for an unsolicited pitch with no contact yet. Save `creative-direction.md` with status `deferred`, the reason, whatever homework and directions exist so far, and what will resume it. Build the pitch on the builder's guess: write it in §7 as the chosen direction, labeled a guess, so `clone-intake` has something to vet the template against.

Resume when the pitch turns into paid work, the owner replies or books a call, the owner pushes back on a build, or a client returns for a redesign. Resuming starts from the saved file: reread it, mark anything stale, keep every earlier direction, and ask only what is still open. Nothing collected before the skip is deleted. A deferred direction never counts as approved.

A returning client starts the same way: read the existing `creative-direction.md` and its change log first, then ask only what changed since the last approval.

## 1. Homework before any question

Read what exists: the seed link or PRD, their current site, social profiles, Google profile, logo, photos and reels, and any brand or site the owner has mentioned. The same pass fills the PRD's research table, so don't research twice.

Write the **vibe read** at the top of `creative-direction.md`, keeping four kinds of note apart:

- **Confirmed:** what the owner said or approved.
- **Observed:** what their presence actually shows.
- **Guessed:** your hypothesis, labeled as one.
- **Unknown.**

Then record **where they are now** (how much real work exists, what they can honestly promise today) next to **where they want to be** (the impression they're after). Close that gap with selection, hierarchy and truthful storytelling. Never close it with invented clients, inflated credentials, fabricated team members or AI work passed off as theirs.

- Their social style is not automatically the site style. Their posts show what their audience responds to (Phase B uses that); they don't decide how the site looks.
- A business name or logo hints at an aspiration. It is still a guess until the owner confirms it.
- **Read the market, not only the business.** `references/market-read.md`: who lives where they sell, three to five local competitors screen by screen, how buyers search and talk, the tags in use, and what the heroes in this trade lead with. It ends in one page the builder reads before choosing a template, and it supplies the numbers for the hype set's stat cards. On an outbound pitch this is the step that replaces the interview, so don't thin it.
- **Scout the look.** `references/design-scout.md`: five to eight reference sites for the niche (Awwwards, Land-book, Lapa Ninja and the best real businesses in the trade), then a template search brief with the filters and search words that get close, three close and three wide.
- **No real logo or colors?** Run `references/brand-kit.md` (step 0b): keep whatever customers already recognize, propose the rest starting from the name set in type, and mark every proposed part as proposed until the owner says yes.
- **Pinterest and Reddit, every time.** Any look at what is current (heroes, mockups, reels, brand boards, hooks) includes both, dated and written down. Take the structure of what works; never copy a line, a layout or a picture.
- **Check the front door.** Most visitors reach the site from somewhere else first: an Instagram or Facebook page, a Google listing, an ad. Open it the way a buyer would and note whether the name, handle, photo, bio and link match the site about to be built. A mismatch goes in the vibe read as Observed and on the owner sheet as a question. Fixing a social page is its own job with its own scope and price: name it, never fold it into the site quietly. An owner who thinks the front door looks amateur won't launch the site behind it, and will say so about the site.

**Start the language bank in the same pass.** Copy `copy-bank/assets/language-bank-template.md` to the project as `language-bank.md` and fill §1–4 (`copy-bank` §2–3): the buyer situations and how aware each is of the problem, the buyers' own words from reviews, comments and threads (verbatim, with links and dates, in every site language), what peer businesses already say, and the phrases the owner uses about their business. Read the `copy-bank` files for the trade first and add what you find to them. Phase B writes the hooks from this file; a hero written without it is a guess.

## 2. Sort every link: template or reference brand

| | Template | Reference brand |
|---|---|---|
| Signs | A marketplace page, `*.webflow.io` or `*.framer.website`, "Get template" / "Buy", demo copy, fictional clients | A real team, named clients, a registered company, a "website by" credit, real contact details |
| Use | Clone candidate once licensed. `clone-intake` vets the fit. | Study only: their niche, their promise, how they show proof, how a visitor buys. Never clone the look; never borrow the claims. |

**Decode what is admired.** A reference is usually admired for one quality, not the whole site: its visual design, its positioning, its content hierarchy, its credibility, how easy it is to buy from, its volume of work, or something else in the owner's words. Ask which ("What's the one thing you'd take from that site?") and record it per reference. Only that quality transfers; the table in `references/question-bank.md` says what does and doesn't. Envy of a competitor is often about the volume of work, not the interface, and those have different fixes. A good-looking competitor is a pattern, not proof that it converts. A reference is never a template to clone unless it is a licensed template and the admired quality is how it looks.

**Map the argument when they admire how it sells.** When the quality is positioning, content hierarchy or how easy it is to buy, write its argument map under that reference in `creative-direction.md`: the hidden problem it names, how it shows proof, the system it sells, how the offer is structured (services, packages, terms), the objections it answers, and its one CTA. Mark which points the client can honestly make today and which need a fact first (a package, a term, a real result). Phase B follows the map with the client's own facts; the reference's wording, numbers and claims never transfer.

**A link the owner sends after seeing a build is feedback.** "Take a look at this agency" is pushback, even when it sounds like a tip. Log their words in §9, decode the admired quality, write the argument map, and hold it against the current build section by section before anything is designed (section 7).

## 3. The ask-first list

Three to five questions for a text or a call (up to about nine in the PDF), each settling a decision the homework left open. `references/question-bank.md` lists the core decisions every business has and two or three add-ons per industry. Each question:

- is tied to something the homework found ("Your reels are fast cuts and trending audio. Should the site feel like that, or calmer?");
- names what the answer decides: template, density, motion, voice, offer order, or what leads;
- offers concrete options plus **Not sure** and **Other**, with room to explain where the reason matters;
- is ordered so the questions that would change the template come first.

Skip anything the homework already answered. Never send a 25-question form. If a style-picker brief exists (exported from a site's intake form), read it first: its picks are a starting point, and the list asks only what is still missing.

Always settle, in some form, unless the homework already did:

1. Who do you show this to, and what should they say after 10 seconds?
2. Who do you look up to, and what exactly about them?
3. What feels like too much? (when there's a current site or a pitch to react to)
4. What should people see first, and what can you show for it? (section 4)
5. Three words for how you should come across, and what it should never look like.

**Question types that get the real answer fast.** Use them openly. No hidden tracking and no steering: an owner defends a direction they know they chose, and second-guesses one they were led into.

- **This or that:** two concrete options, "go with your gut".
- **React to something real:** show two or three quick versions, or the current site. "Which one, and what bugs you about the others?" Owners can't describe what they want, but they react instantly.
- **No design words:** "If the business were a car, which one?" "What would a customer tell a friend about you?"
- **Why, two or three times:** that's how "minimalist" becomes "I don't want to look like I'm faking a big agency".
- **Never this:** "Which of these is definitely not you?" is easier to answer than "what are you?".
- **Customer before taste:** who visits and what worries them settles many style questions.
- **Unpack vague words:** "simpler" can mean fewer sections, less motion, fewer words or a different template. Ask which before picking a style.

**How to ask.** By text or on a call needs nothing installed. The owner sheet (section 8) carries the same questions with the same ids, next to the plans and the facts only the owner has, so everything open is asked once. Record each answer with its channel, date and the owner's own words.

**Can't ask before pitching?** Pick a direction, record it as approved by the builder and labeled a guess, build the pitch on it, and take the ask-first list to the meeting. The pitch becomes the first "react to something real". If the operator chose Skip for now, the status stays `deferred` until the list is asked.

## 4. What leads, and what proves it

"Show our work" means different things by trade: the products, the craft, the deliverables, verified results, credibility, how the service works, the place, or the people (definitions and typical trades in `references/question-bank.md`). Record two things apart in `creative-direction.md` §4:

- **Desired emphasis:** what the owner wants to lead with.
- **Available evidence:** what exists, where it is, and whether we may use it.

When they don't match, write the gap, lead with an emphasis the evidence can carry, and put the missing evidence on the setup-list. A result is shown only with its source, its date and the client's permission. Never estimate, round up or borrow one.

## 5. Directions

Each direction gets a plain name with the designer's term beside it, so the builder learns the vocabulary ("Calm and spacious (minimal / Swiss grid)"). For each, write:

- what a visitor feels in the first 10 seconds;
- the look: type, color approach, page density, imagery, motion, navigation;
- how the client's real work is used, and what leads;
- what it gives up or risks;
- why the evidence supports it;
- candidate templates, if any are known.

Recommend one. Directions are written in words; mood images can help but are never client proof. If two candidates land on the same direction, say so: a choice only helps when the options feel different.

**How many options to build is the builder's call.** One site or several, on any templates the builder wants to try. Two things keep options useful:

- **They differ on something the owner cares about.** When the owner's words are about what the site says (the offer, the proof, what leads), a different look won't settle it. Change what the first screen says, or put the plans in front of them.
- **When an owner stalls in front of several, stop adding.** Recommend one in a sentence and ask for a veto: "We'd go with this one because you asked for simpler. Anything you'd change?" An owner afraid of choosing wrong answers a veto and stalls on a menu.

## 6. Alignment statement and approval

Copy `assets/creative-direction-template.md` to `creative-direction.md`. Status uses the PRD's words (`draft` / `approved` / `approved-with-blockers`), plus `deferred` for Skip for now.

Before anything is built for the client, write the **alignment statement**: a few plain sentences the owner can read in under a minute. Who the site is for, what they should feel and say, what leads and the evidence behind it, the one action, the three words, what it must never look like, and the direction and template that carry it. The owner approves this statement, not the questionnaire.

The **approval record** says who approved (name and role), the date, the channel, their words or where the evidence is kept, and which version of the statement. These are not approval:

- a returned questionnaire or a filled PDF (it's input);
- silence, or "looks good" on an unrelated message;
- the builder's own sign-off on paid work.

A builder's approval on a pitch is written as the builder's and never presented as the client's; confirm it with the owner when the pitch becomes paid work.

## 7. When the client pushes back

Rejection, hesitation or "something's off" after seeing a design goes to `references/feedback-diagnosis.md` before any rebuild: write down what they said, find which decision is wrong (promise, audience, offer order, what leads, proof, feel, density and motion, navigation, technical quality, or one element), ask one locating question, keep the previous direction as a version, and log the change in §9. A strategy-level change needs the alignment statement approved again.

## 8. The owner sheet

One fillable PDF the owner answers once, so nothing is asked piecemeal: the plans with a suggested price and a blank for their own, the recommended design with a veto question, and the facts only they have. Twelve numbered items at most, a fallback under every tick question, options lettered so "4C 5A" by text is an answer. On an outbound pitch it goes with the pitch as the way to steer it; for an inbound client it goes before the build. The owner never gets Markdown, a vendor name or a key to paste. A returned sheet fills §3 and §4. It never fills §8's approval.

Rules, the question file's options, the build and read commands, and what to check before it goes out: `references/owner-sheet.md`. Example: `assets/owner-sheet.example.json`. It lives in `deliverables/owner-sheet/`; returned copies and answers go in `discovery/`.

## Gate

| Project mode | What it needs |
|---|---|
| `client-production` | The client's approval of the alignment statement before client-facing Phase B. A `draft` or `deferred` direction still allows research, the media inventory and the rebrand plan; it blocks settling the look as final. |
| `near-final-pitch` | The builder's approval, labeled as such. `deferred` is enough to build the pitch on a labeled guess. |
| `reference-only` | Skip this step. Phase A runs without a direction, and nothing claims a client direction is settled. |

If the direction is missing or contradictory, ask the one question that unblocks it. Never adopt a competitor's style by default.

**When the owner replies.** Anything the owner says after seeing a build (a complaint, a competitor's link, a change of subject, "I'm scared to pick wrong") goes into §9 as said and gets a layer (`references/feedback-diagnosis.md`) before the next round is designed. What to build next is the builder's call. The pipeline's part is making sure the next round answers what was said, and the owner sheet is the quickest way to find out.

A `creative-direction.md` the client approved before the alignment statement existed (v1.7.0) keeps its approval. Write the statement from it and confirm it at the next client touchpoint; don't block work that was already approved.

## Anti-patterns

- "Their Instagram looks like X, so the site looks like X."
- "He said simpler, so it's minimalist." Ask what simpler means.
- "She loves competitor Y, so copy Y." Ask what about Y. Y's achievements are never ours.
- "Premium look, two projects, so add case studies." Show the two well, tell the process, ask for more work.
- A 25-question form, or a quiz built to steer the answer.
- Agency questions sent to a restaurant. The core decisions are shared; the options and add-ons come from their trade.
- "Show our work" read as one thing. Craft, deliverables and results need different evidence.
- A result on the page that nobody can source.
- A returned questionnaire filed as approval.
- Rebuilding after "I don't like it" before finding which decision was wrong.
- Answering "show what they get" with a new look.
- Another option for an owner who hasn't picked from the ones they have.
- Pitching on a thin read: no competitors opened, no local numbers, a hero chosen because the template had one.
- A question to a client with no fallback, left to hold a paid job for weeks.
- A setup-list with API keys and vendor names sent to an owner.
- Building behind a front door the owner is embarrassed by, without naming it.
- Reading the direction off a template's CSS or a `DESIGN.md`. Those encode a chosen direction; they don't choose it.

## Acceptance scenarios

| Scenario | Expected behavior |
|---|---|
| Edgy reels, but the owner asks for a calm site | The direction follows what the owner said, not the reels. |
| Owner names a successful competitor | Decode what is admired (look, positioning, hierarchy, credibility, ease of buying, work volume); borrow no claims. |
| Premium wish, two projects | Curate and tell the process; missing work goes on the setup-list; nothing fabricated. |
| Pitch with only a logo and a URL | A builder-approved guess, labeled; the ask-first list goes to the meeting. |
| Unsolicited pitch, operator picks Skip for now | `deferred` saved with the homework and the reason; the pitch is built on a labeled guess. |
| That pitch becomes paid work | Resume from the saved file; ask only what's open; the client approves the alignment statement before Phase B. |
| Contractor wants to lead with results, has job photos only | Desired `results`, evidence `craft`; lead with the work, results go on the setup-list. |
| Restaurant owner loves a competitor's site "because it's easy to order" | The quality is customer experience: the ordering path transfers, the look doesn't. |
| Owner returns a fully answered PDF | Answers fill §3–§4; the alignment statement still needs their approval. |
| Returned PDF was printed and scanned | `read` says `flattened`; answers are transcribed by hand and labeled `transcribed`. |
| Spanish-speaking owner | Questions and the PDF in Spanish, in their register; same ids. |
| A busy template for an approved calm direction | Flagged in `clone-intake` before Phase A; Phase A stays faithful. |
| Template-fidelity exercise | `reference-only`: skip this step; claim no client direction. |
| Existing PRD or brief | Reuse its decisions; conflicts become questions, not overwrites. |
| Direction unknown at Phase B on paid work | Stop client-facing Phase B and name the missing decision. |
| Owner says "make it simpler" after seeing a build | Feedback diagnosis: ask what feels like too much, on the page itself, before restyling; the old direction is kept and the change logged. |
| Client returns a year later for a redesign | Read the file and change log first; ask only what changed; earlier directions stay on record. |
| Owner sends a competitor's site after seeing the build | Logged in §9 as pushback; the argument map is held against the build, so the next round changes what the map says is missing. |
| Owner says the competitor "shows the output" | Quote the word back on the owner sheet with what it could mean (what clients get, results in numbers, the work shown bigger); the plans go on the sheet first. |
| Outbound pitch, nobody to ask | The market read and the design scout carry the guess; the builder picks the template from the search brief; the owner sheet goes with the pitch. |
| Builder wants to try three templates from a subscription | Fine: options are the builder's call. Each one is vetted in `clone-intake`; they differ on something the owner cares about. |
| Several designs shown, owner won't pick | Stop adding. One recommendation with a veto question on the owner sheet, each tick with a fallback. |
| Owner says the social page looks amateur | Front door: ask which part; scope it as its own job; the site decision stays separate. |
| The date passes with no answer | Each fallback stands as the builder's decision, logged `default, owner silent`; the job moves; the alignment statement is still unapproved. |
| Owner answers "4C 5A" by text | Transcribed with `answers-template`, provenance `transcribed`, their message kept. |
