# Shared Context Protocol

## Purpose

Carry verified project knowledge and skill decisions forward without turning
conversation summaries into an undocumented source of truth.

## Context envelope

The initial protocol is a versioned YAML or JSON document with these sections:

```yaml
schema_version: 1
project:
  id: ""
  repository: ""
  revision: ""
run:
  id: ""
  started_at: ""
goals: []
constraints: []
state:
  facts: []
  assumptions: []
  uncertainties: []
decisions: []
artifacts: []
risks: []
skill_runs: []
handoff:
  next_skills: []
  reason: ""
```

Every fact, assumption, uncertainty, decision, artifact, and risk must have a
stable ID, authoring skill, timestamp, provenance, and confidence where relevant.

## Lifecycle

```text
read context
  -> validate schema and revision
  -> inspect current state
  -> perform specialized reasoning
  -> propose or make authorized decisions
  -> validate results
  -> append attributable context changes
  -> emit report
  -> create explicit handoff
```

## Write discipline

- Skills may write only fields declared in their registry entry.
- Preserve prior values and attribution; corrections supersede records rather
  than erasing history.
- Separate observed facts from model inferences and user-approved decisions.
- Record contradictions instead of choosing silently between sources.
- Never place secrets, raw customer payloads, credentials, or prohibited personal
  data in shared context.
- Bind code-derived facts to a repository revision when one is available.

## Concurrency and recovery

Use optimistic revision checks. A writer reads revision `n` and may publish
revision `n+1` only if the base revision remains current. Conflicts require merge
or human resolution. Context writes must be atomic and recoverable.

## Minimal operation

A skill may run without an existing context file by creating an in-memory
envelope and reporting that persistence was unavailable. This preserves backward
compatibility while preventing a hard dependency on future orchestration.

