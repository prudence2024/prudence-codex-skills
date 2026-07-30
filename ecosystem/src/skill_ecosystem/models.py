"""Small shared result models."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

Severity = Literal["error", "warning", "info"]
Status = Literal["pass", "fail", "partial", "not_applicable", "not_verified"]


@dataclass(frozen=True)
class Issue:
    code: str
    message: str
    severity: Severity = "error"
    path: str | None = None
    details: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value not in (None, {})}


@dataclass
class CheckResult:
    name: str
    status: Status
    issues: list[Issue] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status,
            "issues": [issue.as_dict() for issue in self.issues],
            "evidence": self.evidence,
        }

    @property
    def failed(self) -> bool:
        return self.status == "fail" or any(issue.severity == "error" for issue in self.issues)

