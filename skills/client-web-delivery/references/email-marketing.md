# Email marketing: signups, automatic emails and the monthly newsletter

Every client site that collects emails gets this, built on Resend and Cloudflare (`cloudflare-stack.md`). The goal is retention: customers who come back, leave reviews and open the monthly email. Part of it runs by itself (the automatic emails) and part of it stays manual on purpose: the monthly newsletter is the builder's work inside the monthly plan, and it's the part the owner sees every month.

Research behind this page: Nov 2026, from popup and email benchmark studies (Omnisend, Popupsmart, Wisepops, Klaviyo, Stripo), Nielsen Norman Group on overlays, review-timing guides (Feefo, Housecall Pro, BetterBunch), bike-industry retention write-ups (Workstand, RideClub), and Resend's docs. Sources at the end. Redo the research when a trade is new to the pipeline: how that trade's customers talk about the emails they like and the ones they unsubscribe from (Reddit, reviews), through `copy-bank`.

## 1. Capture: the signup popup and the inline form

What the research agrees on, and what we build:

- **Never on arrival, never full screen.** People hate popups that block reading, especially on phones (NN/g), and search engines penalize intrusive ones on mobile. Timing studies disagree with each other (6–10 s, over 5 s, no difference), so don't tune by seconds: tune by interest.
- **Show it after real interest:** the visitor read about half a page, or opened a second page, and has been on the site at least ~12 seconds. Never while the cookie banner is up, never on the booking, checkout, tracking or privacy pages, never to bots or the prerender.
- **Shape:** a small card in a desktop corner; on phones a bar at the bottom, about a quarter of the screen at most, field and button on one row. A visible close button (44 px target), Esc closes, no focus trap, no dimmed page.
- **Memory:** closed = don't show again for 30 days; subscribed (here, at booking, or in the footer) = never again. Stored in `localStorage` inside try/catch.
- **Ask for the email only.** Every extra field costs signups. The name comes later (booking, order).
- **Say exactly what they get and how often**, in the buyer's words from `language-bank.md`: "One email when new bikes come in or there's a deal. That's it." A concrete perk (a discount, a free check, early access) roughly doubles signup rates in the studies, but **only the owner can offer one**: put it on the owner sheet as a question, and never invent it.
- **Also inline:** a signup band in the footer of every public page, and an **unticked** "also email me offers" box on the booking or order form, shown only when they typed an email.
- **Bilingual**, like the rest of the site.
- **Consent line** under every form: what they get, unsubscribe anytime, link to the privacy page.

Testing it: Playwright sets `navigator.webdriver` and a "Headless" user agent, and the popup correctly hides from bots. In the test, set a normal user agent and override `navigator.webdriver` with `addInitScript`, or it will never appear. Check: not on arrival, not on time alone, appears after scrolling, stays closed after closing, phone width has no horizontal scroll, the email field isn't squashed (a `flex-col` row with `flex-1` collapses its height).

## 2. Where the list lives

- Signups go through `POST /api/subscribe` on the Worker: same-origin check, rate limit, honeypot, the same answer whether the email is new or not.
- The Worker stores them in the site's own database (D1 on a static site, the app's database when there is one), lowercased, with the date of consent, the language and where they signed up. Admin-only read access in the panel when there is one.
- Then it adds them to the provider's **"Offers" segment** (create the contact; if it already exists, update it and add it to the segment; a fresh signup is fresh consent) and sends the `subscriber.new` event once.

## 3. Automatic emails (Resend Automations)

The Worker only sends events. The waits and the emails live in Resend, where the builder can change copy and timing without a deploy. Pick the ones that fit the trade:

| Automation | Event | Timing (from the research) | Fits |
|---|---|---|---|
| Welcome | signup | right away (the most-opened email anyone sends) | every site |
| Review request | job done / order delivered | within a day: most guides say same day to 48 h; send it the next morning | services, shops |
| Warranty / "how is it going" | same event | about a week later (bike shops: cables settle, free adjustment period) | repairs, installs, new products |
| Service reminder | a date the app knows | when the item is due (bike shops: 3–5 months) | maintenance trades |
| We miss you | no visit in N months | 3–24 months lapsed | repeat-visit businesses |
| Item birthday | purchase date | one year later | big purchases |

