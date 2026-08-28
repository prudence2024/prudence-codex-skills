# ADE Phase 2.3 Corpus Governance Audit

## Scope

This audit evaluates whether the existing Phase 2.1 and Phase 2.2 knowledge architecture/runtime can safely govern the current staging corpus. It does not add sources, start production ingestion, install Graphiti, integrate Hermes, build a crawler, or create new ADE skills.

## Corpus Snapshot

- Source records: 40
- Extracted items: 932
- Source file: `docs/knowledge/ADE-SOURCE-RECORDS.json`
- Extracted item file: `docs/knowledge/ADE-EXTRACTED-ITEMS.jsonl`
- Source type counts:
- MD: 1
- PDF: 33
- TXT: 6

## Extraction Categories

- Design knowledge: 60
- Knowledge candidate: 169
- Operational instruction: 368
- Prompt / agent instruction: 286
- Security knowledge: 20
- Tool / package knowledge: 12
- Visibility / AEO knowledge: 17

## Provenance Findings

Every extracted item can be tied to source metadata through `source_id`, `source_location`, `source_section`, `original_text_reference`, `content_type`, `topic`, `subtopic`, `technology`, `project`, and `status`. Source records preserve original filename, source type, topic, projects, technologies, prompt/procedure/decision flags, stale flag, hash, raw location, and text dump reference.

No production trust is implied by extraction. The corpus state is `SOURCE AVAILABLE` and `EXTRACTED`; selected records are `NORMALIZED` into the knowledge core. `VALIDATED`, `INDEXED`, and `RETRIEVABLE` remain distinct states.

## Runtime Deficiencies Tested

| Deficiency | Evidence | Fix |
| --- | --- | --- |
| Prompt records could be treated like procedures. | Content category `Prompt / agent instruction` appears 286 times. | Added `KnowledgeType.PROMPT` and importer mapping. |
| Project/restricted knowledge could be retrieved globally. | Existing search had no access scope primitive. | Added `AccessScope` and default global/project filtering. |
| Archived source records could still appear in default retrieval. | Source revocation semantics require hiding removed-source items. | Default search excludes `ARCHIVED` and `SUPERSEDED`; `archive_source` added. |
| AI inference could be stored as objective fact. | Phase 2.3 requires inference not become fact. | `KnowledgeItem` rejects AI-inferred or AI-synthesized `FACT` without validation. |

## Assumption Table

| Assumption | How to break it | Expected | Test | Evidence | Result |
| --- | --- | --- | --- | --- | --- |
| Prompt corpus records are not facts. | Import a prompt-type JSONL record. | Imported item type is `PROMPT`. | `test_prompt_records_import_as_prompt_not_fact` | Focused tests passed. | PASS |
| Restricted knowledge is not global. | Search without project/access filters. | Restricted item omitted. | `test_project_specific_and_restricted_knowledge_are_not_retrieved_globally` | Focused tests passed. | PASS |
| Removed source items stop default retrieval. | Archive a source then search. | Archived item omitted unless explicitly requested. | `test_archived_source_items_are_not_retrieved_by_default` | Focused tests passed. | PASS |
| AI inference is not objective fact. | Create `FACT` with AI-inferred provenance. | Runtime raises `KnowledgeCoreError`. | `test_ai_inference_cannot_be_presented_as_objective_fact` | Focused tests passed. | PASS |

## Governance Verdict

The model can govern the staging corpus safely enough for Phase 2.4. It remains a staging model, not a production memory system.
