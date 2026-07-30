# Post Production migration report

## Summary

- **Date:** 2026-07-30
- **Status:** completed
- **Skill contract:** `post-production` 1.0.0, stable
- **Backward compatibility:** original ID, trigger, directory, audit matrix,
  agent identity, and standalone coordination behavior are preserved.

## Outcome

Post Production now has the Universal Skill Standard, Shared Context, registry,
coordination decision schema, standardized reporting, validation, tests, and
extension points.

It coordinates Design Toolkit, Visibility, Security, Session Security, Legal
Business, Incident Response, and Support Triage while preserving specialist
identity, version, evidence, environment, limitations, risks, and handoffs.
Post Production owns scope, deployment truth, coverage, sequencing, conflicts,
aggregate priority, readiness calculation, and consolidated reporting.

## Boundaries and trade-offs

- Primary domain reasoning remains with the seven specialist skills.
- Existing audit guidance remains unchanged.
- Single primary ownership and provenance add report structure but prevent
  duplicated or unattributed conclusions.
- Readiness requires a published denominator, formula, environment, and evidence;
  otherwise the result is `Not enough evidence`.

## Validation

- Upstream quick validation: `pass`
- Strict Post Production validation: `pass`
- Decision fixture and migration tests: `pass`
- Full repository suite after migration: **70 passed**
- Legacy audit matrix changes: zero
- `.system` changes: zero

## Files changed

- `post-production/SKILL.md`
- `post-production/skill.yaml`
- `post-production/agents/openai.yaml`
- `post-production/references/orchestration.md`
- `post-production/schemas/post-production-decision.json`
- `ecosystem/registry/skills.json`
- `tests/fixtures/post-production-decision.yaml`
- `tests/test_post_production_migration.py`
- `docs/migrations/post-production.md`

## Checks not run

- Audit of a supplied live product
- Live deployment identity comparison
- Specialist execution against a real application
- Production provider, field metric, owner approval, or external delivery checks

## Handoff

All approved first-party skill migrations are complete. Run consolidated
repository validation and await approval before Design Intelligence work.
