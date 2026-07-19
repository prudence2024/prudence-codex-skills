# Observability and recovery reference

Use this reference to prepare for incidents or audit detection and recovery. During an active incident, prioritize mitigation and the factual timeline in `incident-system.md`.

## Error tracking and logs

- Connect a real error-tracking service to client and server failure boundaries. Show users a bounded, useful fallback instead of a blank screen or raw stack trace.
- Publish source maps securely so production reports resolve to readable files and lines without exposing source maps publicly when the platform supports private upload.
- Emit structured, searchable logs with timestamp, severity, service, environment, route/action, request or correlation ID, and a non-sensitive user/account identifier when justified.
- Never record passwords, tokens, payment-card data, raw sensitive payloads, or unnecessary personal data. Configure scrubbing in both application code and the monitoring provider.
- Distinguish client errors, dependency failures, warnings, and critical server failures. Group repeated events so volume does not hide the number of distinct defects.

## Alerts and triage

- Alert on user impact and critical-path symptoms such as sustained availability loss, elevated 5xx rate, failed checkout/auth flows, or breached latency thresholds.
- Route critical alerts to a channel that wakes an owner; route lower-severity warnings to a review queue. Avoid alerting on every individual error.
- Include service, environment, start time, impact signal, dashboard/runbook link, and correlation context in alert payloads.
- Intentionally trigger a safe test error and verify capture, grouping, source resolution, notification delivery, and redaction end to end.

## Uptime and health checks

- Monitor from outside the application platform so a platform outage cannot silence the check.
- Expose a lightweight liveness check and, where appropriate, a separate readiness check for required dependencies such as the database or queue.
- Do not call a service healthy merely because the process responds while critical user workflows are broken.
- Set a detection target for important services and verify the polling interval and alert delay can meet it.

## Backup and recovery objectives

- Define a recovery point objective (maximum tolerable data loss) and recovery time objective (maximum tolerable restoration time) for each critical data store or workflow.
- Match backup frequency to the recovery point objective. Store protected copies outside the primary failure domain, with access control and retention suited to the data.
- Restore a backup into an isolated environment and verify data integrity and application behavior; a completed backup job alone is insufficient.
- Maintain a fast rollback path for bad deployments and record the exact known-good release or artifact.

## Runbook and communication

- Write calm, step-by-step runbooks for common failures: deploy regression, database outage or deletion, expired credential, dependency outage, and traffic overload.
- Include detection, ownership, containment, rollback/restore steps, verification, escalation, and safe abort conditions.
- Maintain a status-page or equivalent user-communication path independent enough to work during the main outage.
- Communicate known impact, current mitigation, and next update time without speculation or promises the evidence cannot support.

## Recovery drill

1. Choose a safe non-production scenario and state the expected detection and recovery times.
2. Trigger or simulate the failure without risking live data.
3. Verify alert delivery, ownership, logs, dashboards, runbook accuracy, rollback or restore, and user-facing status.
4. Record actual detection time, recovery time, data loss, gaps, and follow-up owners.
5. Update the runbook and repeat until the objectives are met.
