---
name: support-triage
description: Classify and route customer support tickets, form failures, booking or payment issues, complaints, bug reports, and sensitive escalations. Use when Codex needs to resolve a known support issue automatically, gather an assisted-triage context package, identify human-required legal/privacy/security or policy cases, or produce a structured support handoff.
---

# Support Triage

## Purpose and boundaries

Classify each support issue on arrival, resolve only known and authorized paths,
and deliver complete context to the correct owner. Use the highest-risk
applicable tier.

- Support Triage owns intake classification, safe known-path resolution,
  context gathering, customer acknowledgements, routing, handoff quality, and
  support closure criteria.
- `$incident-response` owns active service incidents, public status, recovery,
  and incident communication. Consume approved customer-safe status.
- `$security` owns security and privacy investigation or remediation.
- `$legal-business` owns refunds, legal conclusions, policy exceptions, and
  business commitments requiring judgment.
- Product, engineering, billing, and account owners retain decisions that exceed
  the supplied automation authority.

## Classification tiers

### `automated_resolution`

Use only when evidence matches a known, current, authorized, deterministic
resolution path and no higher-risk criterion applies. Perform or explain the
resolution, log the action, verify the outcome when possible, and close only
when resolved or the next customer action is clear.

### `assisted_triage`

Use for incomplete, unknown, ambiguous, or mixed issues. Gather only necessary
context, ask concise blocking questions, inspect authorized evidence, record
what was checked and ruled out, and hand off a package that the receiving owner
can act on without reconstructing the conversation.

### `human_required`

Use immediately for billing disputes, refunds, chargebacks, duplicate charges,
policy exceptions, emotional escalation, threats, harassment, distress, legal,
privacy, abuse, safety, security, account ownership, identity verification
beyond approved flows, or any request requiring human judgment.

If tiers conflict, select the highest risk. If safe automation cannot be
established, use assisted triage.

## Workflow

1. Validate Shared Context or create an in-memory envelope. Record the ticket,
   channel, customer-visible facts, environment, relevant identifiers, prior
   contact, known issues, current incidents, authorization limits, and
   uncertainty.
2. Minimize and redact evidence. Do not include secrets, full payment data,
   authentication tokens, unnecessary personal data, or private logs in
   customer responses or broadly accessible handoffs.
3. Identify customer impact, urgency, safety, security, privacy, legal, billing,
   policy, operational, and emotional-escalation signals.
4. Compare the evidence with maintained known-resolution paths and current
   Incident Response status. Verify version, preconditions, authorization,
   reversibility, and expected outcome.
5. Select the tier and explain why. Record credible alternative tiers, why they
   were rejected, risks, trade-offs, and uncertainty.
6. For automated resolution, perform only authorized actions, validate the
   outcome, log the exact action, and state rollback or failure handling.
7. For assisted or human-required work, assemble the escalation context package:
   summary, request, timeline, identifiers, environment, evidence, attempted
   fixes, ruled-out causes, uncertainty, impact, urgency, risk, recommended next
   action, and named owner when known.
8. Send a calm, specific acknowledgement. Do not expose internal details, assign
   blame, or promise refunds, compensation, timelines, policy exceptions, legal
   outcomes, or incident resolution without authority.
9. Update Shared Context with attributable support facts and handoffs. Record
   customer response, owner acceptance, follow-up state, and closure evidence.

## Decision and reporting contract

Validate structured decisions against
`schemas/support-triage-decision.json`. Every report includes classification,
rationale, impact, evidence, context gathered, action, authorization, customer
communication, next owner, next step, risks, uncertainty, checks not run, Shared
Context changes, and handoffs.

## Guardrails

- Never automate a destructive, money-moving, identity-changing, policy-changing,
  or security-sensitive action unless a current approved path explicitly permits
  it and required confirmation succeeds.
- Do not treat a known incident as the cause without matching evidence.
- Do not close on message delivery alone; distinguish sent, received, accepted,
  resolved, and verified states.
- Preserve the complete relevant interaction history for human escalation while
  applying access controls and data minimization.
