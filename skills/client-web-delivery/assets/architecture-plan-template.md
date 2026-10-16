---
framework: astro
locales: [en, es]            # primary first; every site ships a second language (live showcase standard)

deployment:
  provider: cloudflare-workers
  rendering: static
  server_runtime_required: false
  api_worker: true          # /api/subscribe, plus /api/inquiries when primary_action is a form; false only if the client's tools host every form
  reason: >

database:
  provider: cloudflare-d1   # subscribers (+ inquiries when the primary action is a form), unless another requirement picks none/supabase/convex
  realtime_required: false
  reason: >

authentication:
  provider: none
  required: false
  reason: >

storage:
  provider: static-assets
  r2_required: false
  reason: >

content:
  strategy: static
  blog_required: false
  client_editing_required: false
  reason: >

analytics:
  provider: cloudflare-web-analytics
  consent_required: true    # loaded only after the cookie banner says Accept
  reason: >

conversion:                 # from PRD.md; the plan does not restate the PRD, only what the stack must deliver
  primary_action: >         # call / estimate form / insight form / order / booking
  completion_route: >       # where it lands: D1 inquiries until handoff, then inbox / CRM / POS / scheduler
  destination_owner: >      # the person who answers it; UNKNOWN blocks calling conversions "live"

features:
  newsletter_signup: true   # always on; see "Live showcase standard"
  newsletter_hook: >        # what THIS business sends: new drinks + birthday treats / new-home alerts / ...
  cookie_consent: true      # always on
  contact_form: false       # true when primary_action is a form (estimate / insight) -> /api/inquiries
  booking: false
  live_availability: false
  accounts: false
  admin_dashboard: false
  uploads: false
---

# Architecture Plan

## Summary

{{One paragraph. Name the smallest stack that satisfies the real requirements. Say what was deliberately left out.}}

## Why each service is here

{{Repeat every non-`none` choice in a sentence a developer can re-read in six months. If a field is `none`, say why that absence is correct.}}

## Not selected

- Database: {{none / why not Supabase / why not Convex}}
- Auth: {{none unless a protected area exists}}
- R2: {{none unless someone uploads after launch}}
- D1: subscribers table (email capture), plus inquiries when the primary action is a form. Anything else in D1 needs its own reason.
- KV: not auto-selected
- Blog: {{only if they will actually publish}}

## Open business questions

{{Setup-list items that would change this plan. Empty if inference was enough.}}
