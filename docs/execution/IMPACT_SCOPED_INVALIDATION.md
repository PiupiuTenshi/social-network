# Impact-scoped invalidation

Use this after a task changes an accepted output. It reduces unrelated revalidation
without weakening the gate.

1. Add `dependency_scopes` only for the exact predecessor output the task consumes.
   Leave an edge unannotated when its dependency is broad or uncertain.
2. In the changed task's completion receipt, classify the change as `none`, `additive`,
   or `breaking`, list scopes, explain the decision, and point to already-hashed
   reviewable artifacts.
3. A reviewer checks the classification. Use `breaking` and `*` for any removed,
   renamed, behavior-changing, permission-changing, or uncertain contract/data/event
   change.
4. Run `task_gate.py check ID`. A non-overlapping additive or none impact may leave a
   direct successor valid. All other results require the normal DoR and evidence flow.

Examples:

| Change | Classification | Scope |
| --- | --- | --- |
| Add browser refresh-cookie operation | additive | `contract:auth:refresh` |
| Evidence-only rerun with no delivered-output change | none | `[]` |
| Remove or change an existing API DTO/permission | breaking | `[*]` |

Do not use an empty scope list to conceal an output change. The separate review is the
control that validates this claim.
