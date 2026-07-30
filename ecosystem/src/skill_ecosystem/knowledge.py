"""Domain-oriented Design Knowledge Base access and querying."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .errors import DataError
from .io import load_yaml
from .models import Issue
from .schema import validate_instance


@dataclass(frozen=True)
class KnowledgeQuery:
    domains: tuple[str, ...] = ()
    industries: tuple[str, ...] = ()
    ux_goals: tuple[str, ...] = ()
    accessibility: tuple[str, ...] = ()
    performance: tuple[str, ...] = ()
    confidence_levels: tuple[str, ...] = ()
    min_evidence_confidence: float = 0.0
    min_recommendation_score: float = 0.0
    text: str | None = None


def load_patterns(root: Path) -> tuple[list[dict[str, Any]], list[Issue]]:
    knowledge_root = root / "design-intelligence" / "knowledge"
    schema_path = root / "ecosystem" / "schemas" / "knowledge-pattern.json"
    patterns: list[dict[str, Any]] = []
    issues: list[Issue] = []
    if not knowledge_root.exists():
        return patterns, issues

    domains_path = root / "design-intelligence" / "config" / "domains.yaml"
    allowed_domains: set[str] = set()
    if domains_path.is_file():
        try:
            domains_data = load_yaml(domains_path)
            allowed_domains = (
                set(domains_data.get("domains", []))
                if isinstance(domains_data, dict)
                else set()
            )
        except DataError as exc:
            issues.append(
                Issue("knowledge.domains_load_failed", str(exc), path=str(domains_path))
            )

    for path in sorted(knowledge_root.rglob("*.yaml")):
        try:
            pattern = load_yaml(path)
        except DataError as exc:
            issues.append(Issue("knowledge.load_failed", str(exc), path=str(path)))
            continue
        if not isinstance(pattern, dict):
            issues.append(
                Issue("knowledge.invalid_type", "Pattern must be a mapping", path=str(path))
            )
            continue
        validation = validate_instance(pattern, schema_path, subject=f"pattern {path.name}")
        if validation:
            issues.extend(
                Issue(issue.code, issue.message, issue.severity, str(path), issue.details)
                for issue in validation
            )
            continue
        if allowed_domains and pattern["domain"] not in allowed_domains:
            issues.append(
                Issue(
                    "knowledge.domain.unknown",
                    f"Pattern domain is not configured: {pattern['domain']}",
                    path=str(path),
                )
            )
            continue
        pattern = dict(pattern)
        pattern["_path"] = path.relative_to(root).as_posix()
        patterns.append(pattern)
    return patterns, issues


def _overlaps(values: Iterable[str], expected: tuple[str, ...]) -> bool:
    return not expected or bool(set(values) & set(expected))


def query_patterns(patterns: Iterable[dict[str, Any]], query: KnowledgeQuery) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    text = query.text.casefold() if query.text else None
    for pattern in patterns:
        scores = pattern["scores"]
        if query.domains and pattern["domain"] not in query.domains:
            continue
        if not _overlaps(pattern.get("industries", []), query.industries):
            continue
        if not _overlaps(pattern.get("ux_goals", []), query.ux_goals):
            continue
        if query.accessibility and pattern["accessibility"]["rating"] not in query.accessibility:
            continue
        if query.performance and pattern["performance"]["rating"] not in query.performance:
            continue
        if query.confidence_levels and scores["confidence_level"] not in query.confidence_levels:
            continue
        if scores["evidence_confidence"] < query.min_evidence_confidence:
            continue
        if scores["recommendation_score"] < query.min_recommendation_score:
            continue
        if text:
            haystack = " ".join(
                [
                    pattern["id"],
                    pattern["name"],
                    pattern["summary"],
                    *pattern.get("tags", []),
                    *pattern.get("ux_goals", []),
                ]
            ).casefold()
            if text not in haystack:
                continue
        matches.append(pattern)
    return sorted(
        matches,
        key=lambda pattern: (
            pattern["scores"]["recommendation_score"],
            pattern["scores"]["evidence_confidence"],
            pattern["id"],
        ),
        reverse=True,
    )

