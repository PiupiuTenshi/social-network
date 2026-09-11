# P0 contract baseline

This directory is the implementation input accepted by ADR-0011. It is a planning
artifact, not proof of a deployed service.

| Artifact | Purpose |
| --- | --- |
| `openapi.json` | HTTP P0 operations, DTOs, error envelope, permissions and ETags |
| `asyncapi.json` | Durable Kafka events, partitioning, actor/scope and replay rules |
| `fixtures.json` | Positive and negative contract cases, including privacy and real-time projection |

## P0 API conventions

All responses use JSON. Errors use `{ "error": { "code", "message",
"correlationId" } }`. An authenticated caller is required unless an operation says
otherwise. Resource permissions are checked after authentication and return `403`.
An absent resource returns `404`. Rate limiting returns `429`; unavailable
dependencies return `503`.

Writes that mutate an aggregate return an `ETag`. `PATCH` and destructive commands
require `If-Match`; stale versions return `412 precondition_failed`. `409 conflict`
means a semantic conflict, including reuse of an idempotency key for a different
request. See ADR-0011 for the complete distinction.

## Locked P0 operation groups

| Group | Operations |
| --- | --- |
| Account | register, login, logout, current user, current settings, patch settings |
| Social | list/create/delete relationships, list/create/delete blocks |
| Feed | list/create/get/patch/delete posts, list/create comments |
| Chat | list/get/create conversations, list/create/edit/delete messages |
| Federation | discover actor, fetch actor document, receive inbox activity |

The named P0 reads are explicit operations rather than UI assumptions. P1/P2
features (media, full-text search, moderation workflows, federation delivery and
advanced channels) remain disabled references; their inclusion here would require
a new task and contract.

## Durable and real-time conventions

The AsyncAPI document defines durable messages. The only P0 message editing event
is `MessageEdited`. A SignalR client observes `MessageUpdated` after the durable
write has committed. A SignalR reconnect must reload HTTP state; it cannot replay
the durable log.

Privacy events include a policy version. A consumer that lacks the corresponding
policy or authorization must withhold the projection and request a fresh permitted
read. This makes propagation fail closed.

