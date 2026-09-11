#!/usr/bin/env python3
"""Đồng bộ MANIFEST và checksums của kit; chỉ dùng sau review thay đổi."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
from kit_inventory import kit_files

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    files = [p for p in kit_files(ROOT) if p.name != "MANIFEST.md" or p.parent != ROOT]
    # checksums là thành phần của danh mục, dù đang tạo bộ kit lần đầu.
    if ROOT/"checksums.sha256" not in files:
        files.append(ROOT/"checksums.sha256")
    files.sort(key=lambda p: p.relative_to(ROOT).as_posix())
    lines = ["# Danh mục tệp — Twight Light Project Vibe Coding Kit", "", "## Thống kê", "",
             f"- Tổng tệp không tính `MANIFEST.md`: **{len(files)}**",
             f"- Prompt subtask: **{len(list((ROOT/'docs/execution/prompts').glob('*.md')))}**",
             "- Màn hình UI/UX: **47**", "", "Không liệt kê .git, work, cache hoặc artifact build/test.", "", "## Tệp", ""]
    manifest = "\n".join(lines + [f"- `{p.relative_to(ROOT).as_posix()}`" for p in files]) + "\n"
    if args.check:
        if not (ROOT/"MANIFEST.md").is_file() or (ROOT/"MANIFEST.md").read_text(encoding="utf-8") != manifest:
            print("MANIFEST lệch")
            return 1
    else:
        (ROOT/"MANIFEST.md").write_text(manifest, encoding="utf-8", newline="\n")
    checksum_files = [p for p in kit_files(ROOT) if p != ROOT/"checksums.sha256"]
    checksums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  ./{p.relative_to(ROOT).as_posix()}\n" for p in checksum_files)
    if args.check:
        if (ROOT/"checksums.sha256").read_text(encoding="utf-8") != checksums:
            print("checksums lệch (hash bytes; checkout đổi newline cần tạo snapshot phân phối mới)")
            return 1
    else:
        (ROOT/"checksums.sha256").write_text(checksums, encoding="utf-8", newline="\n")
    print(f"Inventory/checksums: OK, {len(checksum_files)} files được băm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
