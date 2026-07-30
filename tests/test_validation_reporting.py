from __future__ import annotations

from pathlib import Path

from skill_ecosystem.discovery import discover_skills
from skill_ecosystem.models import CheckResult, Issue
from skill_ecosystem.reporting import create_validation_report, render_markdown, validate_report
from skill_ecosystem.validation import validate_infrastructure, validate_skill


FIXTURE = Path(__file__).parent / "fixtures" / "repository"


def test_infrastructure_schemas_are_valid(repository_root):
    result = validate_infrastructure(repository_root)
    assert result.status == "pass", result.issues


def test_fixture_skill_validates(repository_root):
    skill = discover_skills(FIXTURE)[0]
    result = validate_skill(skill, repository_root)
    assert result.status == "pass", result.issues


def test_report_validates_and_renders(repository_root):
    report = create_validation_report(
        [CheckResult("example", "partial", [Issue("example", "Needs review", "warning")])],
        title="Fixture report",
        scope="tests",
        generated_at="test",
    )
    assert report["summary"]["status"] == "partial"
    assert validate_report(report, repository_root) == []
    rendered = render_markdown(report)
    assert "# Fixture report" in rendered
    assert "Needs review" in rendered

