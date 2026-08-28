# ADE Knowledge Classification Matrix

Phase: 2.3  
Corpus state: STAGING CORPUS  
Sources: 40  
Extracted items: 932

## Classification Counts From Current Corpus

These are source extraction categories, not final trusted knowledge classifications.

- Design knowledge: 60
- Knowledge candidate: 169
- Operational instruction: 368
- Prompt / agent instruction: 286
- Security knowledge: 20
- Tool / package knowledge: 12
- Visibility / AEO knowledge: 17

Prompt-like records observed by text/category scan: 292. The Phase 2.3 work order identifies 297 prompt-like records; the strict content-type count is 286 `Prompt / agent instruction` records.

## Runtime Knowledge Types

| Runtime type | Use | Governance rule |
| --- | --- | --- |
| FACT | Validated objective claim | Must not be created from AI-inferred or AI-synthesized provenance without validation. |
| CONCEPT | Explanatory or definitional knowledge | Retrieve as context, not as proof. |
| PROCEDURE | Operational workflow or steps | Treat as candidate procedure; does not override ADE system rules. |
| PATTERN | Reusable design or engineering pattern | Must retain source and scope. |
| DECISION | Project or architecture decision | Must remain scoped to project/source context. |
| OBSERVATION | Reported result or finding | Must preserve evidence and test context. |
| HYPOTHESIS | Startup/product/technical assumption | Must not be treated as validated market or engineering evidence. |
| RESEARCH_FINDING | Source-backed research result | Must retain source quality and freshness. |
| PROMPT | Prompt, role, reusable task instruction, or agent instruction | Retrieve separately from facts and procedures. |
| INSTRUCTION | Imperative operational instruction | Must remain non-authoritative unless promoted by reviewed ADE policy. |
| RECOMMENDATION | Suggested action or tool choice | Must separate evidence from advice. |
| PREFERENCE | User or project preference | Must not become objective technical fact. |
| PROJECT_KNOWLEDGE | Project-specific information | Must require project-aware retrieval. |
| EXTERNAL_KNOWLEDGE | External docs, educational, community, or vendor material | Must retain source quality and freshness. |
| AI_INFERENCE | Model-derived conclusion from evidence | Must remain explicitly inferred. |
| UNKNOWN | Ambiguous record | Must require review before durable use. |

## Collision Audit

| Collision | Current risk | Governance decision |
| --- | --- | --- |
| Prompt vs procedure | Many prompts contain procedural steps. | `Prompt / agent instruction` imports as `PROMPT`; procedural reuse requires reviewed promotion. |
| Instruction vs fact | Imported instructions can sound authoritative. | Instructions remain `PROCEDURE` or `INSTRUCTION`, never system policy by import alone. |
| Recommendation vs fact | Tool advice can be mistaken for current fact. | Recommendations need evidence fields and current-research checks before use. |
| Preference vs objective claim | User preferences can read like universal rules. | Preferences use `PREFERENCE` or project scope; retrieval must preserve context. |
| AI inference vs evidence | Synthesized conclusions can appear source-backed. | Runtime rejects AI-derived objective `FACT` items without validation. |
| Project decision vs general best practice | ADE/project decisions can leak into global answers. | Runtime includes `AccessScope` and project filtering. |

## Classification Verdict

The runtime can now represent the classes required by Phase 2.3. Automatic classification remains conservative and staging-only. The corpus is sufficiently governed for Phase 2.4 planning because ambiguous, prompt, project, restricted, and AI-inferred material can be represented without pretending it is trusted fact.
