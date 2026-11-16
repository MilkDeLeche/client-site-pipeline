# Amateur check: what makes a page look unfinished, and what makes it sell weakly

A look-for list, run on the built page before anything goes to an owner. It is a way of looking, with the reason for each item; add to it whenever a builder or an owner calls something amateur. A page can pass every technical check and still read as amateur to a stranger in five seconds.

It works on a cloned template too. A premium template filled with a client's real content often breaks in exactly these places: the template was designed around its own copy lengths, image shapes and item counts.

## How to run it

1. Open the production build at phone width and at desktop width. Look at the first screen for five seconds, then look away and write down what the business does, who it's for, and what you'd tap. If you can't, the first screen fails.
2. Scroll the whole page once at each width, the way a stranger would.
3. Write each finding as: the element, why a stranger reads it as amateur or weak, and the fix.
4. Sort the findings: **fix now** (no decision needed), **ask the builder** (it changes the template's layout or cuts something), **the owner's call** (a fact, a claim, a permission).
5. Put them in the readiness report. Render the page again after fixing and look: an element can be right in the code and invisible on the page.

## Looks amateur

| Look for | Why it reads that way |
|---|---|
| No single line to remember: the first screen is a paragraph set at headline size | Nothing to repeat to someone else. A headline is one thought |
| No button on the first screen | The visitor has to hunt for what to do |
| The main action is the weakest thing on the page: grey, only in the footer, or hidden inside a phone menu | The thing that makes money looks optional, or disabled |
| A grid that looks unfinished: empty cells, one item alone on a row | The template expected more items than the client has. Change the grid to fit the count |
| Media in the wrong shape: vertical video cropped into a wide frame, a wide photo squeezed tall | It was shot one way and shown another, and heads, text and products get cut off. Show it the way it was shot |
| Small labels: tags and captions too small to read on a phone | Reads as filler nobody expected to be read |
| A picture that doesn't match the words beside it | Looks like the picture was dropped in to fill a slot |
| The look changes between pages: the form or the contact page is in a different design | Feels like leaving the site at the moment of asking |
| Links that look disabled: grey text that turns out to be a link | Visitors don't try them |
| A headline that ends on one orphaned word, or wraps differently than intended on a phone | Looks unedited |
| Blurry, stretched or heavily compressed pictures and video | The work itself looks low quality, which is fatal for anyone selling visual work |
| Leftovers: template names, placeholder text, a link to nowhere | Proves nobody checked |
| Something in the code that doesn't show on the page: text the same color as its background, an element under another | Only looking at the render catches it. Blend modes and overlays are the usual cause |
| A column the template hides below desktop (`display: none` under 1200 px) that now holds selling copy or a link | Templates drop their "nice to have" column on phones. Once it carries the case for a service, most visitors (on phones) never see it. Check every filled slot at phone and tablet width, and move the column under the main one instead of hiding it |
| Photos that can't explain an idea (stages, a process, a before-and-after) | A real photo shows a moment, not a stage. Build three coded directions on one local preview page with the real captions under each (drawn phone screens, type posters in the brand colors, one simple drawing per idea), let the builder pick, then delete the preview |

## Sells weakly

| Look for | Why it's weak |
|---|---|
| A visitor can't say what they'd get | They see style and no offer. Name the services and what's in each |
| Features named without what they do for the buyer | A list of techniques means nothing to an owner. Say what each one gets them |
| Nothing says who it's for or where | A local buyer needs to see their kind of business and their area |
| No reason to trust: no real work in view, no people, no place | Claims without anything to check |
| A long list where a few groups would do | Twelve services read as none. Group them under a handful of names |
| The form asks things that don't change the reply, or misses the one that would | Friction with no benefit (`client-web-delivery` → `references/request-form.md`) |
| A claim nothing backs: a number, "best", a result | One doubtful claim makes the true ones doubtful too |
| Captions that describe what's on screen, or lines about how the agency works behind the scenes | Describing isn't selling, and the workflow is the agency's business, not the buyer's. `copy-bank` §5, "Supporting lines" |

## What it is not

Not a redesign. The template's look is the direction; this finds where the client's real content broke it, and where the page doesn't sell. A finding against the template itself goes to the builder as a proposal, never as a silent edit.
