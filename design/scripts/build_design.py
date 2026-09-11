#!/usr/bin/env python3
"""Build DESIGN_DRAFT.md or the gated final design.md."""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

from common import (
    ROOT,
    approval_summary,
    load_approval,
    load_inventory,
    normalize_screen_body,
    split_front_matter,
)

SOURCE_ORDER = [
    "00-product-goals.md",
    "01-users-jobs.md",
    "02-information-architecture.md",
    "03-navigation.md",
    "04-user-flows.md",
    "05-design-system.md",
    "06-component-library.md",
    "07-interactions-motion.md",
    "08-responsive.md",
    "09-accessibility.md",
    "10-content-style.md",
    "11-state-matrix.md",
    "12-frontend-handoff.md",
    "13-route-map.md",
    "14-analytics-events.md",
    "15-privacy-security-ux.md",
    "16-design-qa.md",
    "17-source-traceability.md",
    "18-backend-contract-gaps.md",
    "19-frontend-contract-readiness.md",
]

VALID_SCREEN_STATUSES = {"draft", "needs_changes", "approved", "deferred"}
REQUIRED_SHARED = ("sources", "tokens", "flows", "boards")


def demote_markdown_headings(text: str, levels: int = 2) -> str:
    """Demote ATX headings while preserving fenced code blocks."""
    output: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            output.append(line)
            continue
        if not in_fence:
            match = re.match(r"^(#{1,6})(\s+.*)$", line)
            if match:
                line = "#" * min(6, len(match.group(1)) + levels) + match.group(2)
        output.append(line)
    return "\n".join(output)


def final_gate(inventory: list[dict], approval: dict) -> list[str]:
    errors: list[str] = []
    screen_status = approval.get("screens", {})
    for item in inventory:
        info = screen_status.get(item["id"])
        if not isinstance(info, dict):
            errors.append(f"Thiếu trạng thái duyệt cho {item['id']}.")
            continue
        status = str(info.get("status", "draft"))
        required = bool(info.get("required", item.get("priority") in {"P0", "P1"}))
        if status not in VALID_SCREEN_STATUSES:
            errors.append(f"{item['id']} có trạng thái không hợp lệ: {status}.")
        if required and status != "approved":
            errors.append(f"{item['id']} là màn hình bắt buộc nhưng chưa approved (hiện tại: {status}).")
        if not required and status not in {"approved", "deferred"}:
            errors.append(
                f"{item['id']} là màn hình tùy chọn; trước khi khóa bản cuối phải approved hoặc deferred "
                f"(hiện tại: {status})."
            )
    shared = approval.get("shared", {})
    for key in REQUIRED_SHARED:
        if shared.get(key) != "approved":
            errors.append(f"Khối dùng chung '{key}' chưa approved.")
    return errors


def make_header(mode: str, approval: dict) -> str:
    today = dt.date.today().isoformat()
    summary = approval_summary(approval)
    final = mode == "final"
    status = "ĐÃ KHÓA ĐỂ TRIỂN KHAI FRONTEND" if final else "BẢN NHÁP ĐỂ DUYỆT"
    filename = "design.md" if final else "DESIGN_DRAFT.md"
    return f"""<!-- Tệp được sinh tự động. Không sửa trực tiếp; hãy sửa sources/, screens/, tokens/ hoặc review/approval-status.yaml. -->
# Thiết kế UI/UX Twight Light

> **Trạng thái:** {status}  
> **Tệp:** `{filename}`  
> **Ngày sinh:** {today}  
> **Phiên bản thiết kế:** 1.2 Final  
> **Nguồn nghiệp vụ:** Thiết kế hệ thống chi tiết v3.0  
> **Ngôn ngữ giao diện:** Tiếng Việt  
> **Gallery:** `review/FINAL_REVIEW_GALLERY_STANDALONE.html`

## Cách sử dụng tài liệu

- Tài liệu hệ thống/OpenAPI/AsyncAPI là nguồn chuẩn cho API, dữ liệu, quyền và sự kiện.
- Tài liệu này là nguồn chuẩn cho kiến trúc thông tin, luồng, màn hình, component, trạng thái, responsive và accessibility.
- Không suy ra endpoint hoặc quyền mới chỉ từ mockup.
- Khi hợp đồng và UI mâu thuẫn, dừng triển khai và tạo yêu cầu làm rõ hoặc ADR.
- PNG dùng để duyệt; SVG trong `assets/editable/` là nguồn hình có thể chỉnh sửa.

## Tóm tắt duyệt

| Trạng thái | Số màn hình |
|---|---:|
| Đã duyệt | {summary['approved']} |
| Bản nháp | {summary['draft']} |
| Cần chỉnh sửa | {summary['needs_changes']} |
| Hoãn | {summary['deferred']} |

"""


