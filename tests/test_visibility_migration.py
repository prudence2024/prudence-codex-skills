from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "SEO, local SEO, AI-crawlability, structured data, sitemap/robots/llms.txt, "
    "social preview, analytics, and indexing workflow for websites. Use when Codex "
    "needs to audit or implement website visibility improvements, optimize hotels/"
    "restaurants/physical businesses for local search and Google Business Profile "
    "readiness, fix client-rendered SPA crawlability issues, add schema code, generate "
    "or verify sitemap.xml/robots.txt/llms.txt, improve Open Graph/Twitter metadata, "
    "validate SSR/prerendered HTML, configure GA4/search-console workflows, or prepare "
    "a site for Google Search Console, Bing Webmaster Tools, AI assistants, and link "
    "previews."
)


def test_visibility_preserves_trigger_identity(repository_root):
    frontmatter = parse_skill_frontmatter(repository_root / "visibility" / "SKILL.md")
    assert frontmatter == {"name": "visibility", "description": DESCRIPTION}


def test_visibility_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "visibility")
    assert skill is not None
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_registry_exposes_full_visibility_contract(repository_root):
    registry = build_registry(repository_root, generated_at="test")
    entry = next(item for item in registry["skills"] if item["id"] == "visibility")
    assert entry["status"] == "stable"
    assert entry["version"] == "1.0.0"
    assert entry["category"] == "visibility"
    assert entry["dependencies"]["required"] == []
    assert entry["dependencies"]["optional"] == ["design-toolkit", "security"]
    assert "crawler-validators" in entry["extension_points"]


def test_visibility_owns_all_required_domains(repository_root):
    manifest = load_yaml(repository_root / "visibility" / "skill.yaml")
    owned = " ".join(manifest["scope"]["includes"]).casefold()
    for domain in (
        "seo",
        "discoverability",
        "indexing",
        "structured data",
        "metadata",
        "social",
        "crawlability",
        "search-performance",
        "visibility",
    ):
        assert domain in owned


def test_visibility_consumes_design_without_duplicating_it(repository_root):
    manifest = load_yaml(repository_root / "visibility" / "skill.yaml")
    responsibilities = " ".join(manifest["responsibilities"]).casefold()
    exclusions = " ".join(manifest["scope"]["excludes"]).casefold()
    assert "consume applicable design toolkit decisions" in responsibilities
    for excluded in (
        "design reasoning",
        "component selection",
        "visual hierarchy",
        "interaction design",
        "accessibility implementation",
        "general frontend-performance",
    ):
        assert excluded in exclusions


def test_visibility_decision_fixture_validates(repository_root):
    decision = load_yaml(repository_root / "tests" / "fixtures" / "visibility-decision.yaml")
    issues = validate_instance(
        decision,
        repository_root / "visibility" / "schemas" / "visibility-decision.json",
        subject="visibility decision fixture",
    )
    assert issues == []


def test_visibility_local_markdown_links_resolve(repository_root):
    skill_root = repository_root / "visibility"
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

