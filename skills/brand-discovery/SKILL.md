---
name: brand-discovery
description: Pipeline step 0 — find how the client wants the business to come across before the PRD and the template are settled. Produces a vibe read from their site, social profiles or seed link, a short "ask first" list of questions the builder can text the owner, two or three named creative directions, and a signed-off creative-direction.md (from assets/creative-direction-template.md). Sorts every link into a template (clone candidate) or a reference brand (study only). Use at the start of a client site or near-final pitch, when the user says "start the pipeline", shares a client link, seed PRD, style-picker brief or reference sites, or when a client pushes back on how a finished site looks or feels ("make it simpler", "not my vibe", "I want to look like them").
---

# Brand discovery

**Pipeline step 0** (`client-site-pipeline`, steps 0–5). Next: `client-web-delivery`. Produces `creative-direction.md` (template: `assets/creative-direction-template.md`).

A site can be correct, fast and good-looking and still be wrong for the owner. On an agency pitch the build followed the owner's trendy social edits. The owner wanted something much simpler: a site his non-technical buyers could follow, sized to the amount of work he actually had, instead of a "maxed out" agency site. Nobody had asked him. This step asks.

The PRD owns the business: what is sold, to whom, the money action, the proof. This step owns how the business comes across: the impression, voice, look, density, motion, what to avoid, and which template can carry that. It never repeats PRD fields; it points to them.

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

## 2. Sort every link: template or reference brand

| | Template | Reference brand |
|---|---|---|
| Signs | A marketplace page, `*.webflow.io` or `*.framer.website`, "Get template" / "Buy", demo copy, fictional clients | A real team, named clients, a registered company, a "website by" credit, real contact details |
| Use | Clone candidate once licensed. `clone-intake` vets the fit. | Study only: their niche, their promise, how they show proof, how a visitor buys. Never clone the look; never borrow the claims. |

When the owner admires a reference brand, ask what exactly: the look, how much work they have, who their clients are, or how easy they are to buy from. Envy of a competitor is often about the volume of work, not the interface, and those have different fixes. A good-looking competitor is a pattern, not proof that it converts.

## 3. The ask-first list

Three to five questions, written so the builder can text them or ask in person. Each one:

- is tied to something the homework found ("Your reels are fast cuts and trending audio. Should the site feel like that, or calmer?");
- names what the answer decides: template, density, motion, voice, or what leads;
- is ordered so the questions that would change the template come first.

Skip anything the homework already answered. Never send a 25-question form. If a style-picker brief exists (exported from a site's intake form), read it first: its picks are a starting point, and the list asks only what is still missing.

Always cover, in some form:

1. Who do you show this to, and what should they say after 10 seconds?
2. Who do you look up to, and what exactly about them?
3. What feels like too much? (when there's a current site or a pitch to react to)
4. What are your best three to five pieces of work?
5. Three words for how you should come across, and what it should never look like.

**Question types that get the real answer fast.** Use them openly. No hidden tracking and no steering: an owner defends a direction they know they chose, and second-guesses one they were led into.

- **This or that:** two concrete options, "go with your gut".
- **React to something real:** show two or three quick versions, or the current site. "Which one, and what bugs you about the others?" Owners can't describe what they want, but they react instantly.
- **No design words:** "If the business were a car, which one?" "What would a customer tell a friend about you?"
- **Why, two or three times:** that's how "minimalist" becomes "I don't want to look like I'm faking a big agency".
- **Never this:** "Which of these is definitely not you?" is easier to answer than "what are you?".
- **Customer before taste:** who visits and what worries them settles many style questions.
- **Unpack vague words:** "simpler" can mean fewer sections, less motion, fewer words or a different template. Ask which before picking a style.

**Can't ask before pitching?** Pick a direction, record it as approved by the builder and labeled a guess, build the pitch on it, and take the ask-first list to the meeting. The pitch becomes the first "react to something real".

## 4. Two or three directions

Each direction gets a plain name with the designer's term beside it, so the builder learns the vocabulary ("Calm and spacious — minimal / Swiss grid"). For each, write:

- what a visitor feels in the first 10 seconds;
- the look: type, color approach, page density, imagery, motion, navigation;
- how the client's real work is used;
- what it gives up or risks;
- why the evidence supports it;
- candidate templates, if any are known.

Recommend one. Directions are written in words; mood images can help but are never client proof. If two candidates land on the same direction, say so: a choice only helps when the options feel different.

## 5. Save it

Copy `assets/creative-direction-template.md` to `creative-direction.md`. Status uses the PRD's words (`draft` / `approved` / `approved-with-blockers`) plus who approved it. A builder's approval on a pitch is written as the builder's and never presented as the client's; confirm it with the owner when the pitch becomes paid work.

## Gate

| Project mode | What it needs |
|---|---|
| `client-production` | Client approval before client-facing Phase B. A draft still allows research, the media inventory and the rebrand plan; it blocks settling the look as final. |
| `near-final-pitch` | The builder's approval, labeled as such. |
| `reference-only` | Skip this step. Phase A runs without a direction, and nothing claims a client direction is settled. |

If the direction is missing or contradictory, ask the one question that unblocks it. Never adopt a competitor's style by default.

## Anti-patterns

- "Their Instagram looks like X, so the site looks like X."
- "He said simpler, so it's minimalist." Ask what simpler means.
- "She loves competitor Y, so copy Y." Ask what about Y. Y's achievements are never ours.
- "Premium look, two projects, so add case studies." Show the two well, tell the process, ask for more work.
- A 25-question form, or a quiz built to steer the answer.
- Reading the direction off a template's CSS or a `DESIGN.md`. Those encode a chosen direction; they don't choose it.

## Acceptance scenarios

| Scenario | Expected behavior |
|---|---|
| Edgy reels, but the owner asks for a calm site | The direction follows what the owner said, not the reels. |
| Owner names a successful competitor | Ask what exactly is admired; separate look, work volume, clients and ease of buying; borrow no claims. |
| Premium wish, two projects | Curate and tell the process; missing work goes on the setup-list; nothing fabricated. |
| Pitch with only a logo and a URL | A builder-approved guess, labeled; the ask-first list goes to the meeting. |
| A busy template for an approved calm direction | Flagged in `clone-intake` before Phase A; Phase A stays faithful. |
| Template-fidelity exercise | `reference-only`: skip this step; claim no client direction. |
| Existing PRD or brief | Reuse its decisions; conflicts become questions, not overwrites. |
| Direction unknown at Phase B on paid work | Stop client-facing Phase B and name the missing decision. |
| Owner says "make it simpler" after seeing a build | Ask what feels like too much, on the page itself, before restyling. |
