#!/usr/bin/env python3
"""Validate structure, metadata, links, images, tokens and approval state."""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from PIL import Image

from common import ROOT, load_approval, load_inventory, split_front_matter

ALLOWED_PRIORITIES = {"P0", "P1", "P2"}
ALLOWED_STATUSES = {"draft", "needs_changes", "approved", "deferred"}
REQUIRED_SCREEN_KEYS = {
    "id", "title", "group", "route", "priority", "status", "roles", "functions", "desktop_svg", "mobile_svg"
}


def check_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)", text):
        raw = next((x for x in target if x), "").strip()
        if not raw or raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = raw.split("#", 1)[0].replace("%20", " ")
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)} có liên kết thoát khỏi bộ thiết kế: {raw}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)} có liên kết hỏng: {raw}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-final", action="store_true", help="Yêu cầu design.md tồn tại và cổng duyệt đạt.")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    inventory = load_inventory()
    approval = load_approval()

    ids: set[str] = set()
    paths: set[str] = set()
    for item in inventory:
        sid = str(item.get("id", ""))
        if sid in ids:
            errors.append(f"Mã màn hình trùng: {sid}")
        ids.add(sid)
        file_rel = str(item.get("file", ""))
        if file_rel in paths:
            errors.append(f"Đường dẫn đặc tả trùng: {file_rel}")
        paths.add(file_rel)
        path = ROOT / file_rel
        if not path.exists():
            errors.append(f"Thiếu đặc tả màn hình: {file_rel}")
            continue
        meta, body = split_front_matter(path.read_text(encoding="utf-8"))
        missing = REQUIRED_SCREEN_KEYS - set(meta)
        if missing:
            errors.append(f"{file_rel} thiếu front matter: {', '.join(sorted(missing))}")
        if meta.get("id") != sid:
            errors.append(f"{file_rel}: id không khớp inventory ({meta.get('id')} != {sid})")
        if meta.get("priority") not in ALLOWED_PRIORITIES:
            errors.append(f"{file_rel}: priority không hợp lệ: {meta.get('priority')}")
        if meta.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{file_rel}: status không hợp lệ: {meta.get('status')}")
        for key in ("desktop_svg", "mobile_svg"):
            rel = meta.get(key)
            if not rel or not (ROOT / rel).exists():
                errors.append(f"{file_rel}: thiếu {key}: {rel}")
        if "## Trạng thái bắt buộc" not in body:
            errors.append(f"{file_rel}: thiếu phần Trạng thái bắt buộc")
        if "## Accessibility" not in body:
            errors.append(f"{file_rel}: thiếu phần Accessibility")
        check_markdown_links(path, errors)

    approval_screens = approval.get("screens", {})
    for sid in ids:
        if sid not in approval_screens:
            errors.append(f"approval-status.yaml thiếu {sid}")
            continue
        status = str((approval_screens.get(sid) or {}).get("status", ""))
        if status not in ALLOWED_STATUSES:
            errors.append(f"approval-status.yaml: {sid} có status không hợp lệ: {status}")
    extra = set(approval_screens) - ids
    if extra:
        warnings.append(f"approval-status.yaml có mã không còn trong inventory: {', '.join(sorted(extra))}")

    expected = {
        "desktop_svg": ROOT / "assets/editable/svg/desktop",
        "mobile_svg": ROOT / "assets/editable/svg/mobile",
        "desktop_png": ROOT / "assets/preview/png/desktop",
        "mobile_png": ROOT / "assets/preview/png/mobile",
    }
    for label, directory in expected.items():
        if not directory.exists():
            errors.append(f"Thiếu thư mục {directory.relative_to(ROOT)}")
            continue
        suffix = ".svg" if "svg" in label else ".png"
        count = len(list(directory.glob(f"*{suffix}")))
        if count != len(inventory):
            errors.append(f"{label} có {count} tệp, kỳ vọng {len(inventory)}")

    for svg in (ROOT / "assets/editable").rglob("*.svg"):
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"SVG không hợp lệ {svg.relative_to(ROOT)}: {exc}")
        text = svg.read_text(encoding="utf-8")
        if re.search(r'fill="\d+(?:\.\d+)?"|stroke-width="none"', text):
            errors.append(f"SVG có thuộc tính hình học sai: {svg.relative_to(ROOT)}")

    for kind, size in (("desktop", (1440, 1024)), ("mobile", (780, 1688))):
        for png in (ROOT / f"assets/preview/png/{kind}").glob("*.png"):
            try:
                with Image.open(png) as im:
                    if im.size != size:
                        errors.append(f"{png.relative_to(ROOT)} có kích thước {im.size}, kỳ vọng {size}")
            except Exception as exc:
                errors.append(f"Không đọc được PNG {png.relative_to(ROOT)}: {exc}")

    token_json = ROOT / "tokens/design-tokens.json"
    try:
        json.loads(token_json.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"design-tokens.json không hợp lệ: {exc}")

    for md in ROOT.rglob("*.md"):
        if md.name in {"DESIGN_DRAFT.md", "design.md", "MANIFEST.md"}:
            continue
        check_markdown_links(md, errors)

    if args.require_final:
        final = ROOT / "design.md"
        if not final.exists():
            errors.append("Thiếu design.md. Hãy duyệt và chạy build_design.py --final.")
        for sid, info in approval_screens.items():
            info = info or {}
            required = bool(info.get("required", False))
            status = info.get("status", "draft")
            if required and status != "approved":
                errors.append(f"{sid} bắt buộc nhưng chưa approved.")
            if not required and status not in {"approved", "deferred"}:
                errors.append(f"{sid} tùy chọn nhưng chưa approved/deferred.")
        for key in ("sources", "tokens", "flows", "boards"):
            if approval.get("shared", {}).get(key) != "approved":
                errors.append(f"Khối dùng chung {key} chưa approved.")

    print(f"Màn hình: {len(inventory)}")
    print(f"SVG: {len(list((ROOT / 'assets/editable').rglob('*.svg')))}")
    print(f"PNG: {len(list((ROOT / 'assets/preview').rglob('*.png')))}")
    for warning in sorted(set(warnings)):
        print(f"CẢNH BÁO: {warning}")
    if errors:
        print("\nKHÔNG ĐẠT:")
        for error in sorted(set(errors)):
            print(f"- {error}")
        sys.exit(1)
    print("ĐẠT: cấu trúc, metadata, liên kết, SVG, PNG và token hợp lệ.")


if __name__ == "__main__":
    main()
