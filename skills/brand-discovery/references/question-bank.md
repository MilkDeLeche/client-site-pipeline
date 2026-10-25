# Question bank

Where the ask-first list comes from. Every question settles one decision the homework left open. Pick **three to five** for a text or a call. The optional PDF can carry up to about nine, because the owner answers it alone at their own pace. Skip any decision the site, socials, PRD or a style-picker brief already settle, and say in `creative-direction.md` where that answer came from.

Use the same question `id` in every channel (text, call, PDF), so answers stay comparable and a returning client's old answers line up with new ones.

## How to write each question

- **Tie it to what you found.** "Your reels are mostly the dining room at night. Should people see the food first, or the place?" beats "What's your brand personality?"
- **The owner's words, not design words.** Their trade's vocabulary is fine; ours ("hierarchy", "density", "brand voice") is not.
- **Two to five concrete options**, then **Not sure, help me choose** and **Other: ___**. Add room to explain where the reason matters more than the pick (who the site is for, what leads, what they like about a reference). By text: "A, B, or something else? Not sure is fine too."
- **One decision per question.** "Who is it for and what should they do?" is two questions.
- **Name what it decides**, for us. The `decides` field in the questions file and the Decides column in `creative-direction.md` are never shown to the client.
- **Order by impact.** A question whose answer could change the template goes first.

## Core decisions

These apply to every industry. Rewrite the options from the homework; the examples show the shape.

| id | Decides | Ask when | Question | Spanish |
|---|---|---|---|---|
| `visitor` | Who the first screen speaks to | Always, unless the PRD names one clear buyer | Who do you most want to reach with the new site? | ¿A quién quieres llegar con la nueva página? |
| `takeaway` | The hero promise | Always | After 10 seconds on the site, what should they say about you? | Después de 10 segundos en la página, ¿qué deben decir de ti? |
| `action` | The main button | When the money action isn't obvious from how they sell today | What should a visitor do first? | ¿Qué debe hacer primero alguien que entra? |
| `offer` | Which service leads and the section order | When they sell several things | If the site could sell one thing this month, which one? | Si la página pudiera vender una sola cosa este mes, ¿cuál sería? |
| `lead` | What the first screen shows (showcase emphasis, below) | Always | What should people see first? | ¿Qué debe ver la gente primero? |
| `proof` | What the site can show as evidence | Always. Ask only for what exists | What can we show? Only what you already have. | ¿Qué podemos mostrar? Solo lo que ya tienes. |
| `feel` | Look and voice | Always | Which two or three words should describe how the site feels? | ¿Con qué dos o tres palabras describirías cómo se debe sentir la página? |
| `too_much` | Density and motion | When there is a current site or a pitch to react to | Looking at this, what feels like too much? | Viendo esto, ¿qué se siente como demasiado? |
| `reference` | What to take from a site they like (decoding, below) | When they name or send one | What do you like about that site? | ¿Qué te gusta de esa página? |
| `never` | Hard limits | Always | Anything we must keep, avoid or never say? | ¿Algo que debamos mantener, evitar o nunca decir? |

## What leads: showcase emphasis

"Show our work" means different things in different trades. Record two things separately, in `creative-direction.md` §4:

- **Desired emphasis:** what the owner wants to lead with.
- **Available evidence:** what actually exists, where it is, and whether we may use it.

| Emphasis (`lead` value) | It means | Often fits | Evidence that carries it | When the evidence is missing |
|---|---|---|---|---|
| `product` | The thing itself | Restaurants, retail, makers, food trucks | Real photos of the products, a menu or price list they approve | Plan a shoot; until then lead with the place or the people |
| `craft` | The work and how it's made | Contractors, salons, barbers, tattoo, creative studios | Finished work, before and after, process photos or clips | Show fewer pieces, larger; tell the process; ask for more |
| `deliverables` | What the client walks away with | Agencies, consultants, photographers, accountants | Sample deliverables, a package list, an example report (with permission) | Describe the package plainly; mock a sample only if labeled as one |
| `results` | Outcomes for past clients | Agencies, gyms, tutors, law firms, contractors | A number or outcome with its source, date, and the client's permission | Lead with something else. Never estimate, round up or borrow a result |
| `credibility` | Why a stranger can trust them | Licensed pros, medical, legal, insurance, trades | License number, years in business they can show, certifications, named reviews used with permission | Say only what can be checked; put the rest on the setup-list |
| `explain` | How it works, what it costs | Services buyers find confusing: tax, insurance, financing, solar | Clear steps, price ranges or starting prices the owner approves | Ask the owner to walk you through a first visit; write that |
| `place` | What it's like to be there | Restaurants, bars, venues, salons, hotels | Real photos or video of the space | Lead with the product or the people until there's footage |
| `people` | The owner or the team | Barbers, family businesses, trainers, realtors | Real photos, names used with consent | Lead with the work; a stock face is never a team member |

