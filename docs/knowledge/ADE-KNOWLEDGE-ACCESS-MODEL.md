# ADE Knowledge Access Model

## Access Scopes

| Scope | Meaning | Retrieval rule |
| --- | --- | --- |
| GLOBAL | General ADE knowledge available across projects. | Searchable by default. |
| PROJECT | Project-specific knowledge. | Returned only when project context matches. |
| PRIVATE | Private user or confidential project material. | Requires explicit future authorization boundary. |
| RESTRICTED | Licensed, sensitive, or tightly scoped source material. | Hidden from default search; exact scoped retrieval only. |

## Implemented Runtime Behavior

`KnowledgeItem` includes `access_scope`. Default search returns global material and matching project material only. Restricted/private-like records are not retrieved globally. Archived and superseded records are hidden unless `include_archived=True` is explicitly requested.

## Deferred Work

This is not authentication. Phase 2.4+ must define identity, project membership, source licensing, startup confidentiality, and deletion propagation before production retrieval.
