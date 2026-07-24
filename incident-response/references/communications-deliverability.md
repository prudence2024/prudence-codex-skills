# Incident communications and email deliverability

Use this reference when a project needs an independent status page, planned-maintenance messaging, subscriber communication, or transactional-email delivery monitoring.

## Public status page

- Host the status page on a provider independent from the main application. A subdomain on the same application deployment is not independent.
- Use a dedicated hostname such as `status.example.com`, protect its DNS account with MFA, and monitor it externally.
- Represent only real components. Typical components are web app, API, database, payments, and email. Mark absent services `N/A`; do not report synthetic systems as operational.
- Support `operational`, `degraded_performance`, `partial_outage`, `major_outage`, and `maintenance`.
- Publish an incident title, affected components, severity, status, impact, UTC timestamps, local display time, factual updates, and the next update time.
- Keep subscriber data and private operational detail out of the public incident payload.

## Severity and communication cadence

| Severity | Meaning | Public update cadence |
| --- | --- | --- |
| SEV-1 Critical | Broad outage, data/security risk, or critical workflow unavailable | At least every 30 minutes |
| SEV-2 Degraded | Material partial outage or sustained degradation | At least every 2 hours |
| SEV-3 Minor | Limited impact with workaround | On meaningful change |
| SEV-4 Informational | No current customer impact | At closure or scheduled summary |

Every public update states confirmed impact, current action, and the next update time. Do not speculate, assign blame, expose security detail, or promise an unverified restoration time.

## Scheduled maintenance

For user-impacting planned downtime:

1. Create one maintenance record with a stable idempotency key, affected components, UTC start/end, local timezone display, expected impact, owner, rollback criteria, and cancellation state.
2. At T-24 hours, publish the status-page notice, email eligible active subscribers, and expose an in-app banner.
3. Send any later reminder only when the business has approved it; do not repeatedly email subscribers by default.
4. At start, mark affected components `maintenance` and update the banner.
5. At completion, verify critical workflows, resolve the maintenance event, remove the banner, and send a completion notice only when useful.
6. Make every scheduled action idempotent and audit delivery attempts, retries, cancellation, and operator changes.

The banner must remain readable without animation, include the window and impact, link to the independent status page, and avoid blocking critical navigation.

## Subscriber safeguards

- Define who is an eligible active subscriber and the lawful purpose for service notices.
- Keep operational notices separate from marketing consent and marketing content.
- Provide preference and unsubscribe controls where legally or contractually required.
- Minimize stored data, enforce retention/deletion, restrict access, and document the email/status providers as subprocessors where applicable.

## Transactional email reputation

- Prefer a dedicated transactional sending subdomain such as `notify.example.com`; keep bulk marketing on another subdomain such as `news.example.com`.
- Isolate streams by domain, From address, suppression list, templates, and monitoring. This reduces the chance that marketing complaints or list-quality problems impair password resets, receipts, and incident notices.
- Use one SPF record per hostname. Merge authorized senders rather than publishing multiple SPF TXT records.
- Copy DKIM selectors and values exactly from the sending provider. Never guess selector names or key values.
- Configure DMARC deliberately, beginning with monitored policy when the domain has no established evidence, then tighten after alignment and legitimate senders are verified.
- Verify custom return-path/bounce-domain alignment when supported.
- Publish DNS changes only after identifying the authoritative DNS provider and checking for existing records.

## Delivery monitoring

Combine the sending provider's signed webhooks with an independent inbox-placement seed test:

- Record accepted, delivered, deferred, bounced, complained, opened, and clicked events using the provider event id for idempotency.
- Verify webhook signatures against the raw request body, reject stale/replayed events, redact unnecessary recipient data, and return quickly before asynchronous processing.
- Track delivered/accepted rate, hard and soft bounce rate, spam complaint rate, deferral rate, latency, and suppression growth by sending domain and message category.
- Inbox placement cannot be inferred from a `delivered` event. Measure it with a current independent seed-testing product and label it separately.
- Alert against the current mailbox-provider and sending-provider thresholds; verify those thresholds from primary documentation rather than freezing potentially stale values in code.
- Maintain Gmail Postmaster Tools and equivalent mailbox-provider feedback when volume and eligibility permit.

## Communication templates

### Investigating

`We are investigating [confirmed impact] affecting [components]. The issue began at [time]. Our team is working to identify the cause. Next update by [time].`

### Identified

`We identified [customer-safe cause] affecting [components]. We are [mitigation]. [Workaround, if verified.] Next update by [time].`

### Monitoring

`Service has been restored and we are monitoring [components] for stability. We will confirm resolution after verification. Next update by [time].`

### Resolved

`This incident is resolved. Impact lasted from [start] to [end] and affected [workflows]. We will complete a blameless review and track prevention work.`

## Post-incident report

Include executive summary, customer impact, detection, UTC timeline, technical cause, contributing process/control gaps, mitigation and recovery, communication effectiveness, email-delivery evidence, what worked, what did not, and prevention actions with owner, priority, due date, verification method, and status.