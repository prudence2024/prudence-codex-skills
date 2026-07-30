# Visibility migration report

## Summary

- **Date:** 2026-07-30
- **Status:** completed
- **Skill contract:** `visibility` 1.0.0, stable
- **Outcome:** Visibility owns search-facing discoverability and evidence while
  consuming applicable Design Toolkit decisions.
- **Backward compatibility:** existing skill ID, trigger description, folder,
  reference paths, display name, and standalone operation are preserved.

## Scope

Migrate Visibility to the Universal Skill Standard, integrate it with Shared
Context, register it, add a structured visibility-decision contract, align
reporting and validation, and document its boundary with Design Toolkit.

Do not migrate another first-party skill. Do not modify `.system`.

## Current state and evidence

Before migration, Visibility already provided strong implementation guidance for
SEO, local search, crawlability, structured data, metadata, social previews,
analytics, indexing, verification, and truthful evidence claims. It had no
first-party manifest, Shared Context contract, structured decision output,
registry metadata, formal ownership boundary with Design Toolkit, or
standardized reporting requirements.

Baseline SHA-256 hashes were recorded for the four existing skill files before
implementation. The three existing reference documents remain unchanged and
available at their original paths.

## Architectural decisions

### Keep search-facing responsibility in Visibility

Visibility owns SEO, discoverability, indexing, structured data, metadata,
social previews, crawlability, search performance, and web visibility. Its
workflow now evaluates these domains explicitly and records evidence states
without treating deployment, registration, receipt, indexing, or measured
performance as interchangeable.

### Consume design decisions instead of duplicating design reasoning

Where navigation, hierarchy, page composition, accessibility, responsive
behavior, or frontend performance decisions influence visibility, Visibility
reads applicable Design Toolkit decisions from Shared Context or supplied
artifacts. It validates their search-facing consequences and returns visibility
requirements or conflicts. It does not choose visual systems, components,
interaction patterns, motion, or general frontend implementation strategy.

### Preserve overlap as evidence and handoff

Accessibility and performance can affect discoverability, so Visibility may
measure and report their search-facing impact. General remediation strategy
remains with Design Toolkit; security-policy changes remain with Security.
This avoids duplicate ownership while preserving actionable diagnostics.

### Keep domain logic separate from shared infrastructure

The visibility decision schema is owned by the skill and composes with the
common Shared Context and reporting contracts. Future provider, crawler,
structured-data, or analytics adapters return bounded evidence; they do not
replace Visibility's decision ownership or require changes to the common
infrastructure schema.

### Preserve standalone operation

No required skill dependency was introduced. Design Toolkit and Security are
optional collaborators. When their output or persisted Shared Context is
unavailable, Visibility continues from project evidence, labels the limitation,
and avoids inventing upstream decisions.

## Decisions and trade-offs

- Preserve the original frontmatter description to minimize routing and trigger
  compatibility risk.
- Require at least one credible alternative for material visibility decisions.
  This adds reporting work but makes defaults and rejected approaches explicit.
- Keep the existing crawlability and SEO reference documents unchanged. This
  preserves deep links and prior guidance, while the new reasoning reference
  supplies the ownership and Shared Context contract.
- Separate implementation evidence from provider and search-engine outcomes.
  This prevents overclaiming but means some outcomes remain unresolved until an
  authorized owner performs external registration or measurement.
- Model Design Toolkit and Security as optional dependencies. This preserves
  standalone use but requires explicit handoffs when their authority is needed.

## Shared Context changes

The manifest declares reads for project facts, goals, constraints, state,
decisions, artifacts, risks, prior skill runs, and applicable Design Toolkit
outputs. It declares attributable writes for visibility facts, decisions,
artifacts, risks, uncertainty, validation evidence, skill runs, and handoffs.

No persistent project context was created during this repository migration.

## Registry changes

The generated registry now exposes:

- ID `visibility`
- version `1.0.0`
- category `visibility`
- status `stable`
- the nine owned visibility domains
- Design Toolkit consumption and non-duplication boundaries
- inputs, outputs, configuration, processing, validation, and reporting
- optional Design Toolkit and Security dependencies
- Shared Context reads and writes
- future adapter extension points

## Validation results

- Upstream skill-creator quick validation: `pass`
- Strict Visibility validation: `pass`
- Visibility-decision fixture schema validation: `pass`
- Reference-link validation: `pass`
- Trigger identity compatibility test: `pass`
- Required visibility-domain ownership test: `pass`
- Design Toolkit consumption and non-duplication test: `pass`
- Registry contract test: `pass`
- Infrastructure validation: `pass`
- Knowledge validation: `pass` with zero production patterns
- Source-manifest validation: `pass` with zero production manifests
- Registry freshness: `pass`, current
- Full repository test suite: **34 passed**
- Repository audit: `partial`, zero failed checks and six expected partial
  checks for the remaining unmigrated first-party skills
- `.system` changes: zero
- Other in-sequence first-party skill changes: zero
- Trailing-whitespace findings: zero

## Files changed

- `visibility/SKILL.md`
- `visibility/skill.yaml`
- `visibility/agents/openai.yaml`
- `visibility/references/visibility-reasoning.md`
- `visibility/schemas/visibility-decision.json`
- `ecosystem/registry/skills.json`
- `tests/fixtures/visibility-decision.yaml`
- `tests/test_visibility_migration.py`
- `docs/migrations/visibility.md`

## Risks and warnings

- No live site was supplied, so crawl responses, rendered HTML, bot access,
  structured-data eligibility, social previews, and indexing were not observed.
- Search Console, Bing Webmaster Tools, analytics, local-business profiles, and
  other provider dashboards were not accessed.
- The production Design Knowledge Base remains empty, so knowledge querying is
  structurally validated but not calibrated on real visibility patterns.
- Existing public-practice references were preserved but not externally
  reverified during this migration.
- Search-engine behavior and emerging AI-discovery conventions can change; the
  skill therefore requires current evidence and avoids guarantees.

## Errors

None remaining.

## Recommendations

- Exercise the migrated skill on a representative live and repository-backed
  visibility audit before changing its trigger description.
- Add provider-specific adapters only through the documented extension contract
  and with fixtures that distinguish configured, reachable, received, indexed,
  and measured states.
- Migrate Security next so CSP, headers, redirects, and exposure-related
  visibility handoffs use a full skill contract.

## Checks not run

- Live crawler and bot-user-agent requests
- Rendered HTML and hydration validation on a deployed site
- Search Console or Bing registration and indexing checks
- Social-card previews on external platforms
- Production analytics and search-performance measurement
- Local-business profile verification
- External structured-data rich-result testing

These checks require a live artifact, external service, provider authorization,
or production measurement window.

## Handoff

Next proposed owner: Security migration.

Approval is required before beginning Security.
