# Feedback diagnosis

When a client rejects, questions or hedges on a design ("not my vibe", "make it simpler", "I don't know, something's off"), find which decision is wrong before changing anything. Most rebuilds that miss a second time missed because they changed the look when the problem was the audience, the offer or the proof.

## 1. Write it down as said

In `creative-direction.md` §9: their exact words, the channel and date, and what they were looking at (which page, which version, phone or desktop). A paraphrase loses the clue. "It's too much" and "it's a lot" can be different complaints.

## 2. Don't rebuild yet

Don't restyle, don't swap the template, and don't defend the design. A quick, cheap fix the client asked for by name ("make the logo bigger") can go ahead and still gets logged.

## 3. Map it to a layer

| Layer | Sounds like | Check | Where the fix lives |
|---|---|---|---|
| Promise | "That's not what we do", "Sounds too big for us" | Hero line against the PRD offer and where they are now | Copy, PRD |
| Audience | "My customers won't get this" | Who the first screen speaks to | `visitor`, the buyer list |
| Offer order | "We mostly do X, not Y" | Section order against what they want more of | `offer`, section map |
| What leads | "Why is the first thing the office?" | Desired emphasis and available evidence (§4) | `lead`, media inventory |
| Proof | "We haven't done that", "That's not ours" | Every claim slot against the media inventory | Remove the untrue claim now, then fix |
| Feel | "Too dark", "Too fancy", "Not us" | Three words, color, type, imagery treatment | Chosen direction (§7) |
| Density and motion | "Busy", "Too much", "Simpler" | Section count, words per section, animations per screen | Chosen direction, rebrand plan |
| Navigation and clarity | "Where do I click?", "Couldn't find prices" | Menu labels, the main button, what's above the fold on a phone | Section map, CTA |
| Technical quality | "It's slow", "Broken on my phone" | `launch-audit`, a device check | The build, not the direction |
| One element | "I don't like that font" | That element only | A token or a component |

One complaint can touch two layers. "Too much" is often density plus promise: the site looks like a firm ten times their size.

## 4. Ask one locating question

On the page, if possible. Make it easy to answer:

- "Is it the words, the photos, or how much is going on?"
- "Show me the part that bugs you most."
- "Should it feel more like this one or this one?" (two quick versions, when they're cheap)

Not "What don't you like?" with no options. Record the answer next to the feedback.

## 5. Size the change

- **Element:** one component or token. Fix it and log it.
- **Section:** content, order or media in one section. Fix it within the template's grammar.
- **Direction:** feel, density or motion across the site. Write a revised direction.
- **Strategy:** promise, audience, offer order, what leads or proof. Write a revised alignment statement.

If the revised direction can't be carried by the current template, go back to `clone-intake` with the new direction. Phase A is never restyled to force it.

## 6. Keep the previous direction

Before changing §7 or §8, copy the current chosen direction and alignment statement into §9 as the previous version, with the build's commit or tag. Nothing is deleted. The client may want parts of it back, and the next agent needs to see what was tried.

## 7. Approve again when strategy changed

- **Strategy-level change:** rewrite the alignment statement and get it approved (§8) before the rebuild.
- **Direction-level change:** confirm the revised direction in a line ("Calmer, fewer sections, same photos. OK?") before the rebuild.
- **Element or section:** approval of the revised page is enough.

Then rebuild in Phase B and redline against the revised direction.

## Example (anonymized)

A video agency pitch, built in the owner's high-energy social style. His reply: "It's nice, but it's too much." Diagnosis:

- **Said:** "too much", looking at the home page on his phone.
- **Locating question:** "Is it the motion, the amount of sections, or how big it makes you sound?" Answer: "My clients are restaurant owners. They just need to see what they get and call me."
- **Layers:** audience (restaurant owners, not other creatives), what leads (`deliverables` over a showreel), density (twelve sections for six projects), promise (the hero read like a large agency).
- **Size:** strategy. The previous direction was kept as v1 in §9; a revised alignment statement was approved by text; the rebuild kept the template and cut it to five sections.

## Anti-patterns

- Rebuilding the whole site after "I don't like it".
- Swapping the template over feedback on one element.
- Overwriting the old direction instead of versioning it.
- Treating silence, or "looks fine" on an unrelated message, as approval of a revision.
- Fixing the look when the complaint was about the offer or the proof.
