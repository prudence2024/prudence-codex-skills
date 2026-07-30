# Universal first-party skill standard

## Scope

Apply this standard to first-party skills only. `.system` skills are discovered
through a compatibility adapter and are not migrated.

## Required files

Every first-party skill must contain:

- `SKILL.md` with `name` and `description` frontmatter plus concise procedural
  guidance.
- `agents/openai.yaml` with matching UI metadata.
- `skill.yaml` containing the ecosystem contract.

References, scripts, schemas, and assets remain optional.

## `skill.yaml` contract

The manifest must declare:

```yaml
schema_version: 1
id: design-toolkit
name: Design Toolkit
version: 1.0.0
category: design
status: stable
purpose: ""
scope:
  includes: []
  excludes: []
responsibilities: []
inputs: []
outputs: []
dependencies:
  required: []
  optional: []
configuration: []
context:
  reads: []
  writes: []
pipeline:
  processing: []
  reasoning: []
validation: []
reporting:
  report_type: skill-run
extension_points: []
```

Use semantic versions for the skill contract, not for every wording correction.
Increment the major version for incompatible input, output, or context changes.

## Reasoning pipeline

Each skill must:

1. Read available project context.
2. establish current state and evidence;
3. identify goals, constraints, unknowns, and risk;
4. evaluate applicable alternatives;
5. make and justify decisions;
6. validate the proposed or implemented result;
7. update only its declared context fields;
8. generate a structured report and handoff.

Never disguise missing evidence as a decision. Record unresolved questions and
confidence explicitly.

## Boundary rules

- Give every responsibility one primary owner.
- Express cross-domain work as a dependency or handoff rather than duplicating
  the full specialist workflow.
- A coordinator may aggregate specialist findings but must not silently replace
  specialist validation.
- Skills may degrade gracefully when optional dependencies are unavailable.
- A required dependency failure must be reported, not bypassed.

## Extension points

Declare supported additions such as validators, report sections, context fields,
knowledge domains, source adapters, and provider integrations. Extensions must
not change existing contracts without a versioned migration.

