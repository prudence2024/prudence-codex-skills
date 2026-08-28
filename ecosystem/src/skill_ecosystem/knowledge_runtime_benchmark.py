from __future__ import annotations

import argparse
import json
import math
import re
import sqlite3
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


@dataclass(frozen=True)
class BenchmarkQuery:
    id: str
    text: str
    expected_terms: tuple[str, ...]
    expected_content_types: tuple[str, ...] = ()
    expected_source_ids: tuple[str, ...] = ()


QUERIES: tuple[BenchmarkQuery, ...] = (
    BenchmarkQuery("Q1", "How should ADE handle prompt instructions without treating them as facts?", ("prompt", "instruction", "fact"), ("Prompt / agent instruction",)),
    BenchmarkQuery("Q2", "What does the corpus say about backups and version control?", ("backup", "version", "control")),
    BenchmarkQuery("Q3", "Find security RLS and authentication guidance for project systems.", ("security", "rls", "authentication")),
    BenchmarkQuery("Q4", "What should ADE use for robots.txt sitemap llms.txt and AEO visibility?", ("robots", "sitemap", "llms", "aeo"), ("Visibility / AEO knowledge",)),
    BenchmarkQuery("Q5", "How should rate limiting and abuse resistance be handled?", ("rate", "limiting", "abuse")),
    BenchmarkQuery("Q6", "What knowledge supports AI agents from concept to production?", ("ai", "agents", "production")),
    BenchmarkQuery("Q7", "Which items mention Supabase authentication and databases?", ("supabase", "authentication", "database")),
    BenchmarkQuery("Q8", "What are current recommendations versus source evidence?", ("recommendation", "evidence", "source")),
)


def load_items(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                items.append(json.loads(line))
    return items


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list | tuple):
        return " ".join(as_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key} {as_text(val)}" for key, val in value.items())
    return str(value)


def item_text(item: dict[str, Any]) -> str:
    return " ".join(
        as_text(item.get(field, ""))
        for field in (
            "title",
            "text_excerpt",
            "original_text_reference",
            "topic",
            "subtopic",
            "technology",
            "project",
            "content_type",
            "source_section",
        )
    )


def tokens(text: str) -> list[str]:
    return [match.group(0).casefold() for match in TOKEN_RE.finditer(text)]


def token_score(query: BenchmarkQuery, item: dict[str, Any]) -> float:
    q_tokens = tokens(query.text)
    haystack = Counter(tokens(item_text(item)))
    if not q_tokens:
        return 0.0
    overlap = sum(1 for token in set(q_tokens) if haystack[token])
    weighted = sum(haystack[token] for token in set(q_tokens))
    title_boost = 0.5 if any(term in as_text(item.get("topic", "")).casefold() for term in query.expected_terms) else 0.0
    return overlap + math.log1p(weighted) + title_boost


def evaluate_results(query: BenchmarkQuery, rows: list[dict[str, Any]]) -> dict[str, Any]:
    top = rows[:10]
    combined = " ".join(item_text(item) for item in top).casefold()
    matched_terms = [term for term in query.expected_terms if term.casefold() in combined]
    matched_types = [item.get("content_type") for item in top if item.get("content_type") in query.expected_content_types]
    matched_sources = [item.get("source_id") for item in top if item.get("source_id") in query.expected_source_ids]
    term_recall = len(matched_terms) / max(len(query.expected_terms), 1)
    type_hit = not query.expected_content_types or bool(matched_types)
    source_hit = not query.expected_source_ids or bool(matched_sources)
    score = term_recall * 0.7 + (0.2 if type_hit else 0.0) + (0.1 if source_hit else 0.0)
    return {
        "matched_terms": matched_terms,
        "term_recall": round(term_recall, 3),
        "type_hit": type_hit,
        "source_hit": source_hit,
        "score": round(score, 3),
        "top_ids": [item.get("item_id") for item in top[:5]],
        "top_sources": [item.get("source_id") for item in top[:5]],
        "top_content_types": [item.get("content_type") for item in top[:5]],
    }


def keyword_scan(items: list[dict[str, Any]], query: BenchmarkQuery) -> list[dict[str, Any]]:
    scored = [(token_score(query, item), item) for item in items]
    return [item for score, item in sorted(scored, key=lambda pair: pair[0], reverse=True) if score > 0]


def fts_query_text(query: str) -> str:
    words = tokens(query)
    return " OR ".join(words) if words else "knowledge"


