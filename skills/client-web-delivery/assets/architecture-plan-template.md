---
framework: astro

deployment:
  provider: cloudflare-workers
  rendering: static
  server_runtime_required: false
  api_worker: true          # /api/subscribe for the email list; false only if the client's email tool hosts the form
  reason: >

database:
  provider: cloudflare-d1   # subscribers table only, unless another requirement picks none/supabase/convex
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

features:
  newsletter_signup: true   # always on; see "Live showcase standard"
  newsletter_hook: >        # what THIS business sends: new drinks + birthday treats / new-home alerts / ...
  cookie_consent: true      # always on
  contact_form: false
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
- D1: subscribers table only (email capture). Anything else in D1 needs its own reason.
- KV: not auto-selected
- Blog: {{only if they will actually publish}}

## Open business questions

{{Setup-list items that would change this plan. Empty if inference was enough.}}
