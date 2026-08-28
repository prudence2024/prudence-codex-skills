from __future__ import annotations

import json
from pathlib import Path

from skill_ecosystem.knowledge_runtime_benchmark import QUERIES, run_benchmark


def test_phase_2_4_benchmark_runs_against_current_corpus():
    corpus = Path(__file__).resolve().parents[1] / "docs" / "knowledge" / "ADE-EXTRACTED-ITEMS.jsonl"
    results = run_benchmark(corpus)
    assert results["corpus_items"] == 932
    assert set(results["strategies"]) == {"jsonl_keyword_scan", "sqlite_fts5_bm25", "governed_lexical_hybrid_rrf"}
    assert len(results["queries"]) == len(QUERIES)
    assert results["strategies"]["sqlite_fts5_bm25"]["avg_term_recall"] >= 0.9
    assert results["strategies"]["governed_lexical_hybrid_rrf"]["avg_score"] >= 0.9


def test_phase_2_4_benchmark_artifact_is_valid_json_if_present():
    artifact = Path(__file__).resolve().parents[1] / "docs" / "knowledge" / "ADE-PHASE-2.4-RETRIEVAL-BENCHMARK.json"
    if not artifact.exists():
        return
    data = json.loads(artifact.read_text(encoding="utf-8"))
    assert data["corpus_items"] == 932
    assert "governed_lexical_hybrid_rrf" in data["strategies"]