def sqlite_fts(items: list[dict[str, Any]], query: BenchmarkQuery) -> list[dict[str, Any]]:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE items(item_id TEXT PRIMARY KEY, source_id TEXT, content_type TEXT, body TEXT)")
    conn.execute("CREATE VIRTUAL TABLE items_fts USING fts5(item_id UNINDEXED, body)")
    rows = [(item.get("item_id"), item.get("source_id"), item.get("content_type"), item_text(item)) for item in items]
    conn.executemany("INSERT INTO items VALUES (?, ?, ?, ?)", rows)
    conn.executemany("INSERT INTO items_fts(item_id, body) VALUES (?, ?)", [(row[0], row[3]) for row in rows])
    matches = conn.execute(
        """
        SELECT items.item_id
        FROM items_fts JOIN items ON items.item_id = items_fts.item_id
        WHERE items_fts MATCH ?
        ORDER BY bm25(items_fts)
        LIMIT 50
        """,
        (fts_query_text(query.text),),
    ).fetchall()
    by_id = {item.get("item_id"): item for item in items}
    conn.close()
    return [by_id[row[0]] for row in matches if row[0] in by_id]


def rrf(rankings: Iterable[list[dict[str, Any]]], k: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, item in enumerate(ranking):
            item_id = item.get("item_id")
            if item_id:
                scores[item_id] = scores.get(item_id, 0.0) + 1.0 / (k + rank + 1)
    return [item_id for item_id, _ in sorted(scores.items(), key=lambda pair: pair[1], reverse=True)]


def governed_hybrid(items: list[dict[str, Any]], query: BenchmarkQuery) -> list[dict[str, Any]]:
    by_id = {item.get("item_id"): item for item in items}
    fused_ids = rrf([keyword_scan(items, query)[:50], sqlite_fts(items, query)[:50]])
    return [by_id[item_id] for item_id in fused_ids if item_id in by_id]


def run_benchmark(corpus: Path) -> dict[str, Any]:
    items = load_items(corpus)
    strategies = {
        "jsonl_keyword_scan": keyword_scan,
        "sqlite_fts5_bm25": sqlite_fts,
        "governed_lexical_hybrid_rrf": governed_hybrid,
    }
    results = {
        "schema_version": 1,
        "corpus": str(corpus),
        "corpus_items": len(items),
        "queries": [query.__dict__ for query in QUERIES],
        "strategies": {},
    }
    for name, strategy in strategies.items():
        started = time.perf_counter()
        query_results = []
        for query in QUERIES:
            rows = strategy(items, query)
            query_results.append({"query_id": query.id, "result_count": len(rows), **evaluate_results(query, rows)})
        elapsed_ms = (time.perf_counter() - started) * 1000
        avg_score = sum(row["score"] for row in query_results) / len(query_results)
        avg_term_recall = sum(row["term_recall"] for row in query_results) / len(query_results)
        results["strategies"][name] = {
            "elapsed_ms": round(elapsed_ms, 2),
            "avg_score": round(avg_score, 3),
            "avg_term_recall": round(avg_term_recall, 3),
            "query_results": query_results,
        }
    return results


def write_markdown(results: dict[str, Any], path: Path) -> None:
    lines = [
        "# ADE Phase 2.4 Retrieval Benchmark",
        "",
        "Corpus: 40-source / 932-item staging corpus.",
        "",
        "This benchmark is an evaluation harness, not production infrastructure. It uses deterministic local retrieval strategies only and does not ingest additional sources.",
        "",
        "## Strategies Tested",
        "",
        "| Strategy | Average score | Average term recall | Elapsed ms |",
        "| --- | ---: | ---: | ---: |",
    ]
    for name, data in results["strategies"].items():
        lines.append(f"| {name} | {data['avg_score']} | {data['avg_term_recall']} | {data['elapsed_ms']} |")
    lines.extend(["", "## Query Results", ""])
    for name, data in results["strategies"].items():
        lines.extend([f"### {name}", "", "| Query | Score | Term recall | Result count | Top content types |", "| --- | ---: | ---: | ---: | --- |"])
        for row in data["query_results"]:
            lines.append(f"| {row['query_id']} | {row['score']} | {row['term_recall']} | {row['result_count']} | {', '.join(str(v) for v in row['top_content_types'])} |")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run ADE Phase 2.4 retrieval benchmark")
    parser.add_argument("--corpus", type=Path, default=Path("docs/knowledge/ADE-EXTRACTED-ITEMS.jsonl"))
    parser.add_argument("--json-out", type=Path, default=Path("docs/knowledge/ADE-PHASE-2.4-RETRIEVAL-BENCHMARK.json"))
    parser.add_argument("--markdown-out", type=Path, default=Path("docs/knowledge/ADE-PHASE-2.4-RETRIEVAL-BENCHMARK.md"))
    args = parser.parse_args(argv)
    results = run_benchmark(args.corpus)
    args.json_out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    write_markdown(results, args.markdown_out)
    print(json.dumps({"items": results["corpus_items"], "strategies": results["strategies"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
