# The request form: designed for each client

There is no standard field list. A plant seller, a caterer and a roofer each need to know different things before they can give a real answer, and their buyers want to say different things. The agent designs the form for this business from research, the same way it writes the hero.

Use it whenever the PRD's `primary_action` is a form.

## What the agent does

1. **Name the moment.** What is the visitor asking for (a quote, a booking, an order, a visit, a callback), and what does the owner do next and how soon? One sentence each. If nobody knows what happens next, that is the first thing to find out.

2. **Find what the owner needs for a real first reply.** A real reply is a price range, a yes or no, or a time, not "thanks, we'll be in touch". Look at:
   - how they take requests today: their booking tool, the auto-reply on their DMs, what their posts tell people to send;
   - the forms of three to five competitors (market read §3, the "Form fields" column);
   - how the trade talks about it: forum and subreddit threads where owners say what they ask a new customer, and the default fields in the booking tools the trade uses.

3. **Find what the buyer wants to say.** Their reviews and local threads (market read §4): what people asked before buying, what they wished they'd been asked, what went wrong when nobody asked.

4. **Draft the fields and test each one.**
   - Would the owner's first reply change with this answer? If not, cut it.
   - Can the buyer answer in five seconds without looking anything up? If not, make it a pick list, make it optional, or cut it.
   - Is it in the buyer's words? Labels and options come from `language-bank.md`.

5. **Keep it short.** Seven visible fields at most. One column on a phone. Pick lists over typing. One way to reach them is required and they choose which. Photos are asked for after ("We'll text you for a photo of the spot") unless the architecture plan includes uploads.

6. **Write the promise.** The line after sending says what happens next and by when. It is a promise, so the owner confirms it (the owner sheet's "who gets it" question). Until then it says only that the request arrived.

7. **Record it in `PRD.md` section 2,** under the primary action:

   | Field | Kind (text, pick list, date) | Options | Required | Why it's there (source) |
   |---|---|---|---|---|

   Then build it in Phase C, in both languages, saving to `/api/inquiries` with the visitor's `locale` and the page it came from.

## How the thinking goes, by trade

These show the reasoning. The fields for a real client come from that client's research, never from this table.

| Business | The owner's first reply needs | So the form asks |
|---|---|---|
| Plant seller or garden design studio | What they're after, where it will live, and whether it has to be delivered | What are you looking for (plants for a spot, a full yard design, an install); sun, shade or indoors; how big the space is; pickup or delivery, with a zip code; when |
| Caterer or restaurant taking events | Whether the date is free and how much food | The date; how many people; the kind of event; pickup, delivery or served |
| Roofer or contractor | Whether it's their kind of job and their area | What's wrong or what they want built; the zip code; own or rent; how soon |
| Salon, barber or spa without online booking | Which service and who with | The service; a preferred person; days that work |
| Realtor | Which side of a sale and where | Buying, selling or renting; the area; a price range as a pick list; how soon |
| Content agency, designer, web builder | What they run and where to see it | What they need; the link to their Instagram or current site; when |

## Agencies, and the builder's own site

For a business that sells to other businesses, the form asks for **the link to the lead's Instagram or current site**. That link starts the next job: it is the seed for that client's step 0, and its answers (the trade, the need, the timing) are copied into the new `creative-direction.md` before anything else is asked. These sites also use the owner sheet (`brand-discovery` section 8) once a lead becomes a client. Other clients' sites get only their own form.

## Done when

- [ ] The moment and the owner's next step are written in one sentence each
- [ ] Every field passed both tests and names its source
- [ ] Seven visible fields or fewer, one column on a phone, both languages
- [ ] The after-sending line promises only what the owner confirmed
- [ ] The field table is in `PRD.md`, and a named person receives the requests before the form is called live
