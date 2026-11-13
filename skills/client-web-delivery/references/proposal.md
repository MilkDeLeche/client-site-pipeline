# The proposal: what it costs and how to say yes

One page the owner can agree to. The plan poster makes them want the site; this says what they pay, when, and what happens next. It goes out only after the owner has shown interest, and only when the builder says so.

Template: `assets/proposal-template.html`, rendered with `scripts/render_pages.py` into `deliverables/pitch/<client>-proposal.pdf`.

## Where the numbers come from

The builder's profile (`~/.client-site-pipeline/builder.json`, section `offer`). Never invent a price, a discount or a term. A value the profile leaves empty is left as a blank line on the page for the builder to fill in by hand, and listed in the readiness report.

The builder's standard offer has three parts:

1. **The site:** one price for the design and build, part to start and the rest when the owner says it is done.
2. **A monthly plan:** the lower one keeps a simple site online and working. The higher one adds being found on Google and in AI search, updates, the email newsletter, analytics and a report.
3. **Add-ons the builder chooses to include,** such as an AI chat assistant. It is listed only when the builder offers it to this client, as part of the higher plan.

## What the page says

1. Who it is for and the date.
2. **What you get:** the site that is already built, in one line, with the link.
3. **What it costs:** the build price, the amount to start, the amount at the end and what triggers it. Then the monthly plans side by side with what each includes, in the owner's words.
4. **What you never have to deal with:** the builder sets up and runs the hosting, the domain, the email service, search setup and reporting. Say it as what the owner is spared. **Never name the builder's tools or what they cost** (the profile's `private_tools`): the owner is buying the result.
5. **What stays yours:** the domain, the words, the photos, the list of customers who signed up.
6. **How to start:** the first payment, a start date, and what the builder needs from them (the owner sheet).
7. A line to sign or a plain "Reply YES to start".

## Rules

- A proposal is a promise. Every line is something the builder will do at that price.
- No results promised: no rankings, no sales, no follower counts.
- Terms the builder hasn't set (notice to cancel, how many edits a month, how fast) are blanks, never the agent's guess.
- Plain words through `copywriting` and `antislop-copywriting`. Owners read "plans", never "packages".
- Second language when the owner works in it.
- The contract-questions sheet (`assets/contract-questions-template.md`) uses the same numbers. If they disagree, fix both before either goes out.

## Done when

- [ ] Every number matches the builder profile, and every blank is listed in the readiness report
- [ ] No tool, vendor or cost of the builder's appears anywhere
- [ ] One page, rendered, opened on a phone
- [ ] The builder knows it is in `deliverables/pitch/` and that nothing was sent
