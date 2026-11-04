---
name: copy-bank
description: The shared tagline and hook library, and the method for using it. Find the buyer's own words with web research, write many candidate lines from proven patterns, filter them, give the owner a shortlist, and log what they pick or reject so the bank grows with every client. Holds patterns.md (hook structures with real, credited examples and the buyer awareness level each fits), banned.md (overused category lines and every line an owner rejected, with why), approved.md (lines owners picked) and industries/ (buyer quotes and competitor claims by trade). Produces a per-client language-bank.md. Use for hero lines, hooks, taglines, slogans, headline options, service-card lines and signup hooks, when copy reads generic, cringe or "like every other agency", at brand-discovery homework, and at the Phase B hook bank.
---

# Copy bank

Pros rarely invent a strong line from nothing. They find how the buyer already talks: reviews, threads, DMs, sales calls. They match the line to how aware the buyer is of the problem. They study a swipe file of patterns that worked, write far more lines than they need, and cut hard. The owner's ear picks the winner. This skill is that method, plus a library that grows with every client, so each job starts from proven patterns and real local language instead of a blank page.

A list of the most-used taglines isn't the goal: a line everyone uses is generic by definition. The most-used lines go into `banned.md`. The bank is built from patterns, buyer words and the owner's picks.

| File | What it holds |
|---|---|
| `patterns.md` | Hook structures, each with real credited examples, the awareness level it fits, when it works and when it fails |
| `banned.md` | Category clichés (English and Spanish), competitor lines seen in the market, and every line an owner rejected, with the reason |
| `approved.md` | Lines owners picked: the line, its pattern, the industry and region, the buyer words it came from, the date |
| `industries/<trade>.md` | Buyer quotes with links, what competitors claim, the hidden problem, the awareness level, buyer-side research |
| `assets/language-bank-template.md` | The per-client file this skill produces |

Drafting runs through `copywriting`; filtering through `antislop-copywriting` (DURING mode). Neither overrides the facts file: no invented reviews, prices, results or contact details, in any line.

## 1. Read the bank first

Before writing a single line: read `banned.md`, `approved.md`, and the `industries/` file for the client's trade, plus the file for **their buyers'** trades when the client sells to businesses (an agency, a sign shop, a bookkeeper). A line already in `banned.md` never goes to the owner again. A line in `approved.md` is a pattern to learn from, not copy to reuse for another client.

## 2. Find the buyer's words (research)

Copy `assets/language-bank-template.md` to the project as `language-bank.md`. Fill §2 from, in this order of value:

1. The client's own reviews, comments, DMs and FAQs; what customers say to the owner at the counter (ask).
2. Reviews of competitors and of the category (Google, Yelp, Facebook).
3. Threads where buyers talk among themselves (Reddit, Facebook groups, forums), in the site's languages. Spanish-speaking buyers write differently from translated English; search in Spanish too.
4. Peer sites in the client's region. These feed §3, the avoid list, not the hooks.
5. Industry surveys and studies. Research notes only: a number reaches the page only from a primary source, with its date.

Write each quote verbatim, under 15 words, with the link and the date read. Mark secondary sources (a mirror, a summary, a blog citing a survey) as secondary. Group quotes into themes: the time they don't have, the guilt, what didn't work, what they envy, what they're proud of. The most valuable quotes are the ones that name a problem the owner hadn't put into words.

Add anything new to `industries/<trade>.md`, so the next client in that trade starts with it.

## 3. Set the awareness level

From Eugene Schwartz, *Breakthrough Advertising* (1966). Each buyer situation in §1 gets one level, and it decides what the opening line is allowed to assume:

| Level | The buyer | The line opens with |
|---|---|---|
| Unaware | Doesn't see a problem | Their world: a scene, their pride, their customer's behavior |
| Problem-aware | Feels it, hasn't looked for a fix | The problem in their words, then the relief |
| Solution-aware | Knows fixes exist (agencies, apps) | Why this way works for someone like them |
| Product-aware | Knows this business | The offer, the proof, the reason to act now |
| Most aware | Ready | The name, the price or package, the button |

A hero for owners "with a problem they didn't know they had" is written for unaware or problem-aware readers. A bare question about the problem ("Got a bar?") fails there: they don't feel addressed yet. Start from their world, or from the problem in the words they use, and land the payoff.

