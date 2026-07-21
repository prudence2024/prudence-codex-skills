---
name: support-triage
description: Classify and route customer support tickets, form failures, booking or payment issues, complaints, bug reports, and sensitive escalations. Use when Codex needs to resolve a known support issue automatically, gather an assisted-triage context package, identify human-required legal/privacy/security or policy cases, or produce a structured support handoff.
---

# Support Triage Skill

Use this skill on any project with a customer support surface where tickets,
messages, form submissions, emails, chats, or reports need to be classified and
routed.

## Purpose

Classify every support ticket on arrival and route it immediately to the right
resolution path. Do not wait for manual sorting after the fact.

The goal is to resolve known issues automatically, escalate ambiguous issues with
full context, and protect human time for cases that genuinely require human
judgment.

## Three-Tier Classification

### 1. Automated Resolution

Use this tier for known issues the agent can handle end-to-end without human
involvement.

Examples:

- Password reset or account access flows with a known process.
- Form submission errors with a known validation fix or documented workaround.
- Common setup questions already covered by documentation.
- Known service status issues with an approved customer-facing response.
- Re-sending confirmation emails, receipts, or booking details when permitted.
- Simple troubleshooting with deterministic steps.

Requirements:

- Confirm the issue matches a known resolution path.
- Perform the fix or provide the exact resolution steps.
- Log the action taken.
- Close the ticket only when the customer-facing issue is resolved or the next
  customer action is clearly stated.

Do not use automated resolution when the ticket includes billing uncertainty,
emotional escalation, legal/privacy risk, security risk, or a request that
changes product/business policy.

### 2. Assisted Triage

Use this tier for unknown, incomplete, ambiguous, or mixed issues where a human
may need to decide, but the agent can still gather context first.

Examples:

- A bug report without enough reproduction details.
- A customer complaint that may be caused by configuration, user error, or a
  real product issue.
- A request involving multiple systems where ownership is unclear.
- A failed payment, failed email, failed booking, or missing notification where
  logs need to be checked before escalation.
- A support message that is unclear but not emotionally escalated.

Requirements:

- Gather the relevant context before routing.
- Ask concise follow-up questions only if the missing information is required.
- Check available logs, request payloads, timestamps, customer identifiers,
  environment, browser/device details, and recent changes where applicable.
- Summarize what is known, what was checked, what remains unclear, and the
  recommended next action.
- Route to the correct human/team only after the context package is complete.

Assisted triage is not a cold handoff. The receiving human should be able to
understand the issue without re-reading the entire conversation from scratch.

### 3. Human-Required

Use this tier for anything that genuinely needs a person.

Human-required examples:

- Billing disputes where the customer may be right and the system may be wrong.
- Refund decisions, chargebacks, double charges, or price exceptions.
- Feature requests disguised as bug reports.
- Customer requests that require business approval or policy judgment.
- Escalated emotional situations, threats, harassment, distressed customers, or
  repeated frustration.
- Legal, privacy, compliance, abuse, safety, or security-sensitive reports.
- Account ownership disputes or identity verification beyond approved automated
  flows.

Requirements:

- Route immediately to the appropriate human owner.
- Include the complete customer interaction history.
- Include all gathered context, logs, timestamps, screenshots, payloads, account
  identifiers, order/booking identifiers, and previous attempted fixes.
- Clearly mark why the ticket is human-required.
- Do not make promises about refunds, compensation, timelines, legal outcomes,
  or policy exceptions unless explicitly authorized.

## Automatic Routing Rules

Every incoming ticket must be classified at arrival into one of:

- `automated_resolution`
- `assisted_triage`
- `human_required`

Routing should happen before any manual queue sorting.

Use the highest-risk applicable tier. If a ticket fits both automated and
human-required criteria, route it as human-required. If the agent lacks enough
information to safely automate, use assisted triage.

## Escalation Context Package

Any escalation to `assisted_triage` or `human_required` must include:

- Customer name or identifier, if available.
- Contact channel and reply destination.
- Full customer interaction history.
- Ticket summary in 2-5 sentences.
- Exact customer request or complaint.
- Timeline of events with timestamps.
- Relevant account, booking, order, invoice, or submission IDs.
- Browser, device, location, app version, or environment details if relevant.
- Logs, error codes, request URLs, response statuses, and payload summaries.
- Steps already taken by the agent.
- What the agent ruled out.
- Remaining uncertainty.
- Recommended next action.
- Urgency and risk level.

## Customer Communication

Keep responses clear, calm, and specific.

- For automated resolution, tell the customer what was fixed or what to do next.
- For assisted triage, acknowledge the issue and explain that the team is
  reviewing the gathered details.
- For human-required cases, acknowledge the concern without overpromising and
  state that a person will review it.

Avoid blame. Avoid exposing internal logs or sensitive implementation details to
the customer.

## Classification Output Format

When classifying a ticket, produce:

```text
Classification: automated_resolution | assisted_triage | human_required
Reason:
Customer impact:
Context gathered:
Action taken:
Next owner:
Next step:
```

For `automated_resolution`, `Next owner` may be `agent`.

For `assisted_triage` and `human_required`, `Next owner` must name the relevant
team or person if known.
