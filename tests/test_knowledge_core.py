from __future__ import annotations

import json
from pathlib import Path

import pytest

from skill_ecosystem.knowledge_core import (
    Confidence, CorpusImporter, Entity, Freshness, InMemoryGraph,
    InMemoryKnowledgeRepository, KnowledgeCoreError, KnowledgeItem,
    KnowledgeSearchQuery, KnowledgeStatus, KnowledgeType, MemoryCategory,
    MemoryRecord, MemoryStore, Provenance, Relationship, RetrievalInterface,
    Source, SourceDerivation, UnsupportedBackendError, ensure_transition,
    import_research_candidates_from_extraction, stable_id,
)


FIXTURE_RECORD = {
    "item_id": "ITEM-TEST-001",
    "source_id": "SRC-001",
    "source_location": "raw-corpus/text-dumps/SRC-001-frontier.txt",
    "source_section": "Workflow",
    "original_text_reference": "SRC-001 section 1, chunk 1",
    "content_type": "Operational instruction",
    "topic": ["Security and verification"],
    "subtopic": "Workflow",
    "technology": ["Python"],
    "project": ["ADE"],
    "status": ["EXTRACTED", "STALE_CANDIDATE", "CONFLICT_REVIEW_CANDIDATE"],
    "evidence_confidence": "medium",
    "recommendation_score": "not_assessed",
    "source_quality": "User-provided source",
    "text_excerpt": "Verify generated code with tests before treating it as knowledge.",
}


def provenance() -> Provenance:
    return Provenance(
        source_id="SRC-001",
        source_location="raw-corpus/text-dumps/SRC-001-frontier.txt",
        source_section="Workflow",
        original_text_reference="SRC-001 section 1, chunk 1",
        observed_at="2026-08-28T00:00:00+00:00",
        derivation=SourceDerivation.SOURCE_DERIVED,
    )


def knowledge_item(item_id: str = "ITEM-1", content: str = "Use provenance for every knowledge item.") -> KnowledgeItem:
    prov = provenance()
    return KnowledgeItem(
        id=item_id,
        type=KnowledgeType.PROCEDURE,
        title="Provenance rule",
        content=content,
        summary=content,
        source_id="SRC-001",
        source_location=prov.source_location,
        source_type="User-provided source",
        domain="engineering",
        topics=("provenance",),
        project="ADE",
        created_at="2026-08-28T00:00:00+00:00",
        observed_at=prov.observed_at,
        updated_at=prov.observed_at,
        version=None,
        status=KnowledgeStatus.EXTRACTED,
        freshness=Freshness.UNKNOWN,
        confidence=Confidence(evidence_confidence=0.6, recommendation_score=0.1),
        provenance=prov,
    )


def test_source_and_knowledge_require_provenance_and_no_secrets():
    Source(
        source_id="SRC-001",
        original_filename="frontier.txt",
        source_type="TXT",
        origin="User-provided zip corpus",
        location="raw-corpus/frontier.txt",
        authority="user_provided",
        processing_status=KnowledgeStatus.EXTRACTED,
    )
    with pytest.raises(KnowledgeCoreError, match="secret"):
        knowledge_item(content="api_key = 'sk-abcdefghijklmnopqrstuvwxyz123456'")


def test_confidence_fields_are_independent():
    confidence = Confidence(evidence_confidence=0.95, recommendation_score=0.2)
    assert confidence.evidence_confidence == 0.95
    assert confidence.recommendation_score == 0.2
    with pytest.raises(KnowledgeCoreError):
        Confidence(evidence_confidence=1.2, recommendation_score=0.2)


def test_lifecycle_transitions_are_guarded():
    item = knowledge_item()
    assert item.transition(KnowledgeStatus.NORMALIZED).status == KnowledgeStatus.NORMALIZED
    with pytest.raises(KnowledgeCoreError, match="invalid lifecycle transition"):
        ensure_transition(KnowledgeStatus.RAW, KnowledgeStatus.INDEXED)


