# PRD template: business intent for a client site

Copy to `PRD.md` at the project root. This is a **starter, not an approved PRD**.

- If the user or client supplied a PRD (a file, a doc, a link), read it first. Keep their decisions and add a clearly labeled **Supplement** for missing fields. Never silently overwrite it.
- The PRD holds **intent and strategy**: who buys, what they need to believe, what action makes the business money. Publishable facts (phone, address, hours, prices, URLs) live in `src/data/<client>.ts`. The PRD may point to them; it is not a second facts store.
- Mark anything unverified `UNKNOWN` or `NEEDS APPROVAL`. Never invent proof, prices, reviews, results, or contact destinations.

---

# PRD: {{BUSINESS NAME}}

| | |
|---|---|
| Project mode | `client-production` (client is paying) / `near-final-pitch` (built before the sale; looks finished, nothing labeled preview or prototype) / `reference-only` (template clone, no client yet) |
| Status | `draft` / `approved` / `approved-with-blockers` |
| Approved by | {{the client, or the builder for a near-final pitch}}, {{date}} |
| Reference template | {{URL / name}}, license: {{owned / to buy / unknown}} |
| Sources reviewed | {{their site, Google profile, reviews, social, menu/booking pages, the client's brief}}, {{dates}} |
| Facts file | `src/data/{{client}}.ts` |

## 1. What the business does

- **Offer:** {{what exactly is sold or provided}}
- **Who buys it:** {{customer type, situation, location if it matters}}
- **How it operates:** {{service area, in person / online, ordering or booking system}}
- **Real differentiators:** {{only verifiable ones}}
- **Constraints:** {{capacity, languages, policies, budget, legal}}

## 2. The outcome this site exists for

- **Primary business goal:** {{e.g. qualified estimate requests / booked consultations / online orders / qualified project inquiries}}
- **Primary visitor action:** {{the thing a visitor actually completes: call, estimate form, order, booking, insight form}}
- **Completion means:** {{form accepted AND delivered / booking confirmed / payment authorized}}
- **What makes a lead or order valuable:** {{real qualifying criteria, e.g. budget range, timeline, owns a lot, company size}}
- **Secondary action (optional):** {{call, directions, view projects, sign up for alerts}}
- **Out of scope:** {{no login, no e-commerce, etc.}}

**Follow-through**

| | |
|---|---|
| Where the action lands | {{inbox / scheduler / POS / CRM; in a near-final pitch: captured to D1 until handoff}} |
| Who answers it | {{named person or team; `UNKNOWN` blocks any "live leads" claim}} |
| What happens next | {{reply within a day, quote, confirmation email, etc.}} |
| Open dependency | {{client inbox, Brevo account, booking login, domain}} |

## 3. Who arrives, and what they need

| Entry source | What they want to know | Proof they need | Best next action |
|---|---|---|---|
| {{Local search / "near me"}} | | | |
| {{Paid ad → landing page}} | | | |
| {{Referral / social}} | | | |

Keep only real rows. An ad usually deserves a focused landing page that answers that one offer. Don't route it through the homepage, and don't add a form where the right action is an order, a reservation or directions.

## 4. Research (what was observed, not what converts)

| Source + date | What was observed | Why it matters here | Confidence |
|---|---|---|---|
| {{their reviews / FAQ / questions customers ask}} | | | verified / tentative |
| {{published UX guidance for this industry, e.g. Google's industry UX playbooks, NN/g, Baymard}} | | | guidance, context-dependent |
| {{a peer business}} | | | visual pattern only, not proof of results |

A beautiful or popular site is a design reference, not evidence that it converts. Never invent conversion rates or keyword volumes.

## 5. Message and trust

- **Value proposition (one sentence):** {{specific and honest}}
- **Top three things a visitor must understand:** {{1}} / {{2}} / {{3}}
- **Main objections:** {{price, trust, timeline, fit, logistics}}
- **Proof available:** {{real projects, permissioned reviews, process, licenses where verified}}
- **Proof missing:** {{goes on the setup-list}}
- **Tone:** {{client-approved adjectives and an example line}}
- **Primary CTA label + destination:** {{e.g. "Request an Estimate" → /contact#estimate}}

## 6. The template and the creative direction

- **Why this template was chosen:** {{the look, type, motion, sections the user loves}}
- **Must-preserve:** {{strongest visual features; Phase A clones all of it regardless}}
- **Brand assets:** {{logo files, palette, fonts, photos; rights for each}}
- **Imagery plan:** {{client photos first; AI images (Krea) only as labeled illustrative fill, never as the client's own work, team or results}}
- **Approved changes after Phase A:** {{colors, logo placement, sections to add or remove, as approved}}

## 7. Page plan (a hypothesis for Phase B, not a Phase A instruction)

| Section | Job for this audience | Proof / media | CTA | Template section it maps to |
|---|---|---|---|---|
| {{Hero}} | | | | |
| {{Services / work}} | | | | |
| {{Proof / process}} | | | | |
| {{Contact / order / booking}} | | | | |

Phase B turns this into `section-purpose-map.md` after looking at the verified clone.

## 8. Functional needs (feeds `architecture-plan.md`)

| Need | Business behavior | Existing system | Priority | Status |
|---|---|---|---|---|
| {{Insight / estimate form}} | {{a completed inquiry reaches the agreed person}} | | must | |
| {{Signup (live showcase standard)}} | {{signups saved; promise: "…"}} | | must | |
| {{Booking / order / payment}} | {{confirmed real outcome}} | | | |

No credentials in this file. The architecture plan picks the smallest stack for these needs.

## 9. Acceptance

- [ ] A visitor can tell what's offered and what to do next without guessing.
- [ ] Every claim and image honestly represents this business; illustrative images are labeled.
- [ ] The site still looks and moves like the chosen template, apart from approved changes.
- [ ] Every enabled conversion was tested end to end (see `launch-audit` → conversion journey checks).
- [ ] A real person owns every inquiry before it is called "live".
- [ ] Mobile, accessibility, privacy and performance were checked.

**Success measure:** {{completed estimate requests / orders / bookings per month; baseline or `unknown`}}

## 10. Open questions and approval

| Question | State | Source | Impact if unresolved | Owner |
|---|---|---|---|---|
| {{destination inbox}} | `CONFIRMED` / `PROPOSED` / `UNKNOWN` / `BLOCKED` | | | |

- **Safe to start Phase A?** {{yes after clone-intake; the PRD never changes Phase A}}
- **Safe to start Phase B?** {{yes/no + blockers}}
- **Safe to switch conversions live?** {{yes/no + missing owners and systems}}
