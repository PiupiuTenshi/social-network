"""Validate the PH02 Account P0 schema decision without external packages."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "docs" / "data" / "p0" / "account-schema.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def by_name(tables: list[dict[str, object]], name: str) -> dict[str, object]:
    for table in tables:
        if table["name"] == name:
            return table
    raise ValueError(f"missing table: {name}")


def main() -> None:
    document = json.loads(SCHEMA.read_text(encoding="utf-8"))
    require(document["task"] == "PH02-DATA-ACC-P0-01", "wrong task")
    database = document["database"]
    require(database["name"] == "account_db" and database["owner"] == "Account", "Account must own account_db")
    tables = document["tables"]
    require({table["name"] for table in tables} == {"account", "profile", "account_setting", "refresh_token"}, "unexpected Account P0 tables")
    account = by_name(tables, "account")
    profile = by_name(tables, "profile")
    settings = by_name(tables, "account_setting")
    refresh = by_name(tables, "refresh_token")
    require("email is unique" in account["constraints"], "email uniqueness missing")
    require("username is unique" in profile["constraints"], "username uniqueness missing")
    for table in (profile, settings, refresh):
        require(table["foreignKeys"] == [{"columns": ["account_id"], "target": "account"}], f"non-local Account FK: {table['name']}")
    require({"token_hash", "family_id", "version", "expires_at", "created_at"} <= set(refresh["columns"]), "refresh token security columns missing")
    require("token_hash is unique" in refresh["constraints"], "token hash uniqueness missing")
    require({tuple(index["columns"]) for index in refresh["indexes"]} == {("token_hash",), ("family_id", "revoked_at"), ("account_id", "expires_at")}, "refresh-token indexes are incomplete")
    require(document["migration"]["runner"] == "one approved Account runner", "migration runner policy missing")
    require(not document["migration"]["applicationStartupMigration"], "startup migration is forbidden")
    require(document["recovery"] == {"rpoHours": 24, "rtoHours": 4}, "recovery targets changed")
    print("Account P0 schema validation passed: 4 Account-owned tables, local FKs, token rotation indexes")


if __name__ == "__main__":
    main()
