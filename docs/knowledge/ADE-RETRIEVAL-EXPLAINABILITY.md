# ADE Retrieval Explainability

## Required Explanation Fields

Every future retrieval answer should be able to explain:

- what item was retrieved;
- why it matched;
- source ID and source location;
- content type;
- provenance and derivation;
- confidence;
- freshness;
- access scope;
- project scope;
- conflicts;
- whether output is evidence, recommendation, preference, or inference.

## Current Runtime

`retrieve_context` returns context packets with item ID, title, body, source, confidence, freshness, related entities, and use limits. Search supports query text, type, domain, project, tag, source ID, freshness, access scope, and archived inclusion.

## Gaps For Production

The current runtime is explainable enough for staging tests, but production systems must add ranking explanations, filtered-out reasons, conflict surfacing, semantic match evidence, graph path explanations, and recommendation derivation traces.

## Query Governance

| Query | Required behavior |
| --- | --- |
| What is the current recommended approach? | Separate current evidence from recommendation and cite freshness. |
| What did ADE decide? | Return project decision records, not external advice. |
| What does the source material teach? | Return source-derived material with no trust inflation. |
| What should I use for this project? | Combine evidence, project constraints, and recommendation reasoning. |
