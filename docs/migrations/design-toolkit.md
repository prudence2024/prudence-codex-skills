# Design Toolkit migration report

## Summary

- **Date:** 2026-07-30
- **Status:** completed
- **Skill contract:** `design-toolkit` 1.0.0, stable
- **Outcome:** Design Toolkit is the repository's primary design reasoning skill.
- **Backward compatibility:** existing skill ID, trigger description, folder,
  reference paths, display name, and standalone operation are preserved.

## Scope

Migrate Design Toolkit to the Universal Skill Standard, integrate it with Shared
Context, register it, add a structured design-decision contract, align reporting
and validation, and document future reasoning-module extension points.

Do not migrate another first-party skill. Do not modify `.system`.

## Current state and evidence

Before migration, Design Toolkit was a concise sourcing layer with strong
local-first, accessibility, performance, responsive, progressive-enhancement,
and anti-copying guidance. It had no first-party manifest, Shared Context
contract, structured decision output, registry metadata, reasoning extension
contract, or standardized report requirements.

Baseline SHA-256 hashes were recorded for all four existing skill files before
implementation.

## Architectural decisions

### Keep final design reasoning in Design Toolkit

Design Toolkit now synthesizes business objectives, user goals, brand identity,
product context, target audience, conversion objectives, accessibility,
performance, maintainability, design consistency, and technical constraints.

No Business Analyzer, User Analyzer, Brand Analyzer, Motion Planner,
Accessibility Planner, Design Critic, or other specialist reasoning module was
created.

### Keep Design Intelligence separate

Design Toolkit may query and interpret validated domain records. It may not own
website ingestion, pattern extraction, normalization, evidence collection,
independence grouping, confidence scoring, recommendation scoring, pattern
promotion, or knowledge storage.

### Add advisory extension points without fragmenting ownership

Future reasoning modules must use the `reasoning-modules` extension contract.
They receive bounded context and knowledge references and return advisory
evidence, confidence, risk, and uncertainty. Design Toolkit validates their
output, makes the final decision, writes Shared Context, and produces the unified
report.

Module-specific output uses versioned extension records so the core decision
schema need not change.

### Preserve reference paths

Keep `references/toolkit.md` and `references/frontend-foundations.md` to avoid
breaking existing instructions. Add `references/design-reasoning.md` for the
expanded workflow and extension contract.

### Preserve standalone operation

Require no skill dependency. Treat Visibility and Security as optional handoff
targets. When persisted Shared Context or validated Design Intelligence records
are unavailable, continue with an in-memory context envelope and project
evidence, and report the limitation.

## Decisions and trade-offs

- Preserve the original frontmatter description rather than broadening the
  trigger during the first contract migration. This minimizes routing risk but
  leaves some new reasoning detail discoverable only after the skill triggers.
- Retain unscored curated techniques as labeled inspiration rather than
  deleting them. This preserves useful ideas without treating sparse observation
  as best practice.
- Require at least one credible alternative in material machine-readable design
  decisions. This increases reporting work but prevents unexplained defaults.
- Use a project-local decision schema rather than expanding the common report
  schema. This keeps domain logic separate from infrastructure.
- Keep external visual scoring optional and `not_verified`. This preserves the
  workflow without treating an opaque score as evidence.

## Shared Context changes

The manifest declares reads for project, goals, constraints, state, decisions,
artifacts, risks, and prior skill runs. It declares attributable writes for
facts, uncertainty, decisions, artifacts, risks, skill runs, and handoff.

No persistent project context was created during this repository migration.

## Registry changes

The generated registry now exposes:

- ID `design-toolkit`
- version `1.0.0`
- category `design`
- status `stable`
- purpose, scope, responsibilities, inputs, outputs, configuration, and
  pipelines
- optional Visibility and Security dependencies
- Shared Context reads and writes
- validation and reporting requirements
- future extension points

## Validation results

- Upstream skill-creator quick validation: `pass`
- Strict Design Toolkit validation: `pass`
- Design-decision fixture schema validation: `pass`
- Reference-link validation: `pass`
- Trigger identity compatibility test: `pass`
- Required reasoning-dimension test: `pass`
- Design Intelligence ownership-boundary test: `pass`
- Registry contract test: `pass`
- Infrastructure validation: `pass`
- Knowledge validation: `pass` with zero production patterns
- Source-manifest validation: `pass` with zero production manifests
- Registry freshness: `pass`, current
- Full repository test suite: **27 passed**
- Repository audit: `partial`, zero failed checks and seven expected partial
  checks for remaining unmigrated first-party skills
- `.system` changes: zero
- Other first-party skill changes: zero
- Trailing-whitespace findings: zero

## Files changed

- `design-toolkit/SKILL.md`
- `design-toolkit/skill.yaml`
- `design-toolkit/agents/openai.yaml`
- `design-toolkit/references/design-reasoning.md`
- `design-toolkit/references/frontend-foundations.md`
- `design-toolkit/references/toolkit.md`
- `design-toolkit/schemas/design-decision.json`
- `docs/architecture/migration-plan.md`
- `ecosystem/registry/skills.json`
- `tests/fixtures/design-decision.yaml`
- `tests/test_design_toolkit_migration.py`
- `docs/migrations/design-toolkit.md`

## Risks and warnings

- The production Design Knowledge Base is empty, so the query workflow is
  structurally validated but not calibrated on real pattern records.
- Current source-catalog tools were not externally verified during this
  repository migration. The skill now requires availability and compatibility
  checks before use.
- No live application was designed or audited, so browser, device,
  accessibility-tree, or performance behavior was not exercised here.
- Future reasoning modules will require separate schemas, validation fixtures,
  compatibility ranges, and approval before implementation.

## Errors

None remaining.

## Recommendations

- Use the migrated skill on a representative frontend task before changing its
  trigger description.
- Calibrate Design Intelligence scores on a reviewed corpus in the approved
  Design Intelligence phase.
- Migrate Visibility next so frontend accessibility, performance, and
  crawlability handoffs use a full contract.

## Checks not run

- Live browser and device validation
- External design-QA services
- MCP or third-party source availability checks
- Production knowledge-corpus calibration
- Forward-testing on a real frontend artifact

These checks require a task artifact, external service, approved corpus, or a
separate validation exercise.

## Handoff

Next proposed owner: Visibility migration.

Approval is required before beginning Visibility.

