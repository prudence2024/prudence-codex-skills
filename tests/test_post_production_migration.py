from __future__ import annotations

import re

from skill_ecosystem.discovery import discover_skills, find_skill
from skill_ecosystem.io import load_yaml, parse_skill_frontmatter
from skill_ecosystem.registry import build_registry
from skill_ecosystem.schema import validate_instance
from skill_ecosystem.validation import validate_skill


DESCRIPTION = (
    "Coordinate a complete evidence-based post-production audit and hardening pass for "
    "websites and web applications across SEO, AI discoverability, accessibility, "
    "performance, Core Web Vitals, security, metadata, structured data, analytics, "
    "monitoring, deployment, progressive enhancement, mobile behavior, crawlability, "
    "indexability, and code quality. Use before launch, after a major release, when "
    "reviewing Lighthouse/PageSpeed/Search Console/Bing findings, when comparing a live "
    "deployment with a repository revision, or when the user requests a production-"
    "readiness score and prioritized remediation report."
)


def test_post_production_preserves_trigger_identity(repository_root):
    assert parse_skill_frontmatter(repository_root / "post-production" / "SKILL.md") == {
        "name": "post-production", "description": DESCRIPTION
    }


def test_post_production_manifest_validates_strictly(repository_root):
    skill = find_skill(discover_skills(repository_root), "post-production")
    result = validate_skill(skill, repository_root, require_manifest=True)
    assert result.status == "pass", result.issues


def test_post_production_registry_contract(repository_root):
    entry = next(item for item in build_registry(repository_root, generated_at="test")["skills"]
                 if item["id"] == "post-production")
    assert entry["version"] == "1.0.0"
    assert entry["category"] == "orchestration"
    assert entry["dependencies"]["optional"] == [
        "design-toolkit", "visibility", "security", "session-security",
        "legal-business", "incident-response", "support-triage"
    ]
    assert "specialist-skills" in entry["extension_points"]


def test_post_production_coordinates_without_duplicating(repository_root):
    manifest = load_yaml(repository_root / "post-production" / "skill.yaml")
    responsibilities = " ".join(manifest["responsibilities"]).casefold()
    exclusions = " ".join(manifest["scope"]["excludes"]).casefold()
    for skill in ("design toolkit", "visibility", "security", "session security",
                  "legal business", "incident response", "support triage"):
        assert skill in responsibilities
    assert "primary design, visibility, security, session, legal, incident, or support domain reasoning" in exclusions


def test_post_production_decision_fixture_validates(repository_root):
    issues = validate_instance(
        load_yaml(repository_root / "tests" / "fixtures" / "post-production-decision.yaml"),
        repository_root / "post-production" / "schemas" / "post-production-decision.json",
        subject="post production decision fixture",
    )
    assert issues == []


def test_post_production_local_links_resolve(repository_root):
    root = repository_root / "post-production"
    broken = []
    for path in root.rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and "://" not in target and not (path.parent / target).resolve().exists():
                broken.append((path.name, target))
    assert broken == []
