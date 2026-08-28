"""Non-production ADE knowledge retrieval runtime prototype.

This module proves the Phase 2.4 architecture contract locally without starting
PostgreSQL, pgvector, a production embedding migration, Hermes, or any crawler.
Provider-specific behavior stays behind small interfaces so a later production
adapter can swap in real infrastructure.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
import hashlib
import json
import math
import re
import time
from pathlib import Path
from typing import Iterable, Protocol

from .knowledge_core import (
    AccessScope,
    ConflictRecord,
    CorpusImporter,
    Freshness,
    InMemoryKnowledgeRepository,
    KnowledgeItem,
    KnowledgeSearchQuery,
    KnowledgeStatus,
    KnowledgeType,
    SourceDerivation,
)
from .knowledge_runtime_benchmark import QUERIES


TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def tokenize(text: str) -> tuple[str, ...]:
    return tuple(match.group(0).casefold() for match in TOKEN_RE.finditer(text))


@dataclass(frozen=True)
class Principal:
    """Retrieval caller context for ACL and project filtering."""

    principal_id: str
    projects: tuple[str, ...] = ()
    access_scopes: tuple[AccessScope, ...] = (AccessScope.GLOBAL,)


@dataclass(frozen=True)
class RuntimeQuery:
    text: str
    principal: Principal = field(default_factory=lambda: Principal("anonymous"))
    project: str | None = None
    freshness: Freshness | None = None
    knowledge_type: KnowledgeType | None = None
    as_of: str | None = None
    include_stale: bool = False
    include_conflicts: bool = True
    include_archived: bool = False
    min_evidence_confidence: float | None = None
    version: str | None = None
    limit: int = 5
    rerank: bool = False


@dataclass(frozen=True)
class RetrievalHit:
    item: KnowledgeItem
    score: float
    provider: str
    rank: int
    reason: str


@dataclass(frozen=True)
class ExplainableResult:
    item_id: str
    title: str
    claim: str
    source_id: str
    source_location: str
    source_section: str
    original_text_reference: str
    content_type: str
    status: str
    freshness: str
    access_scope: str
    project: str
    derivation: str
    evidence_confidence: float
    recommendation_score: float
    providers: tuple[str, ...]
    score: float
    why_retrieved: str
    conflicts: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class ContextPacket:
    query: str
    generated_at_ms: float
    results: tuple[ExplainableResult, ...]
    metrics: dict[str, float | int]
    filters: dict[str, str | bool | None]


@dataclass(frozen=True)
class SourceManifestRecord:
    source_id: str
    original_filename: str
    source_type: str
    raw_location: str
    text_dump: str
    hash_sha256: str
    origin: str
    extraction_status: str
    extracted_items: int = 0


@dataclass(frozen=True)
class SourceIntegrityResult:
    source_count: int
    missing_raw_files: int
    missing_text_dumps: int
    hash_mismatches: int
    missing_inputs: int
    input_hash_mismatches: int


class SourceRepository(Protocol):
    def get_source(self, source_id: str) -> SourceManifestRecord | None: ...
    def list_sources(self) -> list[SourceManifestRecord]: ...
    def item_source_exists(self, source_id: str) -> bool: ...
    def verify_integrity(self) -> SourceIntegrityResult: ...


class JsonManifestSourceRepository:
    """Read-only source repository backed by ADE-SOURCE-RECORDS.json."""

    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.knowledge_root = repository_root / "docs" / "knowledge"
        self.manifest_path = self.knowledge_root / "ADE-SOURCE-RECORDS.json"
        self.items_path = self.knowledge_root / "ADE-EXTRACTED-ITEMS.jsonl"
        self._manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self._item_counts = self._load_item_counts()

    def get_source(self, source_id: str) -> SourceManifestRecord | None:
        for source in self._manifest.get("sources", []):
            if source.get("source_id") == source_id:
                return self._record(source)
        return None

    def list_sources(self) -> list[SourceManifestRecord]:
        return [self._record(source) for source in self._manifest.get("sources", [])]

    def item_source_exists(self, source_id: str) -> bool:
        return self.get_source(source_id) is not None

    def verify_integrity(self) -> SourceIntegrityResult:
        missing_raw = 0
        missing_dump = 0
        mismatches = 0
        for source in self._manifest.get("sources", []):
            raw = self.knowledge_root / source["raw_location"]
            dump = self.knowledge_root / source["text_dump"]
            if not raw.exists():
                missing_raw += 1
            elif _sha256(raw) != source.get("hash_sha256"):
                mismatches += 1
            if not dump.exists():
                missing_dump += 1
        missing_inputs = 0
        input_mismatches = 0
        input_specs = []
        if self._manifest.get("preserved_zip"):
            input_specs.append((self._manifest["preserved_zip"], self._manifest.get("zip_sha256")))
        for batch in self._manifest.get("batches", []):
            for input_spec in batch.get("inputs", []):
                input_specs.append((input_spec.get("preserved"), input_spec.get("sha256")))
        for preserved, expected_hash in input_specs:
            path = self.knowledge_root / preserved
            if not path.exists():
                missing_inputs += 1
            elif expected_hash and _sha256(path) != expected_hash:
                input_mismatches += 1
        return SourceIntegrityResult(
            source_count=len(self._manifest.get("sources", [])),
            missing_raw_files=missing_raw,
            missing_text_dumps=missing_dump,
            hash_mismatches=mismatches,
            missing_inputs=missing_inputs,
            input_hash_mismatches=input_mismatches,
        )

    def _record(self, source: dict[str, object]) -> SourceManifestRecord:
        source_id = str(source["source_id"])
        return SourceManifestRecord(
            source_id=source_id,
            original_filename=str(source.get("original_filename", "")),
            source_type=str(source.get("source_type", "")),
            raw_location=str(source.get("raw_location", "")),
            text_dump=str(source.get("text_dump", "")),
            hash_sha256=str(source.get("hash_sha256", "")),
            origin=str(source.get("origin", "")),
            extraction_status=str(source.get("extraction_status", "")),
            extracted_items=self._item_counts.get(source_id, 0),
        )

    def _load_item_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        with self.items_path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    record = json.loads(line)
                    source_id = str(record.get("source_id", ""))
                    counts[source_id] = counts.get(source_id, 0) + 1
        return counts


class StructuredStore(Protocol):
    def search(self, query: KnowledgeSearchQuery) -> list[KnowledgeItem]: ...
    def list(self) -> list[KnowledgeItem]: ...
    def conflicts_for(self, item_id: str) -> list[ConflictRecord]: ...
    def archive_source(self, source_id: str) -> list[KnowledgeItem]: ...


class FullTextProvider(Protocol):
    name: str
    def search(self, query: RuntimeQuery, items: Iterable[KnowledgeItem]) -> list[RetrievalHit]: ...


class VectorProvider(Protocol):
    name: str
    def search(self, query: RuntimeQuery, items: Iterable[KnowledgeItem]) -> list[RetrievalHit]: ...


class Reranker(Protocol):
    name: str
    def rerank(self, query: RuntimeQuery, hits: list[RetrievalHit]) -> list[RetrievalHit]: ...


class PrototypeStructuredStore:
    """PostgreSQL-shaped store contract backed by the existing in-memory repo."""

    def __init__(self, repository: InMemoryKnowledgeRepository) -> None:
        self.repository = repository

    def search(self, query: KnowledgeSearchQuery) -> list[KnowledgeItem]:
        return self.repository.search(query)

    def list(self) -> list[KnowledgeItem]:
        return self.repository.list()

    def conflicts_for(self, item_id: str) -> list[ConflictRecord]:
        return [
            conflict for conflict in self.repository.conflicts
            if conflict.claim_a == item_id or conflict.claim_b == item_id
        ]

    def archive_source(self, source_id: str) -> list[KnowledgeItem]:
        return self.repository.archive_source(source_id)


class PrototypeFullTextProvider:
    """PostgreSQL FTS-shaped lexical provider using deterministic token scoring."""

    name = "prototype_postgres_fts"

    def search(self, query: RuntimeQuery, items: Iterable[KnowledgeItem]) -> list[RetrievalHit]:
        query_terms = set(tokenize(query.text))
        hits: list[RetrievalHit] = []
        for item in items:
            terms = tokenize(_searchable_text(item))
            counts = Counter(terms)
            overlap = sum(1 for term in query_terms if counts[term])
            if not overlap:
                continue
            score = overlap + math.log1p(sum(counts[term] for term in query_terms))
            hits.append(RetrievalHit(item, score, self.name, 0, "lexical token overlap over governed candidate set"))
        return _rank(hits)


class PrototypeVectorProvider:
    """pgvector-shaped provider using local hashed token vectors, not embeddings."""

    name = "prototype_pgvector_hash"

    def __init__(self, dimensions: int = 96, min_score: float = 0.25) -> None:
        self.dimensions = dimensions
        self.min_score = min_score

    def search(self, query: RuntimeQuery, items: Iterable[KnowledgeItem]) -> list[RetrievalHit]:
        query_vec = _hashed_vector(query.text, self.dimensions)
        hits: list[RetrievalHit] = []
        for item in items:
            score = _cosine(query_vec, _hashed_vector(_searchable_text(item), self.dimensions))
            if score < self.min_score:
                continue
            hits.append(RetrievalHit(item, score, self.name, 0, "hashed-vector similarity over governed candidate set"))
        return _rank(hits)


class GovernanceReranker:
    """Optional post-fusion reranker that promotes governed, fresher evidence."""

    name = "governance_reranker"

    def rerank(self, query: RuntimeQuery, hits: list[RetrievalHit]) -> list[RetrievalHit]:
        adjusted: list[RetrievalHit] = []
        for hit in hits:
            item = hit.item
            score = hit.score
            if item.freshness == Freshness.STALE:
                score -= 0.25
            if item.provenance.derivation in {SourceDerivation.AI_INFERRED, SourceDerivation.AI_SYNTHESIZED}:
                score -= 0.2
            if item.status == KnowledgeStatus.VALIDATED:
                score += 0.15
            adjusted.append(RetrievalHit(item, score, self.name, hit.rank, f"{hit.reason}; governance rerank applied"))
        return _rank(adjusted)


class KnowledgeRetrievalRuntime:
    """End-to-end non-production retrieval runtime."""

    def __init__(
        self,
        store: StructuredStore,
        full_text: FullTextProvider,
        vector: VectorProvider,
        reranker: Reranker | None = None,
        source_repository: SourceRepository | None = None,
    ) -> None:
        self.store = store
        self.full_text = full_text
        self.vector = vector
        self.reranker = reranker
        self.source_repository = source_repository

    def retrieve(self, query: RuntimeQuery) -> ContextPacket:
        started = time.perf_counter()
        candidates = self._governed_candidates(query)
        fts_hits = self.full_text.search(query, candidates)
        vector_hits = self.vector.search(query, candidates)
        fused = _fuse_rrf((fts_hits, vector_hits))
        if query.rerank and self.reranker:
            fused = self.reranker.rerank(query, fused)
        results = tuple(self._explain(query, hit) for hit in fused[: query.limit])
        elapsed_ms = (time.perf_counter() - started) * 1000
        metrics = {
            "candidate_count": len(candidates),
            "fts_hits": len(fts_hits),
            "vector_hits": len(vector_hits),
            "fused_hits": len(fused),
            "result_count": len(results),
            "elapsed_ms": round(elapsed_ms, 3),
        }
        return ContextPacket(
            query=query.text,
            generated_at_ms=round(elapsed_ms, 3),
            results=results,
            metrics=metrics,
            filters={
                "project": query.project,
                "freshness": query.freshness.value if query.freshness else None,
                "include_stale": query.include_stale,
                "include_archived": query.include_archived,
                "min_evidence_confidence": query.min_evidence_confidence,
                "version": query.version,
                "knowledge_type": query.knowledge_type.value if query.knowledge_type else None,
            },
        )

    def _governed_candidates(self, query: RuntimeQuery) -> list[KnowledgeItem]:
        filtered: list[KnowledgeItem] = []
        for item in self.store.list():
            if not query.include_archived and item.status in {KnowledgeStatus.ARCHIVED, KnowledgeStatus.SUPERSEDED}:
                continue
            if query.project and item.project != query.project:
                continue
            if query.freshness and item.freshness != query.freshness:
                continue
            if query.knowledge_type and item.type != query.knowledge_type:
                continue
            if query.min_evidence_confidence is not None and item.evidence_confidence < query.min_evidence_confidence:
                continue
            if query.version and item.version != query.version:
                continue
            if item.access_scope not in query.principal.access_scopes:
                if not (item.access_scope == AccessScope.PROJECT and item.project in query.principal.projects):
                    continue
            if item.access_scope == AccessScope.PROJECT and item.project not in query.principal.projects:
                continue
            if not query.include_stale and item.freshness == Freshness.STALE:
                continue
            if query.as_of and item.valid_from and item.valid_from > query.as_of:
                continue
            if query.as_of and item.valid_until and item.valid_until < query.as_of:
                continue
            filtered.append(item)
        return filtered

    def _explain(self, query: RuntimeQuery, hit: RetrievalHit) -> ExplainableResult:
        item = hit.item
        conflicts = tuple(conflict.conflict_id for conflict in self.store.conflicts_for(item.id)) if query.include_conflicts else ()
        warnings: list[str] = []
        if item.freshness in {Freshness.STALE, Freshness.STALE_RISK, Freshness.TIME_SENSITIVE}:
            warnings.append(f"freshness={item.freshness.value}")
        if item.provenance.derivation in {SourceDerivation.AI_INFERRED, SourceDerivation.AI_SYNTHESIZED}:
            warnings.append("ai_inference_not_authoritative_fact")
        if item.status not in {KnowledgeStatus.VALIDATED, KnowledgeStatus.INDEXED}:
            warnings.append("not_validated")
        if item.type in {KnowledgeType.PROMPT, KnowledgeType.INSTRUCTION}:
            warnings.append("source_content_not_agent_instruction")
        if self.source_repository and not self.source_repository.item_source_exists(item.source_id):
            warnings.append("source_record_missing")
        return ExplainableResult(
            item_id=item.id,
            title=item.title,
            claim=item.summary,
            source_id=item.source_id,
            source_location=item.source_location,
            source_section=item.provenance.source_section,
            original_text_reference=item.provenance.original_text_reference,
            content_type=item.type.value,
            status=item.status.value,
            freshness=item.freshness.value,
            access_scope=item.access_scope.value,
            project=item.project,
            derivation=item.provenance.derivation.value,
            evidence_confidence=item.evidence_confidence,
            recommendation_score=item.recommendation_score,
            providers=(hit.provider,),
            score=round(hit.score, 6),
            why_retrieved=hit.reason,
            conflicts=conflicts,
            warnings=tuple(warnings),
        )


def load_phase_2_5_runtime(corpus: Path) -> KnowledgeRetrievalRuntime:
    importer = CorpusImporter()
    report = importer.import_jsonl(corpus)
    if report.records_accepted != 932:
        raise RuntimeError(f"Phase 2.5 expects the 932-item staging corpus, got {report.records_accepted}")
    return KnowledgeRetrievalRuntime(
        PrototypeStructuredStore(importer.repository),
        PrototypeFullTextProvider(),
        PrototypeVectorProvider(),
        GovernanceReranker(),
        JsonManifestSourceRepository(corpus.resolve().parents[2]),
    )


def evaluate_runtime(runtime: KnowledgeRetrievalRuntime) -> dict[str, object]:
    query_results = []
    for benchmark_query in QUERIES:
        packet = runtime.retrieve(RuntimeQuery(benchmark_query.text, limit=10, rerank=True))
        combined = " ".join(
            " ".join((result.title, result.claim, result.source_id, result.source_location, result.content_type, result.why_retrieved))
            for result in packet.results
        ).casefold()
        matched_terms = [term for term in benchmark_query.expected_terms if term.casefold() in combined]
        term_recall = len(matched_terms) / max(len(benchmark_query.expected_terms), 1)
        query_results.append({
            "query_id": benchmark_query.id,
            "result_count": len(packet.results),
            "term_recall": round(term_recall, 3),
            "matched_terms": matched_terms,
            "elapsed_ms": packet.metrics["elapsed_ms"],
        })
    return {
        "schema_version": 1,
        "runtime": "phase_2_5_non_production_provider_neutral",
        "queries": query_results,
        "avg_term_recall": round(sum(row["term_recall"] for row in query_results) / len(query_results), 3),
    }


def _searchable_text(item: KnowledgeItem) -> str:
    return " ".join((item.title, item.content, item.summary, item.source_id, item.source_location, item.domain, item.project, *item.topics))


def _hashed_vector(text: str, dimensions: int) -> tuple[float, ...]:
    values = [0.0] * dimensions
    for token in tokenize(text):
        values[int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16) % dimensions] += 1.0
    norm = math.sqrt(sum(value * value for value in values))
    if norm == 0:
        return tuple(values)
    return tuple(value / norm for value in values)


def _cosine(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    return sum(a * b for a, b in zip(left, right, strict=False))


def _rank(hits: list[RetrievalHit]) -> list[RetrievalHit]:
    ranked = sorted(hits, key=lambda hit: (hit.score, hit.item.evidence_confidence, hit.item.id), reverse=True)
    return [RetrievalHit(hit.item, hit.score, hit.provider, rank, hit.reason) for rank, hit in enumerate(ranked, start=1)]


def _fuse_rrf(rankings: Iterable[list[RetrievalHit]], k: int = 60) -> list[RetrievalHit]:
    scores: dict[str, float] = {}
    items: dict[str, KnowledgeItem] = {}
    providers: dict[str, list[str]] = {}
    reasons: dict[str, list[str]] = {}
    for ranking in rankings:
        for rank, hit in enumerate(ranking, start=1):
            item_id = hit.item.id
            scores[item_id] = scores.get(item_id, 0.0) + 1.0 / (k + rank)
            items[item_id] = hit.item
            providers.setdefault(item_id, []).append(hit.provider)
            reasons.setdefault(item_id, []).append(hit.reason)
    fused = [
        RetrievalHit(items[item_id], score, "+".join(sorted(set(providers[item_id]))), 0, "; ".join(sorted(set(reasons[item_id]))))
        for item_id, score in scores.items()
    ]
    return _rank(fused)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
