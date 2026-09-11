#!/usr/bin/env python3
"""Kiểm tra cấu trúc và các cổng an toàn cơ bản của một bộ prompt."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = [
    "00-input.md",
    "01-context.md",
    "02-plan.md",
    "03-implementation-prompt.md",
    "04-test-prompt.md",
    "05-review-prompt.md",
    "06-docs-sync-prompt.md",
    "07-handoff-template.md",
]
REQUIRED_TEXT = {
    "01-context.md": ["Nguồn phải đọc", "Bằng chứng kho mã"],
    "02-plan.md": ["Chế độ thực hiện", "Quy trình", "Điều kiện dừng"],
    "03-implementation-prompt.md": ["Tiêu chí chấp nhận", "Quy trình", "Điều kiện dừng"],
    "04-test-prompt.md": ["Kiểm thử", "Tiêu chí chấp nhận"],
    "05-review-prompt.md": ["Rà soát", "bằng chứng"],
    "06-docs-sync-prompt.md": ["Đồng bộ", "tài liệu"],
    "07-handoff-template.md": ["Kiểm chứng", "Tiêu chí chấp nhận"],
}
PLACEHOLDER = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder")
    args = parser.parse_args()
    folder = Path(args.folder).resolve()
    errors: list[str] = []

    if not folder.is_dir():
        print(f"Không tìm thấy thư mục: {folder}")
        return 2

    for name in REQUIRED:
        path = folder / name
        if not path.is_file():
            errors.append(f"Thiếu {name}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) < 120:
            errors.append(f"{name} quá ngắn")
        if "\x00" in text:
            errors.append(f"{name} chứa ký tự NUL")
        placeholders = sorted(set(PLACEHOLDER.findall(text)))
        if placeholders:
            errors.append(f"{name} còn biến chưa thay: {', '.join(placeholders)}")
        for token in REQUIRED_TEXT.get(name, []):
            if token.casefold() not in text.casefold():
                errors.append(f"{name} thiếu nội dung: {token}")

    input_path = folder / "00-input.md"
    if input_path.is_file():
        input_text = input_path.read_text(encoding="utf-8", errors="replace")
        if "Không commit, push" not in input_text and "không commit, push" not in input_text:
            errors.append("00-input.md thiếu ranh giới quyền commit/push/deploy")

    extras = sorted(p.name for p in folder.glob("*.md") if p.name not in REQUIRED)
    if extras:
        errors.append("Có tệp Markdown ngoài bộ chuẩn: " + ", ".join(extras))

    if errors:
        print("Bộ prompt chưa hợp lệ:")
        print("\n".join(f"- {item}" for item in errors))
        return 1

    print(f"Bộ prompt hợp lệ: {folder}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
