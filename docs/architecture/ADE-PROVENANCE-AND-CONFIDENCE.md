# ADE Provenance And Confidence

Status: Phase 2.1 architecture specification only.

## Purpose

ADE must know where knowledge came from, how strong the evidence is, how fresh it is, and how useful it is for a recommendation. A source is not trustworthy merely because it exists.

## Provenance Model

Every knowledge item should retain an evidence chain. Provenance should answer:

```text
WHAT was observed?
WHERE did it come from?
WHO authored or supplied it?
WHEN was it created, updated, and observed?
HOW was it extracted or synthesized?
WHAT transformations occurred?
WHAT license or access constraints apply?
```

## Source Types

- Official documentation: vendor, standards body, first-party API docs, release notes, and official guides.
- Educational material: tutorials, courses, books, guides, and explanatory articles.
- Community source: forums, discussions, issue comments, Q&A, and social posts.
- User-provided content: files, notes, instructions, documents, examples, or direct statements from the user.
- Project decision: repository-local decision, architecture record, report, test outcome, or owner approval.
- Experimental observation: benchmark, runtime test, browser observation, screenshot, log, or prototype result.
- AI inference: model-generated hypothesis or synthesis that requires validation before becoming fact.
- Research synthesis: source-backed analysis produced from a research workflow.

## Source Quality Dimensions

- Authority: how close the source is to the owner of the fact.
- Freshness: whether the source is current for the relevant version/time.
- Specificity: whether the source directly answers the question.
- Corroboration: whether independent sources agree.
- Version relevance: whether package/API/framework versions match the task.
- Evidence quality: whether the claim is supported by code, tests, official statements, measurements, or direct observation.
- Conflict status: whether credible sources disagree.
- Access and license: whether ADE may retain and reuse the information.

## Confidence Fields

### evidence_confidence

`evidence_confidence` measures how strong the supporting evidence is. It should rise with primary sources, direct tests, corroboration, current versions, and clear provenance. It should fall with stale sources, weak authority, missing versions, anecdotal reports, or unresolved conflicts.

### recommendation_score

`recommendation_score` measures how useful an item is for a specific decision. A claim can have high evidence confidence but low recommendation score if it is true but irrelevant, risky, too costly, or mismatched to the project.

These values must remain separate.

## Confidence Labels

Suggested labels:

- `established`: strong evidence, current, corroborated, low conflict.
- `contextual`: valid in a known context or version boundary.
- `promising`: useful but not yet broadly validated.
- `experimental`: observed or hypothesized, needs more evidence.
- `conflicted`: credible disagreement exists.
- `stale_risk`: likely to change or source is old.
- `rejected`: not suitable or disproven.

## Conflict Handling

When sources disagree:

1. Preserve both claims.
2. Record source types, dates, versions, and authority.
3. Identify whether conflict is temporal, version-specific, contextual, or factual.
4. Prefer direct/current/official evidence only when justified.
5. Mark unresolved conflicts explicitly.
6. Escalate to a human when risk is high, source quality is insufficient, or a business/project decision is required.

Do not overwrite one source simply because another appears later.

## AI Inference Rules

AI inference may help form hypotheses, summaries, and candidate relationships. It must not silently become fact. Any AI-derived knowledge item must identify itself as AI inference or research synthesis and link to the source evidence used.

## Privacy And Security

Do not store secrets, credentials, private tokens, raw sensitive personal data, or unauthorized third-party content in the knowledge layer. If sensitive source material must inform a decision, store a minimal, access-controlled summary with provenance and retention limits.

## Related Documents

- [ADE-KNOWLEDGE-MODEL.md](ADE-KNOWLEDGE-MODEL.md)
- [ADE-KNOWLEDGE-LIFECYCLE.md](ADE-KNOWLEDGE-LIFECYCLE.md)
- [ADE-INGESTION-ARCHITECTURE.md](ADE-INGESTION-ARCHITECTURE.md)
