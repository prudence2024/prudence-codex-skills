"""Read-only repository audit orchestration."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .reporting import create_validation_report
from .validation import validate_repository


def audit_repository(root: Path, *, strict: bool = False) -> dict[str, Any]:
    results = validate_repository(root, require_manifests=strict)
    report = create_validation_report(
        results,
        title="Skill ecosystem audit",
        scope=str(root.resolve()),
    )
    unmigrated = [
        issue.message
        for result in results
        for issue in result.issues
        if issue.code == "skill.manifest.missing"
    ]
    if unmigrated:
        report["recommendations"].append(
            {
                "id": "migrate-first-party-manifests",
                "status": "proposed",
                "summary": f"Migrate {len(unmigrated)} first-party skills after Phase 3 approval gates.",
            }
        )
    return report

