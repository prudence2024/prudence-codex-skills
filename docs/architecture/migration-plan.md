# Migration plan

## Principles

- Preserve existing behavior wherever practical.
- Migrate first-party skills incrementally.
- Complete, validate, document, and review one skill before starting the next.
- Keep `.system` unchanged.
- Separate architecture, foundation implementation, skill migration, design
  ingestion, and learning automation into approval-gated phases.
- Keep every commit in a working state.

## Phase 3 — Ecosystem foundation

Implement schemas, configuration, first-party manifest validation, registry
discovery, shared-context validation, report generation, a developer CLI, and
tests using fixtures before migrating live skills.

Exit criteria:

- deterministic offline validation passes;
- `.system` is discovered read-only;
- invalid manifests, dependencies, and context writes are rejected;
- a sample run produces a conforming report;
- design knowledge supports structured domain and quality queries.

Status: completed and verified before first-party migration.

## Phase 4 — First-party migration

Add `skill.yaml`, Shared Context integration, structured validation, reporting,
and migration documentation to one skill at a time in this approved order:

1. `design-toolkit`;
2. `visibility`;
3. `security`;
4. `session-security`;
5. `legal-business`;
6. `incident-response`;
7. `support-triage`;
8. `post-production`.

Validate trigger compatibility, dependency boundaries, context declarations,
reports, registry freshness, and the full repository test suite after every
skill. Stop for approval before continuing to the next skill.

Migrate `post-production` last so its coordinator contract depends on fully
migrated specialist skills.

## Phase 5 — Design intelligence

Create domain schemas, secure archive inspection, tracked source manifests,
observation extraction, independence grouping, confidence calculation, domain
record generation, search, and recommendation reports. Calibrate thresholds on
a reviewed sample before importing a large corpus.

Keep Design Toolkit responsible for final design reasoning. Keep Design
Intelligence responsible for website ingestion, pattern extraction,
normalization, evidence, scoring, and knowledge storage.

## Phase 6 — Skill learning

Implement approved-source configuration, provenance snapshots, comparison,
recommendation records, review states, and stale-guidance detection. Keep skill
edits outside the learning runner.

## Phase 7 — Integration

Test skill communication, context conflicts, report consistency, registry
integrity, migration compatibility, design-confidence calibration, learning
provenance, and documentation. Forward-test first-party skills only after the
test plan and prompts are approved when required.

