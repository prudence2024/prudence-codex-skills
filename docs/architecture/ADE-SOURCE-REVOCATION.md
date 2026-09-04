# ADE Source Revocation

Source revocation propagates deterministically from source ID to derived knowledge items through `SourceRevocationService`, which archives derived items and emits a structured `source_revoked` event. Archived and superseded items are excluded from default retrieval.
