# ADR-0011: P0 contract baseline

- Status: Accepted
- Date: 2026-09-07
- Decision owner: project owner, delegated to this PH00 planning task
- Supersedes: only the conflicting P0 portions of the reference catalogs named below

## Context

The audited baseline has contradictions in optimistic concurrency, read endpoints,
message event names, topic partitioning, and privacy propagation.  A UI approval is
not an API approval.  This decision supplies a machine-readable P0 baseline in
[`../contracts/p0/`](../contracts/p0/) without claiming that product code exists.

## Decisions

1. `If-Match` carries the current aggregate ETag.  A stale ETag returns `412
   precondition_failed`.  `409 conflict` is reserved for a valid request that
   conflicts with current business state, including reuse of an idempotency key
   with a different payload.  Repeating the same idempotent request returns its
   original successful response.
2. The P0 read surface includes `GET /users/me`, `GET /users/me/settings`,
   `GET /users/me/relationships`, `GET /users/me/blocks`,
   `GET /posts/{postId}/comments`, `GET /conversations`, and
   `GET /conversations/{conversationId}`. Collection reads use an opaque
   `cursor` and return `items` and nullable `nextCursor`.
3. Kafka domain messages use past-tense names. `MessageEdited` is the canonical
   durable event. SignalR is a client notification projection and uses
   `MessageUpdated`; it is not a source of truth. Persistent writes commit before
   a notification is emitted.
4. The `community.lifecycle.v1` topic is partitioned by `communityId`.
   `ChannelCreated` retains `channelId` in its data and has `communityId` as its
   aggregate id. The future `social.moderation.v1` topic is partitioned by
   `reportId`; `targetId` is data, never a competing key. Replays retain the
   original `eventId` and `correlationId`, and append `replay.runId`,
   `replay.requestedBy`, and `replay.originalOccurredAt`.
5. Each durable event has `aggregateId`, monotonic `aggregateVersion`, optional
   actor subject/kind, and a minimum privacy `scope` (visibility and policy
   version). Audience member lists and direct PII do not travel in event payloads.
   Consumers resolve authorized projections and fail closed when policy state is
   unavailable.
6. `UserPrivacySettingsChanged`, `UserBlocked`, and `UserUnblocked` propagate
   policy changes. Feed, social, and chat projections invalidate or withhold data
   when the policy version is stale. Read and real-time delivery authorize again at
   the consumer boundary.
7. P0 post and chat content are text-only. `mediaRefs` is absent from P0 write
   schemas and a request containing it fails with `422 media_not_available_in_p0`.
   P1/P2 contracts remain reference-only and disabled by default outside
   development.

## Consequences

The authoritative implementation inputs are `openapi.json`, `asyncapi.json`, and
`fixtures.json` in `docs/contracts/p0`. Existing reference catalogs remain audit
evidence; a later catalog synchronization task must cite this ADR rather than
silently overwrite it. Any scope expansion, external audience delivery, media,
or new topic must receive its own approved decision and contract test.

