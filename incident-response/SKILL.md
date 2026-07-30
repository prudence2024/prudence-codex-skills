---
name: incident-response
description: Establish, implement, or audit production observability, incident handling, recovery, public status communication, scheduled-maintenance notices, and email-delivery health across software projects. Use when Codex needs error tracking, structured logs, severity-based alerts, uptime and health checks, independent status pages, subscriber and in-app incident notices, SPF/DKIM/DMARC guidance, deliverability monitoring, recovery runbooks or drills, incident ownership, automatic 48-hour post-mortem scheduling, blameless reviews, remediation tracking, or recurring-failure detection.
---

# Incident Response

## Purpose and boundaries

Establish or operate an evidence-backed lifecycle for detection, triage,
mitigation, recovery, communication, review, and organizational learning. Reuse
the project's monitoring, storage, jobs, and notification capabilities where
practical.

- Incident Response owns observability readiness, severity and command,
  timelines, mitigation and recovery coordination, public status and maintenance
  communication, transactional-email health, reviews, remediation tracking, and
  recurring-pattern learning.
- `$security` owns preventive security controls and vulnerability assessment.
  Consume its facts; return active threats and control gaps for follow-up.
- `$support-triage` owns ticket classification and customer-support routing.
  Consume impact reports and supply approved incident status.
- `$legal-business` owns legal notification requirements and contractual
  interpretation. Provide verified facts without making legal conclusions.
- `$visibility` owns public search behavior; `$design-toolkit` owns status and
  banner interface design.

## Reference routing

- Read [observability-recovery.md](references/observability-recovery.md) for
  detection, alerts, health, recovery objectives, runbooks, and drills.
- Read [communications-deliverability.md](references/communications-deliverability.md)
  for status pages, maintenance, subscriber safeguards, DNS/email health, and
  communication templates.
- Read [incident-system.md](references/incident-system.md) for records, the
  five-field review, 48-hour automation, and prior-incident matching.
- Read [incident-reasoning.md](references/incident-reasoning.md) for lifecycle,
  Shared Context, evidence, reporting, and handoff rules.

## Workflow

1. Validate Shared Context or create an in-memory envelope. Inventory services,
   critical workflows, owners, monitoring, logs, alerts, health checks, status
   channels, backups, rollback, runbooks, jobs, subscribers, email delivery, and
   legal or contractual constraints.
2. For readiness work, trace detection through ownership, mitigation,
   communication, recovery, verification, review, and prevention. Configuration
   alone is not exercised evidence.
3. For an active incident, establish an incident lead, severity, affected
   services, confirmed impact, next update time, and append-only UTC timeline.
   Separate facts, hypotheses, decisions, and follow-up.
4. Restore service first using bounded mitigation, rollback, failover, or restore
   actions. Do not let paperwork block mitigation.
5. Communicate confirmed impact, current action, and next update time at the
   severity cadence. Avoid speculation, blame, sensitive detail, and unverified
   recovery promises.
6. Verify critical workflows and monitoring before resolving. Distinguish
   mitigated, monitoring, resolved, review pending, and closed.
7. On incident creation, calculate `review_due_at` no later than 48 hours after
   logging and enqueue one idempotent reminder/escalation sequence.
8. Complete the five-field blameless review. Identify technical and process
   causes, not a person as root cause.
9. Assign accepted prevention actions to owners, priorities, due dates,
   verification methods, and statuses. Do not close while accepted critical
   actions are untracked.
10. Store completed reviews in a searchable knowledge base. Surface prior matches
    with reasons and require human confirmation.
11. Validate alert, retry, scheduling, status, communication, deliverability,
    recovery, review, access-control, and matching paths with safe drills.
12. Record decisions and evidence, update Shared Context, report, and hand off
    security, support, legal, design, visibility, or owner work.

## Decision and report contract

For every material incident or readiness decision, record the selected approach,
alternatives, rejection reasons, severity, facts, hypotheses, timeline, impact,
communication, recovery evidence, review state, actions, risks, trade-offs,
uncertainties, context changes, and handoffs.

Validate structured decisions against
`schemas/incident-response-decision.json`. Use the common report and Shared
Context schemas for run output.

## Guardrails

- Keep timeline events and review revisions append-only.
- Restrict incident detail by role; redact secrets, credentials, customer
  payloads, and unnecessary personal data.
- Make scheduling, reminders, maintenance actions, webhooks, and notifications
  idempotent.
- Store timestamps in UTC and display an appropriate local timezone.
- Keep the public status path outside the main application's failure domain.
- Never invent DNS, provider, delivery, backup, restore, monitoring, or dashboard
  evidence.
- Treat prior-incident similarity as a lead, not proof.
