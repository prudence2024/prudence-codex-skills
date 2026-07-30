"""Developer CLI for the skill ecosystem."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .audit import audit_repository
from .discovery import discover_skills, find_skill
from .errors import EcosystemError
from .io import dump_json, load_json
from .knowledge import KnowledgeQuery, load_patterns, query_patterns
from .migration import apply_migrations, plan_migrations
from .registry import build_registry, write_registry
from .reporting import create_validation_report, render_markdown, validate_report
from .validation import (
    validate_document,
    validate_infrastructure,
    validate_knowledge_base,
    validate_registry,
    validate_repository,
    validate_skill,
    validate_source_manifests,
)


def _root(value: str) -> Path:
    path = Path(value).resolve()
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Repository root does not exist: {path}")
    return path


def _csv(values: list[str] | None) -> tuple[str, ...]:
    if not values:
        return ()
    return tuple(item for value in values for item in value.split(",") if item)


def _emit(data, *, as_json: bool = True) -> None:
    if as_json:
        print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        print(data)


def _add_root(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--root", type=_root, default=Path.cwd(), help="Repository root")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="skill-ecosystem")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate ecosystem artifacts")
    _add_root(validate)
    validate.add_argument(
        "--scope",
        choices=("infrastructure", "repository", "skill", "context", "report", "knowledge", "sources"),
        default="repository",
    )
    validate.add_argument("--skill", help="Skill ID for --scope skill")
    validate.add_argument("--path", type=Path, help="Document path for context or report scope")
    validate.add_argument("--strict", action="store_true", help="Require first-party manifests")
    validate.add_argument("--markdown", action="store_true")

    audit = subparsers.add_parser("audit", help="Run a read-only ecosystem audit")
    _add_root(audit)
    audit.add_argument("--strict", action="store_true")
    audit.add_argument("--markdown", action="store_true")

    register = subparsers.add_parser("register", help="Generate or check the skill registry")
    _add_root(register)
    register.add_argument("--output", type=Path)
    register.add_argument("--check", action="store_true")

    test = subparsers.add_parser("test", help="Run the ecosystem pytest suite")
    _add_root(test)
    test.add_argument(
        "pytest_args",
        nargs=argparse.REMAINDER,
        help="Start with a test path, then provide pytest flags",
    )

    migrate = subparsers.add_parser("migrate", help="Plan approval-gated skill migration")
    _add_root(migrate)
    migrate.add_argument("action", choices=("plan", "apply"))
    migrate.add_argument("--output", type=Path)

    manage = subparsers.add_parser("manage", help="List or inspect skills")
    _add_root(manage)
    manage.add_argument("action", choices=("list", "show"))
    manage.add_argument("--skill")

    knowledge = subparsers.add_parser("knowledge", help="Query the Design Knowledge Base")
    _add_root(knowledge)
    knowledge.add_argument("action", choices=("query", "validate"))
    knowledge.add_argument("--domain", action="append")
    knowledge.add_argument("--industry", action="append")
    knowledge.add_argument("--ux-goal", action="append")
    knowledge.add_argument("--accessibility", action="append")
    knowledge.add_argument("--performance", action="append")
    knowledge.add_argument("--confidence-level", action="append")
    knowledge.add_argument("--min-evidence-confidence", type=float, default=0.0)
    knowledge.add_argument("--min-recommendation-score", type=float, default=0.0)
    knowledge.add_argument("--text")
    return parser


def _required_path(args: argparse.Namespace) -> Path:
    if not args.path:
        raise EcosystemError(f"--path is required with --scope {args.scope}")
    return args.path if args.path.is_absolute() else args.root / args.path


def _validation_command(args: argparse.Namespace) -> int:
    if args.scope == "infrastructure":
        results = [validate_infrastructure(args.root)]
    elif args.scope == "skill":
        if not args.skill:
            raise EcosystemError("--skill is required with --scope skill")
        skill = find_skill(discover_skills(args.root), args.skill)
        if skill is None:
            raise EcosystemError(f"Unknown skill: {args.skill}")
        results = [validate_skill(skill, args.root, require_manifest=args.strict)]
    elif args.scope == "context":
        results = [
            validate_document(
                _required_path(args),
                root=args.root,
                schema_name="shared-context.json",
                check_name="shared-context",
            )
        ]
    elif args.scope == "report":
        results = [
            validate_document(
                _required_path(args),
                root=args.root,
                schema_name="report.json",
                check_name="report",
            )
        ]
    elif args.scope == "knowledge":
        results = [validate_knowledge_base(args.root)]
    elif args.scope == "sources":
        results = [validate_source_manifests(args.root)]
    else:
        results = validate_repository(args.root, require_manifests=args.strict)
    report = create_validation_report(
        results,
        title="Skill ecosystem validation",
        scope=args.scope,
    )
    report_issues = validate_report(report, args.root)
    if report_issues:
        raise EcosystemError(report_issues[0].message)
    _emit(render_markdown(report) if args.markdown else report, as_json=not args.markdown)
    return 1 if report["summary"]["status"] == "fail" else 0


def _register_command(args: argparse.Namespace) -> int:
    if args.check and args.output:
        output = args.output if args.output.is_absolute() else args.root / args.output
        if not output.is_file():
            raise EcosystemError(f"Registry snapshot does not exist: {output}")
        existing = load_json(output)
        generated_at = existing.get("generated_at") if isinstance(existing, dict) else None
        expected = build_registry(args.root, generated_at=generated_at)
        result = validate_registry(existing, args.root)
        payload = result.as_dict()
        payload["current"] = not result.failed and existing == expected
        if not payload["current"]:
            payload.setdefault("issues", []).append(
                {
                    "code": "registry.stale",
                    "message": "Registry snapshot differs from current discovery",
                    "severity": "error",
                    "path": str(output),
                }
            )
            payload["status"] = "fail"
        _emit(payload)
        return 1 if payload["status"] == "fail" else 0

    registry = build_registry(args.root)
    if args.check:
        result = validate_registry(registry, args.root)
        _emit(result.as_dict())
        return 1 if result.failed else 0
    if args.output:
        output = args.output if args.output.is_absolute() else args.root / args.output
        write_registry(registry, output)
    else:
        _emit(registry)
    return 0


def _knowledge_command(args: argparse.Namespace) -> int:
    patterns, issues = load_patterns(args.root)
    if args.action == "validate":
        _emit(
            {
                "status": "fail" if issues else "pass",
                "patterns": len(patterns),
                "issues": [issue.as_dict() for issue in issues],
            }
        )
        return 1 if issues else 0
    if issues:
        raise EcosystemError(f"Knowledge base has {len(issues)} validation issue(s)")
    query = KnowledgeQuery(
        domains=_csv(args.domain),
        industries=_csv(args.industry),
        ux_goals=_csv(args.ux_goal),
        accessibility=_csv(args.accessibility),
        performance=_csv(args.performance),
        confidence_levels=_csv(args.confidence_level),
        min_evidence_confidence=args.min_evidence_confidence,
        min_recommendation_score=args.min_recommendation_score,
        text=args.text,
    )
    matches = query_patterns(patterns, query)
    _emit({"count": len(matches), "patterns": matches})
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            return _validation_command(args)
        if args.command == "audit":
            report = audit_repository(args.root, strict=args.strict)
            _emit(render_markdown(report) if args.markdown else report, as_json=not args.markdown)
            return 1 if report["summary"]["status"] == "fail" else 0
        if args.command == "register":
            return _register_command(args)
        if args.command == "test":
            import pytest

            targets = args.pytest_args or [str(args.root / "tests")]
            return int(pytest.main(targets))
        if args.command == "migrate":
            if args.action == "apply":
                apply_migrations(args.root)
            plan = plan_migrations(discover_skills(args.root))
            if args.output:
                output = args.output if args.output.is_absolute() else args.root / args.output
                dump_json(plan, output)
            else:
                _emit(plan)
            return 0
        if args.command == "manage":
            skills = discover_skills(args.root)
            if args.action == "list":
                _emit(
                    [
                        {
                            "id": skill.id,
                            "source_path": skill.source_path,
                            "upstream": skill.upstream,
                            "status": "upstream"
                            if skill.upstream
                            else (skill.manifest.get("status") if skill.manifest else "unmigrated"),
                        }
                        for skill in skills
                    ]
                )
                return 0
            if not args.skill:
                raise EcosystemError("--skill is required for manage show")
            skill = find_skill(skills, args.skill)
            if not skill:
                raise EcosystemError(f"Unknown skill: {args.skill}")
            _emit(build_registry(args.root, skills=[skill])["skills"][0])
            return 0
        if args.command == "knowledge":
            return _knowledge_command(args)
        parser.error("Unknown command")
    except (EcosystemError, PermissionError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

