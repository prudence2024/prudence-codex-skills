---
name: incident-response
description: Establish, implement, or audit production observability, incident handling, and recovery across software projects. Use when Codex needs error tracking, structured logs, severity-based alerts, uptime and health checks, recovery runbooks or drills, incident ownership, automatic 48-hour post-mortem scheduling, blameless reviews, remediation tracking, or recurring-failure detection.
---

# Incident Response

Build detection and response before the first production incident. Adapt storage and automation to the project's existing stack; do not add a new service when the current monitoring, database, job runner, or notification system can support it.

## Workflow

1. Inventory monitoring, error tracking, logs, alerting, ownership, backups, rollback paths, jobs, and notification channels.
2. For pre-incident readiness or recovery work, apply [references/observability-recovery.md](references/observability-recovery.md) and validate the detection-to-recovery path.
3. Define an incident record with severity, status, service, timestamps, impact, responders, root-cause category, failure-pattern tags, remediation items, and review deadline.
4. On incident creation, set `review_due_at` no later than 48 hours after logging and enqueue an idempotent reminder/escalation job.
5. Preserve a factual event timeline during response. Separate confirmed facts, hypotheses, decisions, and follow-up work.
6. Restore service first; never let post-mortem paperwork block mitigation.
7. Complete the five-field post-mortem from [references/incident-system.md](references/incident-system.md).
8. Frame analysis around "what process allowed this to reach production?" Never assign personal blame.
9. Store completed reviews in a searchable knowledge base indexed by root-cause category, failure-pattern tags, affected service, and date.
10. When a new incident is logged, search prior completed reviews and surface likely matches with links and match reasons. Treat similarity as a lead, not proof.
11. Track prevention actions to named owners and due dates; an incident is not fully closed while accepted critical actions are untracked.

## Guardrails

- Keep audit history append-only for timeline events and review revisions.
- Restrict sensitive incident data by role and redact secrets, credentials, customer payloads, and unnecessary personal data.
- Make scheduling and reminders idempotent so retries cannot create duplicate reviews or notifications.
- Record timestamps in UTC and display the user's local timezone.
- Test creation, 48-hour scheduling, reminder retry, review completion, search, access control, and prior-pattern matching.
- Test alerts, backups, restores, rollback, and runbooks with safe drills; configuration alone is not proof of recovery.
