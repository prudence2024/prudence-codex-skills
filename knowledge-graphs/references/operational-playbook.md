# Knowledge Graphs Operational Playbook

Use this playbook when entity relationships, time, provenance, and conflict-aware retrieval matter more than simple notes or documents.

## When To Use A Graph

Use graph storage when the task needs relationships such as people-to-projects, decisions-to-files, packages-to-capabilities, incidents-to-causes, or temporal facts that change over time.

Do not use a graph for one-off notes, simple key-value memory, small flat lists, or facts that will not be queried by relationship.

## Inputs

- Raw information: documents, decisions, source observations, research, memory records, test evidence.
- Entity candidates, relationship candidates, timestamps, provenance, confidence, and contradictions.
- Query goals: what future retrieval should answer.

## Procedure

1. Define the query the graph must support. If no relationship query exists, do not graph it.
2. Extract entities: person, project, repository, file, skill, package, provider, feature, decision, incident, requirement, test, source.
3. Normalize entity names and stable IDs. Keep aliases rather than duplicating nodes.
4. Extract relationships with verbs: depends_on, decided_by, implemented_in, verified_by, conflicts_with, supersedes, uses, observed_in.
5. Add temporal metadata: observed_at, valid_from, valid_until, superseded_at, or unknown.
6. Add provenance: source path/URL, report, command, user statement, runtime evidence, or research source.
7. Assign confidence and source type. Graph retrieval is not proof.
8. Store contradictions explicitly using `conflicts_with`; do not overwrite without authority.
9. Retrieve by relationship and freshness, then return provenance with every answer.
10. Update by adding new observations or supersession edges rather than destroying history unless deletion is required.

## Graphiti Note

Graphiti can be evaluated as one implementation option for temporal knowledge graphs. Do not make ADE dependent on Graphiti unless an architecture decision approves it.

## Failure Modes To Break

- Treating graph search results as verified truth.
- Losing provenance when facts become nodes.
- Merging similarly named entities incorrectly.
- Keeping stale facts without temporal boundaries.
- Overbuilding a graph when context or memory is enough.

## Verification

Test representative queries:

- Can the graph explain why a decision was made and when?
- Can it show current and superseded facts separately?
- Can it return evidence for each relationship?
- Can it surface conflicts instead of hiding them?

## Outputs

```text
GRAPH_DECISION: use graph / do not use graph
ENTITIES:
RELATIONSHIPS:
TEMPORAL_FIELDS:
PROVENANCE:
CONFLICTS:
RETRIEVAL_QUERIES:
RISKS:
```

## Related Skills

- memory-engineering for durable project memory policy.
- research-intelligence for source quality and freshness.
- context-engineering for packaging retrieved graph facts into task context.
