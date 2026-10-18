# Phase B: intent-aware rebrand

Loaded by `clone-workflow` when Phase B starts. It does not change Phase A, Phase C, or the five-step order.

Phase A gave you a faithful clone of a template the user chose because they love how it looks and moves. Phase B turns it into a site that **sells for this business**. That means the right message, proof and action in each slot, while the page still looks like the template built it. Don't just swap photos at random.

## What "done" means

Phase B is done when a stranger who matches the PRD's buyer (a bar owner, a realtor, a shop that's about to open) lands on the first screen and sees, without scrolling, three things: **this is for me, here is what I'd get, and here is real proof.** A filled slot is not done.

Swapping content into the template's slots is *how* you implement Phase B. It is not the goal. The common failure is a rebrand by substitution: every photo replaced, every heading reworded, tidy service categories, and nobody in the target audience ever addressed. It looks finished and it sells nothing.

## Prerequisites (name the blocker if one fails)

- [ ] Phase A is verified against the source, screenshot crops and video, and still reachable as a baseline (route or `reference/phase-a-snapshot/`).
- [ ] `PRD.md` is `approved` or `approved-with-blockers` (for a near-final pitch the builder approves it). A `reference-only` PRD allows Phase A only; finish the business brief before client-facing Phase B.
  A **draft** PRD blocks an invented positioning. It does not block the research, the media-truth inventory, or drafting buyer hooks and slot assignments for approval. Do that work and bring the PRD to approval; don't settle for the one move that needs no decision (swapping images).
- [ ] `src/data/<client>.ts` holds the publishable facts; the setup-list holds what's missing.
- [ ] `architecture-plan.md` exists for anything that must actually work.
- [ ] Every brand asset and photo has a known source and right to use.

## Boundaries

| Phase | Owns | Must not do |
|---|---|---|
| A | Faithful clone: source, CSS values, motion, verification | Client content, strategy edits, new components |
| **B** | Message, proof, media and CTAs per section; approved brand tokens; additions built from the template's own grammar | Invented facts, unexplained restructuring, backend wiring |
| C | Forms, bookings, orders, email, analytics, APIs named in the architecture plan | Redesign as a side effect |

## The room: run Phase B as a senior team

Phase B is four jobs. Work through each role in turn, in writing, before building, and keep each one's output in the files named here. Skip a role and the result is a substitution pass.

| Role | Owns | Writes |
|---|---|---|
| **Strategist / analyst** | Who buys, sorted by *situation* ("opening a second location", "listing goes live Friday"), the words they use, where they arrive from, what they must believe, the funnel. Research before opinions (section 1). | PRD research table, the buyer list in `section-purpose-map.md` |
| **Copywriter** | Writes with the `copywriting` skill and `antislop-copywriting` from the first draft (antislop DURING mode), not as a later rewrite. A hook bank: one line per buyer situation, in the buyer's words, written in **both** site languages (the second language is rewritten for how local owners talk, never translated word for word). Headlines, card titles, CTA support lines. Punchy is welcome; invented reviews, prices, contact details and result numbers are not. | Hook bank and copy columns in `section-purpose-map.md` |
| **Art director** | The media-truth inventory (section 2b), then which real file proves which claim in which slot. Krea/AI only where no real file can do the job, prompted from the researched visual style. | `media-inventory.md`, media column of the map |
| **UX / front-end lead** | The design-grammar inventory (section 2), the lead capture for this site type (section 5), what the page still fails to do (section 7, step 5), grammar additions, the build, the redline loop. | Grammar block, rebrand plan, the build |

**Redline, then fix.** After the build, each role reviews the running page on desktop and phone against its own column and the first-screen test, with the antislop skills as the checklist for what we added (`antislop-ui`, `antislop-layoutmobile`, `antislop-human`, `antislop-copywriting`; the cloned template's grammar is their design direction), and writes its misses one line each ("Strategist: a realtor can't tell this is for them until the fourth section"). Fix them, then run the round once more if anything structural changed. A role that finds nothing says why. "Looks good" is not a review.

## 1. Read the business, not the photos folder

From `PRD.md`, extract: what is sold and to whom, where visitors arrive from, the **one action that makes the business money** and what completes it, what they must believe (proof), their main objections, who answers the inquiry, and what the user loves about the template.

**Research the decision, briefly and honestly.** Use the client's own reviews, FAQs and the questions customers actually ask, plus published UX guidance for the industry (for example Google's industry UX playbooks, Nielsen Norman Group, Baymard for e-commerce). Look at peer sites for patterns. Record what you observed and the date in the PRD's research table. A good-looking competitor is a pattern, not proof it converts.

