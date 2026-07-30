from __future__ import annotations

from pathlib import Path

import pytest

from skill_ecosystem.discovery import discover_skills
from skill_ecosystem.migration import apply_migrations, plan_migrations


FIXTURE = Path(__file__).parent / "fixtures" / "repository"


def test_migration_plan_skips_migrated_and_upstream():
    plan = plan_migrations(discover_skills(FIXTURE))
    assert plan["mode"] == "plan_only"
    assert plan["plans"] == []


def test_migration_apply_requires_later_approval():
    with pytest.raises(PermissionError, match="disabled"):
        apply_migrations(FIXTURE)

