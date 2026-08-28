# ADE Corpus Classification Audit

## Corpus Counts

- Sources: 40
- Extracted items: 932
- Prompt-like records by text/category scan: 303
- Strict prompt content-type records: 286
- Operational instructions: 368
- Research/staleness candidates: 505
- Conflict candidates: 288

## Extraction Categories

| Category | Count |
| --- | ---: |
| Design knowledge | 60 |
| Knowledge candidate | 169 |
| Operational instruction | 368 |
| Prompt / agent instruction | 286 |
| Security knowledge | 20 |
| Tool / package knowledge | 12 |
| Visibility / AEO knowledge | 17 |

## Distinctions Preserved

The current model keeps source, knowledge, memory, context, research, prompt, instruction, procedure, fact, concept, pattern, decision, preference, observation, hypothesis, recommendation, and AI inference distinguishable through `KnowledgeType`, `MemoryCategory`, `ResearchCandidate`, `SourceDerivation`, lifecycle `KnowledgeStatus`, `Freshness`, and access scope.

## Ambiguity Findings

- Prompt-like records can contain procedures; they must remain prompt/data unless reviewed for promotion.
- Operational instructions are candidate procedures, not agent control instructions.
- Research/staleness candidates are not durable knowledge.
- Conflict candidates are not automatically genuine conflicts.
- User/project statements must remain scoped and must not become universal facts.

## Verdict

Classification is trustworthy enough for a runtime prototype, but still needs human review before durable knowledge promotion. Ambiguous records are preserved and not automatically converted into objective facts.