Minimum before the hook bank: three peer sites in the client's own category and region (what they lead with, how they show proof, what the first CTA asks for), the industry guidance that applies, and the client's own best-performing public posts (what their audience already responds to). When the client is an agency or a service provider, also research **their buyers' industries**: what a bar owner, a realtor or a gym owner is trying to fix this month.

## 2. Inventory the template's design grammar (before any edit)

Write this down once, at the top of `section-purpose-map.md`. Every Phase B change must be built from it, so the result looks like the template made it.

| Grammar | What to record |
|---|---|
| **Buttons** | Every variant (class names, e.g. `primary-button`, `secondary-button`, `link-button`) and **where the template places each**: hero, nav, end of a section heading, card footer. |
| **Typography** | Font families and weights actually loaded, and the heading/label/paragraph classes. |
| **Spacing** | Container widths, section padding, section margins, grid gaps: the template's own CSS variables or values. |
| **Form controls** | Input, label, select, error, success and submit styles, if the template has a form. A new form reuses exactly these. |
| **Section patterns** | The repeating structures: heading block + summary + grid, alternating backgrounds, card types. |
| **Image slots** | Each slot's pixel size and aspect ratio, and whether layout depends on the image's own size. |
| **Motion** | Reveal and hover behavior and how it is bound (classes, data attributes, per-page IDs). |
| **Color + icons** | Color tokens and the icon set in use. |

**Rules for anything added, moved or removed in Phase B:**

- **Buttons:** only existing variants, and only in slot types where the inventory recorded the template using that kind of button (if some section headings carry a button, another section heading may; a slot type that never has one gets none). Never a button floating mid-grid because "it needs a CTA there". Hover and focus states come from the variant.
- **Fonts:** only families and weights the template already loads. No new font, unless the user directs a brand font (`USER_DIRECTED`).
- **Spacing:** only the template's spacing values. A new block gets the same padding, margin, container and gap as its neighbors.
- **Order:** changing section order is a structural change; it goes in the rebrand plan and waits for approval.
- **New section:** duplicate an existing section pattern (its markup, classes and reveal binding) and change the content. Don't write a new layout. Keep background alternation intact.
- **Removed section:** only when there is no truthful content for it (no reviews → no testimonials block). Check the page rhythm still works and nothing now points to it.
- **Images:** crop to the slot's exact size and aspect. Where layout depends on the image's own size, keep the template's pixel size (serve a 2x copy with `srcset` "1x, 2x").
- **Motion:** new items reuse the template's own reveal and hover bindings. On Webflow, IX2 reveals are bound per page and per row by `data-w-id`; copy the binding from that exact context or the element stays invisible.
- **Colors:** brand tokens replace template tokens. Check every literal copy of the old color too (SVG fills, animation configs). Check contrast after each change.

Structural additions and removals go in the rebrand plan (step 5 below) with their reason; build them once the user approves the plan. A user's direct design request ("make the hero navy", "add a financing section") is approved by definition: record it and build it in the same grammar, unless they ask for deliberate contrast.

## 2b. Media-truth inventory (before any image is assigned)

Open every client file before using it: view each image, and make a contact sheet of each video (`clone-workflow`, "Reading a motion video"). Write `media-inventory.md`, one line per file:

| File | What is actually in frame | Origin | Proves which offer / buyer | May enter which slots |
|---|---|---|---|---|
| `brewskies.mp4` | Sports bar, wall of screens, bar top, wide room | real client work | "Got a bar?" | hero, services, proof |
| `joggers.mp4` | Two runners on a trail, 5 s, same composition as an AI still | AI-generated | nothing | no claim slot |

