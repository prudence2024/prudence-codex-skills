---
name: security
description: Production security, architecture, and launch-readiness workflow for web apps, APIs, forms, auth, databases, payments, uploads, dependencies, secrets, deployment, cloud cost, caching, scaling, observability, backups, and CI/CD. Use when Codex needs to review or implement security controls, harden form/API handling, verify environment hygiene, add rate limiting or headers, audit dependencies, or assess whether an AI-built application is safe and operationally ready for production.
---

# Security

## Overview

Use this skill to keep production web projects from shipping with avoidable security and operational gaps. Treat production readiness as a launch gate: validate secrets, inputs, auth, authorization, headers, dependencies, data design, deployment, cost controls, capacity, logs, backups, and failure handling before calling work done.

## Reference Routing

- Read `references/security-skill-source.md` for the full checklist, form validation examples, launch checklist, and detailed section guidance.
- Use the reference when the task touches forms, public APIs, authentication, payments/webhooks, database access, file uploads, deployment, dependency audits, or production launch checks.
- Read `references/production-foundations.md` when the task includes backend contracts, schema quality, deploy/rollback readiness, cloud cost, version-control discipline, caching/CDN behavior, or load and scaling checks.

## Core Workflow

1. Establish scope and risk.
   - Identify stack, deployment target, data stores, auth provider, payment/provider integrations, public APIs, forms, uploads, and admin routes.
   - Treat anything handling personal data, money, credentials, bookings, or admin actions as high risk.

2. Check secrets and environment hygiene first.
   - Confirm `.env`, `.env.local`, and `.env.*.local` are ignored.
   - Confirm `.env.example` lists required names with empty values.
   - Search for committed secrets without printing secret values.
   - Ensure frontend-exposed env vars are genuinely public.

3. Review inputs, forms, and APIs.
   - Validate every payload server-side with an explicit schema.
   - Sanitize or escape user content before storage/rendering.
   - Save only expected fields, never raw submitted objects.
   - Add honeypot and rate limiting for public forms.
   - Return generic client errors and log detailed server errors only server-side.

4. Review auth, authorization, and data access.
   - Use a proven auth provider.
   - Enforce authorization server-side on every sensitive request.
   - Verify row/table policies or equivalent access controls are least privilege.
   - Test cross-user access by changing IDs/URLs where applicable.

5. Review infrastructure controls.
   - Restrict CORS to exact origins.
   - Set CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and related headers.
   - Verify file upload type/content/size checks and safe storage.
   - Verify payments/webhooks use signature checks and idempotency.

6. Run dependency and code checks.
   - Run the project’s build/test/lint/security audit commands when available.
   - Use ecosystem tools such as `npm audit`, `pip-audit`, or `cargo audit`.
   - Investigate high/critical findings before launch.
   - Avoid adding unknown packages without checking registry existence and maintenance history.

7. Check operations readiness.
   - Confirm error tracking, structured logs, uptime monitoring, and billing alerts exist.
   - Confirm backups exist, location/frequency are known, and restore has been tested.
   - Confirm incident/breach response ownership and contact path are defined.
   - Apply the production-foundation checks relevant to the stack and expected traffic.

## Output Expectations

When reviewing, lead with findings ordered by severity and include file/line references when local code is available. Separate confirmed issues from recommendations. Include commands run and any checks that could not be completed. Do not expose secret values in output.

When implementing, keep fixes narrowly scoped, preserve user changes, and avoid dummy or development-only security behavior in production branches unless the user explicitly requests it.
