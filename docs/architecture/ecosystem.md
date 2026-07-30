# Skill ecosystem architecture

## Status

Phase 2 specification. Implementation requires a separate approved phase.

## Goals

Build a modular, reasoning-first ecosystem for first-party skills while preserving
their current triggers and useful domain guidance. Treat `.system` as a read-only
upstream compatibility layer.

Do not build ADE. Do not create a general agent runtime.

## Architectural layers

1. **Compatibility layer** — discover `.system` skills for dependency checks
   without changing their files or requiring first-party metadata from them.
2. **First-party skills** — keep each domain skill independently upgradeable and
   give it a common manifest, context contract, validation contract, and report
   contract.
3. **Shared context** — exchange versioned facts, constraints, decisions,
   uncertainties, artifacts, and handoffs between skills.
4. **Registry** — discover skills and expose capabilities, dependencies, declared
   context access, schemas, validators, and status.
5. **Validation and reporting** — apply common structural checks and produce
   evidence-backed reports with consistent status vocabulary.
6. **Design intelligence** — learn domain-organized design knowledge from curated,
   untrusted website archives without copying websites.
7. **Skill learning** — compare first-party skills with curated public practices
   and emit provenance-backed recommendations that require human approval.

## Repository target

```text
.
|-- .system/                         # read-only upstream compatibility layer
|-- docs/architecture/               # approved ecosystem specifications
|-- ecosystem/
|   |-- config/
|   |-- registry/
|   |-- schemas/
|   |-- validators/
|   `-- reporting/
|-- context/                         # project/run context, normally generated
|-- design-intelligence/
|   |-- config/
|   |-- manifests/
|   |-- observations/
|   |-- knowledge/
|   |-- references/raw/              # curated local archives; Git-ignored
|   |-- reports/
|   `-- schemas/
|-- skill-learning/
|   |-- config/
|   |-- snapshots/
|   |-- recommendations/
|   |-- reports/
|   `-- schemas/
`-- <first-party-skill>/
    |-- SKILL.md
    |-- skill.yaml
    |-- agents/openai.yaml
    |-- references/
    |-- schemas/                     # optional domain contracts
    `-- scripts/                     # optional deterministic operations
```

Only create optional directories when a skill actually needs them.

## Compatibility rules

- Do not modify files below `.system`.
- Keep `SKILL.md` frontmatter compatible with the upstream skill-creator
  convention: only `name` and `description`.
- Put ecosystem metadata in `skill.yaml`, not additional frontmatter.
- Preserve existing skill names and trigger descriptions during migration unless
  a separately approved trigger change fixes a demonstrated routing defect.
- Make generated registry and reports reproducible from tracked inputs.
- Do not require a network service, database, or vector store for the initial
  implementation.

## Decision ownership

Architecture and policy changes require human approval. Validators may reject
invalid artifacts, but no learning process may update a skill automatically.
Every applied recommendation must link to an approval record and the evidence
that motivated it.

