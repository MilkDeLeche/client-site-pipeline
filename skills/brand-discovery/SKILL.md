---
name: brand-discovery
description: Pipeline step 0. Find how the client wants the business to come across before the PRD and the template are settled. Starts with a Yes / Skip for now choice (skipping saves a resumable deferred state). Produces a vibe read from their site, social profiles or seed link, a short "ask first" list of adaptive questions for any industry (text, call, or an optional branded fillable PDF), what should lead and the evidence that exists for it, what each reference is actually admired for, two or three named creative directions, and a creative-direction.md (from assets/creative-direction-template.md) with an alignment statement and an approval record. Sorts every link into a template (clone candidate) or a reference brand (study only). Use at the start of a client site or near-final pitch, when the user says "start the pipeline", shares a client link, seed PRD, style-picker brief or reference sites, when a pitch turns into paid work or a client returns, or when a client pushes back on how a finished site looks or feels ("make it simpler", "not my vibe", "I want to look like them"), which goes to feedback diagnosis before any rebuild.
---

# Brand discovery

**Pipeline step 0** (`client-site-pipeline`, steps 0–5). Next: `client-web-delivery`. Produces `creative-direction.md` (template: `assets/creative-direction-template.md`).

A site can be correct, fast and good-looking and still be wrong for the owner. On an agency pitch the build followed the owner's trendy social edits. The owner wanted something much simpler: a site his non-technical buyers could follow, sized to the amount of work he actually had, instead of a "maxed out" agency site. Nobody had asked him. This step asks.

The PRD owns the business: what is sold, to whom, the money action, the proof. This step owns how the business comes across: the impression, voice, look, density, motion, what leads, what to avoid, and which template can carry that. It never repeats PRD fields; it points to them.

| File | Use |
|---|---|
| `references/question-bank.md` | Core decisions, showcase emphasis, reference decoding, industry add-ons, Spanish notes |
| `references/feedback-diagnosis.md` | When a client rejects or questions a design |
| `assets/creative-direction-template.md` | The record this step produces |
| `scripts/discovery_pdf.py` + `assets/*.example.json` | Optional fillable PDF kit (section 8) |

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

## 2. Sort every link: template or reference brand

| | Template | Reference brand |
|---|---|---|
| Signs | A marketplace page, `*.webflow.io` or `*.framer.website`, "Get template" / "Buy", demo copy, fictional clients | A real team, named clients, a registered company, a "website by" credit, real contact details |
| Use | Clone candidate once licensed. `clone-intake` vets the fit. | Study only: their niche, their promise, how they show proof, how a visitor buys. Never clone the look; never borrow the claims. |

**Decode what is admired.** A reference is usually admired for one quality, not the whole site: its visual design, its positioning, its content hierarchy, its credibility, how easy it is to buy from, its volume of work, or something else in the owner's words. Ask which ("What's the one thing you'd take from that site?") and record it per reference. Only that quality transfers; the table in `references/question-bank.md` says what does and doesn't. Envy of a competitor is often about the volume of work, not the interface, and those have different fixes. A good-looking competitor is a pattern, not proof that it converts. A reference is never a template to clone unless it is a licensed template and the admired quality is how it looks.

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

**How to ask.** By text or on a call is the default and needs nothing installed. The optional PDF (section 8) asks the same questions with the same ids, for owners who'd rather answer on their own time or when a more formal ask suits the agency. Record each answer with its channel, date and the owner's own words.

**Can't ask before pitching?** Pick a direction, record it as approved by the builder and labeled a guess, build the pitch on it, and take the ask-first list to the meeting. The pitch becomes the first "react to something real". If the operator chose Skip for now, the status stays `deferred` until the list is asked.

## 4. What leads, and what proves it

"Show our work" means different things by trade: the products, the craft, the deliverables, verified results, credibility, how the service works, the place, or the people (definitions and typical trades in `references/question-bank.md`). Record two things apart in `creative-direction.md` §4:

- **Desired emphasis:** what the owner wants to lead with.
- **Available evidence:** what exists, where it is, and whether we may use it.

When they don't match, write the gap, lead with an emphasis the evidence can carry, and put the missing evidence on the setup-list. A result is shown only with its source, its date and the client's permission. Never estimate, round up or borrow one.

## 5. Two or three directions

Each direction gets a plain name with the designer's term beside it, so the builder learns the vocabulary ("Calm and spacious (minimal / Swiss grid)"). For each, write:

- what a visitor feels in the first 10 seconds;
- the look: type, color approach, page density, imagery, motion, navigation;
- how the client's real work is used, and what leads;
- what it gives up or risks;
- why the evidence supports it;
- candidate templates, if any are known.

Recommend one. Directions are written in words; mood images can help but are never client proof. If two candidates land on the same direction, say so: a choice only helps when the options feel different.

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

## 8. Optional: the discovery PDF kit

A branded, fillable PDF of the same questions, for owners who prefer to answer alone. Nothing is hosted, uploaded or stored online: the operator sends the file through their own channel and reads the returned copy on their own machine.

```
node ~/.claude/skills/client-site-pipeline/scripts/setup.mjs   # installs reportlab and pypdf if missing; it prints the Python to use
python scripts/discovery_pdf.py build discovery/questions.json --agency ~/.client-site-pipeline/agencies/<slug>.json --out discovery/client-discovery-v1.pdf
python scripts/discovery_pdf.py read discovery/returned.pdf --questions discovery/questions.json --out discovery/answers.json
python scripts/discovery_pdf.py answers-template discovery/questions.json --out discovery/answers.json   # text or call answers, no dependencies
```

- **Questions:** copy `assets/questions.example.json` into the project's `discovery/` folder, keep only what the homework left open, and rewrite the options from the research. Not sure and Other are added automatically; `note: true` adds room to explain; `conflicts` flags answers that pull apart. `locale: "es"` switches the built-in text to Spanish.
- **Agencies:** one profile per sending agency, from `assets/agency-profile.example.json`, kept outside any public repo (suggested `~/.client-site-pipeline/agencies/<slug>.json`). The logo is optional (PNG or JPG). Without one, or when it can't be read, the PDF sets the agency name in type and prints a note.
- **Privacy:** questions, returned PDFs and answers live in the project's `discovery/` folder, which is gitignored. Agency profiles and client answers never go into this skills repo.
- **Reading it back:** `read` flags blanks, Other without text, too many picks, Not sure mixed with answers, and conflicts. A copy that was printed, scanned or flattened has no fields left: `read` says `flattened`, and the answers are typed into an `answers-template` file by hand with provenance `transcribed`. Every flag becomes a follow-up question, not a guess.
- **Dependencies are the agent's job.** Before the first `build`, run the setup above yourself (or `python -m pip install --user -r scripts/requirements.txt`); never ask the owner or the user to install anything. If it still can't install, the rest of the pipeline is unaffected: ask by text or call. Tests: `python -m unittest test_discovery_pdf` from `scripts/`.

A returned PDF fills §3 and §4. It never fills §8's approval.

## Gate

| Project mode | What it needs |
|---|---|
| `client-production` | The client's approval of the alignment statement before client-facing Phase B. A `draft` or `deferred` direction still allows research, the media inventory and the rebrand plan; it blocks settling the look as final. |
| `near-final-pitch` | The builder's approval, labeled as such. `deferred` is enough to build the pitch on a labeled guess. |
| `reference-only` | Skip this step. Phase A runs without a direction, and nothing claims a client direction is settled. |

If the direction is missing or contradictory, ask the one question that unblocks it. Never adopt a competitor's style by default.

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
