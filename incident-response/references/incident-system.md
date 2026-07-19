# Incident system reference

## Minimum incident record

```text
id, title, summary, severity, status, affected_services
detected_at, logged_at, mitigated_at, resolved_at, review_due_at, review_completed_at
impact_summary, customer_impact, responders, incident_lead
root_cause_category, failure_pattern_tags
timeline_events, remediation_actions, prevention_actions
prior_incident_matches, created_by, updated_at
```

Recommended statuses: `investigating`, `identified`, `mitigating`, `monitoring`, `resolved`, `review_pending`, `closed`.

## Five-field post-mortem template

### 1. What happened

Describe the event in plain language. Include the UTC timeline from detection through recovery, what changed, how the issue was observed, and which systems were involved. Separate confirmed facts from hypotheses.

### 2. Impact assessment

State affected users, workflows, regions, data, revenue, availability, integrity, confidentiality, duration, and support burden. Write “no known impact” only after documenting how that conclusion was checked.

### 3. Root cause analysis

Identify the technical cause and the process/control gaps that allowed it to reach production or delayed detection. Use evidence. Avoid naming a person as the root cause. Useful categories include deployment, configuration, dependency, capacity, data migration, authorization, validation, observability, third-party, and operational procedure.

### 4. Remediation steps

List what restored service and verified recovery, including rollbacks, feature flags, configuration changes, data repair, or vendor action. Note temporary workarounds explicitly.

### 5. Prevention measures

Create specific, testable actions with owner, priority, due date, verification method, and status. Cover prevention, earlier detection, reduced blast radius, and faster recovery where applicable.

## Automatic 48-hour review rule

- On create: calculate `review_due_at = logged_at + 48 hours`.
- Insert or enqueue one job keyed by `incident_id + review_due_at`.
- Notify the incident lead immediately, at 24 hours remaining, and when overdue.
- Cancel future reminders when `review_completed_at` is set.
- Escalate overdue reviews without auto-closing them.
- Audit every reminder attempt and retry transient failures with backoff.

## Knowledge-base matching

Index structured fields and full post-mortem text. Rank candidates using shared root-cause category, overlapping failure-pattern tags, affected service, and text similarity. Display why each result matched. Require a human to confirm that a prior incident is genuinely related.
