# ADE Ingestion Architecture

Status: Phase 2.1 architecture specification only. This document does not implement ingestion, crawlers, OCR, scraping, embeddings, or storage.

## Purpose

ADE ingestion should convert permitted sources into provenance-preserving raw source records and candidate knowledge. Ingestion must not imply validation or belief.

## Supported Source Classes

The abstract architecture should support:

- Markdown
- PDF
- DOCX
- TXT
- CSV
- JSON
- Web pages
- GitHub repositories
- Official documentation
- Chat exports
- User notes
- Images
- Future media

## Ingestion Flow

```text
Source registration
-> Permission and access check
-> Format detection
-> Raw capture or reference
-> Metadata extraction
-> Content extraction
-> Candidate item extraction
-> Provenance record
-> Privacy/license review
-> Normalization handoff
```

## Source Registration

Before ingestion, ADE should know:

- source identity;
- source owner or author when known;
- access scope;
- license/terms when known;
- source type;
- project/user scope;
- ingestion purpose;
- retention expectations.

## Format Requirements

- Markdown/TXT: preserve headings, links, code blocks, and source paths.
- PDF/DOCX: preserve title, page/section references, author metadata when available, and extraction confidence.
- CSV/JSON: preserve schema, column names, record boundaries, and type hints.
- Web pages: preserve URL, fetched time, canonical URL, title, update date when available, and crawl permission.
- GitHub repositories: preserve repository URL, commit/ref, license, file paths, and timestamps.
- Chat exports/user notes: distinguish user statements, assistant output, timestamps, and privacy scope.
- Images/future media: preserve file metadata, source, rights, derived observations, and extraction uncertainty.

## Privacy And Security Gate

Before content is retained, check for:

- secrets and credentials;
- personal information;
- private project data;
- third-party content restrictions;
- license constraints;
- access-control requirements;
- irrelevant sensitive material.

Secrets must not be ingested into the knowledge layer.

## Output

Ingestion should output a raw source record and candidate extracted items, not validated knowledge.

```text
SOURCE_RECORD:
SOURCE_TYPE:
ACCESS_SCOPE:
LICENSE:
OBSERVED_AT:
EXTRACTION_METHOD:
EXTRACTION_CONFIDENCE:
CANDIDATES:
PRIVACY_NOTES:
NEXT_STAGE:
```

## User-Provided Knowledge

User content must be classified before promotion:

- user-provided fact;
- user opinion;
- user preference;
- user project decision;
- user hypothesis;
- user-created material.

User-provided content can be authoritative for user/project intent while still uncertain for external facts.

## External Knowledge

External knowledge ingestion must preserve freshness, source authority, and terms. Fast-moving sources should receive review schedules or stale-risk labels.

## Related Documents

- [ADE-KNOWLEDGE-LIFECYCLE.md](ADE-KNOWLEDGE-LIFECYCLE.md)
- [ADE-PROVENANCE-AND-CONFIDENCE.md](ADE-PROVENANCE-AND-CONFIDENCE.md)
- [ADE-KNOWLEDGE-MODEL.md](ADE-KNOWLEDGE-MODEL.md)
