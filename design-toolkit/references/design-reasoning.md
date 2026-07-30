# Design reasoning and extension contract

Use this reference for material design choices. Keep final synthesis in Design
Toolkit even when advisory reasoning extensions are introduced later.

## Contents

1. Context model
2. Evidence and knowledge queries
3. Alternative evaluation
4. Decision requirements
5. Design Intelligence boundary
6. Future reasoning-module contract
7. Shared Context integration
8. Reporting and handoff

## Context model

Evaluate every dimension below. Record `not_applicable` or `not_verified` with a
reason when evidence is unavailable.

### Business objectives

- Identify the business outcome, operating model, constraints, and success
  signal.
- Distinguish a requested visual treatment from the business result it is meant
  to support.
- Avoid design choices that create operational promises the business cannot
  maintain.

### User goals

- Identify the primary user tasks, urgency, frequency, knowledge level, and
  failure cost.
- Preserve task completion and comprehension ahead of novelty.
- Consider new, returning, keyboard, touch, assistive-technology, slow-network,
  and error-recovery contexts where relevant.

### Brand identity

- Identify established voice, visual assets, typography, palette, personality,
  and prohibited treatments.
- Extend existing brand rules consistently. Do not infer missing brand rules
  from a reference website.
- Record unresolved brand choices rather than silently inventing them.

### Product context

- Classify the surface: marketing, commerce, content, authenticated product,
  dashboard, workflow, onboarding, settings, support, or another context.
- Account for content density, data sensitivity, interaction frequency, and
  lifecycle state.

### Target audience

- Identify audience segments, devices, locales, accessibility needs, technical
  literacy, and trust expectations.
- Avoid assuming that a pattern effective for one audience transfers to another.

### Conversion objectives

- Define the intended action and prerequisites for an informed decision.
- Support clarity and trust; do not use dark patterns, hidden costs, false
  scarcity, obstructive consent, or misleading visual hierarchy.
- Treat conversion evidence separately from pattern prevalence.

### Accessibility

- Prefer native semantics and inclusive interaction.
- Evaluate keyboard order, focus, contrast, labels, errors, reduced motion,
  zoom/reflow, screen-reader behavior, and touch targets as applicable.
- Reject or adapt patterns with unresolved material accessibility risks.

### Performance

- Evaluate initial rendering, LCP media, JavaScript cost, hydration, fonts,
  animation, third parties, caching, and slow-network behavior as applicable.
- Do not trade core content access for spectacle.

### Maintainability

- Prefer existing primitives, tokens, conventions, and dependencies.
- Consider component ownership, state complexity, testability, upgrade cost,
  content operations, and team capability.
- Require a concrete benefit before adding a library or bespoke abstraction.

### Design consistency

- Reuse tokens, hierarchy, spacing, control behavior, and interaction language.
- Explain intentional exceptions and keep them bounded.

### Technical constraints

- Inspect the real framework, rendering model, browser support, deployment,
  dependency policy, data flow, and project instructions.
- Do not recommend an implementation that the project cannot safely support.

## Evidence and knowledge queries

Query validated Design Intelligence domain records when they are available:

```text
skill-ecosystem knowledge query
  --domain <domain>
  --industry <industry>
  --ux-goal <goal>
  --accessibility <rating>
  --performance <rating>
  --confidence-level <tier>
  --min-evidence-confidence <0..1>
  --min-recommendation-score <0..1>
```

Record query filters and result IDs in the design decision. Do not query raw
archives as knowledge.

Interpret:

- `evidence_confidence` as recurrence confidence in the stated context;
- `recommendation_score` as suitability after quality and fit factors;
- `novelty` as inspiration value, not validation;
- contraindications and contradictory evidence before selecting a pattern.

Use established patterns as defaults only when project context matches. Present
experimental patterns as labeled alternatives. When no applicable knowledge
record exists, use project evidence and verified references, and record the
knowledge gap.

## Alternative evaluation

For each credible option, evaluate:

- fit to all context dimensions;
- reuse of existing components and design-system primitives;
- accessibility and performance implications;
- maintainability and consistency;
- technical feasibility;
- dependency and operational cost;
- supporting and contradictory evidence;
- reversibility and failure behavior.

Avoid fake comparison sets. Include only credible alternatives. Reject an option
with a specific reason tied to context, evidence, or risk.

## Decision requirements

Every material decision must state:

1. what was selected;
2. why it best fits the current context;
3. which alternatives were considered;
4. why each alternative was rejected;
5. risks and mitigations;
6. trade-offs accepted;
7. remaining uncertainties;
8. validation evidence and checks not run;
9. existing components or systems reused;
10. new dependencies, if any, and their justification.

Validate machine-readable decisions against
`schemas/design-decision.json`.

## Design Intelligence boundary

Design Toolkit may:

- query validated domain records;
- filter and compare patterns;
- interpret scores in project context;
- combine reusable principles into an original solution;
- report knowledge gaps or suspected stale guidance.

Design Toolkit may not:

- ingest website archives;
- execute reference code during ingestion;
- extract or normalize canonical patterns;
- group independent sources;
- collect evidence;
- calculate confidence or recommendation scores;
- promote pattern lifecycle status;
- write canonical knowledge records.

Route those responsibilities to the Design Intelligence Framework.

## Future reasoning-module contract

Do not implement separate Business Analyzer, User Analyzer, Brand Analyzer,
Motion Planner, Accessibility Planner, Design Critic, or similar modules in this
phase.

Allow future advisory modules through the `reasoning-modules` extension point.
Each module must declare:

- stable module ID and version;
- narrow purpose and non-goals;
- inputs and output schema;
- Shared Context fields read and proposed for writing;
- applicable Design Intelligence domains and query filters;
- required evidence and confidence semantics;
- validation rules;
- risks, uncertainties, and failure behavior;
- compatibility range for Design Toolkit.

Use this integration lifecycle:

```text
Design Toolkit validates context
  -> selects applicable advisory modules
  -> provides a bounded context snapshot and knowledge references
  -> module returns advice, evidence, confidence, risks, and uncertainty
  -> Design Toolkit validates and compares the advice
  -> Design Toolkit makes the final design decision
  -> Design Toolkit writes context and the unified report
```

Advisory modules must not:

- become independent final decision-makers;
- mutate Shared Context directly unless a later contract explicitly authorizes
  and validates the write;
- bypass Design Intelligence provenance or score semantics;
- install dependencies or implement changes without the Design Toolkit workflow;
- silently override user decisions or project constraints.

Adding a module must not require changing the core decision schema. Put
module-specific results in extension records identified by module ID and schema
version.

## Shared Context integration

Read goals, constraints, facts, assumptions, uncertainties, prior decisions,
artifacts, risks, and skill runs. Bind code-derived observations to the inspected
repository revision.

Write attributable records only to declared fields. Separate:

- facts observed directly;
- inferences with confidence;
- user-approved decisions;
- unresolved uncertainty;
- generated or changed artifacts;
- risks and specialist handoffs.

Supersede incorrect context records rather than erasing history. Use optimistic
revision checks when context is persisted.

## Reporting and handoff

Produce the common report sections plus the design-decision summary. Mark
external scores or provider results `not_verified` until evidence is supplied.

Handoff:

- SEO, metadata, crawlability, indexing, and search-platform work to
  `$visibility`;
- application/API security, secrets, authorization, CSP policy ownership, and
  data protection controls to `$security`;
- archive ingestion, evidence, scoring, and canonical knowledge maintenance to
  Design Intelligence infrastructure.

