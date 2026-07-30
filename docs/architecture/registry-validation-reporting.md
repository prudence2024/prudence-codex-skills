# Registry, validation, and reporting

## Skill Registry

Generate the registry by discovering first-party `skill.yaml` manifests and
read-only `.system/*/SKILL.md` metadata.

Each entry must expose:

- skill ID, name, category, version, and status;
- purpose, scope, and responsibilities;
- required and optional dependencies;
- inputs and outputs;
- context fields read and written;
- validation requirements;
- report type and extension points;
- source path and discovery timestamp.

The generated registry is an artifact, not a hand-maintained authority. Duplicate
IDs, missing dependencies, dependency cycles, conflicting context ownership, and
invalid paths must fail validation.

System entries must be labeled `upstream: true`, `read_only: true`, and may omit
first-party-only contract fields.

## Validation layers

1. **Structure** — required files, naming, YAML, and allowed frontmatter.
2. **Manifest** — schema, version, declared paths, dependencies, and status.
3. **Context** — schema, provenance, allowed writes, revision, and sensitive-data
   exclusions.
4. **Skill output** — declared output schema and required evidence.
5. **Report** — required sections, status vocabulary, and context-change linkage.
6. **Repository** — registry uniqueness, dependency integrity, documentation
   links, and first-party consistency.

Validators must be deterministic, non-destructive, and offline by default.
Network-dependent checks must be separate and explicit.

## Report contract

Every major phase and skill run must report:

- summary and scope;
- evidence and current state;
- decisions and trade-offs;
- validation results;
- risks, warnings, and errors;
- recommendations;
- context changes;
- files or artifacts changed;
- checks not run and why;
- next owner or handoff;
- approval required.

Use `pass`, `fail`, `partial`, `not_applicable`, and `not_verified` as the common
validation statuses. Recommendations use `proposed`, `approved`, `rejected`,
`implemented`, or `superseded`.

## Evidence integrity

Claims must point to local paths, command outputs, source identifiers, or public
provenance records. A configured control is not equivalent to a verified live
control. Validators and reports must preserve that distinction.

