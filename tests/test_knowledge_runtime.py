from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pytest

from skill_ecosystem.knowledge_core import (
    AccessScope,
    Confidence,
    ConflictRecord,
    Freshness,
    InMemoryKnowledgeRepository,
    KnowledgeCoreError,
    KnowledgeItem,
    KnowledgeStatus,
    KnowledgeType,
    Provenance,
    SourceDerivation,
)
from skill_ecosystem.knowledge_runtime import (
    GovernanceReranker,
    KnowledgeRetrievalRuntime,
    Principal,
    PrototypeFullTextProvider,
    PrototypeStructuredStore,
    PrototypeVectorProvider,
    RuntimeQuery,
    evaluate_runtime,
    load_phase_2_5_runtime,
)


def provenance(source_id: str = "SRC-TEST", derivation: SourceDerivation = SourceDerivation.SOURCE_DERIVED) -> Provenance:
    return Provenance(
        source_id=source_id,
        source_location=f"raw-corpus/text-dumps/{source_id}.txt",
        source_section="Runtime fixture",
        original_text_reference=f"{source_id} section 1 chunk 1",
        observed_at="2026-08-28T00:00:00+00:00",
        derivation=derivation,
    )


def item(
    item_id: str,
    content: str,
    *,
    source_id: str = "SRC-TEST",
    knowledge_type: KnowledgeType = KnowledgeType.PROCEDURE,
    access_scope: AccessScope = AccessScope.GLOBAL,
    project: str = "ADE",
    freshness: Freshness = Freshness.UNKNOWN,
    status: KnowledgeStatus = KnowledgeStatus.EXTRACTED,
    derivation: SourceDerivation = SourceDerivation.SOURCE_DERIVED,
    valid_from: str | None = None,
    valid_until: str | None = None,
) -> KnowledgeItem:
    prov = provenance(source_id, derivation)
    return KnowledgeItem(
        id=item_id,
        type=knowledge_type,
        title=f"Runtime item {item_id}",
        content=content,
        summary=content,
        source_id=source_id,
        source_location=prov.source_location,
        source_type="User-provided source",
        domain="engineering",
        topics=("runtime", "retrieval"),
        project=project,
        created_at=prov.observed_at,
        observed_at=prov.observed_at,
        updated_at=prov.observed_at,
        version=None,
        status=status,
        freshness=freshness,
        confidence=Confidence(evidence_confidence=0.7, recommendation_score=0.1),
        provenance=prov,
        valid_from=valid_from,
        valid_until=valid_until,
        access_scope=access_scope,
    )


def runtime_for(repo: InMemoryKnowledgeRepository) -> KnowledgeRetrievalRuntime:
    return KnowledgeRetrievalRuntime(
        PrototypeStructuredStore(repo),
        PrototypeFullTextProvider(),
        PrototypeVectorProvider(),
        GovernanceReranker(),
    )


def test_runtime_returns_explainable_context_packet_with_provenance():
    repo = InMemoryKnowledgeRepository()
    repo.create(item("ITEM-1", "Use provenance access filters and explainable context packets."))
    packet = runtime_for(repo).retrieve(RuntimeQuery("provenance context", limit=1))
    assert packet.metrics["candidate_count"] == 1
    result = packet.results[0]
    assert result.source_id == "SRC-TEST"
    assert result.source_location.endswith("SRC-TEST.txt")
    assert result.original_text_reference == "SRC-TEST section 1 chunk 1"
    assert result.why_retrieved
    assert result.providers
    assert "not_validated" in result.warnings


def test_access_boundaries_prevent_global_project_and_restricted_leakage():
    repo = InMemoryKnowledgeRepository()
    repo.create(item("ITEM-GLOBAL", "global checkout verification rule"))
    repo.create(item("ITEM-PROJECT", "client alpha checkout verification rule", access_scope=AccessScope.PROJECT, project="Client Alpha"))
    repo.create(item("ITEM-RESTRICTED", "restricted checkout verification rule", access_scope=AccessScope.RESTRICTED))
    runtime = runtime_for(repo)

    global_packet = runtime.retrieve(RuntimeQuery("checkout verification", limit=10))
    assert [result.item_id for result in global_packet.results] == ["ITEM-GLOBAL"]

    project_packet = runtime.retrieve(RuntimeQuery(
        "checkout verification",
        project="Client Alpha",
        principal=Principal("engineer", projects=("Client Alpha",), access_scopes=(AccessScope.GLOBAL, AccessScope.PROJECT)),
        limit=10,
    ))
    assert [result.item_id for result in project_packet.results] == ["ITEM-PROJECT"]

    restricted_packet = runtime.retrieve(RuntimeQuery(
        "restricted checkout",
        principal=Principal("reviewer", access_scopes=(AccessScope.GLOBAL, AccessScope.RESTRICTED)),
        limit=10,
    ))
    assert [result.item_id for result in restricted_packet.results] == ["ITEM-RESTRICTED", "ITEM-GLOBAL"]


