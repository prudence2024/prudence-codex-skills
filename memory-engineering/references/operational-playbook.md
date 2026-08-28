# Memory Engineering Operational Playbook

Use this playbook when deciding what an AI system should remember, retrieve, update, or forget.

## Four-Way Distinction

- Knowledge: generally reusable facts or patterns with provenance.
- Memory: project/user history, preferences, decisions, and durable context.
- Context: the current task packet given to an agent now.
- Research: active investigation not yet promoted to trusted knowledge or memory.

Do not collapse these into one storage bucket.

## Inputs

- Candidate memory or retrieval request.
- Source artifact: user instruction, repo decision, test evidence, report, runtime observation, or research result.
- Timestamp, scope, owner, confidence, and sensitivity.
- Existing memories that may duplicate or conflict.

## Procedure

1. Classify the item: preference, project decision, constraint, fact, workflow note, incident, or temporary task state.
2. Decide whether memory is warranted. Store only information likely to help future work and safe to retain.
3. Set scope: user-wide, project-specific, repository-specific, task-specific, or temporary.
4. Record provenance: who/what said it, where it came from, when observed, and supporting evidence.
5. Add freshness rules: expiry date, review trigger, version boundary, or stale-risk note.
6. Check privacy and sensitivity. Do not store secrets, unnecessary personal data, private audio, tokens, or credentials.
7. Before writing, search for existing memories about the same entity/decision.
8. If a conflict exists, keep both with timestamps and confidence; do not silently overwrite.
9. Retrieve by relevance to the current task, not by dumping all memories.
10. Update or delete when the user corrects it, source evidence changes, the project changes, or retention is no longer justified.

## Decision Points

- Remember a user preference only when it is stable and likely reusable.
- Remember a project decision when it affects future architecture, constraints, workflows, or tests.
- Do not remember transient state that belongs only in current context.
- Promote research to memory only after provenance and confidence are clear.

## Failure Modes To Break

- Stale memory overriding current source.
- Sensitive data retained without need.
- Conflicting decisions merged into a false single truth.
- AI inference stored as user intent.
- Memory retrieval polluting unrelated tasks.

## Verification

A memory operation is successful only if it can answer:

```text
WHAT is remembered?
WHY is it useful later?
WHERE did it come from?
WHEN was it observed?
WHO/WHAT is authoritative?
HOW stale could it become?
WHAT conflicts with it?
HOW can it be updated or deleted?
```

## Outputs

- Memory write/update/delete recommendation.
- Scope and retention rule.
- Provenance and confidence.
- Conflict notes.
- Retrieval guidance for future context-engineering.

## Related Skills

- context-engineering for current task packets.
- research-intelligence for active investigations.
- knowledge-graphs for relationship-heavy memory structures.
