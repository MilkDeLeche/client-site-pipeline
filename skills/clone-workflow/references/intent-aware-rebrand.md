# Phase B: intent-aware rebrand

Loaded by `clone-workflow` when Phase B starts. It does not change Phase A, Phase C, or the five-step order.

Phase A gave you a faithful clone of a template the user chose because they love how it looks and moves. Phase B turns it into a site that **sells for this business**. That means the right message, proof and action in each slot, while the page still looks like the template built it. Don't just swap photos at random.

## Prerequisites (name the blocker if one fails)

- [ ] Phase A is verified against the source, screenshot crops and video, and still reachable as a baseline (route or `reference/phase-a-snapshot/`).
- [ ] `PRD.md` is `approved` or `approved-with-blockers` (for a near-final pitch the builder approves it). A `reference-only` PRD allows Phase A only; finish the business brief before client-facing Phase B.
- [ ] `src/data/<client>.ts` holds the publishable facts; the setup-list holds what's missing.
- [ ] `architecture-plan.md` exists for anything that must actually work.
- [ ] Every brand asset and photo has a known source and right to use.

## Boundaries

| Phase | Owns | Must not do |
|---|---|---|
| A | Faithful clone: source, CSS values, motion, verification | Client content, strategy edits, new components |
| **B** | Message, proof, media and CTAs per section; approved brand tokens; additions built from the template's own grammar | Invented facts, unexplained restructuring, backend wiring |
| C | Forms, bookings, orders, email, analytics, APIs named in the architecture plan | Redesign as a side effect |

## 1. Read the business, not the photos folder

From `PRD.md`, extract: what is sold and to whom, where visitors arrive from, the **one action that makes the business money** and what completes it, what they must believe (proof), their main objections, who answers the inquiry, and what the user loves about the template.

**Research the decision, briefly and honestly.** Use the client's own reviews, FAQs and the questions customers actually ask, plus published UX guidance for the industry (for example Google's industry UX playbooks, Nielsen Norman Group, Baymard for e-commerce). Look at peer sites for patterns. Record what you observed and the date in the PRD's research table. A good-looking competitor is a pattern, not proof it converts.

## 2. Inventory the template's design grammar (before any edit)

Write this down once, at the top of `section-purpose-map.md`. Every Phase B change must be built from it, so the result looks like the template made it.

| Grammar | What to record |
|---|---|
| **Buttons** | Every variant (class names, e.g. `primary-button`, `secondary-button`, `link-button`) and **where the template places each**: hero, nav, end of a section heading, card footer. |
| **Typography** | Font families and weights actually loaded, and the heading/label/paragraph classes. |
| **Spacing** | Container widths, section padding, grid gaps: the template's own CSS variables or values. |
| **Section patterns** | The repeating structures: heading block + summary + grid, alternating backgrounds, card types. |
| **Image slots** | Each slot's pixel size and aspect ratio, and whether layout depends on the image's own size. |
| **Motion** | Reveal and hover behavior and how it is bound (classes, data attributes, per-page IDs). |
| **Color + icons** | Color tokens and the icon set in use. |

**Rules for anything added, moved or removed in Phase B:**

- **Buttons:** only existing variants, and only in places where the template puts that kind of button. Never a button floating mid-grid because "it needs a CTA there". Hover and focus states come from the variant.
- **Fonts:** only families and weights the template already loads. No new font.
- **Spacing:** only the template's spacing values. A new block gets the same padding, container and gap as its neighbors.
- **New section:** duplicate an existing section pattern (its markup, classes and reveal binding) and change the content. Don't write a new layout. Keep background alternation intact.
- **Removed section:** only when there is no truthful content for it (no reviews → no testimonials block). Check the page rhythm still works and nothing now points to it.
- **Images:** crop to the slot's exact size and aspect. Where layout depends on the image's own size, keep the template's pixel size (serve a 2x copy with `srcset` "1x, 2x").
- **Motion:** new items reuse the template's own reveal and hover bindings. On Webflow, IX2 reveals are bound per page and per row by `data-w-id`; copy the binding from that exact context or the element stays invisible.
- **Colors:** brand tokens replace template tokens. Check every literal copy of the old color too (SVG fills, animation configs). Check contrast after each change.

Structural additions and removals go in the rebrand plan (step 5 below) with their reason; build them once the user approves the plan. A user's direct design request ("make the hero navy", "add a financing section") is approved by definition: record it and build it in the same grammar, unless they ask for deliberate contrast.

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

Example (home builder on a roofing template): the hero gets an offer-first headline plus a real finished home at dusk. The "brands we work with" logo row is removed (no real partners). The ratings row is reused with three real home photos and a true portfolio count instead of fake stars. The process section's steps are rewritten into the client's real build process. The testimonials section is hidden until there are permissioned reviews.

## 4. Pick media like an editor