def test_stale_and_temporal_filters_are_enforced_before_retrieval():
    repo = InMemoryKnowledgeRepository()
    repo.create(item("ITEM-CURRENT", "framework guidance current", freshness=Freshness.CURRENT, valid_from="2026-01-01"))
    repo.create(item("ITEM-STALE", "framework guidance stale", freshness=Freshness.STALE, valid_until="2024-01-01"))
    runtime = runtime_for(repo)

    packet = runtime.retrieve(RuntimeQuery("framework guidance", limit=10))
    assert [result.item_id for result in packet.results] == ["ITEM-CURRENT"]

    stale_packet = runtime.retrieve(RuntimeQuery("framework guidance", include_stale=True, as_of="2023-01-01", limit=10))
    assert {result.item_id for result in stale_packet.results} == {"ITEM-STALE"}
    assert any("freshness=stale" in result.warnings for result in stale_packet.results)


def test_conflicting_sources_are_preserved_in_explanation():
    repo = InMemoryKnowledgeRepository()
    first = repo.create(item("ITEM-A", "use tool alpha for retrieval", source_id="SRC-A"))
    repo.create(item("ITEM-B", "do not use tool alpha for retrieval", source_id="SRC-B"))
    repo.conflicts.append(ConflictRecord("CONFLICT-1", first.id, "ITEM-B", "SRC-A", "SRC-B"))
    packet = runtime_for(repo).retrieve(RuntimeQuery("tool alpha retrieval", limit=1))
    assert packet.results[0].conflicts == ("CONFLICT-1",)


def test_ai_inference_stays_labeled_and_cannot_be_fact():
    with pytest.raises(KnowledgeCoreError):
        item("ITEM-BAD", "AI inferred objective fact", knowledge_type=KnowledgeType.FACT, derivation=SourceDerivation.AI_INFERRED)
    repo = InMemoryKnowledgeRepository()
    repo.create(item("ITEM-AI", "AI inferred retrieval recommendation", knowledge_type=KnowledgeType.AI_INFERENCE, derivation=SourceDerivation.AI_INFERRED))
    packet = runtime_for(repo).retrieve(RuntimeQuery("inferred retrieval", limit=1, rerank=True))
    assert packet.results[0].derivation == SourceDerivation.AI_INFERRED.value
    assert "ai_inference_not_authoritative_fact" in packet.results[0].warnings


def test_duplicate_information_is_not_silently_collapsed():
    repo = InMemoryKnowledgeRepository()
    repo.create(item("ITEM-DUP-1", "Preserve provenance source references during normalization."))
    repo.create(item("ITEM-DUP-2", "Preserve provenance source references during normalization."))
    packet = runtime_for(repo).retrieve(RuntimeQuery("provenance source references normalization", limit=10))
    assert repo.duplicates
    assert {result.item_id for result in packet.results} == {"ITEM-DUP-1", "ITEM-DUP-2"}


def test_source_revocation_removes_items_from_default_retrieval():
    repo = InMemoryKnowledgeRepository()
    repo.create(item("ITEM-REVOKE", "revoked source retrieval contract", source_id="SRC-REVOKE"))
    store = PrototypeStructuredStore(repo)
    runtime = KnowledgeRetrievalRuntime(store, PrototypeFullTextProvider(), PrototypeVectorProvider())
    assert runtime.retrieve(RuntimeQuery("revoked source", limit=5)).results
    store.archive_source("SRC-REVOKE")
    assert runtime.retrieve(RuntimeQuery("revoked source", limit=5)).results == ()


def test_phase_2_5_runtime_metrics_against_existing_corpus():
    corpus = Path(__file__).resolve().parents[1] / "docs" / "knowledge" / "ADE-EXTRACTED-ITEMS.jsonl"
    runtime = load_phase_2_5_runtime(corpus)
    metrics = evaluate_runtime(runtime)
    assert metrics["avg_term_recall"] >= 0.85
    assert len(metrics["queries"]) == 8
