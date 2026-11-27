# The billable (cobro)

A short document that shows the owner what they are paying for and why the price is fair: everything that was built, in their words, next to what the same things cost elsewhere. It's the builder's to send, when the builder says so.

## When

- When the builder decides to charge for a job, or for work added after the original build.
- **After every update that adds something the owner can use** (a new feature, an automatic email, a security round), the existing billable is brought up to date in the same session as the update brochure. A new line goes in, the comparison is checked again, and the date changes. Ask the builder whether the price changes: never change a price on your own.
- Not a contract and not an invoice for taxes. If the owner needs a tax invoice, that's the builder's accountant.

## Where

`deliverables/cobros/<YYYY-MM-DD>-cobro-<client>.html`, exported next to it as `.pdf` (letter) and one `.png` per page. A new date when it's reissued; the old one stays for the record.

## What goes on it

1. **Header:** the client's name, a folio (`XX-001`, +1 per billable for that client), the date, and the brand the builder works as for this client (`Working as:` in `pipeline-state.md`; if it isn't there, ask, offering the `brands` in the builder profile). The same brand and tagline go in the footer of every page. Built in the client's design kit, like the update brochure.
2. **Page 1, what it does for them:** each feature as one line led by what the owner or their customers gain ("customers book from their phone at midnight"; "a review request goes out the day after every pickup"), grouped (the site, the shop system, email marketing, security). Only features that are live and verified.
3. **Page 2:**
   - A table: every line with its status. Lines included in the price say "Included", so the owner sees the size of the work.
   - The total, and the payment line (how and when).
   - **What it would cost elsewhere:** what comparable tools charge per month, each with its source and the date it was checked (for example a booking tool, a shop-management system, an email marketing tool). Real prices from the vendors' pages, never invented, never a "value" made up from hours.
   - **The monthly plan, on every client's billable by default** (builder rule, Nov 2026): its price and what it includes, from the builder profile (`offer.plans`). Always list **the monthly emails with their promotions** (the builder designs and sends one each month to the client's subscriber list), next to the other monthly work (updates, the report). That's the work the owner sees every month, and it's what makes the plan worth paying. Put the comparison next to it: what an email tool alone costs, with its source, and that nobody writes the emails for them there.
   - **Exception: a one-time purchase.** When the builder sold the job as a single payment, leave the plan off, and don't promise any monthly work anywhere on the billable or the brochures: say the newsletter template is ready, not who sends it each month. Record the client's deal (one-time or monthly) in `pipeline-state.md` so the next billable gets it right.
   - **"Por qué importa" / "Why it matters"**, the closing block: one or two plain sentences on what this protects or brings in for their business.

## Voice and checks

Same rules as the update brochure (`update-brochure.md`): the owner's language, short sentences, researched voice, run through `humanizer` / `antislop-copywriting`, no tool or vendor brand names except where they help ("React Router 7"), no secrets, nothing a run didn't prove. Open the PNGs and read them as the owner would before telling the builder where they are.

## Private

The billable and the builder's prices stay in `deliverables/` (gitignored). Never in the repo, never in a public pipeline example with a real client's name or price.
