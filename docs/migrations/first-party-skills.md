# Consolidated first-party skill migration report

## Summary

- **Date:** 2026-07-30
- **Status:** completed
- **Scope:** all eight first-party skills
- **Registry:** eight stable first-party skills at version `1.0.0`
- **Upstream compatibility:** six `.system` skills remain read-only and unchanged
- **Repository validation:** pass, 18 checks, zero partials, zero failures
- **Full test suite:** 70 passed
- **Next gate:** approval required before Design Intelligence Framework work

## Migrated skills

| Skill | Primary ownership | Structured output |
| --- | --- | --- |
| Design Toolkit | Product and frontend design reasoning | `design-decision.json` |
| Visibility | SEO, discoverability, indexing, metadata, schema, social previews, crawlability, and search performance | `visibility-decision.json` |
| Security | Application, API, data, infrastructure, supply-chain, backup, and launch security | `security-decision.json` |
| Session Security | Timeout, activity, warning, extension, coordination, reauthentication, and restoration | `session-security-decision.json` |
| Legal Business | Legal and business drafts, fact provenance, consistency, review, and approval readiness | `legal-business-decision.json` |
| Incident Response | Observability, incident command, recovery, communication, review, remediation, and learning | `incident-response-decision.json` |
| Support Triage | Risk-first support classification, known-path resolution, context, routing, and closure | `support-triage-decision.json` |
| Post Production | Specialist orchestration, deployment truth, coverage, priority, readiness, and consolidated reporting | `post-production-decision.json` |

## Common architecture delivered

Every first-party skill now provides:

- preserved `SKILL.md` identity and trigger compatibility;
- a versioned `skill.yaml` Universal Skill Standard manifest;
- explicit included and excluded scope;
- declared inputs, outputs, dependencies, configuration, processing, reasoning,
  validation, reporting, and extension points;
- Shared Context reads and attributable writes;
- a skill-owned structured decision schema;
- alternatives, rejection reasons, risks, trade-offs, and uncertainty;
- standardized evidence and reporting behavior;
- registry integration;
- a valid `agents/openai.yaml`;
- schema fixtures, migration tests, and local-link validation;
- a per-skill migration report.

No first-party skill has a required dependency. Optional dependencies preserve
standalone operation while enabling provenance-preserving collaboration.

## Responsibility boundaries

### Design and visibility

Design Toolkit remains the primary design reasoning skill. Visibility consumes
applicable design decisions and owns only search-facing discoverability and
evidence. Design Intelligence ingestion, extraction, normalization, scoring,
and storage remain outside both skills.

### Security and sessions

Security owns authentication architecture, threats, authorization, data, APIs,
infrastructure, dependencies, resilience, and security evidence. Session
Security consumes those constraints and owns timeout state, meaningful activity,
warning UX requirements, cross-instance coordination, and restoration.

### Legal, incidents, and support

Legal Business consumes verified operational facts but retains legal drafting,
consistency, counsel markers, and approval readiness. Incident Response owns the
operational incident lifecycle. Support Triage owns customer intake,
classification, safe known-path resolution, and specialist routing.

### Coordination

Post Production coordinates all seven specialists. It preserves skill identity,
version, decision ID, environment, evidence, limitations, risks, and checks not
run. It does not rewrite specialist conclusions or duplicate domain reasoning.

## Backward compatibility

- Original skill IDs and directory names are unchanged.
- Original frontmatter descriptions are unchanged and covered by exact identity
  tests.
- Existing user-facing display names and short descriptions are preserved.
- Legacy reference paths remain available.
- Legacy references for Security, Session Security, Legal Business, Incident
  Response, Support Triage, and Post Production were not rewritten.
- Design Toolkit and Visibility compatibility decisions remain documented in
  their individual reports.
- Required dependencies remain empty, allowing skills to run without a
  persisted Shared Context or every optional collaborator.

## Registry

The regenerated registry contains:

- eight first-party entries, all stable at `1.0.0`;
- six upstream `.system` entries, all read-only;
- full purpose, scope, responsibility, interface, dependency, context,
  validation, reporting, and extension metadata;
- no missing first-party manifests;
- a current registry checksum and schema-valid artifact.

## Validation results

- Upstream `skill-creator` quick validation: pass for each migrated skill
- Strict repository validation: **pass**
- Repository checks: **18**
- Failed checks: **0**
- Partial checks: **0**
- Infrastructure schema and configuration validation: pass
- Shared Context and report schema validation: pass
- Design Knowledge schema validation: pass, zero production patterns
- Source-manifest validation: pass, zero production source manifests
- Registry freshness: pass
- Full pytest suite: **70 passed**
- Legacy reference diffs for the six migrations in this phase: zero
- `.system` changes: zero
- Diff whitespace errors: zero

## Per-skill phase results

| Phase | Suite after phase | Result |
| --- | ---: | --- |
| Design Toolkit | 27 passed | Complete |
| Visibility | 34 passed | Complete |
| Security | 40 passed | Complete |
| Session Security | 46 passed | Complete |
| Legal Business | 52 passed | Complete |
| Incident Response | 58 passed | Complete |
| Support Triage | 64 passed | Complete |
| Post Production | 70 passed | Complete |

## Migration documentation

- `docs/migrations/design-toolkit.md`
- `docs/migrations/visibility.md`
- `docs/migrations/security.md`
- `docs/migrations/session-security.md`
- `docs/migrations/legal-business.md`
- `docs/migrations/incident-response.md`
- `docs/migrations/support-triage.md`
- `docs/migrations/post-production.md`

## Risks and checks not run

- No representative live product was supplied for cross-skill forward testing.
- Provider dashboards, production deployments, field metrics, external
  deliveries, legal approvals, support systems, and incident tooling were not
  accessed.
- Active security tests, production load tests, fault injection, live incident
  operations, external publication, and destructive recovery exercises were not
  authorized or run.
- The production Design Knowledge Base and curated source-manifest collection
  remain empty. Their schemas and query infrastructure validate, but their
  scoring behavior has not been calibrated on a reviewed corpus.
- Optional specialist collaboration is contract-tested through manifests and
  fixtures, not yet exercised end to end on one live application.

## Recommendations

- Forward-test the full skill chain on one representative repository plus a
  non-production deployment.
- Preserve the decision schemas as versioned contracts; introduce compatibility
  migrations before breaking changes.
- Add provider adapters only through declared extension points with provenance,
  authorization, redaction, and evidence-state requirements.
- Keep `.system` skills as upstream read-only compatibility layers.
- Begin the Design Intelligence Framework only after explicit approval and keep
  its ingestion, evidence, scoring, and storage responsibilities separate from
  Design Toolkit reasoning.

## Handoff

All approved first-party migrations are complete.

Stop here. Human approval is required before beginning the Design Intelligence
Framework.
