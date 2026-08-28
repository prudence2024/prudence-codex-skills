"""Provider-agnostic ADE knowledge core models, interfaces, and importers."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import StrEnum
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable, Protocol


class KnowledgeCoreError(ValueError):
    """Raised when a knowledge-core object or transition is invalid."""


class UnsupportedBackendError(NotImplementedError):
    """Raised when an interface exists but no backend has been implemented."""


class KnowledgeStatus(StrEnum):
    RAW = "RAW"
    EXTRACTED = "EXTRACTED"
    NORMALIZED = "NORMALIZED"
    CANDIDATE = "CANDIDATE"
    VALIDATED = "VALIDATED"
    INDEXED = "INDEXED"
    SUPERSEDED = "SUPERSEDED"
    ARCHIVED = "ARCHIVED"


LEGAL_TRANSITIONS: dict[KnowledgeStatus, set[KnowledgeStatus]] = {
    KnowledgeStatus.RAW: {KnowledgeStatus.EXTRACTED, KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.EXTRACTED: {KnowledgeStatus.NORMALIZED, KnowledgeStatus.CANDIDATE, KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.NORMALIZED: {KnowledgeStatus.CANDIDATE, KnowledgeStatus.VALIDATED, KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.CANDIDATE: {KnowledgeStatus.VALIDATED, KnowledgeStatus.SUPERSEDED, KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.VALIDATED: {KnowledgeStatus.INDEXED, KnowledgeStatus.SUPERSEDED, KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.INDEXED: {KnowledgeStatus.SUPERSEDED, KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.SUPERSEDED: {KnowledgeStatus.ARCHIVED},
    KnowledgeStatus.ARCHIVED: set(),
}


class Freshness(StrEnum):
    CURRENT = "current"
    TIME_SENSITIVE = "time_sensitive"
    STALE_RISK = "stale_risk"
    STALE = "stale"
    UNKNOWN = "unknown"


class KnowledgeType(StrEnum):
    FACT = "fact"
    CONCEPT = "concept"
    PROCEDURE = "procedure"
    PATTERN = "pattern"
    DECISION = "decision"
    OBSERVATION = "observation"
    HYPOTHESIS = "hypothesis"
    RESEARCH_FINDING = "research_finding"
    PROMPT = "prompt"
    INSTRUCTION = "instruction"
    RECOMMENDATION = "recommendation"
    PREFERENCE = "preference"
    PROJECT_KNOWLEDGE = "project_knowledge"
    EXTERNAL_KNOWLEDGE = "external_knowledge"
    AI_INFERENCE = "ai_inference"
    UNKNOWN = "unknown"


class SourceDerivation(StrEnum):
    SOURCE_DERIVED = "SOURCE_DERIVED"
    USER_PROVIDED = "USER_PROVIDED"
    EXPERIMENTAL = "EXPERIMENTAL"
    RESEARCH_DERIVED = "RESEARCH_DERIVED"
    AI_INFERRED = "AI_INFERRED"
    AI_SYNTHESIZED = "AI_SYNTHESIZED"


class AccessScope(StrEnum):
    GLOBAL = "global"
    PROJECT = "project"
    PRIVATE = "private"
    RESTRICTED = "restricted"


class MemoryCategory(StrEnum):
    PROJECT = "project_memory"
    DECISION = "decision_memory"
    WORKFLOW = "workflow_memory"
    PREFERENCE = "preference_memory"
    HISTORICAL_STATE = "historical_state"


SECRET_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"(?i)sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"(?i)pk_(live|test)_[A-Za-z0-9_\-]{20,}"),
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256("\u241f".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


def contains_secret(value: str) -> bool:
    return any(pattern.search(value) for pattern in SECRET_PATTERNS)


def require_text(name: str, value: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise KnowledgeCoreError(f"{name} is required")


def ensure_no_secret(name: str, value: str) -> None:
    if contains_secret(value):
        raise KnowledgeCoreError(f"{name} appears to contain a secret and cannot be imported")


def ensure_transition(current: KnowledgeStatus, target: KnowledgeStatus) -> None:
    if target == current:
        return
    if target not in LEGAL_TRANSITIONS[current]:
        raise KnowledgeCoreError(f"invalid lifecycle transition: {current} -> {target}")


@dataclass(frozen=True)
class Confidence:
    evidence_confidence: float
    recommendation_score: float
    label: str = "contextual"

    def __post_init__(self) -> None:
        for name, value in (("evidence_confidence", self.evidence_confidence), ("recommendation_score", self.recommendation_score)):
            if not 0 <= value <= 1:
                raise KnowledgeCoreError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class Provenance:
    source_id: str
    source_location: str
    source_section: str
    original_text_reference: str
    observed_at: str
    derivation: SourceDerivation = SourceDerivation.SOURCE_DERIVED
    extracted_at: str | None = None
    modified_at: str | None = None
    transformations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        require_text("source_id", self.source_id)
        require_text("source_location", self.source_location)
        require_text("source_section", self.source_section)
        require_text("original_text_reference", self.original_text_reference)
        require_text("observed_at", self.observed_at)


@dataclass(frozen=True)
class Source:
    source_id: str
    original_filename: str
    source_type: str
    origin: str
    location: str
    authority: str
    processing_status: KnowledgeStatus
    date: str | None = None
    version: str | None = None

    def __post_init__(self) -> None:
        for name in ("source_id", "original_filename", "source_type", "origin", "location", "authority"):
            require_text(name, getattr(self, name))


@dataclass(frozen=True)
class KnowledgeItem:
    id: str
    type: KnowledgeType
    title: str
    content: str
    summary: str
    source_id: str
    source_location: str
    source_type: str
    domain: str
    topics: tuple[str, ...]
    project: str
    created_at: str
    observed_at: str
    updated_at: str
    version: str | None
    status: KnowledgeStatus
    freshness: Freshness
    confidence: Confidence
    provenance: Provenance
    valid_from: str | None = None
    valid_until: str | None = None
    superseded_by: str | None = None
    access_scope: AccessScope = AccessScope.GLOBAL

    def __post_init__(self) -> None:
        for name in ("id", "title", "content", "summary", "source_id", "source_location", "source_type", "domain", "project", "created_at", "observed_at", "updated_at"):
            require_text(name, getattr(self, name))
        if not self.topics:
            raise KnowledgeCoreError("topics is required")
        ensure_no_secret("content", self.content)
        if self.provenance.source_id != self.source_id:
            raise KnowledgeCoreError("provenance source_id must match knowledge source_id")
        if self.type == KnowledgeType.FACT and self.provenance.derivation in {SourceDerivation.AI_INFERRED, SourceDerivation.AI_SYNTHESIZED}:
            raise KnowledgeCoreError("AI-derived information cannot be created as objective fact without validation")

    @property
    def evidence_confidence(self) -> float:
        return self.confidence.evidence_confidence

    @property
    def recommendation_score(self) -> float:
        return self.confidence.recommendation_score

    def transition(self, target: KnowledgeStatus, *, updated_at: str | None = None) -> "KnowledgeItem":
        ensure_transition(self.status, target)
        return replace(self, status=target, updated_at=updated_at or utc_now())

@dataclass(frozen=True)
class PromptRecord:
    prompt_id: str
    source_id: str
    source_location: str
    purpose: str
    category: str
    content_reference: str
    inputs: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    quality_notes: str = ""

    def __post_init__(self) -> None:
        for name in ("prompt_id", "source_id", "source_location", "purpose", "category", "content_reference"):
            require_text(name, getattr(self, name))


@dataclass(frozen=True)
class OperationalInstruction:
    instruction_id: str
    source_id: str
    purpose: str
    trigger: str
    preconditions: tuple[str, ...]
    steps: tuple[str, ...]
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    failure_conditions: tuple[str, ...]
    verification: tuple[str, ...]

    def __post_init__(self) -> None:
        for name in ("instruction_id", "source_id", "purpose", "trigger"):
            require_text(name, getattr(self, name))
        if not self.steps:
            raise KnowledgeCoreError("steps is required")


@dataclass(frozen=True)
class SkillCandidate:
    skill_candidate_id: str
    name: str
    purpose: str
    trigger: str
    inputs: tuple[str, ...]
    workflow: tuple[str, ...]
    outputs: tuple[str, ...]
    dependencies: tuple[str, ...]
    source_evidence: tuple[str, ...]
    overlap: tuple[str, ...]
    confidence: str


@dataclass(frozen=True)
class ResearchCandidate:
    research_id: str
    claim: str
    source_id: str
    reason_for_review: str
    freshness: Freshness
    priority: str
    status: str
    last_checked: str | None
    resolution: str | None
    evidence: tuple[Provenance, ...]

    def __post_init__(self) -> None:
        for name in ("research_id", "claim", "source_id", "reason_for_review", "priority", "status"):
            require_text(name, getattr(self, name))
        if not self.evidence:
            raise KnowledgeCoreError("research candidates require provenance evidence")


@dataclass(frozen=True)
class Project:
    project_id: str
    name: str
    scope: str
    provenance: Provenance | None = None


@dataclass(frozen=True)
class Decision:
    decision_id: str
    title: str
    rationale: str
    status: str
    provenance: Provenance


@dataclass(frozen=True)
class Pattern:
    pattern_id: str
    name: str
    domain: str
    context: str
    evidence: tuple[Provenance, ...]
    confidence: Confidence


@dataclass(frozen=True)
class Entity:
    entity_id: str
    entity_type: str
    name: str
    aliases: tuple[str, ...] = ()
    properties: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)
    observed_at: str = field(default_factory=utc_now)
    provenance: Provenance | None = None
    confidence: Confidence | None = None
    status: KnowledgeStatus = KnowledgeStatus.CANDIDATE


@dataclass(frozen=True)
class Relationship:
    relationship_id: str
    from_entity: str
    to_entity: str
    relationship_type: str
    properties: dict[str, Any] = field(default_factory=dict)
    valid_from: str | None = None
    valid_until: str | None = None
    observed_at: str = field(default_factory=utc_now)
    provenance: Provenance | None = None
    confidence: Confidence | None = None
    status: KnowledgeStatus = KnowledgeStatus.CANDIDATE


@dataclass(frozen=True)
class DuplicateRecord:
    left_id: str
    right_id: str
    relationship_type: str
    reason: str


@dataclass(frozen=True)
class ConflictRecord:
    conflict_id: str
    claim_a: str
    claim_b: str
    source_a: str
    source_b: str
    status: str = "UNRESOLVED"


@dataclass(frozen=True)
class ImportReport:
    records_processed: int = 0
    records_accepted: int = 0
    records_rejected: int = 0
    duplicates: int = 0
    conflicts: int = 0
    missing_provenance: int = 0
    malformed_records: int = 0
    unsupported_records: int = 0
    research_candidates: int = 0
    errors: tuple[str, ...] = ()

    def add_error(self, message: str, *, malformed: bool = False, missing_provenance: bool = False, unsupported: bool = False) -> "ImportReport":
        return replace(
            self,
            records_rejected=self.records_rejected + 1,
            malformed_records=self.malformed_records + (1 if malformed else 0),
            missing_provenance=self.missing_provenance + (1 if missing_provenance else 0),
            unsupported_records=self.unsupported_records + (1 if unsupported else 0),
            errors=(*self.errors, message),
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "records_processed": self.records_processed,
            "records_accepted": self.records_accepted,
            "records_rejected": self.records_rejected,
            "duplicates": self.duplicates,
            "conflicts": self.conflicts,
            "missing_provenance": self.missing_provenance,
            "malformed_records": self.malformed_records,
            "unsupported_records": self.unsupported_records,
            "research_candidates": self.research_candidates,
            "errors": list(self.errors),
        }


@dataclass(frozen=True)
class KnowledgeSearchQuery:
    query: str | None = None
    domain: str | None = None
    topic: str | None = None
    project: str | None = None
    source: str | None = None
    knowledge_type: KnowledgeType | None = None
    status: KnowledgeStatus | None = None
    min_evidence_confidence: float | None = None
    freshness: Freshness | None = None
    access_scope: AccessScope | None = None
    include_archived: bool = False


class KnowledgeRepository(Protocol):
    def create(self, item: KnowledgeItem) -> KnowledgeItem: ...
    def get(self, item_id: str) -> KnowledgeItem | None: ...
    def update(self, item: KnowledgeItem) -> KnowledgeItem: ...
    def delete(self, item_id: str) -> None: ...
    def search(self, query: KnowledgeSearchQuery) -> list[KnowledgeItem]: ...
    def list(self) -> list[KnowledgeItem]: ...
    def supersede(self, old_id: str, new_item: KnowledgeItem) -> tuple[KnowledgeItem, KnowledgeItem]: ...


class InMemoryKnowledgeRepository:
    """Small test backend for schemas and import validation, not production storage."""

    def __init__(self) -> None:
        self._items: dict[str, KnowledgeItem] = {}
        self.duplicates: list[DuplicateRecord] = []
        self.conflicts: list[ConflictRecord] = []

    def create(self, item: KnowledgeItem) -> KnowledgeItem:
        if item.id in self._items:
            raise KnowledgeCoreError(f"knowledge item already exists: {item.id}")
        for existing in self._items.values():
            if _substantial_overlap(existing.content, item.content):
                self.duplicates.append(DuplicateRecord(existing.id, item.id, "OVERLAPPING", "content similarity threshold met"))
        self._items[item.id] = item
        return item

    def get(self, item_id: str) -> KnowledgeItem | None:
        return self._items.get(item_id)

    def update(self, item: KnowledgeItem) -> KnowledgeItem:
        if item.id not in self._items:
            raise KnowledgeCoreError(f"knowledge item does not exist: {item.id}")
        self._items[item.id] = item
        return item

    def delete(self, item_id: str) -> None:
        if item_id in self._items:
            self._items[item_id] = self._items[item_id].transition(KnowledgeStatus.ARCHIVED)

    def list(self) -> list[KnowledgeItem]:
        return list(self._items.values())

    def list_by_source(self, source_id: str) -> list[KnowledgeItem]:
        return [item for item in self._items.values() if item.source_id == source_id]

    def archive_source(self, source_id: str) -> list[KnowledgeItem]:
        archived = []
        for item in self.list_by_source(source_id):
            if item.status != KnowledgeStatus.ARCHIVED:
                item = item.transition(KnowledgeStatus.ARCHIVED)
                self._items[item.id] = item
            archived.append(item)
        return archived

    def search(self, query: KnowledgeSearchQuery) -> list[KnowledgeItem]:
        results = []
        text = query.query.casefold() if query.query else None
        for item in self._items.values():
            if not query.include_archived and item.status in {KnowledgeStatus.ARCHIVED, KnowledgeStatus.SUPERSEDED}:
                continue
            if query.access_scope and item.access_scope != query.access_scope:
                continue
            if query.access_scope is None and item.access_scope != AccessScope.GLOBAL and query.project != item.project:
                continue
            if query.domain and item.domain != query.domain:
                continue
            if query.topic and query.topic not in item.topics:
                continue
            if query.project and item.project != query.project:
                continue
            if query.source and item.source_id != query.source:
                continue
            if query.knowledge_type and item.type != query.knowledge_type:
                continue
            if query.status and item.status != query.status:
                continue
            if query.freshness and item.freshness != query.freshness:
                continue
            if query.min_evidence_confidence is not None and item.evidence_confidence < query.min_evidence_confidence:
                continue
            if text and text not in " ".join([item.title, item.summary, item.content, *item.topics]).casefold():
                continue
            results.append(item)
        return sorted(results, key=lambda item: (item.recommendation_score, item.evidence_confidence, item.id), reverse=True)

    def supersede(self, old_id: str, new_item: KnowledgeItem) -> tuple[KnowledgeItem, KnowledgeItem]:
        old = self._items.get(old_id)
        if old is None:
            raise KnowledgeCoreError(f"knowledge item does not exist: {old_id}")
        self.create(new_item)
        superseded = replace(old.transition(KnowledgeStatus.SUPERSEDED), superseded_by=new_item.id)
        self._items[old_id] = superseded
        return superseded, new_item

class RetrievalInterface:
    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def keyword_search(self, query: str) -> list[KnowledgeItem]:
        return self.repository.search(KnowledgeSearchQuery(query=query))

    def semantic_search(self, query: str) -> list[KnowledgeItem]:
        raise UnsupportedBackendError("semantic_search is a supported interface only; no embedding backend is implemented")

    def hybrid_search(self, query: str) -> list[KnowledgeItem]:
        raise UnsupportedBackendError("hybrid_search is a supported interface only; no semantic backend is implemented")

    def filter(self, query: KnowledgeSearchQuery) -> list[KnowledgeItem]:
        return self.repository.search(query)

    def rank(self, items: Iterable[KnowledgeItem]) -> list[KnowledgeItem]:
        return sorted(items, key=lambda item: (item.recommendation_score, item.evidence_confidence, item.id), reverse=True)

    def retrieve_context(self, query: KnowledgeSearchQuery, *, limit: int = 5) -> list[dict[str, Any]]:
        packets = []
        for item in self.repository.search(query)[:limit]:
            packets.append({
                "ITEM": item.id,
                "WHY_RELEVANT": "Matched metadata or keyword filters in the local repository backend.",
                "CLAIM": item.summary,
                "SOURCE": item.source_id,
                "FRESHNESS": item.freshness.value,
                "CONFIDENCE": item.confidence.label,
                "CONFLICTS": [],
                "USE_LIMITS": "Not validated unless status is VALIDATED or INDEXED.",
            })
        return packets


class GraphInterface:
    def create_entity(self, entity: Entity) -> Entity: ...
    def create_relationship(self, relationship: Relationship) -> Relationship: ...
    def find_related(self, entity_id: str, relationship_type: str | None = None) -> list[Relationship]: ...
    def get_relationships(self, entity_id: str) -> list[Relationship]: ...


class InMemoryGraph(GraphInterface):
    def __init__(self) -> None:
        self.entities: dict[str, Entity] = {}
        self.relationships: dict[str, Relationship] = {}

    def create_entity(self, entity: Entity) -> Entity:
        self.entities[entity.entity_id] = entity
        return entity

    def create_relationship(self, relationship: Relationship) -> Relationship:
        if relationship.from_entity not in self.entities or relationship.to_entity not in self.entities:
            raise KnowledgeCoreError("relationships require existing from_entity and to_entity")
        self.relationships[relationship.relationship_id] = relationship
        return relationship

    def find_related(self, entity_id: str, relationship_type: str | None = None) -> list[Relationship]:
        return [rel for rel in self.relationships.values() if rel.from_entity == entity_id and (relationship_type is None or rel.relationship_type == relationship_type)]

    def get_relationships(self, entity_id: str) -> list[Relationship]:
        return [rel for rel in self.relationships.values() if rel.from_entity == entity_id or rel.to_entity == entity_id]


@dataclass(frozen=True)
class MemoryRecord:
    memory_id: str
    category: MemoryCategory
    content: str
    scope: str
    provenance: Provenance
    status: KnowledgeStatus = KnowledgeStatus.CANDIDATE


class MemoryStore:
    """Explicit memory abstraction; separate from the knowledge repository."""

    def __init__(self) -> None:
        self._records: dict[str, MemoryRecord] = {}

    def create(self, record: MemoryRecord) -> MemoryRecord:
        ensure_no_secret("memory content", record.content)
        self._records[record.memory_id] = record
        return record

    def list(self, *, category: MemoryCategory | None = None, scope: str | None = None) -> list[MemoryRecord]:
        values = list(self._records.values())
        if category:
            values = [record for record in values if record.category == category]
        if scope:
            values = [record for record in values if record.scope == scope]
        return values


class IngestionInterface(Protocol):
    def ingest(self, source: Source) -> ImportReport: ...
    def parse(self, source: Source) -> ImportReport: ...
    def extract(self, source: Source) -> ImportReport: ...
    def normalize(self, record: dict[str, Any]) -> KnowledgeItem: ...
    def validate(self, record: dict[str, Any]) -> list[str]: ...


class CorpusImporter:
    """Importer for Phase 2.1 ADE-EXTRACTED-ITEMS.jsonl records."""

    SUPPORTED_CONTENT_TYPES = {
        "Knowledge candidate",
        "Prompt / agent instruction",
        "Operational instruction",
        "Startup / product knowledge",
        "Tool / package knowledge",
        "Security knowledge",
        "Design knowledge",
        "Visibility / AEO knowledge",
    }

    def __init__(self, repository: InMemoryKnowledgeRepository | None = None) -> None:
        self.repository = repository or InMemoryKnowledgeRepository()
        self.research_candidates: list[ResearchCandidate] = []

    def validate(self, record: dict[str, Any]) -> list[str]:
        required = ["item_id", "source_id", "source_location", "source_section", "original_text_reference", "content_type", "topic", "project", "status", "text_excerpt"]
        errors = [f"missing {field}" for field in required if not record.get(field)]
        if record.get("content_type") and record["content_type"] not in self.SUPPORTED_CONTENT_TYPES:
            errors.append(f"unsupported content_type {record['content_type']}")
        if contains_secret(str(record.get("text_excerpt", ""))):
            errors.append("text_excerpt appears to contain a secret")
        return errors

    def import_jsonl(self, path: Path) -> ImportReport:
        report = ImportReport()
        seen_content: dict[str, str] = {}
        errors: list[str] = []
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                report = replace(report, records_processed=report.records_processed + 1)
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    message = f"line {line_number}: malformed JSON: {exc}"
                    errors.append(message)
                    report = report.add_error(message, malformed=True)
                    continue
                validation_errors = self.validate(record)
                if validation_errors:
                    missing = any(error.startswith("missing") and any(key in error for key in ("source_id", "source_location", "original_text_reference")) for error in validation_errors)
                    unsupported = any(error.startswith("unsupported") for error in validation_errors)
                    message = f"line {line_number}: " + "; ".join(validation_errors)
                    errors.append(message)
                    report = report.add_error(message, malformed=not unsupported, missing_provenance=missing, unsupported=unsupported)
                    continue
                try:
                    item = self.normalize(record)
                    self.repository.create(item)
                    report = replace(report, records_accepted=report.records_accepted + 1)
                    fingerprint = _fingerprint(record["text_excerpt"])
                    if fingerprint in seen_content:
                        self.repository.duplicates.append(DuplicateRecord(seen_content[fingerprint], item.id, "DUPLICATE", "normalized excerpt fingerprint matched"))
                    else:
                        seen_content[fingerprint] = item.id
                    if "STALE_CANDIDATE" in record.get("status", []):
                        self.research_candidates.append(research_candidate_from_record(record, item.provenance))
                    if "CONFLICT_REVIEW_CANDIDATE" in record.get("status", []):
                        self.repository.conflicts.append(ConflictRecord(stable_id("CONFLICT", item.id, record["original_text_reference"]), item.id, "UNRESOLVED_EXTERNAL_CLAIM", item.source_id, "REVIEW_REQUIRED"))
                except KnowledgeCoreError as exc:
                    message = f"line {line_number}: {exc}"
                    errors.append(message)
                    report = report.add_error(message, malformed=True)
        return replace(
            report,
            duplicates=len(self.repository.duplicates),
            conflicts=len(self.repository.conflicts),
            research_candidates=len(self.research_candidates),
            errors=tuple(errors),
        )

    def normalize(self, record: dict[str, Any]) -> KnowledgeItem:
        observed = utc_now()
        provenance = Provenance(
            source_id=record["source_id"],
            source_location=record["source_location"],
            source_section=record.get("source_section", "Unknown"),
            original_text_reference=record["original_text_reference"],
            observed_at=observed,
            extracted_at=observed,
            derivation=SourceDerivation.SOURCE_DERIVED,
            transformations=("phase_2_1_jsonl_to_knowledge_item",),
        )
        topics = tuple(_as_strings(record.get("topic"))) or ("General ADE knowledge",)
        project = ", ".join(_as_strings(record.get("project"))) or "Unspecified / reusable"
        freshness = Freshness.STALE_RISK if "STALE_CANDIDATE" in record.get("status", []) else Freshness.UNKNOWN
        return KnowledgeItem(
            id=record["item_id"],
            type=_knowledge_type_for_content(record["content_type"]),
            title=f"{record['content_type']}: {record.get('subtopic') or record['item_id']}",
            content=record["text_excerpt"],
            summary=record["text_excerpt"][:240],
            source_id=record["source_id"],
            source_location=record["source_location"],
            source_type=record.get("source_quality", "User-provided source"),
            domain=topics[0],
            topics=topics,
            project=project,
            created_at=observed,
            observed_at=observed,
            updated_at=observed,
            version=None,
            status=KnowledgeStatus.EXTRACTED,
            freshness=freshness,
            confidence=Confidence(
                _confidence_to_float(record.get("evidence_confidence")),
                _score_to_float(record.get("recommendation_score")),
                label=str(record.get("evidence_confidence", "contextual")),
            ),
            provenance=provenance,
        )


def research_candidate_from_record(record: dict[str, Any], provenance: Provenance) -> ResearchCandidate:
    return ResearchCandidate(
        research_id=stable_id("RESEARCH", record.get("item_id"), record.get("source_id"), record.get("original_text_reference")),
        claim=record.get("text_excerpt", "")[:500],
        source_id=record["source_id"],
        reason_for_review="Marked STALE_CANDIDATE during Phase 2.1 extraction; current facts are not verified.",
        freshness=Freshness.STALE_RISK,
        priority="normal",
        status="unverified",
        last_checked=None,
        resolution=None,
        evidence=(provenance,),
    )


def import_research_candidates_from_extraction(path: Path) -> tuple[list[ResearchCandidate], ImportReport]:
    importer = CorpusImporter()
    report = importer.import_jsonl(path)
    return importer.research_candidates, report


def _as_strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,) if value else ()
    if isinstance(value, Iterable):
        return tuple(str(item) for item in value if str(item))
    return (str(value),)


def _knowledge_type_for_content(content_type: str) -> KnowledgeType:
    mapping = {
        "Operational instruction": KnowledgeType.PROCEDURE,
        "Prompt / agent instruction": KnowledgeType.PROMPT,
        "Design knowledge": KnowledgeType.PATTERN,
        "Security knowledge": KnowledgeType.PROCEDURE,
        "Visibility / AEO knowledge": KnowledgeType.PROCEDURE,
        "Startup / product knowledge": KnowledgeType.HYPOTHESIS,
        "Tool / package knowledge": KnowledgeType.FACT,
    }
    return mapping.get(content_type, KnowledgeType.CONCEPT)


def _confidence_to_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return {"low": 0.3, "medium": 0.6, "high": 0.85, "established": 0.9}.get(str(value).lower(), 0.5)


def _score_to_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if str(value).lower() in {"not_assessed", "none", "unknown", ""}:
        return 0.0
    return _confidence_to_float(value)


def _fingerprint(text: str) -> str:
    normalized = re.sub(r"\W+", " ", text.casefold()).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _substantial_overlap(left: str, right: str) -> bool:
    left_words = set(re.findall(r"[a-z0-9]{4,}", left.casefold()))
    right_words = set(re.findall(r"[a-z0-9]{4,}", right.casefold()))
    if not left_words or not right_words:
        return False
    overlap = len(left_words & right_words) / min(len(left_words), len(right_words))
    return overlap >= 0.9