- **The filename is not evidence.** `bar.mp4` may be generated; `fabian-beach.mp4` may be a couple on a beach, not the fighter named Fabian. Look.
- Record the origin of every file: real client work, AI-generated, stock, template. Generated footage never fills a slot that says "this is our work" when a real file exists for that claim.
- A still and a video that prove different things don't share a slide.
- Real work goes first to the slots that sell: hero, services, proof. A real file left in a folder while an illustrative image holds the hero is a Phase B failure.

## 3. Map every section to a business purpose

Create `section-purpose-map.md`: one row per inherited section and CTA, **before** editing content.

| Field | Question |
|---|---|
| Section | Hero, services, proof, process, FAQ, CTA, footer… |
| Template component | Which original markup, variant and motion is reused? |
| Visitor need | What does this audience need to know, feel or do here? |
| Business purpose | Explain the offer? Build trust? Handle an objection? Convert? |
| Copy | Headline, support, labels. Mark confirmed vs proposed. |
| Proof | Real project, permissioned review, verified fact, or "none". |
| Media | Exact asset, focal point, crop, slot size, right to use. |
| CTA | Existing variant, label, destination, success state. |
| Edit type | `CONTENT_ONLY` / `BRAND_TOKEN` / `GRAMMAR_ADDITION` / `USER_DIRECTED` / `CONFLICT` |
| Status | `READY` / `NEEDS_ASSET` / `NEEDS_FACT` / `NEEDS_APPROVAL` / `NOT_APPLICABLE` |

**Headlines name the buyer's situation.** Hero lines, section headings and card titles speak to the visitor's situation in their words: "Got a bar?", "Got a listing?", "Opening soon?". Titles named after the vendor's departments ("Video Production", "Professional Content", "Socials Management") fill a card and make nobody feel seen. They are a failed Phase B even when every word is true.

**Hook voice: finesse, not corn.** A hook has two halves: the buyer's situation, then the payoff. The payoff is what the owner gets or feels, in a phrase people already say out loud, in about five words. The body copy does the explaining. Real rewrites from a client pitch, where the owner's version won:

| Corny or literal | With finesse | Why |
|---|---|---|
| Got a shop? → The brand, on the car | Got a nice ride? → Let's show it off | Describes the shot vs. names the owner's pride |
| Got a listing? → Let them walk it from their phone | Got a listing? → Let it sell itself | Explains the mechanism vs. states the outcome |
| Let's make it look booked | Let's put it on the map | A narrow result vs. the one every buyer wants |
| Got a spot? | (cut) | Forced slang; trying to sound local reads as corny |
| Real Valley spots. Real footage. | Serving the Valley. | A staccato stunt vs. a confident label |
| Tap a reel to watch it on Instagram. | Our work | An instruction as a heading vs. a plain label |

"Can the reader picture it?" (copywriting) means picture the result, not the footage. Section headings are confident labels, never stunts or instructions. When a hook carries the page, offer the owner two or three options and let them pick or tweak; their ear for their own customers beats ours.

Example (home builder on a roofing template, and only because these assets existed): the hero gets an offer-first headline plus a real finished home at dusk. The "brands we work with" logo row is removed (no real partners). The ratings row is reused with three real home photos and a true portfolio count instead of fake stars. The process section's steps are rewritten into the client's real build process. The testimonials section is hidden until there are permissioned reviews.

## 4. Pick media like an editor

For each image, check in order:

1. **Relevance:** does it show what the adjacent text claims?
2. **Truth:** is it the client's real work, product or team?
3. **Rights:** can they use it?
4. **Composition:** is the subject in frame on desktop and phone, with room for text?
5. **Fit:** resolution, aspect and slot size, as in section 2.
6. **Story:** does the set read as one page, not repeated filler?

**Claim slots vs. mood slots.** The hero, service cards and proof sections make claims ("this is what we do, this is what you'd get"). They are not decoration. Where real work exists for a slot's claim, real work goes there. "Illustrative mood" is never a reason to keep real proof out of a claim slot.