Rules:
- **Consent.** The newsletter needs an opt-in. Service follow-ups (review, warranty, reminder) go to customers who gave an email for the service and didn't refuse, listed in the privacy notice with how to stop them; every one carries an unsubscribe link. Mexico's new data law (in force since March 2025) requires new consent for purposes the notice didn't list, so update the privacy notice before turning a new follow-up on. US recipients: CAN-SPAM's opt-out and address rules.
- **Never gate reviews.** Ask everyone the same way. Don't send happy customers to Google and unhappy ones to a private form: Google's policy forbids it. "If something isn't right, reply to this email" as a separate line is fine.
- **Don't flood old orders.** The job that sends events only looks at the last few days, and records each event it sent so it's never sent twice.
- **One event per moment.** Sending happens from a daily cron (the morning, local time) or from the endpoint where the thing happens.

Templates for automations use `{{{VARIABLES}}}` with fallbacks (`SALUDO` with "Hi", the item with "your bike"), contain `{{{RESEND_UNSUBSCRIBE_URL}}}` in the footer (Resend doesn't add it to automation emails), and are published before an automation can use them.

## 4. One-click setup

Don't make the builder click through Resend's dashboard. The site gets an admin-only button (or, on a site without a panel, a script run from the project folder with the key in `.dev.vars`) that creates the segment, creates or updates every template, publishes them, and creates each automation with `status: "enabled"` if one with that name doesn't exist. It can be run again: it updates templates and never duplicates automations. It shows one line per step, so a failed step says what Resend answered.

Resend API facts that matter (Nov 2026): Audiences are now **Segments**. `POST /events/send` (`event`, `email`, `payload`) starts automations. Automation steps: `trigger`, `condition` (connections `condition_met` / `condition_not_met`), `delay` (`"6 days"`, max 30 days), `send_email` (template id or alias plus a `variables` map with `{ "var": "event.x" }`). Every request needs a `User-Agent`. 10 requests per second per account. Contacts, events, segments, templates and automations need a **full access** key.

## 5. The monthly newsletter (manual, on purpose)

- One email a month to the "Offers" segment, sent by the builder from Resend → Broadcasts, starting from the client's base template. This is a selling point of the monthly plan, and every client on the plan gets it: the owner sees a new email every month with their new stock or deal, made for them. It's always listed on their billable (`billable.md`). A client who bought the job as a one-time purchase gets the template ready and no monthly emails from the builder.
- Content: what's new, the price, until when, one button (WhatsApp or the booking page). Relationship first, hard sell second: shop news, a tip, what came in. Bike-shop write-ups say a sale in every email makes locals unsubscribe.
- Send yourself a test, read it on a phone, then send.
- **Templates come from Copymail** (the builder's lifetime library): the builder picks one, and it's rebuilt for the client with their brand kit (fonts, colors, logo, real photos) and copy from `language-bank.md`, the same way a MotionSites or Envato site template is adapted. Until then the site's base template is a plain version of the site's own transactional email. The pending-items list reminds the builder to bring the Copymail pick.

## 6. Measuring it

Count signups server-side (the database), and read Resend's numbers for each automation and broadcast. Opens are inflated by Apple Mail's privacy protection: report clicks, bookings and replies instead. A monthly line in the update brochure ("12 new subscribers, the review email brought 3 Google reviews") is the kind of proof that keeps the monthly plan paid. Only numbers that came from the database or Resend.

## 7. Deliverables this produces

- Preview HTML and a PNG of every automatic email and the base newsletter in `deliverables/correos/` (sample data, labeled as previews).
- A line in the update brochure, the billable and the pending-items list (`client-site-pipeline` → `references/pending-items.md`).

## Sources

- Omnisend, email popup statistics: https://www.omnisend.com/blog/email-popup-statistics/
- Popupsmart, popup benchmark data: https://popupsmart.com/our-data and https://popupsmart.com/blog/popup-timing
- Klaviyo, signup form best practices: https://www.klaviyo.com/blog/sign-up-form-best-practices
- Nielsen Norman Group, overlays: https://www.nngroup.com/articles/overlay-overload/
- Stripo, welcome email open rates: https://research.stripo.email/welcome-email-open-rates
- Feefo, when to ask for feedback: https://business.feefo.com/resources/when-to-ask-for-feedback-data-backed-tips-to-boost-engagement
- Housecall Pro, when to ask for reviews: https://www.housecallpro.com/learn/when-how-to-ask-for-reviews/
- BetterBunch, review timing by industry: https://betterbunch.com/blogs-and-articles/timing-is-everything-optimal-timing-for-review-requests-for-different-industries
- Workstand, returning customers: https://blog.workstand.com/how-to-win-returning-customers
- RideClub Engage: https://thebikecooperative.com/rideclub-engage/
- New LFPDPPP summary (EY): https://www.ey.com/es_mx/technical/tax/boletines-fiscales/nueva-ley-federal-proteccion-datos-personal-posesion-particulares
- Resend automations: https://resend.com/docs/dashboard/automations/introduction
