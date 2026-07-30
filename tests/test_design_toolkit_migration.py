from __future__ import annotations

import re
from pathlib import Path

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Frontend design, implementation, and animation toolkit for polished web apps, "
    "landing pages, dashboards, and interactive UI. Use when Codex needs to choose "
    "component libraries or design references, plan responsive and accessible "
    "components, improve forms and frontend performance, select animation techniques, "
    "or run post-build UI quality checks."
)


def test_design_toolkit_preserves_trigger_identity(repository_root):
    frontmatter = parse_skill_frontmatter(repository_root / "design-toolkit" / "SKILL.md")
    assert frontmatter == {"name": "design-toolkit", "description": DESCRIPTION}


def test_design_toolkit_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "design-toolkit")
    assert skill is not None
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_registry_exposes_full_design_toolkit_contract(repository_root):
    registry = build_registry(repository_root, generated_at="test")
    entry = next(item for item in registry["skills"] if item["id"] == "design-toolkit")
    assert entry["status"] == "stable"
    assert entry["version"] == "1.0.0"
    assert entry["category"] == "design"
    assert entry["dependencies"]["required"] == []
    assert entry["dependencies"]["optional"] == ["visibility", "security"]
    assert "reasoning-modules" in entry["extension_points"]


def test_manifest_contains_every_required_reasoning_dimension(repository_root):
    manifest = load_yaml(repository_root / "design-toolkit" / "skill.yaml")
    reasoning = " ".join(manifest["pipeline"]["reasoning"]).casefold()
    for dimension in (
        "business objectives",
        "user goals",
        "brand identity",
        "product context",
        "target audience",
        "conversion objectives",
        "accessibility",
        "performance",
        "maintainability",
        "design consistency",
        "technical constraints",
    ):
        assert dimension in reasoning


def test_design_intelligence_boundary_is_explicit(repository_root):
    manifest = load_yaml(repository_root / "design-toolkit" / "skill.yaml")
    exclusions = " ".join(manifest["scope"]["excludes"]).casefold()
    for responsibility in (
        "website archive ingestion",
        "pattern extraction",
        "normalization",
        "evidence collection",
        "confidence scoring",
        "recommendation scoring",
        "knowledge storage",
    ):
        assert responsibility in exclusions


def test_design_decision_fixture_validates(repository_root):
    decision = load_yaml(repository_root / "tests" / "fixtures" / "design-decision.yaml")
    issues = validate_instance(
        decision,
        repository_root / "design-toolkit" / "schemas" / "design-decision.json",
        subject="design decision fixture",
    )
    assert issues == []


def test_design_toolkit_local_markdown_links_resolve(repository_root):
    skill_root = repository_root / "design-toolkit"
    broken: list[tuple[str, str]] = []
    for path in skill_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or "://" in target:
                continue
            if not (path.parent / target).resolve().exists():
                broken.append((path.relative_to(repository_root).as_posix(), target))
    assert broken == []

