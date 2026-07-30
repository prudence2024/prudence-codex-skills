from __future__ import annotations

from pathlib import Path

from skill_ecosystem.knowledge import KnowledgeQuery, load_patterns, query_patterns


FIXTURE = Path(__file__).parent / "fixtures" / "repository"


def test_loads_domain_oriented_patterns():
    patterns, issues = load_patterns(FIXTURE)
    assert not issues
    assert {pattern["domain"] for pattern in patterns} == {"navigation", "motion"}


def test_queries_by_domain_industry_goal_quality_and_scores():
    patterns, _ = load_patterns(FIXTURE)
    result = query_patterns(
        patterns,
        KnowledgeQuery(
            domains=("navigation",),
            industries=("saas",),
            ux_goals=("efficient-navigation",),
            accessibility=("supports",),
            performance=("neutral",),
            confidence_levels=("established",),
            min_evidence_confidence=0.8,
            min_recommendation_score=0.8,
        ),
    )
    assert [pattern["id"] for pattern in result] == ["command-navigation"]


def test_experimental_variation_is_not_returned_as_established():
    patterns, _ = load_patterns(FIXTURE)
    result = query_patterns(
        patterns,
        KnowledgeQuery(confidence_levels=("established",), min_recommendation_score=0.5),
    )
    assert "ambient-orbit" not in {pattern["id"] for pattern in result}


def test_text_query_searches_tags_and_goals():
    patterns, _ = load_patterns(FIXTURE)
    result = query_patterns(patterns, KnowledgeQuery(text="keyboard"))
    assert [pattern["id"] for pattern in result] == ["command-navigation"]

