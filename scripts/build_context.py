#!/usr/bin/env python3
"""Tạo bản đồ bối cảnh tối thiểu theo miền và loại nhiệm vụ."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / ".ai" / "context-map.yaml"


def unique(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def load_mapping() -> dict:
    try:
        data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Không đọc được {MAP_PATH.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(data.get("base"), list):
        raise SystemExit("context-map.yaml thiếu mảng base")
    return data


def build_map(data: dict, domain: str, task_type: str) -> tuple[list[tuple[str, str]], list[str]]:
    groups = [
        ("Nền dự án", data.get("base", [])),
        (f"Miền {domain}", data.get("domains", {}).get(domain, [])),
        (f"Loại nhiệm vụ {task_type}", data.get("task_types", {}).get(task_type, [])),
    ]
    rows: list[tuple[str, str]] = []
    seen: set[str] = set()
    for group, paths in groups:
        for rel in paths:
            if rel not in seen:
                seen.add(rel)
                rows.append((group, rel))
    missing = [rel for _, rel in rows if not (ROOT / rel).is_file()]
    return rows, missing


def render_map(domain: str, task_type: str, rows: list[tuple[str, str]], missing: list[str]) -> str:
    lines = [
        "# Bản đồ bối cảnh nhiệm vụ",
        "",
        f"- Miền: `{domain}`",
        f"- Loại nhiệm vụ: `{task_type}`",
        f"- Thư mục gốc khi tạo: `{ROOT}`",
        "",
        "## Nguồn phải đọc",
        "",
        "| Nhóm | Tệp | Trạng thái |",
        "| --- | --- | --- |",
    ]
    missing_set = set(missing)
    for group, rel in rows:
        status = "Thiếu - phải xác minh" if rel in missing_set else "Có"
        lines.append(f"| {group} | `{rel}` | {status} |")
    lines += [
        "",
        "## Bằng chứng kho mã phải bổ sung trước khi triển khai",
        "",
        "- `git status` và phần khác biệt chưa commit.",
        "- Tệp khai báo phiên bản, dependency, solution/workspace và cấu hình build.",
        "- Điểm vào, lớp/phương thức, call site và luồng dữ liệu thực tế.",
        "- Kiểm thử tương tự, fixture và lệnh kiểm chứng có thật.",
        "- OpenAPI, lược đồ sự kiện, migration và cấu hình tích hợp bị ảnh hưởng.",
        "",
        "## Cách sử dụng",
        "",
        "1. Đọc trực tiếp các tệp trên; không xem bản đồ này là bản sao của nguồn.",
        "2. Ghi tệp/ký hiệu cụ thể vào kế hoạch sau khi khảo sát mã.",
        "3. Tách rõ dữ kiện, suy luận, giả định và điểm chưa biết.",
        "4. Không đoán phiên bản, đường dẫn, lệnh hoặc hành vi hiện tại.",
        "5. Dừng khi điểm chưa biết có thể làm đổi hợp đồng, dữ liệu, bảo mật, kiến trúc hoặc thao tác phá hủy.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def append_embedded(content: str, rows: list[tuple[str, str]], max_chars: int) -> str:
    remaining = max_chars
    parts = [content.rstrip(), "", "---", "", "# Nội dung nguồn được nhúng theo yêu cầu", ""]
    for _, rel in rows:
        path = ROOT / rel
        if not path.is_file() or remaining <= 0:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text) > remaining:
            text = text[:remaining].rstrip() + "\n\n[ĐÃ CẮT DO GIỚI HẠN BỐI CẢNH]"
        parts += [f"## `{rel}`", "", text.rstrip(), ""]
        remaining -= len(text)
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    data = load_mapping()
    domains = sorted(data.get("domains", {}))
    task_types = sorted(data.get("task_types", {}))

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", required=True, choices=domains)
    parser.add_argument("--task-type", required=True, choices=task_types)
    parser.add_argument("--output")
    parser.add_argument("--list-only", action="store_true")
    parser.add_argument("--embed", action="store_true", help="Nhúng nội dung nguồn; mặc định chỉ tạo bản đồ")
    parser.add_argument("--max-chars", type=int, default=120_000)
    args = parser.parse_args()

    if args.max_chars < 1_000:
        raise SystemExit("--max-chars phải từ 1000 trở lên")

    rows, missing = build_map(data, args.domain, args.task_type)
    if missing:
        raise SystemExit("Thiếu tệp bối cảnh: " + ", ".join(missing))

    if args.list_only:
        print("\n".join(rel for _, rel in rows))
        return 0

    content = render_map(args.domain, args.task_type, rows, missing)
    if args.embed:
        content = append_embedded(content, rows, args.max_chars)

    if args.output:
        output = Path(args.output)
        if not output.is_absolute():
            output = ROOT / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
        print(output)
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
