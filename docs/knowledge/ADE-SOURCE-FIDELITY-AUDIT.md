# ADE Source Fidelity Audit

## Direct Answer

Are the uploaded materials preserved word-for-word / byte-for-byte where applicable?

Answer: yes for the preserved archive/standalone files and the extracted raw source files currently recorded in the repository. All 40 source raw files exist, all 40 recorded SHA-256 hashes match, all 40 text dumps exist, and all 4 preserved input files/archives exist with matching hashes.

## What Is Preserved Exactly

- Preserved input archives/files: 4
- Source records: 40
- Extracted item records: 932
- Raw source files missing: 0
- Text dumps missing: 0
- Raw hash mismatches: 0
- Preserved input files missing: 0
- Preserved input hash mismatches: 0

## What Is Not Fully Preserved Yet

- PDF text extraction does not preserve exact page/paragraph/character offsets in every extracted item.
- ZIP member CRC/compressed-size metadata is not separately recorded in the original manifest, though the consolidated manifest records preserved container and member path where inferable.
- Extracted knowledge items trace to source ID, source section, source location, and original text reference, but not always exact byte offsets.

## Fix Implemented

Created `docs/knowledge/ADE-CONSOLIDATED-SOURCE-FIDELITY-MANIFEST.json` and `docs/knowledge/ADE-CONSOLIDATED-CORPUS-MANIFEST.json`. Added `JsonManifestSourceRepository` in the runtime contract to verify source existence and SHA-256 integrity from `ADE-SOURCE-RECORDS.json`.

## Source Verification Table

| Source | Type | Raw exists | Text dump exists | Hash match | Extracted items |
| --- | --- | --- | --- | --- | ---: |
| SRC-001 | TXT | True | True | True | 93 |
| SRC-002 | TXT | True | True | True | 44 |
| SRC-003 | TXT | True | True | True | 47 |
| SRC-004 | TXT | True | True | True | 97 |
| SRC-005 | PDF | True | True | True | 7 |
| SRC-006 | TXT | True | True | True | 26 |
| SRC-007 | TXT | True | True | True | 140 |
| SRC-008 | PDF | True | True | True | 16 |
| SRC-009 | PDF | True | True | True | 46 |
| SRC-010 | PDF | True | True | True | 21 |
| SRC-011 | PDF | True | True | True | 6 |
| SRC-012 | PDF | True | True | True | 15 |
| SRC-013 | PDF | True | True | True | 8 |
| SRC-014 | PDF | True | True | True | 6 |
| SRC-015 | PDF | True | True | True | 9 |
| SRC-016 | PDF | True | True | True | 5 |
| SRC-017 | PDF | True | True | True | 7 |
| SRC-018 | PDF | True | True | True | 6 |
| SRC-019 | PDF | True | True | True | 26 |
| SRC-020 | PDF | True | True | True | 22 |
| SRC-021 | PDF | True | True | True | 25 |
| SRC-022 | PDF | True | True | True | 22 |
| SRC-023 | PDF | True | True | True | 8 |
| SRC-024 | PDF | True | True | True | 6 |
| SRC-025 | PDF | True | True | True | 66 |
| SRC-026 | PDF | True | True | True | 53 |
| SRC-027 | MD | True | True | True | 8 |
| SRC-028 | PDF | True | True | True | 7 |
| SRC-029 | PDF | True | True | True | 8 |
| SRC-030 | PDF | True | True | True | 7 |
| SRC-031 | PDF | True | True | True | 8 |
| SRC-032 | PDF | True | True | True | 8 |
| SRC-033 | PDF | True | True | True | 7 |
| SRC-034 | PDF | True | True | True | 7 |
| SRC-035 | PDF | True | True | True | 8 |
| SRC-036 | PDF | True | True | True | 8 |
| SRC-037 | PDF | True | True | True | 7 |
| SRC-038 | PDF | True | True | True | 8 |
| SRC-039 | PDF | True | True | True | 7 |
| SRC-040 | PDF | True | True | True | 7 |
