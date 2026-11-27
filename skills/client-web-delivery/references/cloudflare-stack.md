# Cloudflare first: how every outside service connects

Builder rule (Nov 2026): every project runs on Cloudflare, and every outside API is connected the same way. One dashboard holds the domain, the site, the API and the keys, so connecting a service is a short, repeatable routine instead of a new setup each time.

## What lives on Cloudflare

Use Cloudflare for everything it does, on every project:

| Job | Cloudflare piece |
|---|---|
| Domain and DNS | Cloudflare DNS (the domain's nameservers point to Cloudflare) |
| The site | Workers static assets |
| The API | The Worker's `/api/*` routes (`assets.run_worker_first: ["/api/*"]`) |
| Keys and passwords for outside services | Worker secrets (`wrangler secret put`) |
| Settings that aren't secret (sender address, site URL) | `vars` in `wrangler.jsonc` |
| Email capture and form inquiries | D1 |
| Files uploaded after launch | R2 |
| Scheduled jobs (reminders, cleanups) | Cron Triggers in `wrangler.jsonc` |
| Receiving mail at the business address | Email Routing, forwarding to the owner's inbox |
| Analytics | Cloudflare Web Analytics |
| Bot challenge on a form | Turnstile, only when the plan names it |

An outside service is used only for what Cloudflare doesn't do: sending email, taking payments, or a relational database with row-level security when the architecture plan picks one. The browser never holds an outside service's secret key and never calls a secret-keyed API directly. It calls the Worker, and the Worker calls the service. (Keys that a service publishes for browsers by design, like a publishable key, are the exception.)

## Connecting any API: five steps, always in this order

1. **Domain first.** If the service sends from or checks the client's domain, add the DNS records it gives you in Cloudflare DNS, exactly as shown, as **DNS only** (grey cloud). Use the service's automatic Cloudflare setup when it offers one. Wait until the service shows the domain as verified.
2. **The narrowest key.** Create the key with the least access that does the job: sending only, a restricted key, limited to one domain. A leaked sending-only key can't change the account.
3. **Into a Worker secret.** Whoever owns the account runs `npx wrangler secret put NAME` in the project folder and pastes the key when asked. Never in chat, never in `wrangler.jsonc`, never in a committed file. For local work, `.dev.vars` (gitignored). The secret is live as soon as the command finishes; no redeploy.
4. **A health check that shows it.** `/api/health` (or the site's own word for it) returns one true/false per connected service, never a value. The code works without the secret: it skips the send or answers 503 with a plain message, so the site can ship before the key exists.
5. **Prove it with a real action.** Do one real thing on the live site (book, sign up, submit) and check the service's own log, not just the success message.

When walking the builder or owner through it, give these steps one screen at a time: what to click, what to type, what they should see.

## Email

**Sending provider:** Resend by default, called from the Worker. Brevo, Mailchimp or Klaviyo only when the client already uses one.

**Emails to one person** (confirmations, reminders, status changes):
- Built in the Worker for each recipient, from code: one function makes the HTML and a plain-text version from that person's data (name, item, date, link). Nothing is stored as a template in the provider's dashboard.
- Preview files with sample data go in `deliverables/` so the builder can see the design. Say clearly that they are previews; pasting them into the provider would freeze the sample data.
- Set `reply_to` to the business inbox, so a customer's reply reaches a person.
- Reminders run from a Cron Trigger.

**Newsletters and announcements** (one email to many people):
- Use the provider's broadcast feature (Resend Broadcasts), never a loop over the one-person sending API. Broadcasts handle the unsubscribe link and header, bounces and complaints, which inbox providers and privacy law both require.
- The design is the builder's or owner's. Turn it into email-safe HTML (tables, inline styles, tested in Gmail and Outlook) and save it as a provider template with its name and unsubscribe variables.
- Signups come in through the site's `/api/subscribe`. The Worker saves them to D1 and, once the provider is connected, adds them to the provider's audience. The form carries a consent line and the privacy link.

The full method (popup rules from research, which automations fit which trade, consent, the monthly newsletter, the one-click setup, testing) is in `email-marketing.md`.

**Automatic follow-ups** (a welcome after signup, a review request the day after a job is done, a warranty check a week later, a service reminder months later):
- Use the provider's automations (Resend Automations): the Worker sends one event when the thing happens (`suscriptor.nuevo`, `orden.entregada`), and the sequence, waits and emails are set up in the dashboard. The Worker doesn't schedule these itself.
- Only to contacts who opted in to that kind of email. Confirmations the customer needs (their booking, their order) stay as one-person emails from the Worker.
- If events or contacts need a full-access key, the Worker holds that one key as a secret, and the setup-list says so.

**The domain for email:**
- Verify the main domain for one-person email, so the sender stays `name@client-domain`. The provider's records sit on their own names (for example `send.` and `resend._domainkey`), so they don't clash with Email Routing's records on the main domain.
- Add a DMARC record yourself if none exists: `TXT`, name `_dmarc`, content `v=DMARC1; p=none;`.
- On a paid plan, verify a separate subdomain for newsletters (for example `news.client-domain`). If a newsletter gets marked as spam, only that subdomain's reputation drops, and confirmations keep reaching inboxes. Resend's free plan allows one domain (check the pricing page), so on it both kinds of email go from the main domain.

**Keys for newsletters:** managing contacts and broadcasts needs a full-access key. When the site uses automations (below), the Worker holds that key and adds each signup to the provider's list as it comes in. When it doesn't, the Worker keeps the sending-only key and the full-access key stays off it: signups are saved in the site's own database, and a script the builder runs from the project folder (with the key in the gitignored `.dev.vars`) adds new signups to the provider's list and creates the broadcast as a draft. It adds only new contacts, so it never re-subscribes someone who unsubscribed. The builder reviews the draft in the provider's dashboard and sends it there.

**Consent:** only people who opted in get newsletters. Customers in the shop's records who never ticked a box don't. A booking or order form can offer an unticked "send me offers" box, and the privacy page names the purpose and the provider.

## In the architecture plan and the handoff

`architecture-plan.md` names each outside service, why Cloudflare doesn't cover it, the secret's name and its health-check field. The setup-list says who creates each key and that they put it in with `wrangler secret put`. The handoff explains each piece in one plain sentence ("your confirmations are sent by your own server, from your own address").
