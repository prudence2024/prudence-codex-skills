---
name: post-production
description: Coordinate a complete evidence-based post-production audit and hardening pass for websites and web applications across SEO, AI discoverability, accessibility, performance, Core Web Vitals, security, metadata, structured data, analytics, monitoring, deployment, progressive enhancement, mobile behavior, crawlability, indexability, and code quality. Use before launch, after a major release, when reviewing Lighthouse/PageSpeed/Search Console/Bing findings, when comparing a live deployment with a repository revision, or when the user requests a production-readiness score and prioritized remediation report.
---

# Post Production

## Purpose

Coordinate a complete evidence-based production-readiness audit and hardening
pass. Audit the real repository and intended environment. Delegate domain
reasoning to the owning skills and preserve the provenance of their decisions.

Post Production owns scope, deployment truth, coverage, sequencing, conflict
handling, aggregate prioritization, readiness calculation, verification
coordination, and the consolidated report. It does not replace specialists.

## Specialist routing

- `$design-toolkit`: accessibility, responsive and mobile behavior, progressive
  enhancement, forms, browser behavior, and frontend performance.
- `$visibility`: SEO, AI discoverability, crawlability, indexing, metadata,
  structured data, analytics, search platforms, local visibility, and social
  previews.
- `$security`: secrets, APIs, headers, CSP, cookies, dependencies, rate
  limiting, data access, infrastructure, and launch security.
- `$session-security`: timeout and restoration behavior when authenticated
  sessions exist.
- `$legal-business`: legal documents, privacy disclosures, contractual
  commitments, and counsel or owner approvals.
- `$incident-response`: monitoring, logs, alerts, uptime, health, status,
  rollback, backups, restores, runbooks, recovery, and email health.
- `$support-triage`: user-reported failures and support-context handoffs.

Read [audit-matrix.md](references/audit-matrix.md) for the complete checklist.
Read [orchestration.md](references/orchestration.md) for Shared Context,
provenance, scoring, conflict, and reporting rules.

## Workflow

1. Validate Shared Context or create an in-memory envelope. Record the request,
   project instructions, worktree, stack, routes, services, data, auth, payments,
   forms, analytics, hosting, environments, deployment configuration, current
   branch, revision, and unknowns.
2. Establish deployment truth. A commit, push, build, preview, production
   deployment, and live verified response are separate states. Compare build
   identifiers, asset hashes, release metadata, or distinctive markup where
   possible.
3. Produce the baseline before changes. Inventory existing capabilities and
   classify every relevant control as Completed, Partial, Not Started, N/A, or
   Unverified with evidence and owner.
4. Create a specialist execution plan. Route each control to one owner, define
   inputs, dependencies, safe sequencing, validation environment, and handoff.
   Do not copy specialist guidance into the coordinator.
5. Run proportionate project commands and specialist audits. Preserve each
   result's skill ID, version, timestamp, environment, evidence, limitations,
   decisions, risks, and checks not run.
6. Resolve cross-domain conflicts explicitly. Return disputed decisions to their
   owner and record the selected resolution, alternatives, rejection reasons,
   risks, trade-offs, and uncertainty.
7. Apply only authorized fixes. Prefer existing and framework-native patterns;
   keep changes small, reversible, and tied to evidence.
8. Re-run affected checks and the production build. Validate preview before
   production where available and verify live behavior separately after
   deployment.
9. Calculate readiness only from explicit relevant checks. Publish the formula,
   denominator, weights, evidence gaps, and limitations; otherwise report
   `Not enough evidence`. Never invent a score or optimize solely for 100.
10. Deliver the consolidated report: executive outcome, three largest risks,
    category results, severity-ranked findings, changes, verification, owner
    actions, checks run, checks not run, final matrix, handoffs, and a concise
    commit message when project files changed.

## Decision and reporting contract

Validate coordination decisions against
`schemas/post-production-decision.json`. Every result must preserve specialist
provenance. Use the common report and Shared Context schemas for run output.

## Guardrails

- Do not fabricate rankings, indexing, schema facts, provider settings, field
  metrics, production deployment, security controls, legal approval, recovery,
  alerting, or customer resolution.
- Do not add a provider, tracker, cookie, schema type, paid service, or dependency
  without confirming configuration, ownership, cost, and privacy impact.
- Do not run intrusive scans, load tests, destructive recovery, or production
  fault injection without explicit authorization and safe bounds.
- Preserve unrelated work and user data. Record the worktree before editing.
- Keep preview and staging URLs out of public indexing.