def make_inventory(inventory: list[dict], approval: dict, final: bool) -> str:
    rows = [
        "## Danh mục màn hình",
        "",
        "| Mã | Nhóm | Màn hình | Route | Ưu tiên | Trạng thái | Đặc tả |",
        "|---|---|---|---|---|---|---|",
    ]
    statuses = approval.get("screens", {})
    for item in inventory:
        info = statuses.get(item["id"], {}) or {}
        status = info.get("status", "draft")
        if final and status == "deferred":
            state_label = "Hoãn"
        else:
            state_label = {
                "approved": "Đã duyệt",
                "draft": "Bản nháp",
                "needs_changes": "Cần chỉnh sửa",
                "deferred": "Hoãn",
            }.get(status, str(status))
        rows.append(
            f"| {item['id']} | {item['group']} | {item['title']} | `{item['route']}` | "
            f"{item['priority']} | {state_label} | [`{item['file']}`]({item['file']}) |"
        )
    return "\n".join(rows) + "\n\n"


def build(mode: str) -> Path:
    inventory = load_inventory()
    approval = load_approval()
    if mode == "final":
        errors = final_gate(inventory, approval)
        if errors:
            print("Không thể tạo design.md vì cổng duyệt chưa đạt:\n")
            for error in errors:
                print(f"- {error}")
            raise SystemExit(2)

    final = mode == "final"
    sections: list[str] = [make_header(mode, approval), make_inventory(inventory, approval, final)]

    sections.append("## Phần I - Nền tảng thiết kế\n")
    for name in SOURCE_ORDER:
        path = ROOT / "sources" / name
        if not path.exists():
            raise FileNotFoundError(path)
        text = path.read_text(encoding="utf-8").strip()
        sections.append(demote_markdown_headings(text, 2) + "\n")

    sections.append("## Phần II - Đặc tả màn hình\n")
    statuses = approval.get("screens", {})
    for item in inventory:
        info = statuses.get(item["id"], {}) or {}
        status = info.get("status", "draft")
        if final and status == "deferred":
            continue
        screen_path = ROOT / item["file"]
        meta, body = split_front_matter(screen_path.read_text(encoding="utf-8"))
        body = demote_markdown_headings(normalize_screen_body(body), 2)
        note = str(info.get("note", "") or "").strip()
        state_label = {
            "approved": "Đã duyệt",
            "draft": "Bản nháp",
            "needs_changes": "Cần chỉnh sửa",
            "deferred": "Hoãn",
        }.get(status, str(status))
        note_line = ""
        if note and (not final or status != "approved"):
            note_line = f"  \n> **Ghi chú:** {note}"
        sections.append(
            f"\n---\n\n> **Trạng thái duyệt {item['id']}:** {state_label}"
            + note_line
            + "\n\n"
            + body
        )

    deferred = [
        item for item in inventory if (statuses.get(item["id"], {}) or {}).get("status") == "deferred"
    ]
    if final and deferred:
        sections.append("## Phần III - Màn hình hoãn\n")
        sections.append(
            "Các màn hình dưới đây không thuộc phạm vi Frontend của bản phát hành đã khóa. "
            "Không triển khai nếu chưa được duyệt lại.\n\n"
        )
        for item in deferred:
            note = (statuses.get(item["id"], {}) or {}).get("note", "")
            sections.append(f"- **{item['id']} - {item['title']}**: {note or 'Hoãn theo quyết định phạm vi.'}\n")

    sections.append("\n## Phần III - Kế hoạch triển khai Frontend\n")
    sections.append(demote_markdown_headings((ROOT / "FRONTEND_IMPLEMENTATION_PLAN.md").read_text(encoding="utf-8").strip(), 2) + "\n")
    sections.append("\n## Phần IV - Checklist chuyển thiết kế thành mã\n")
    sections.append(demote_markdown_headings((ROOT / "DESIGN_TO_CODE_CHECKLIST.md").read_text(encoding="utf-8").strip(), 2) + "\n")
    sections.append("\n## Phần V - Prompt bàn giao Frontend\n")
    sections.append(demote_markdown_headings((ROOT / "FRONTEND_IMPLEMENTATION_PROMPT.md").read_text(encoding="utf-8").strip(), 2) + "\n")

    output = ROOT / ("design.md" if final else "DESIGN_DRAFT.md")
    output.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")
    print(f"Đã tạo {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes).")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--draft", action="store_true", help="Tạo DESIGN_DRAFT.md.")
    group.add_argument("--final", action="store_true", help="Tạo design.md sau khi vượt cổng duyệt.")
    args = parser.parse_args()
    build("final" if args.final else "draft")


if __name__ == "__main__":
    main()
