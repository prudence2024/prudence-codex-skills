---
name: legal-business
description: Prepare, adapt, or audit pre-launch legal and business protection documents for SaaS products and client applications. Use when Codex needs Terms of Service, a data-accurate Privacy Policy, B2B Data Processing Agreement, Refund Policy, Master Service Agreement with service levels, or a cyber-liability insurance readiness checklist, especially for Nigeria-based or cross-border operations involving NDPA/NDPR, GDPR, clients, subscriptions, or personal data.
---

# Legal & Business Protection

## Purpose and boundaries

Prepare evidence-grounded drafts and issue-spotting reports, not final legal
advice. Require qualified counsel before publication, signature, filing, or
reliance, especially for Nigeria-based, cross-border, regulated, consumer, or
sector-specific matters.

- Legal Business owns document selection, drafting, clause consistency, legal
  and business issue spotting, review markers, and approval readiness.
- `$security` supplies verified security, data, vendor, backup, access, and
  control facts; Legal Business does not certify controls.
- `$incident-response` supplies verified response, notification, recovery, and
  service-level capability; Legal Business does not design incident operations.
- `$support-triage` supplies support and escalation capabilities; Legal Business
  does not operate support queues.
- Design Toolkit and Visibility own interface and discoverability decisions.

## References

- Read [document-templates.md](references/document-templates.md) for the Terms,
  Privacy Policy, DPA, Refund Policy, MSA/SLA, and cyber-insurance starting
  structures.
- Read [legal-reasoning.md](references/legal-reasoning.md) for fact provenance,
  consistency, Shared Context, approval, reporting, and handoff rules.

## Workflow

1. Validate Shared Context or create an in-memory envelope. Establish the legal
   entity, product, customers, pricing, refunds, support, jurisdictions, data
   flows, vendors, hosting, transfers, retention, deletion, cookies, telemetry,
   security, incidents, continuity, and insurance facts.
2. Classify every material statement as verified fact, owner decision,
   assumption, unresolved question, or counsel-dependent conclusion. Never
   invent registrations, addresses, contacts, filings, certifications, coverage,
   regulators, lawful bases, transfer safeguards, or operational capabilities.
3. Consume applicable outputs from Security, Incident Response, Support Triage,
   and project owners. Record stale or conflicting evidence.
4. Select only the required documents and audiences. Keep consumer terms
   separate from negotiated B2B agreements where obligations differ.
5. Compare credible clause and document approaches. Explain selection,
   alternatives, rejection reasons, operational consequences, risks,
   trade-offs, and uncertainty.
6. Draft in plain, precise language. Replace bracketed fields or leave an
   explicit action marker; delete inapplicable alternatives.
7. Cross-check entity names, definitions, dates, governing law, parties, data
   roles, subprocessors, transfers, retention, refunds, fees, service levels,
   security commitments, incident notices, liability, and contacts across the
   entire set.
8. Mark uncertain, jurisdiction-dependent, liability, indemnity, dispute,
   transfer, consumer-right, and regulatory language
   `[LAWYER REVIEW REQUIRED]`.
9. Produce a consistency and approval report. Require business-owner approval
   and qualified legal review before documents go live or are signed.
10. Version and date approved publications; retain prior versions and acceptance
    evidence when required. Update Shared Context and hand off unresolved work.

## Required launch set

- Terms of Service
- Privacy Policy
- Data Processing Agreement for B2B customers
- Refund Policy
- Master Service Agreement and service-level schedule
- Cyber-liability insurance readiness checklist

## Decision and report contract

Validate structured decisions against `schemas/legal-business-decision.json`.
For each document record purpose, audience, facts used, unresolved fields,
selected approach, alternatives, review markers, consistency results, owner
actions, risks, trade-offs, uncertainties, approvals, and handoffs. Use the
common report and Shared Context schemas for run output.

## Guardrails

- Do not guarantee GDPR, UK GDPR, Nigeria Data Protection Act/NDPR, consumer,
  tax, employment, sectoral, cross-border, or other compliance from templates.
- Do not promise uptime, response times, refunds, indemnities, recovery,
  notification, insurance, or security controls the business cannot evidence.
- Do not remove counsel-review markers without qualified legal approval.
- Do not publish, sign, file, accept, or send documents externally unless the
  user explicitly authorizes that action.
