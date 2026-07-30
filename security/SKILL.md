---
name: security
description: Production security, architecture, and launch-readiness workflow for web apps, APIs, forms, auth, databases, payments, uploads, dependencies, secrets, deployment, cloud cost, caching, scaling, observability, backups, and CI/CD. Use when Codex needs to review or implement security controls, harden form/API handling, verify environment hygiene, add rate limiting or headers, audit dependencies, or assess whether an AI-built application is safe and operationally ready for production.
---

# Security

## Purpose

Use this skill to assess or implement evidence-backed application, API, data,
infrastructure, supply-chain, and production security controls. Treat security as
a launch gate and never infer that configuration, deployment, or provider
behavior is verified without evidence.

## Ownership boundaries

- Security owns threat and risk assessment, secrets, input and output handling,
  authentication and authorization controls, data access, API and webhook
  security, uploads, headers, CORS, CSRF, dependencies, CI security gates,
  deployment safeguards, resilience, backups, cost-abuse controls, and
  security-relevant observability.
- `$session-security` owns idle and absolute timeout behavior, warning UX,
  meaningful activity, cross-tab coordination, reauthentication, and workflow
  restoration. Supply it with Security's authentication and server-enforcement
  constraints rather than redesigning those behaviors here.
- `$incident-response` owns active incident command, severity, communications,
  recovery coordination, post-mortems, and remediation tracking. Security may
  identify readiness gaps and create a handoff.
- `$legal-business` owns legal documents and jurisdiction-specific legal
  interpretation. Security supplies verified data and control facts.
- `$design-toolkit` owns interface and interaction design. Security supplies
  constraints for safe forms, errors, authentication, and sensitive actions.
- `$visibility` owns crawlability and search visibility. Coordinate CSP,
  redirects, and public endpoints without taking over search decisions.

## Reference routing

- Read [security-skill-source.md](references/security-skill-source.md) for the
  complete control checklist and implementation examples.
- Read [production-foundations.md](references/production-foundations.md) for
  backend contracts, data design, deployment, cloud cost, delivery, caching, and
  capacity.
- Read [security-reasoning.md](references/security-reasoning.md) for Shared
  Context, evidence levels, decision records, reporting, and handoff rules.

## Workflow

1. Validate supplied Shared Context or create an in-memory envelope. Record the
   project, environment, assets, trust boundaries, data classes, actors,
   integrations, constraints, and unknowns.
2. Inspect the repository and authorized runtime evidence. Do not print secret
   values or perform active testing against production without authorization.
3. Establish threat scenarios and risk using likelihood, impact, reachability,
   existing controls, and evidence strength.
4. Review applicable controls:
   - secrets and environment isolation;
   - server-side validation, sanitization, encoding, query safety, and mass
     assignment;
   - authentication, authorization, least privilege, tenant isolation, cookies,
     CSRF, and login abuse;
   - databases, storage, uploads, payments, webhooks, idempotency, and failure
     handling;
   - CORS, CSP, headers, TLS, caching, deployment, rollback, cost, and capacity;
   - dependencies, lockfiles, provenance, audits, CI/CD, backups, restore
     evidence, logging, alerting, and security ownership.
5. Compare credible remediation alternatives. Prefer existing platform and
   project controls, minimal privileges, and narrowly scoped dependencies.
6. Implement only authorized changes. Preserve existing behavior unless the
   unsafe behavior is the finding being remediated.
7. Validate locally and, when authorized, against the intended environment.
   Separate implemented, built, deployed, reachable, exercised, and monitored
   evidence.
8. Record the decision, update Shared Context, produce the standardized report,
   and hand off domain-owned follow-up.

## Required decision record

For every material security decision, record:

- selected control and why it was chosen;
- credible alternatives, rejection reasons, and trade-offs;
- affected assets, actors, threats, and trust boundaries;
- evidence, validation environment, and residual risk;
- assumptions, uncertainties, owner actions, and rollback considerations;
- Shared Context changes and specialist handoffs.

Validate machine-readable decisions against
`schemas/security-decision.json`. Use the common report and Shared Context
schemas for run reporting and context updates.

## Evidence and safety rules

- Label findings as confirmed, likely, informational, not applicable, or not
  verified; do not convert missing evidence into a confirmed vulnerability.
- Never expose secrets, tokens, private keys, personal data, or exploitable
  detail unnecessarily in reports.
- Do not run destructive, exploitative, high-volume, or production-active tests
  without explicit authorization and a bounded plan.
- Treat client-side validation, hidden UI, CORS, and obscurity as insufficient
  substitutes for server-side controls.
- Do not claim a backup is recoverable until restore has been exercised.
- Do not claim monitoring works until an alert path has been exercised.
- Report the three highest-risk launch blockers first, then lower-priority
  improvements and checks not run.
