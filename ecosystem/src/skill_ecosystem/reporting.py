"""Create and render common ecosystem reports."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .models import CheckResult
from .schema import validate_instance


def create_validation_report(
    results: Iterable[CheckResult],
    *,
    title: str,
    scope: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    checks = list(results)
    failed = sum(result.status == "fail" for result in checks)
    partial = sum(result.status == "partial" for result in checks)
    status = "fail" if failed else ("partial" if partial else "pass")
    return {
        "schema_version": 1,
        "report_type": "validation",
        "title": title,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "scope": scope,
        "summary": {
            "status": status,
            "checks": len(checks),
            "failed": failed,
            "partial": partial,
        },
        "decisions": [],
        "validation_results": [result.as_dict() for result in checks],
        "risks": [],
        "warnings": [
            issue.message
            for result in checks
            for issue in result.issues
            if issue.severity == "warning"
        ],
        "errors": [
            issue.message
            for result in checks
            for issue in result.issues
            if issue.severity == "error"
        ],
        "recommendations": [],
        "context_changes": [],
        "artifacts_changed": [],
        "checks_not_run": [],
        "handoff": {"next_owner": None, "reason": None},
        "approval_required": False,
    }


def validate_report(report: dict[str, Any], root: Path):
    return validate_instance(
        report,
        root / "ecosystem" / "schemas" / "report.json",
        subject="report",
    )


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        f"# {report['title']}",
        "",
        f"Status: `{summary['status']}`",
        "",
        f"Scope: {report['scope']}",
        "",
        "## Validation results",
        "",
    ]
    for result in report["validation_results"]:
        lines.append(f"- `{result['status']}` {result['name']}")
        for issue in result.get("issues", []):
            location = f" ({issue['path']})" if issue.get("path") else ""
            lines.append(f"  - {issue['severity']}: {issue['message']}{location}")
    if report["checks_not_run"]:
        lines.extend(["", "## Checks not run", ""])
        lines.extend(f"- {item}" for item in report["checks_not_run"])
    return "\n".join(lines) + "\n"

