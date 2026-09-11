#!/usr/bin/env python3
"""Kiểm tra tính toàn vẹn của bộ tài liệu Vibe Coding."""
from __future__ import annotations

import json
import py_compile
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from kit_inventory import kit_files

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "RULES.md",
    "rule.md",
    "docs/START_HERE.md",
    "docs/PROJECT_CONTEXT.md",
    "docs/ARCHITECTURE.md",
    "docs/SERVICE_BOUNDARIES.md",
    "docs/DEFINITION_OF_READY.md",
    "docs/DEFINITION_OF_DONE.md",
    "docs/GIT_FLOW.md",
    "docs/GIT_COMMANDS.md",
    "docs/PROMPT_USAGE_EXAMPLES.md",
    "docs/PARALLEL_AGENT_WORKFLOW.md",
    "docs/reference/SOURCE_BASELINE.md",
    "prompts/$build-project-prompts.md",
    "prompts/00-master-orchestrator.md",
    "prompts/23-test-evidence-review.md",
    "templates/SERVICE_AGENTS.md",
    ".ai/context-map.yaml",
    "scripts/build_context.py",
    "scripts/generate_prompt_pack.py",
    "scripts/validate_prompt_pack.py",
    "scripts/validate_all.py",
    "scripts/sync_root_design.py",
    "FRONTEND_START_HERE.md",
    "design.md",
    "design/design.md",
    "design/review/FINAL_REVIEW_GALLERY_STANDALONE.html",
    "design/sources/18-backend-contract-gaps.md",
    "design/sources/19-frontend-contract-readiness.md",
    "source-documents/README.md",
    "source-documents/SocialPlatform_ThietKeHeThongChiTiet_BanCuoi_v3_0.docx",
    "source-documents/SocialPlatform_ThietKeHeThongChiTiet_BanCuoi_v3_0.pdf",
    "docs/execution/README.md",
    "docs/execution/plan.json",
    "docs/execution/state.json",
    "scripts/task_gate.py",
    "scripts/build_execution_plan.py",
    "scripts/test_task_gate.py",
]
MANIFEST_ENTRY = re.compile(r"^- `(.+)`$")
BAD_CHARACTERS = {"\x00": "NUL", "\ufffe": "U+FFFE", "\ufffd": "ký tự thay thế"}


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Thiếu hoặc rỗng: {relative}")

    try:
        mapping = json.loads((ROOT / ".ai/context-map.yaml").read_text(encoding="utf-8"))
        paths: list[str] = list(mapping.get("base", []))
        for group_name in ("domains", "task_types"):
            group = mapping.get(group_name, {})
            if not isinstance(group, dict):
                errors.append(f"context-map.yaml: {group_name} phải là object")
                continue
            for values in group.values():
                if not isinstance(values, list):
                    errors.append(f"context-map.yaml: giá trị trong {group_name} phải là mảng")
                    continue
                paths.extend(values)
        for relative in sorted(set(paths)):
            if not (ROOT / relative).is_file():
                errors.append(f"Context map trỏ tới tệp thiếu: {relative}")
    except Exception as exc:  # noqa: BLE001 - validator must report every parse failure
        errors.append(f"Không đọc được context map: {exc}")

    for path in kit_files(ROOT):
        if path.suffix != ".md":
            continue
        relative = path.relative_to(ROOT)
        if path.stat().st_size == 0:
            errors.append(f"Markdown rỗng: {relative}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for character, label in BAD_CHARACTERS.items():
            if character in text:
                errors.append(f"{relative} chứa {label}")

    with tempfile.TemporaryDirectory(prefix="vibe-kit-pyc-") as temp_dir:
        temp_root = Path(temp_dir)
        for path in (ROOT / "scripts").glob("*.py"):
            try:
                py_compile.compile(
                    str(path),
                    cfile=str(temp_root / f"{path.stem}.pyc"),
                    doraise=True,
                )
            except py_compile.PyCompileError as exc:
                errors.append(f"Python không biên dịch được: {path.name}: {exc.msg}")

    agents_lines = len((ROOT / "AGENTS.md").read_text(encoding="utf-8").splitlines())
    if agents_lines > 500:
        errors.append(f"AGENTS.md quá dài: {agents_lines} dòng")

    manifest = ROOT / "MANIFEST.md"
    actual_files = {
        path.relative_to(ROOT).as_posix()
        for path in kit_files(ROOT)
        if path != ROOT / "MANIFEST.md"
    }
    if manifest.is_file():
        listed = []
        for line in manifest.read_text(encoding="utf-8").splitlines():
            match = MANIFEST_ENTRY.fullmatch(line)
            if match:
                listed.append(match.group(1))
        listed_files = set(listed)
        for relative in sorted(listed_files - actual_files):
            errors.append(f"MANIFEST trỏ tới tệp thiếu: {relative}")
        for relative in sorted(actual_files - listed_files):
            errors.append(f"MANIFEST thiếu tệp: {relative}")
        if len(listed) != len(listed_files):
            errors.append("MANIFEST có mục trùng lặp")
    else:
        errors.append("Thiếu MANIFEST.md")

    link_check = subprocess.run(
        [sys.executable, "-X", "utf8", str(ROOT / "scripts/check_markdown_links.py")],
        check=False,
    )
    if link_check.returncode:
        errors.append("Kiểm tra liên kết Markdown thất bại")

    if errors:
        print("Bộ tài liệu chưa hợp lệ:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    file_count = len(actual_files) + 1  # cộng MANIFEST.md
    print(f"Bộ tài liệu Vibe Coding hợp lệ: {file_count} tệp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
