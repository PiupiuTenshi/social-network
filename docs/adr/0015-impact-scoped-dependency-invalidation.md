# ADR-0015: Impact-scoped dependency invalidation

- Status: Accepted
- Date: 2026-09-11
- Decision owner: project owner delegation

## Context

A dependency receipt previously invalidated every direct successor whenever its digest
changed. That is safe but causes unrelated planning and infrastructure work to repeat
when a narrow contract decision changes.

## Decision

Completion evidence may declare an `impact` object:

```json
{
  "classification": "none | additive | breaking",
  "scopes": ["contract:auth:refresh"],
  "summary": "What changed and why this classification is correct.",
  "artifacts": ["path/already/in/completion-manifest"]
}
```

A dependent subtask may declare `dependency_scopes` in the generated execution plan.
Scopes are hierarchical (`contract:auth` matches `contract:auth:refresh`); a terminal
`*` matches the remainder and `*` alone means all scopes.

When a predecessor receipt changes, the gate retains a dependent receipt only when all
of the following are true:

1. The predecessor is still `DONE` and its current completion evidence validates.
2. The predecessor declares `none` or `additive` impact.
3. The dependent explicitly declares scopes consumed from that predecessor.
4. The two scope sets do not overlap.

Every other case is fail-closed and requires revalidation. A `breaking` change must use
exactly `["*"]`. `none` must use an empty scope list. Completion evidence without
impact metadata is legacy and therefore fail-closed whenever its receipt changes.

## Consequences

The mechanism does not accept an unreviewed change automatically. The completion
manifest hashes its impact artifacts, and the normal separate review must verify the
classification and scopes. Source hash changes, tampered receipts/reports, missing
metadata, unknown consumer scope, and every intersecting or breaking impact continue
to invalidate work. Existing receipts receive scope metadata only through a normal
reopen → validation → review → accept cycle.