The two lists will often disagree ("lead with results" and no results on file). That is a finding, not a failure: write it as a gap, lead with an emphasis the evidence can carry, and put the missing evidence on the setup-list. A conflict rule in the questions file can flag it automatically.

## Decoding a reference

A reference site is usually admired for one quality, not the whole thing. Find which one before anything transfers. Ask "What's the one thing you'd take from that site?" or offer the qualities as options.

| Quality | Sounds like | What transfers | What never transfers |
|---|---|---|---|
| Visual design | "It looks clean", "I like the colors" | Type approach, color approach, spacing, how photos are treated | Their layout pixel for pixel (unless it's a licensed template we clone), their photos, their logo |
| Positioning | "They sound like the real deal" | How plainly the promise is said, and who it's said to | Their claims and their words |
| Content hierarchy | "You see what matters right away" | What goes on the first screen, section order | Sections we have nothing real to fill |
| Credibility | "They look trustworthy" | The kind of proof and where it sits | Their reviews, client logos, awards, numbers |
| Customer experience | "It's so easy to book" | The path to the action, how many steps, the kind of booking tool | Integrations the architecture plan didn't choose |
| Volume of work | "They have so much work" | Nothing visual. Curate what exists, plan a shoot, size the site to the work | Pretending to have more |
| Other | Their words | Write them down and ask once more | |

A reference brand is still study-only (section 2 of `SKILL.md`). Only a licensed template is a clone candidate, and only when the quality they admire is how it looks.

## Industry add-ons

Two or three extra questions per trade, used only when the core decisions leave them open. Each still gets Not sure and Other.

**Restaurant, café, food truck**
- How do most people order today: walk in, call, an app, or catering requests? *Decides the main button.*
- Should the menu show prices? *Decides how the menu section reads.*
- Is the place itself part of why people come? *Decides `place` vs `product` leading.*

**Contractor, builder, home services**
- What jobs do you want more of, and which ones do you turn down? *Decides offer order.*
- Do you have finished-job photos, before and after, or neither? *Decides proof.*
- Do customers need to see licenses or insurance before they call? *Decides credibility placement.*

**Salon, barber, spa, anything booked by appointment**
- Do clients book online, by text, or walk in? *Decides the main button and the booking tool.*
- Do clients pick a specific person? *Decides whether `people` leads.*
- Are prices fixed, "starting at", or by consultation? *Decides the price display.*

**Retail, products, makers**
- Which three products should a first-time visitor see? *Decides the first screen.*
- Do people buy online, in the store, or both? *Decides the action and whether a cart is in scope.*
- Is the story of how it's made part of the sale? *Decides `craft` vs `product`.*

**Licensed professional: law, tax, insurance, medical, real estate brokerage**
- What worries a new client most before they call? *Decides what the first screen answers.*
- Which credentials can we show, with numbers? *Decides credibility; nothing unverifiable.*
- Is there anything you're not allowed to say or promise? *Decides `never`; check the trade's advertising rules.*

**Content or creative agency, photographer, videographer**
- Who are your clients: other businesses, people, or both? *Decides the visitor.*
- When someone hires you, what do they get at the end? *Decides `deliverables` vs `craft`.*
- How many finished projects can we show, honestly? *Decides site size and density.*

**Gym, fitness, coaching**
- Who are you for: beginners, athletes, a niche? *Decides the visitor.*
- What should a new person do first: a free class, a call, a sign-up? *Decides the action.*
- Do you have member results you're allowed to share? *Decides `results`, with permission only.*

**Real estate agent or team**
- Do you mostly work with buyers, sellers, or rentals? *Decides the visitor.*
- Should listings lead, or you? *Decides `product` vs `people`.*
- Which areas do you want to be known for? *Decides local copy and SEO.*

For a trade not listed, write two or three in the same pattern: what they want more of, how customers act today, what a stranger needs to believe.

## Spanish and two-language owners

- Ask in the language the owner writes to you in. Keep the same ids, so a bilingual project has one set of answers.
- Match their register (tú or usted). The built-in PDF strings use tú; rewrite the questions file if the owner writes in usted.
- Write each language for how local owners talk, never word for word from the other. Short and plain beats correct and stiff.

## Recording answers

Each answer in `creative-direction.md` §3 keeps its channel (text, call, meeting, PDF), date, and the owner's own words where they gave them. "Not sure" is a real answer: it means the builder recommends and the owner reacts to a version. A blank is not an answer; ask again or decide and label it a guess.
