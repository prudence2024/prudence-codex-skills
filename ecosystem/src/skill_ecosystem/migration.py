"""Migration planning only; applying plans is intentionally approval-gated."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

from .discovery import DiscoveredSkill


def plan_migrations(skills: Iterable[DiscoveredSkill]) -> dict[str, Any]:
    plans = []
    for skill in skills:
        if skill.upstream or skill.migrated:
            continue
        plans.append(
            {
                "skill_id": skill.id,
                "source_path": skill.source_path,
                "action": "create skill.yaml and add context/report routing",
                "preserve": ["SKILL.md trigger identity", "agents/openai.yaml", "existing references"],
                "requires_human_approval": True,
                "status": "proposed",
            }
        )
    return {
        "schema_version": 1,
        "mode": "plan_only",
        "plans": plans,
        "apply_enabled": False,
        "reason": "First-party migration begins only in an approved later phase.",
    }


def apply_migrations(_: Path) -> None:
    raise PermissionError(
        "Migration apply is disabled. Approve the first-party migration phase before enabling it."
    )

