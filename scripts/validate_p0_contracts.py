"""Validate the accepted P0 planning contracts without third-party packages."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "contracts" / "p0"
REQUIRED_PATHS = {
    "/users/me", "/users/me/settings", "/users/me/relationships",
    "/users/me/blocks", "/posts/{postId}/comments", "/conversations",
    "/conversations/{conversationId}",
}
REQUIRED_OPERATIONS = {
    "getCurrentUser", "getCurrentSettings", "listRelationships", "listBlocks",
    "listPostComments", "listConversations", "getConversation", "createPost",
    "editMessage", "blockUser", "receiveFederationInbox", "refreshSession",
}
REQUIRED_ENVELOPE = {
    "eventId", "eventType", "eventVersion", "occurredAt", "producer",
    "correlationId", "aggregateId", "aggregateVersion", "scope", "data",
}


def load(name: str) -> dict:
    with (CONTRACT / name).open(encoding="utf-8") as stream:
        return json.load(stream)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    openapi = load("openapi.json")
    asyncapi = load("asyncapi.json")
    fixtures = load("fixtures.json")
    require(openapi.get("openapi", "").startswith("3.1"), "OpenAPI 3.1 is required")
    paths = openapi["paths"]
    require(REQUIRED_PATHS <= set(paths), "missing locked P0 read path")
    operation_ids: set[str] = set()
    for path, methods in paths.items():
        for method, operation in methods.items():
            if method not in {"get", "post", "patch", "delete"}:
                continue
            operation_id = operation.get("operationId")
            require(bool(operation_id), f"{path} {method} lacks operationId")
            require(bool(operation.get("x-permission")), f"{operation_id} lacks permission")
            require(bool(operation.get("responses")), f"{operation_id} lacks responses")
            operation_ids.add(operation_id)
    require(REQUIRED_OPERATIONS <= operation_ids, "missing locked P0 operation")
    schemas = openapi["components"]["schemas"]
    require("mediaRefs" not in schemas["TextPostCreateRequest"].get("properties", {}), "P0 must be text-only")
    require({"code", "message", "correlationId"} <= set(schemas["Error"]["properties"]["error"]["required"]), "error envelope incomplete")
    refresh = paths["/auth/refresh"]["post"]
    require(refresh.get("x-permission") == "refresh-cookie", "refresh must use refresh-cookie permission")
    require(schemas["Session"].get("x-client-storage") == "memory-only", "access token storage policy missing")

    require(asyncapi.get("asyncapi") == "2.6.0", "AsyncAPI 2.6 is required")
    event_schema = asyncapi["components"]["schemas"]["EventEnvelope"]
    require(REQUIRED_ENVELOPE <= set(event_schema["required"]), "event envelope incomplete")
    scope_required = event_schema["properties"]["scope"]["required"]
    require({"visibility", "policyVersion"} <= set(scope_required), "event privacy scope incomplete")
    messages = asyncapi["components"]["messages"]
    require(messages["MessageEdited"].get("x-signalr-projection") == "MessageUpdated", "message projection conflict")
    require(messages["ChannelCreated"].get("x-partition-key") == "communityId", "channel partition conflict")
    require(messages["ModerationReportOpened"].get("x-partition-key") == "reportId", "moderation partition conflict")
    require({"UserPrivacySettingsChanged", "UserBlocked", "UserUnblocked"} <= set(messages), "privacy propagation messages absent")

    api_fixtures = fixtures["api"]
    fixture_operations = {item["operationId"] for item in api_fixtures}
    require({"getCurrentUser", "getCurrentSettings", "listBlocks", "listPostComments", "listConversations", "editMessage", "createPost", "getPost", "refreshSession"} <= fixture_operations, "API fixture coverage incomplete")
    fixture_errors = {item.get("error") for item in api_fixtures}
    require({"precondition_failed", "idempotency_key_conflict", "media_not_available_in_p0", "privacy_policy_denied", "refresh_reused"} <= fixture_errors, "negative fixture coverage incomplete")
    for event in fixtures["events"]:
        envelope = event["envelope"]
        require(REQUIRED_ENVELOPE <= set(envelope), f"{event['id']} envelope incomplete")
        require(event["message"] in messages, f"unknown fixture message {event['message']}")
    replay = next(item for item in fixtures["events"] if item["id"] == "replay-preserves-correlation")["envelope"]
    require(replay["eventId"] == "e-original" and replay["correlationId"] == "corr-original" and "replay" in replay, "replay identity rule missing")
    print(f"P0 contract validation passed: {len(operation_ids)} operations, {len(messages)} messages, {len(api_fixtures)} API fixtures, {len(fixtures['events'])} event fixtures")


if __name__ == "__main__":
    main()
