---
name: incident-response
description: Establish, implement, or audit production observability, incident handling, recovery, public status communication, scheduled-maintenance notices, and email-delivery health across software projects. Use when Codex needs error tracking, structured logs, severity-based alerts, uptime and health checks, independent status pages, subscriber and in-app incident notices, SPF/DKIM/DMARC guidance, deliverability monitoring, recovery runbooks or drills, incident ownership, automatic 48-hour post-mortem scheduling, blameless reviews, remediation tracking, or recurring-failure detection.
---

# Incident Response

Build detection and response before the first production incident. Adapt storage and automation to the project's existing stack; do not add a new service when the current monitoring, database, job runner, or notification system can support it.

## Workflow

1. Inventory monitoring, error tracking, logs, alerting, ownership, backups, rollback paths, jobs, and notification channels.
2. For pre-incident readiness or recovery work, apply [references/observability-recovery.md](references/observability-recovery.md) and validate the detection-to-recovery path.
3. For public status pages, planned-maintenance communication, subscriber notices, or email-delivery health, apply [references/communications-deliverability.md](references/communications-deliverability.md).
4. Define an incident record with severity, status, service, timestamps, impact, responders, root-cause category, failure-pattern tags, remediation items, and review deadline.
5. On incident creation, set `review_due_at` no later than 48 hours after logging and enqueue an idempotent reminder/escalation job.
6. Preserve a factual event timeline during response. Separate confirmed facts, hypotheses, decisions, and follow-up work.
7. Restore service first; never let post-mortem paperwork block mitigation.
8. Complete the five-field post-mortem from [references/incident-system.md](references/incident-system.md).
9. Frame analysis around "what process allowed this to reach production?" Never assign personal blame.
10. Store completed reviews in a searchable knowledge base indexed by root-cause category, failure-pattern tags, affected service, and date.
11. When a new incident is logged, search prior completed reviews and surface likely matches with links and match reasons. Treat similarity as a lead, not proof.
12. Track prevention actions to named owners and due dates; an incident is not fully closed while accepted critical actions are untracked.

## Guardrails

- Keep audit history append-only for timeline events and review revisions.
- Restrict sensitive incident data by role and redact secrets, credentials, customer payloads, and unnecessary personal data.
- Make scheduling and reminders idempotent so retries cannot create duplicate reviews or notifications.
- Record timestamps in UTC and display the user's local timezone.
- Test creation, 48-hour scheduling, reminder retry, review completion, search, access control, and prior-pattern matching.
- Test alerts, backups, restores, rollback, and runbooks with safe drills; configuration alone is not proof of recovery.
- Keep the public status path outside the main application's provider failure domain.
- Never invent DNS records, selectors, verification values, or dashboard evidence. Use exact values supplied by the DNS and email providers and distinguish prepared integration from verified production delivery.
