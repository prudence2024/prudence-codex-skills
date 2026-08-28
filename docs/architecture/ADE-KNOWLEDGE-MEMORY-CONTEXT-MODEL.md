# ADE Knowledge, Memory, Context, And Research Model

Status: Phase 2.1 architecture specification only.

## Purpose

ADE must distinguish four related but different concepts: knowledge, memory, context, and research. Confusing them would cause stale facts, user preferences, search results, and task instructions to become indistinguishable.

## Knowledge

Knowledge is information ADE can retrieve and reuse because it has provenance, confidence, lifecycle state, and a defined scope.

Examples:

- Official React documentation for a specific version.
- A validated design pattern extracted from multiple website references.
- A security procedure verified by `system-breaker`.
- A project architecture decision with rationale and date.

Knowledge answers: "What does ADE know, and why should it trust or doubt it?"

## Memory

Memory is information ADE intentionally retains about projects, users, decisions, preferences, history, and relevant persistent state.

Examples:

- The user prefers evidence-backed reports over broad claims.
- A project decided to avoid provider lock-in.
- A repository uses a specific checkout state-machine pattern.
- A prior incident established a recurring risk.

Memory answers: "What should ADE remember for future work, and for how long?"

Memory can reference knowledge, but memory is not a universal knowledge store. It should be scoped, privacy-aware, and updateable.

## Context

Context is the selected information provided to an agent for the current task. Context is temporary, bounded, and task-specific.

Examples:

- The current user request.
- Relevant files and command output.
- The few knowledge items needed for a package decision.
- The latest test failure and constraints.

Context answers: "What does the agent need right now to act well?"

Context can include retrieved knowledge and memory, but only when relevant.

## Research

Research is active investigation. It includes questions, searches, raw sources, source rankings, notes, conflicts, synthesis, confidence, and promotion decisions.

Examples:

- Checking the latest official API docs for a framework.
- Comparing package maintenance status.
- Reviewing GitHub releases for a breaking change.
- Investigating design trends before promoting a pattern.

Research answers: "What is ADE currently trying to find out?"

Research is not automatically knowledge. It must pass promotion rules before becoming durable.

## Boundary Rules

- A search result is research, not knowledge.
- A user statement is source material; classify it before storing as memory or knowledge.
- A memory can be stale and must not override current source evidence without review.
- Context should be rebuilt when source, task, or evidence changes.
- Knowledge must preserve provenance and confidence.
- AI inference is a hypothesis unless validated.

## Promotion Paths

```text
Raw source -> Research -> Candidate knowledge -> Validated knowledge -> Durable knowledge
User preference -> Memory candidate -> Scoped durable memory
Current task evidence -> Context -> Report -> optional memory or knowledge candidate
```

## Examples

### Technical Fact

- Research: "What changed in package X version Y?"
- Knowledge: verified release note, version, source URL, confidence.
- Context: the specific breaking change needed for today's migration.
- Memory: project decision to pin or upgrade package X.

### User Preference

- Source: user says, "Use concise evidence tables."
- Memory: scoped preference with provenance and timestamp.
- Context: included only for tasks where report format matters.
- Knowledge: not a general objective fact.

### Design Pattern

- Research: collect references and observations.
- Knowledge: normalized pattern with examples, accessibility notes, and confidence.
- Context: selected pattern for a website task.
- Memory: project choice to use or avoid the pattern.

## Related Documents

- [ADE-KNOWLEDGE-MODEL.md](ADE-KNOWLEDGE-MODEL.md)
- [ADE-RETRIEVAL-ARCHITECTURE.md](ADE-RETRIEVAL-ARCHITECTURE.md)
- [ADE-PROVENANCE-AND-CONFIDENCE.md](ADE-PROVENANCE-AND-CONFIDENCE.md)