For each image, check in order:

1. **Relevance:** does it show what the adjacent text claims?
2. **Truth:** is it the client's real work, product or team?
3. **Rights:** can they use it?
4. **Composition:** is the subject in frame on desktop and phone, with room for text?
5. **Fit:** resolution, aspect and slot size, as in section 2.
6. **Story:** does the set read as one page, not repeated filler?

**AI images (Krea):** fine for mood and gaps such as a hero atmosphere or an illustrative detail. Prompt them to match the template's photographic style (light, palette, angle). Never use them as the client's own projects, team, results, before/after or reviews. Label them illustrative where a visitor could mistake them for real work, put "send your real photos" on the setup-list, and disclose AI imagery in the privacy policy (`launch-audit` checks it).

**Copy fit:** match the template's content density: line counts, card heights, heading wraps. When real text is longer, first rewrite it accurately to fit. Then consider a template-native variant. Never shrink type or change spacing to cram it in.

## 5. Shape the funnel to the business

There is no universal funnel. Choose from the PRD:

- **Agency / B2B service:** ad → focused landing page → proof (relevant work, capabilities) → **insight form** with qualifying fields (company, website, goal, budget range, timeline) → a named person follows up.
- **Contractor / home builder:** local search or ad → service area, real projects, process → estimate request or call → office response.
- **Restaurant / food:** search or social → menu, hours, location, food photos → order, reserve, call or directions. Usually no qualifying form.
- **Retail:** ad or search → product → variants, price, stock, policies → checkout.
- **Appointment service:** services, availability, expertise, policies → booking.

The primary CTA appears where the template already places primary buttons (hero, section heading blocks, final CTA section), consistently, with the same label throughout.

## 6. Near-final pitch standard

A `near-final-pitch` is built before the sale but must read as about 99% done:

- No "preview", "prototype", "demo", "coming soon", lorem ipsum or template leftovers anywhere: copy, alt text, titles, form messages.
- Every CTA goes somewhere real. Every form genuinely captures what's submitted: signups to D1 (live showcase standard), and the primary inquiry form to D1 as well, until the client's inbox, CRM or Brevo is connected. Success messages say only what is true ("Thanks, your message was received").
- The remaining 1% is the client's own: their email tool, real photos, domain, approvals. It is listed on the setup-list in their language.
- The pitch link stays private: `*.workers.dev`, `noindex` until they buy. None of this shows on the page.

## 7. Phase B sequence

1. Read the PRD and the facts file; note confirmed, proposed and missing facts.
2. Walk the verified Phase A clone on desktop and phone; write the design-grammar inventory.
3. Write `section-purpose-map.md`.
4. Research as needed; log observations in the PRD.
5. **Present a short rebrand plan:** hero message, section order, proof, image assignments, primary CTA, any `GRAMMAR_ADDITION` or removal with its reason, and any `CONFLICT`. Wait for approval of structural items.
6. Implement content and brand tokens from the facts file, reusing the template's components.
7. **First-screen test:** screenshot the top of every page on a phone and on desktop. That first screen alone must answer what they sell, where, why trust them, and what to do next. If it doesn't, fix the message or media before anything else.
   Then check desktop, tablet and phone: crops, real text wraps, contrast, hover and focus, motion and reduced motion, every CTA's destination. Compare page and section geometry with the Phase A baseline; differences must be the approved ones.
8. Log what changed and why (`rebrand-change-log.md` or the project notes). Unresolved items go to the setup-list.

## 8. When the template can't serve a requirement (`CONFLICT`)

Don't redesign quietly. State the requirement and why the inherited layout can't meet it. Then offer options from smallest to largest:

- **A.** Adapt an existing component.
- **B.** A dedicated page or flow built from the template's grammar.
- **C.** A described structural change.

Give the impact of each on layout, motion and mobile. Sometimes the honest answer is a different template.

## 9. Gates

**Phase B passes when:**
- Every section has a mapped purpose with real content and suitable media.
- The site still looks and moves like the template, apart from approved changes.
- No invented proof.
- Every CTA has a destination.
- Phase C needs are listed.
- Desktop and phone were actually inspected.

**Phase B is blocked when:**
- Phase A isn't verified.
- The PRD is missing or unapproved for client work.
- A required claim or image is missing.
- A business-critical change needs unapproved structure.

## Anti-patterns

- "Every photo was replaced, so the rebrand is done."
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
| Lead form wanted, backend not ready | Build the form in the template's form styles, capture to D1, mark delivery as a Phase C item. |
| New brand colors | Apply as tokens, chase literal copies, verify contrast and cohesion. |
| Section needed that the template lacks | Duplicate an existing section pattern, propose it in the rebrand plan, build after approval. |
| Near-final pitch | No preview or prototype wording anywhere; forms capture for real; remaining items on the setup-list. |