**AI images (Krea):** fine for mood and true gaps, such as a background no real file covers or an illustrative detail. Prompt them to match the template's photographic style (light, palette, angle). Never use them as the client's own projects, team, results, before/after or reviews. Label them illustrative where a visitor could mistake them for real work, put "send your real photos" on the setup-list, and disclose AI imagery in the privacy policy (`launch-audit` checks it).

**Copy fit:** match the template's content density: line counts, card heights, heading wraps. When real text is longer, first rewrite it accurately to fit. Then consider a template-native variant. Never shrink type or change spacing to cram it in.

## 5. Shape the funnel to the business

There is no universal funnel. Choose from the PRD, and pick the one action the business already uses: a call → `tel:`; order, reserve or book → their existing ordering or booking URL; an estimate or insight form → one form, one label, `POST /api/inquiries`. A phone call may be the secondary action. Do not add a second form, a cart or a scheduler the architecture plan did not select, and do not add a form where the action is an order, a reservation or directions.

- **Agency / B2B service:** ad → focused landing page → proof (relevant work, capabilities) → **insight form** with qualifying fields (company, website, goal, budget range, timeline) → a named person follows up.
- **Contractor / home builder:** local search or ad → service area, real projects, process → estimate request or call → office response.
- **Restaurant / food:** search or social → menu, hours, location, food photos → order, reserve, call or directions. Usually no qualifying form.
- **Retail:** ad or search → product → variants, price, stock, policies → checkout.
- **Appointment service:** services, availability, expertise, policies → booking.

One label, taken from the PRD, on every primary button the inventory recorded. Do not add a primary button in a slot type the template leaves without one.

**Lead capture is a Phase B decision, per site type.** Not every site needs a lead form, and no site may lose a lead. In the rebrand plan the UX lead states:

- **The money action** for this business type: call, order, booking, directions, or a form. A form only where the business actually quotes or qualifies (agency, contractor, builder, B2B).
- **Qualifying fields:** one per real decision the owner makes before replying ("What do you run?", "When do you open?", "Area and budget"). No field the owner won't read.
- **Where it lands:** `inquiries` in D1 through `POST /api/inquiries` until the client's inbox or CRM is connected, so nothing is lost before handoff.
- **What the visitor sees:** success says only that it was received. If delivery fails, the message hands them a channel that works today (call, DM). Never a dead end, never "form isn't connected".
- **The email list:** every site has one. Its hook comes from the signup table in `client-web-delivery` and is written for this buyer.

## 6. Near-final pitch standard

A `near-final-pitch` is built before the sale but must read as about 99% done:

- No "preview", "prototype", "demo", "coming soon", lorem ipsum or template leftovers anywhere: copy, alt text, titles, form messages.
- Every CTA goes somewhere real. Every form genuinely captures what's submitted: signups to `/api/subscribe` and the primary inquiry form to `/api/inquiries` (both D1), until the client's inbox, CRM or Brevo is connected. A missing fact is omitted or its section hidden, never shown as a visible placeholder. Success messages say only what is true ("Thanks, your message was received").
- The remaining 1% is the client's own: their email tool, real photos, domain, approvals. It is listed on the setup-list in their language.
- The pitch link stays private: `*.workers.dev`, `noindex` until they buy. None of this shows on the page.

## 7. Phase B sequence

1. Read the PRD and the facts file; note confirmed, proposed and missing facts.
2. Research (section 1) and log it in the PRD. Write the buyer list by situation.
3. Walk the verified Phase A clone on desktop and phone; write the design-grammar inventory.
4. Open every client file and write `media-inventory.md`. Then write `section-purpose-map.md` with the hook bank.
5. **Present a short rebrand plan:** the buyer situations and hook bank, hero message, section order, proof, image assignments from `media-inventory.md`, primary CTA, any `GRAMMAR_ADDITION` or removal with its reason, and any `CONFLICT`. It must answer in one sentence: **what does the page still fail to do for the buyer, and should an existing section pattern be duplicated to do it?** For example, all the proof hidden one slide at a time → reuse the template's project grid as a proof row; every lead arrives as a blank message → add one qualifying field from the existing form controls. "Nothing" is an allowed answer; skipping the question is not. Wait for approval of structural items.
6. Implement content and brand tokens from the facts file, reusing the template's components.
7. **First-screen test:** screenshot the top of every page on a phone and on desktop. That first screen alone must answer what they sell, where, why trust them, and what to do next. If it doesn't, fix the message or media before anything else.
   Re-measure the fixed header after the logo swap: a taller client logo makes the header taller than the template's hardcoded first-section offset, and inner-page headings slide under it. Set the offset from the measured header height at each breakpoint.
   Then check desktop, tablet and phone: crops, real text wraps, contrast, hover and focus, motion and reduced motion, every CTA's destination. Compare page and section geometry with the Phase A baseline; differences must be the approved ones.