def test_repository_filters_duplicates_and_supersedes():
    repo = InMemoryKnowledgeRepository()
    first = repo.create(knowledge_item("ITEM-1", "Preserve source references during normalization.").transition(KnowledgeStatus.NORMALIZED).transition(KnowledgeStatus.VALIDATED))
    repo.create(knowledge_item("ITEM-2", "Preserve source references during normalization."))
    assert repo.duplicates
    replacement = knowledge_item("ITEM-3", "Preserve source references and timestamps during normalization.").transition(KnowledgeStatus.NORMALIZED)
    replacement = replacement.transition(KnowledgeStatus.VALIDATED)
    old, new = repo.supersede(first.id, replacement)
    assert old.status == KnowledgeStatus.SUPERSEDED
    assert old.superseded_by == new.id


def test_retrieval_filters_and_context_packets_and_backend_boundaries():
    repo = InMemoryKnowledgeRepository()
    repo.create(knowledge_item("ITEM-1", "Use keyword retrieval for local test backends."))
    retrieval = RetrievalInterface(repo)
    assert retrieval.keyword_search("keyword")[0].id == "ITEM-1"
    packets = retrieval.retrieve_context(KnowledgeSearchQuery(query="keyword"))
    assert packets[0]["SOURCE"] == "SRC-001"
    with pytest.raises(UnsupportedBackendError):
        retrieval.semantic_search("keyword")


def test_graph_interface_preserves_relationships():
    graph = InMemoryGraph()
    graph.create_entity(Entity(entity_id="ENT-1", entity_type="Source", name="SRC-001", provenance=provenance()))
    graph.create_entity(Entity(entity_id="ENT-2", entity_type="Skill", name="system-breaker", provenance=provenance()))
    rel = graph.create_relationship(Relationship(relationship_id="REL-1", from_entity="ENT-1", to_entity="ENT-2", relationship_type="supports", provenance=provenance()))
    assert graph.find_related("ENT-1") == [rel]
    with pytest.raises(KnowledgeCoreError):
        graph.create_relationship(Relationship(relationship_id="REL-2", from_entity="ENT-1", to_entity="MISSING", relationship_type="supports"))


def test_memory_store_is_separate_from_knowledge_repository():
    store = MemoryStore()
    record = store.create(MemoryRecord(memory_id="MEM-1", category=MemoryCategory.PROJECT, content="ADE avoids provider lock-in.", scope="ADE", provenance=provenance()))
    assert store.list(category=MemoryCategory.PROJECT) == [record]
    assert InMemoryKnowledgeRepository().list() == []


def test_importer_validates_malformed_missing_provenance_and_unsupported(tmp_path: Path):
    path = tmp_path / "items.jsonl"
    good = dict(FIXTURE_RECORD)
    missing = dict(FIXTURE_RECORD)
    del missing["source_location"]
    unsupported = dict(FIXTURE_RECORD, item_id="ITEM-TEST-002", content_type="Unknown type")
    path.write_text("\n".join(json.dumps(row) for row in (good, missing, unsupported)) + "\n", encoding="utf-8")
    importer = CorpusImporter()
    report = importer.import_jsonl(path)
    assert report.records_processed == 3
    assert report.records_accepted == 1
    assert report.records_rejected == 2
    assert report.missing_provenance == 1
    assert report.unsupported_records == 1
    assert report.research_candidates == 1
    assert importer.repository.conflicts


def test_import_existing_phase_2_1_extraction_fixture_if_present():
    corpus = Path(__file__).resolve().parents[1] / "docs" / "knowledge" / "ADE-EXTRACTED-ITEMS.jsonl"
    if not corpus.exists():
        pytest.skip("Phase 2.1 extraction fixture not present")
    candidates, report = import_research_candidates_from_extraction(corpus)
    assert report.records_processed == 314
    assert report.records_accepted == 314
    assert report.records_rejected == 0
    assert len(candidates) == 217


def test_stable_identifier_is_repeatable():
    assert stable_id("TEST", "SRC-1", "same") == stable_id("TEST", "SRC-1", "same")
