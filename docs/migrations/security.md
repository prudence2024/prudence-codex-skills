# Security migration report

## Summary

- **Date:** 2026-07-30
- **Status:** completed
- **Skill contract:** `security` 1.0.0, stable
- **Backward compatibility:** original ID, trigger description, directory,
  reference paths, agent identity, and standalone operation are preserved.

## Outcome

Security now has a Universal Skill Standard manifest, Shared Context contract,
registered interfaces, structured security-decision schema, standardized
reporting, validation fixture, tests, and advisory extension points.

It retains ownership of application, API, data, infrastructure, supply-chain,
resilience, backup, cost-abuse, and security-observability controls. It delegates
timeout behavior to Session Security, incident operations to Incident Response,
legal interpretation to Legal Business, interface design to Design Toolkit, and
search strategy to Visibility.

## Decisions and trade-offs

- Existing detailed references remain unchanged to preserve guidance and links.
- Specialist skills are optional dependencies, preserving standalone operation
  while requiring explicit handoffs at ownership boundaries.
- Evidence states distinguish implemented, built, deployed, exercised, and
  monitored controls. This reduces overclaiming but leaves provider-only controls
  unverified without authorized access.
- Active testing requires explicit authorization and bounded targets.

## Validation

- Upstream quick validation: `pass`
- Strict Security validation: `pass`
- Security decision schema fixture: `pass`
- Trigger identity, ownership boundary, registry, and link tests: `pass`
- Full repository suite after migration: **40 passed**
- Legacy Security references changed: zero
- `.system` changes: zero

## Files changed

- `security/SKILL.md`
- `security/skill.yaml`
- `security/agents/openai.yaml`
- `security/references/security-reasoning.md`
- `security/schemas/security-decision.json`
- `ecosystem/registry/skills.json`
- `tests/fixtures/security-decision.yaml`
- `tests/test_security_migration.py`
- `docs/migrations/security.md`

## Checks not run

- Active penetration testing
- Production provider configuration review
- Live secret, alert, backup, restore, or disaster-recovery exercises
- Runtime authorization and tenant-isolation tests against a supplied application

## Handoff

Next migration: Session Security.
