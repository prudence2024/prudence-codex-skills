# Incident Response reasoning and integration

## Lifecycle and evidence

Model readiness, detected, investigating, identified, mitigating, monitoring,
resolved, review pending, and closed states. Require an owner and transition
evidence for each applicable state. Keep configured, delivered, acknowledged,
exercised, recovered, and monitored evidence separate.

During active response, preserve an append-only UTC timeline. Label entries as
confirmed fact, hypothesis, decision, action, result, or follow-up. Corrections
append a new event instead of rewriting history.

## Shared Context

Read services, goals, constraints, decisions, artifacts, risks, uncertainty, and
prior skill runs. Consume Security findings, Support Triage impact reports, Legal
Business notification constraints, and applicable design or visibility
decisions. Write attributable incident facts, decisions, artifacts, risks,
actions, evidence, uncertainties, and handoffs.

Do not place public-sensitive incident payloads or subscriber data in Shared
Context unless the schema, access policy, and task require it.

## Decision quality

Compare mitigation and recovery options against blast radius, reversibility,
data integrity, customer impact, recovery objectives, evidence, communication
needs, cost, and uncertainty. Explain rejected alternatives and safe abort
conditions. A fast reversible containment can precede complete root-cause proof.

## Communications

Public and subscriber updates use confirmed impact, current action, and next
update time. Legal or contractual notification questions go to Legal Business.
Support receives an approved customer-safe status. Security-sensitive detail
stays restricted.

## Extensions

Monitoring, alert, status, notification, delivery, recovery, and knowledge
adapters return provider identity, environment, timestamps, evidence,
limitations, and idempotency identifiers. Incident Response retains severity,
command, communication, review, and closure ownership.
