# Legal Business migration report

## Summary

- **Date:** 2026-07-30
- **Status:** completed
- **Skill contract:** `legal-business` 1.0.0, stable
- **Backward compatibility:** original ID, trigger, directory, reference,
  agent identity, and standalone drafting behavior are preserved.

## Outcome

Legal Business now has the Universal Skill Standard, Shared Context, registry,
decision schema, standardized reporting, validation, tests, and extension
points. It preserves the Terms, Privacy Policy, DPA, Refund Policy, MSA/SLA, and
cyber-insurance readiness set.

The migration formalizes fact provenance, cross-document consistency,
jurisdiction uncertainty, lawyer-review markers, owner approval, publication
authorization, version states, and specialist evidence handoffs.

## Boundaries and trade-offs

- Security, Incident Response, and Support Triage supply verified operational
  facts; they do not become legal conclusions or promises automatically.
- Existing templates remain unchanged.
- Optional collaborators preserve standalone drafting but require unresolved
  facts to remain explicit.
- External publication, signature, filing, or acceptance remains authorization
  gated.

## Validation

- Upstream quick validation: `pass`
- Strict Legal Business validation: `pass`
- Decision fixture and migration tests: `pass`
- Full repository suite after migration: **52 passed**
- Legacy template changes: zero
- `.system` changes: zero

## Files changed

- `legal-business/SKILL.md`
- `legal-business/skill.yaml`
- `legal-business/agents/openai.yaml`
- `legal-business/references/legal-reasoning.md`
- `legal-business/schemas/legal-business-decision.json`
- `ecosystem/registry/skills.json`
- `tests/fixtures/legal-business-decision.yaml`
- `tests/test_legal_business_migration.py`
- `docs/migrations/legal-business.md`

## Checks not run

- Qualified legal review
- Jurisdiction-specific legal research
- External publication or signature
- Live product, vendor, regulator, insurer, or acceptance-evidence verification

## Handoff

Next migration: Incident Response.