## 4. Write many, from the patterns

At least **30 candidates per hero**, across at least six patterns from `patterns.md`, written in every site language. Write the second language natively, the way local owners talk; never translate word for word. Service cards, signup hooks and section heads need fewer, but still several options each.

Each candidate records its pattern and the §2 quote or fact it comes from. A line with no source in §2 or the facts file is a guess and is labeled as one.

## 5. Filter

Every candidate passes all of these before the owner sees it:

- **Counter test:** would the owner say it out loud to a customer at the counter? If it sounds like an ad agency, cut it.
- **Swap test:** could any competitor in `banned.md` §2 sign it unchanged? Then it's generic. Cut or sharpen.
- **Payoff test:** a hook ends on what the owner gets or feels, in an everyday phrase, in about five words. A line that only names the problem fails; so does one that scolds.
- **Picture test:** can the reader picture the result (the full room, the sold sign, the phone ringing), not the footage?
- **Truth test:** every promise in it is something the client actually does, backed by the facts file. "Let it sell itself" is a hope people say every day; "we'll double your sales" is a claim.
- **Banned check:** nothing from `banned.md`, and no AI tells (antislop: no em dashes, no "not X, it's Y", no rule-of-three lists, no staccato stunts).
- **Trademark check:** no famous tagline and no near copy of one. The examples in `patterns.md` are for study.

## 6. Shortlist and the owner's pick

Give the owner three to five lines per slot, each with its pattern and the buyer words behind it, in both languages, plus your recommendation and why. Show them in context when you can (on the running page or a screenshot), because a line reads differently over its photo. The owner picks or tweaks; their ear for their own customers beats ours.

## 7. Log it, so the bank grows

After the owner answers:

- **Picked:** add to `approved.md`: the line in each language, its pattern, the industry and region, the buyer quote or fact it came from, the date. Use the trade and region, never the client's name, and nothing private.
- **Rejected:** add to `banned.md` §4 with the owner's reason in their words. A rejection is as useful as a pick.
- **New buyer words or competitor lines:** add to the `industries/` file.

Write these to the pipeline's source checkout (the folder that holds `install.sh`; ask once if you don't know where it is), then reinstall. The installer replaces the installed copy, so lines written only there are lost on the next install; if that is the only copy available, write there and tell the user which lines to move into the repo. The repo may be public: quotes come from public pages, and no client names, private tools, prices or contact details go in.

## Where the pipeline uses it

| Step | What happens here |
|---|---|
| 0, `brand-discovery` homework | Start `language-bank.md` §1–4: buyer situations, buyer words, the competitor avoid list, the owner's own words |
| 3, Phase B copywriter | Write §5 candidates from the patterns, filter, put the shortlist in the rebrand plan; the hook bank in `section-purpose-map.md` points to the picks |
| After the owner picks | §7 logging; the hero is built from the picked lines only |
| Client feedback on copy ("it's generic", "makes no sense") | Log the rejected lines with the reason, go back to §2 for more buyer words, then §4 |

## Anti-patterns

- Writing the hero from the template's copy or from your own head, with an empty §2.
- "Most used taglines for agencies" as the source. Those go into `banned.md`.
- One perfect line handed to the owner. Give a shortlist with sources.
- The Spanish line translated from the English one.
- A buyer statistic from a blog on the page.
- A famous brand's tagline with one word swapped.
- A rejected line offered again to the same owner, or to the next client.
- Picks and rejections kept in the chat only, so the bank never grows.

## Acceptance scenarios

| Scenario | Expected behavior |
|---|---|
| New client, empty industry file | Research §2 from the web first, add the quotes to a new `industries/` file, then write candidates |
| Owner says the hero lines "make no sense" | Rejected lines go into `banned.md` with the reason; more buyer words, a new shortlist |
| Owner tweaks a shortlisted line | The tweaked version goes into `approved.md`; the original is noted as the source |
| Second client in the same trade | Starts from that trade's file and `approved.md` patterns; writes new lines from its own buyer words |
| A strong line needs a fact nobody has (a result, a guarantee) | It stays off the shortlist; the fact goes on the setup-list |
| Bilingual site | Every candidate and pick has both languages, the second written natively |
