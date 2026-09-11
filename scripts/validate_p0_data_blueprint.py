"""Validate PH00 P0 data planning artifacts using only the standard library."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT = ROOT / "docs" / "data" / "p0" / "data-blueprint.json"
REQUIRED_CHAT = {"conversation", "conversation_member", "message", "message_read_cursor", "notification", "inbox_message", "outbox_message"}
REQUIRED_FEED = {"feed_entry", "feed_user_summary", "feed_post_summary", "projection_checkpoint", "rebuild_run", "inbox_message"}
VERSIONED = {("account_db", "account"), ("account_db", "profile"), ("social_db", "post"), ("social_db", "comment"), ("chat_db", "conversation"), ("chat_db", "message"), ("feed_db", "feed_entry")}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    blueprint = json.loads(BLUEPRINT.read_text(encoding="utf-8"))
    require(blueprint["authority"] == "ADR-0012", "blueprint authority must be ADR-0012")
    databases = {row["name"]: row for row in blueprint["databases"]}
    tables = blueprint["tables"]
    keys = set()
    by_database: dict[str, set[str]] = {name: set() for name in databases}
    for table in tables:
        database = table["database"]
        name = table["name"]
        key = (database, name)
        require(database in databases, f"unknown database: {database}")
        require(key not in keys, f"duplicate table: {database}.{name}")
        require(table["owner"] == databases[database]["owner"], f"owner mismatch: {database}.{name}")
        require(table.get("primaryKey"), f"missing primary key: {database}.{name}")
        require(table.get("aggregate"), f"missing aggregate: {database}.{name}")
        require(table.get("retention"), f"missing retention: {database}.{name}")
        for index in table.get("indexes", []):
            require(index.get("columns") and index.get("accessPattern"), f"ungrounded index: {database}.{name}")
        for foreign_key in table.get("foreignKeys", []):
            target = foreign_key["target"]
            require(target.startswith(database + "."), f"cross-database FK: {database}.{name} -> {target}")
        keys.add(key)
        by_database[database].add(name)
    require(REQUIRED_CHAT <= by_database["chat_db"], "Chat schema is incomplete")
    require(REQUIRED_FEED <= by_database["feed_db"], "Feed schema is incomplete")
    require({"outbox_message", "idempotency_request"} <= by_database["account_db"], "Account transaction support missing")
    require({"outbox_message", "idempotency_request"} <= by_database["social_db"], "Social transaction support missing")
    require({"outbox_message", "inbox_message"} <= by_database["chat_db"], "Chat transaction support missing")
    for database, name in VERSIONED:
        table = next(item for item in tables if item["database"] == database and item["name"] == name)
        require("version" in table["columns"], f"version missing: {database}.{name}")
    post = next(item for item in tables if item["database"] == "social_db" and item["name"] == "post")
    require("type = 'content' in P0" in post.get("checks", []), "P0 post must be text-only content type")
    policy = blueprint["projectionPolicy"]
    require(policy["checkpointRequired"] and policy["exportRequired"] and not policy["kafkaIsBackup"], "rebuild policy incomplete")
    require(policy["onRetentionGap"] == "full controlled rebuild", "retention-gap policy incomplete")
    migration = blueprint["migrationPolicy"]
    require(not migration["applicationStartupMigration"], "application startup migrations are forbidden")
    require(migration["p0RpoHours"] <= 24 and migration["p0RtoHours"] <= 4, "P0 recovery targets exceed baseline")
    print(f"P0 data blueprint validation passed: {len(databases)} databases, {len(tables)} tables, no cross-database FKs")


if __name__ == "__main__":
    main()
