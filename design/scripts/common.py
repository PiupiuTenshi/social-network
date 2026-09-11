#!/usr/bin/env python3
"""Shared helpers for the Twight Light UI/UX design kit."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "data" / "screen-inventory.json"
APPROVAL_PATH = ROOT / "review" / "approval-status.yaml"


def load_inventory() -> list[dict[str, Any]]:
    data = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("screen-inventory.json phải là một mảng.")
    return data


def load_approval() -> dict[str, Any]:
    data = yaml.safe_load(APPROVAL_PATH.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError("approval-status.yaml phải là một object YAML.")
    data.setdefault("screens", {})
    data.setdefault("shared", {})
    return data


def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, text
    meta = yaml.safe_load(parts[1]) or {}
    return meta, parts[2].lstrip()


def screen_slug(item: dict[str, Any]) -> str:
    return Path(item["file"]).stem


def normalize_screen_body(body: str) -> str:
    """Make a screen document safe to concatenate at repository root."""
    body = body.replace("../../assets/", "assets/")
    # Review status is injected from approval-status.yaml by the builder.
    body = re.sub(r"\n## Ghi chú duyệt\n.*\Z", "\n", body, flags=re.S)
    return body.rstrip() + "\n"


def approval_summary(approval: dict[str, Any]) -> dict[str, int]:
    result = {"approved": 0, "draft": 0, "needs_changes": 0, "deferred": 0, "other": 0}
    for info in approval.get("screens", {}).values():
        status = str((info or {}).get("status", "draft"))
        if status in result:
            result[status] += 1
        else:
            result["other"] += 1
    return result
