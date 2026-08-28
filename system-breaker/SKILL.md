---
name: system-breaker
description: Primary adversarial engineering methodology for owned or authorized systems. Use when Codex needs to question assumptions, break safely, verify, fix, retest, harden, or produce evidence-backed engineering validation.
---

# System Breaker

The permanent engineering question is: **PROVE IT.**

Use this skill to test a feature, fix, workflow, deployment, or system component by trying to disprove its assumptions safely. It applies only to systems the user owns or is explicitly authorized to test.

## Core Method

Use this loop:

1. **UNDERSTAND** - Read architecture, requirements, current behavior, constraints, and ownership boundaries.
2. **PLAN** - Identify what changes, what must not change, and which tests are safe to run.
3. **BUILD OR INSPECT** - Implement the smallest robust fix or inspect the current implementation.
4. **IDENTIFY ASSUMPTIONS** - Name each belief the system relies on.
5. **BREAK SAFELY** - Test invalid input, auth/RBAC, IDOR, frontend states, accessibility, API failures, rate limits, webhooks, inventory, concurrency, network, database, third-party, observability, configuration, and state-machine failures where applicable.
6. **OBSERVE** - Capture evidence from runtime behavior, tests, database state, provider test mode, logs, or code inspection.
7. **REPRODUCE AND ROOT CAUSE** - Confirm real failures and explain why they happen.
8. **FIX, RETEST, HARDEN** - Apply targeted fixes, retest the original failure, and add regression guards where practical.
9. **DOCUMENT** - Report evidence, limitations, blocked tests, owner actions, and residual risk.

Do not start from the assumption that the system is correct. Start from: "There is probably an edge case we have not tested yet."

## Reference Routing

Read [references/attack-playbook.md](references/attack-playbook.md) when the request involves a meaningful audit, security/integrity testing, checkout/payment/admin/CMS behavior, concurrency, availability, performance, discoverability, or any claim that something is "done", "fixed", "safe", or "production ready".

For narrower specialist work, hand off or combine with the owning skill:

- `$security` for general security controls, secrets, auth architecture, API hardening, uploads, headers, dependencies, infrastructure, and backups.
- `$session-security` for idle/absolute expiry, timeout warning UX, cross-tab coordination, and reauthentication restoration.
- `$ecommerce-engineering` for commerce state machines, price authority, inventory, orders, coupons, refunds, receipts, and payment integrity.
- `$incident-response` for monitoring, alerts, recovery, status communication, and post-mortems.
- `$visibility` for SEO, crawlability, sitemaps, metadata, and indexing evidence.

## Evidence Rules

A PASS must state the evidence level:

- `RUNTIME VERIFIED`
- `AUTOMATED TEST VERIFIED`
- `DATABASE VERIFIED`
- `DEPLOYMENT VERIFIED`
- `PROVIDER TEST MODE`
- `CLEAN COMMITTED BUILD`
- `OWNER RUNTIME CONFIRMATION`
- `CODE INSPECTION ONLY`
- `BLOCKED`

Never present `CODE INSPECTION ONLY` as equivalent to runtime proof.

What is not enough by itself:

- Code compiles.
- A build passed once.
- A page rendered.
- An API returned 200.
- A happy path worked once.
- A route, file, column, schema, or security control appears in code.
- A previous report or AI message says it was fixed.

## Assumption Table

Every significant fix or audit should produce an assumption table:

```text
ASSUMPTION:       [what we believe]
HOW TO BREAK IT:  [action that tests it]
EXPECTED:         [safe behavior if wrong]
TEST:             [what was done]
EVIDENCE:         [what was observed]
RESULT:           [PASS / FAIL / NOT TESTED]
```

## Safety Boundary

System Breaker performs adversarial quality and security testing, not destructive hacking. Stop and request owner approval before any test or fix that could delete/corrupt production data, send real payments/refunds, rotate credentials, expose secrets, generate abusive traffic, spam users, attack unrelated systems, or change legal/business policy.

Prefer dry-run, test mode, staging, mocks, controlled fixtures, read-only inspection, and bounded local tests.

## Reporting

Lead with confirmed blockers and high-risk findings. For each finding include: ID, severity, area, assumption, attack, expected result, actual result, evidence, reproduction, root cause, fix, regression test, and verification status.

Final status should be one of: `PASS`, `CONDITIONAL PASS`, or `FAIL`. A conditional pass must name exactly what remains untested or owner-blocked.

