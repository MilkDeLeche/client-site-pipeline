# Market read

On an outbound pitch nobody can be asked first, so the research has to do what asking would. The owner should open the pitch and feel known: their town, their buyers, their competitors, what they're proud of. This is that research. It runs inside the step 0 homework and fills the PRD's research table at the same time, so nothing is researched twice.

Output: `market-read.md` at the project root, in the seven parts below. It feeds `creative-direction.md` (what leads, the direction), `language-bank.md` (buyer words), the template search (`design-scout.md`), the request form (`client-web-delivery` → `references/request-form.md`) and the stat cards in the hype set (`client-web-delivery` → `references/hype-set.md`).

## Rules for all of it

- **Open every source.** A search summary is a lead, not a finding. Each row carries the link and the date it was read.
- **Numbers come from whoever counted them:** the Census, a city or county office, a survey's own report with its sample size. A blog repeating a number is a pointer to the source, not the source.
- **Record what was seen, label what was inferred.** "Four of five competitors lead with a phone number" is seen. "Buyers here prefer calling" is inferred from it.
- **Nothing invented:** no search volumes, follower counts, tag counts or percentages that weren't read off a page.
- Some sites block automated readers (the Census QuickFacts pages, Land-book, Instagram). Read them in the builder's own browser, or ask the builder to open the page. Never work around a block.

## 1. The business

What they sell and what each thing is called on their own page. How people buy today (walk in, call, DM, a booking tool, a marketplace). Prices, if they publish them. What their reviews praise and complain about, in the reviewers' words with links (these go to `language-bank.md`). What they post, how often, and which posts got a response. What they're visibly proud of.

## 2. The place

The city and the area they really serve, which may be a county, a metro or a strip of highway.

- **Who lives there:** population, households, languages spoken at home, age, income. `client-web-delivery` has `scripts/census.py`, which reads the county's figures once the builder's free Census key is in the profile; otherwise Census QuickFacts in the builder's browser. Also the city's or the economic development office's own pages.
- **How people there find a business like this:** Google Maps, Facebook groups, Instagram, a local directory, word of mouth. Look at where the competitors put their effort and where their reviews are.
- **What moves demand:** seasons, school calendars, weather, local events, paydays, visitors.
- **Local names:** what residents call the area and its neighborhoods. These go into copy and tags as residents write them.

Each number gets its source, year and link. Mark the three that would mean something to this owner: they become stat cards.

## 3. The competition

Three to five local competitors (search the trade and the city on Google Maps the way a buyer would, and take the ones that show up), plus two or three of the best in the trade anywhere (from the design scout). One row each:

| Competitor + link | First screen says | First screen shows | Main button | How the offer is shown (prices, plans, menu, "call us") | Proof on the page | Form fields | Second language | On a phone | What's missing |
|---|---|---|---|---|---|---|---|---|---|

Then two short lists:

- **What everyone here does.** A buyer expects these; leaving one out reads as a gap.
- **What nobody here does.** This is the opening for the pitch, if the client can honestly fill it.

## 4. How buyers search and talk

- Type the trade and the city into Google and write down the autocomplete suggestions and the "People also ask" questions exactly as shown. No volumes.
- Read local threads (the city's subreddit, Facebook groups, Nextdoor where public) for how people ask for this kind of business and what they warn each other about.
- The questions people ask before buying become FAQ entries and form fields. The warnings become objections the page answers.

## 5. Tags

From the recent public posts of the competitors and of local buyers:

| Tag or location | Kind (trade / place / community) | Seen on (link) | Use it? |
|---|---|---|---|

- Record a tag only where it was seen. Never invent one and never guess its reach.
- **Where they go:** a few per post in the caption, the place tags first; the location tag on every post; the area's own name written the way residents write it. Check the platform's current advice on how many before setting a number.
- **Where they don't go:** the website. The same words go on the site as plain phrases in titles, headings and the Google Business Profile ("barber in Harlingen"), which is how search reads them.

## 6. Heroes

For every competitor and every scouted reference, classify the first screen:

| Site | Leads with (`product` / `craft` / `deliverables` / `results` / `credibility` / `explain` / `place` / `people`) | Media (video, photo, none) | Words on screen | Button | Does it work on a phone |
|---|---|---|---|---|---|

Close with one paragraph: what the hero of this pitch should lead with, what it should show, and which evidence on file carries it (`media-inventory.md`). This is the recommendation the builder reads before choosing a template.

## 7. The read

One page the builder can take in quickly:

- Who the buyer is here, in a sentence.
- The problem they have and haven't named, in their words.
- What to lead with, and the proof behind it.
- The opening the competitors leave.
- Three numbers worth a card, each with its source.
- The tags worth using.
- What the research couldn't settle. These become the owner sheet's questions.
- The template search brief (from `design-scout.md`).