8. **Redline** (see "The room"): each role reviews the running page against its column and the first-screen test, writes its misses, and they get fixed.
9. Log what changed and why (`rebrand-change-log.md` or the project notes). Unresolved items go to the setup-list.

## 8. When the template can't serve a requirement (`CONFLICT`)

Don't redesign quietly. State the requirement and why the inherited layout can't meet it. Then offer options from smallest to largest:

- **A.** Adapt an existing component.
- **B.** A dedicated page or flow built from the template's grammar.
- **C.** A described structural change.

Give the impact of each on layout, motion and mobile. Sometimes the honest answer is a different template.

## 9. Gates

**Phase B passes when:**
- Someone in the target buyer group can tell from the first screen that the site is for them, what they'd get, and see real proof of it.
- `media-inventory.md` exists, and every client file in a claim slot was opened, not judged by its name.
- Headlines and card titles name buyer situations, not service departments.
- The rebrand plan answered what the page still fails to do.
- Each role ran its redline and the misses were fixed or logged.
- Every section has a mapped purpose with real content and suitable media.
- The site still looks and moves like the template, apart from approved changes.
- No invented proof.
- Every CTA has a destination.
- Phase C needs are listed.
- Desktop and phone were actually inspected.

**Phase B is blocked when:**
- Phase A isn't verified.
- The PRD is missing or unapproved for client work.
- A required claim is missing, or a required image is missing and neither a client photo nor a labeled illustrative image can honestly fill it.
- A business-critical change needs unapproved structure.

## Anti-patterns

- "Every photo was replaced, so the rebrand is done."
- "The PRD is a draft, so the only safe move is swapping images." (A draft blocks invented positioning, not a media-truth pass.)
- "The file is called `bar.mp4`, so it's the bar reel."
- An AI mood image in the hero or a service card while real client work for that claim sits in a folder.
- Service cards titled by department ("Video Production") instead of by the buyer's situation ("Got a bar?").
- All the proof behind a one-at-a-time slider, and nobody asked whether a grid pattern the template already has should show it.
- "The PRD says leads, so I added a generic form section with new styling."
- "This competitor looks premium, so it converts."
- "The form shows a success message, so the email works."
- "The client sells food, so they need reservations, a shop and a chatbot."
- A button, font or spacing value that appears nowhere in the original template.
- Three different labels for the same primary action ("Contact Us", "Get Started", "Start Your Home"). Pick one label from the PRD and use it everywhere the primary CTA appears.

## Acceptance scenarios

| Scenario | Expected behavior |
|---|---|
| Phase A of a chosen template | No client content or strategy edits; fidelity and motion checks unchanged. |
| No PRD | Stop Phase B; return to step 1 or continue as `reference-only` clone. |
| 3-card design, 7 services | Group them or propose a grammar-consistent option; never squeeze 7 into 3 cards. |
| Only one real project | Show it well, ask for more, never invent a second. |
| Lead form wanted, backend not ready | Build the form from the template's form controls, capture through `POST /api/inquiries`, mark delivery to the client's inbox as pending. |
| New brand colors | Apply as tokens, chase literal copies, verify contrast and cohesion. |
| Section needed that the template lacks | Duplicate an existing section pattern, propose it in the rebrand plan, build after approval. |
| Near-final pitch | No preview or prototype wording anywhere; forms capture for real; remaining items on the setup-list. |
