#!/usr/bin/env python3
"""Sinh bộ prompt tám bước từ các prompt trung tâm của dự án."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPE_TO_PROMPT = {
    "project-bootstrap": "01-project-bootstrap.md",
    "service-scaffold": "02-service-scaffold.md",
    "feature-plan": "03-feature-spec-to-plan.md",
    "backend-feature": "04-backend-feature.md",
    "frontend-feature": "05-frontend-feature.md",
    "api": "06-api-endpoint.md",
    "database": "07-domain-and-database.md",
    "kafka": "08-kafka-event.md",
    "signalr": "09-signalr-realtime.md",
    "livekit": "10-livekit-rtc.md",
    "tests": "11-generate-tests.md",
    "bug-fix": "12-fix-bug.md",
    "refactor": "13-refactor.md",
    "code-review": "14-code-review.md",
    "security-review": "15-security-review.md",
    "performance": "16-performance-review.md",
    "migration": "17-database-migration.md",
    "release": "18-release.md",
    "docs-sync": "19-documentation-sync.md",
    "incident": "20-incident-debug.md",
    "contract-change": "21-contract-change.md",
    "pr-review": "22-pr-review.md",
}
REQUIRED_OUTPUTS = [
    "00-input.md",
    "01-context.md",
    "02-plan.md",
    "03-implementation-prompt.md",
    "04-test-prompt.md",
    "05-review-prompt.md",
    "06-docs-sync-prompt.md",
    "07-handoff-template.md",
]


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value or "CHƯA BIẾT")
    return text


def read_template(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise SystemExit(f"Thiếu tệp mẫu: {relative}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--task-type", required=True, choices=sorted(TYPE_TO_PROMPT))
    parser.add_argument("--domain", required=True)
    parser.add_argument("--function-id", default="")
    parser.add_argument("--description", required=True)
    parser.add_argument("--evidence", default="CHƯA CÓ; phải khảo sát kho mã")
    parser.add_argument(
        "--constraints",
        default="Tuân thủ AGENTS.md và RULES.md; không commit, push, merge, deploy hoặc thao tác phá hủy",
    )
    parser.add_argument(
        "--acceptance-criteria",
        default="CHƯA CHỐT; phải cụ thể hóa trong bước kế hoạch",
    )
    parser.add_argument("--output-root", default="work/tasks")
    parser.add_argument("--embed-context", action="store_true")
    parser.add_argument("--max-context-chars", type=int, default=120_000)
    parser.add_argument("--force", action="store_true", help="Ghi đè thư mục nhiệm vụ đã có")
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{1,79}", args.task_id):
        raise SystemExit("task-id phải dài 2-80 ký tự và chỉ dùng chữ, số, dấu chấm, gạch dưới hoặc gạch ngang")

    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = ROOT / output_root
    output = (output_root / args.task_id).resolve()

    if output.exists() and any(output.iterdir()):
        if not args.force:
            raise SystemExit(f"Thư mục đã có dữ liệu: {output}. Dùng --force khi thật sự muốn ghi đè.")
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    values = {
        "TASK_ID": args.task_id,
        "TASK_TYPE": args.task_type,
        "DOMAIN": args.domain,
        "FUNCTION_ID": args.function_id or "CHƯA BIẾT",
        "DESCRIPTION": args.description,
        "EVIDENCE": args.evidence,
        "CONSTRAINTS": args.constraints,
        "ACCEPTANCE_CRITERIA": args.acceptance_criteria,
    }

    input_text = f"""# Đầu vào nhiệm vụ - {args.task_id}

- Loại nhiệm vụ: `{args.task_type}`
- Miền: `{args.domain}`
- Mã chức năng hoặc vấn đề: `{args.function_id or 'CHƯA BIẾT'}`
- Kết quả mong muốn: {args.description}
- Bằng chứng hiện có: {args.evidence}
- Ràng buộc và phần ngoài phạm vi: {args.constraints}
- Tiêu chí chấp nhận ban đầu: {args.acceptance_criteria}
- Quyền thực hiện: Không commit, push, merge, deploy, chạy migration phá hủy hoặc thao tác production nếu chưa có ủy quyền riêng.
"""
    (output / "00-input.md").write_text(input_text, encoding="utf-8")

    context_command = [
        sys.executable,
        str(ROOT / "scripts" / "build_context.py"),
        "--domain",
        args.domain,
        "--task-type",
        args.task_type,
        "--output",
        str(output / "01-context.md"),
        "--max-chars",
        str(args.max_context_chars),
    ]
    if args.embed_context:
        context_command.append("--embed")
    subprocess.run(context_command, check=True)

    plan = render(read_template("prompts/03-feature-spec-to-plan.md"), values)
    implementation = render(read_template("prompts/" + TYPE_TO_PROMPT[args.task_type]), values)
    read_only_test_types = {
        "project-bootstrap",
        "feature-plan",
        "code-review",
        "release",
        "docs-sync",
        "incident",
        "contract-change",
        "pr-review",
    }
    test_prompt_name = "23-test-evidence-review.md" if args.task_type in read_only_test_types else "11-generate-tests.md"
    tests = render(read_template("prompts/" + test_prompt_name), values)
    review_name = "15-security-review.md" if args.task_type == "security-review" else "14-code-review.md"
    review = render(read_template("prompts/" + review_name), values)
    docs_sync = render(read_template("prompts/19-documentation-sync.md"), values)
    handoff = read_template("templates/IMPLEMENTATION_REPORT.md").replace("[TASK_ID]", args.task_id)

    outputs = {
        "02-plan.md": plan,
        "03-implementation-prompt.md": implementation,
        "04-test-prompt.md": tests,
        "05-review-prompt.md": review,
        "06-docs-sync-prompt.md": docs_sync,
        "07-handoff-template.md": handoff,
    }
    for name, content in outputs.items():
        (output / name).write_text(content.rstrip() + "\n", encoding="utf-8")

    validator = [sys.executable, str(ROOT / "scripts" / "validate_prompt_pack.py"), str(output)]
    result = subprocess.run(validator)
    if result.returncode:
        return result.returncode

    missing = [name for name in REQUIRED_OUTPUTS if not (output / name).is_file()]
    if missing:
        raise SystemExit("Sinh bộ prompt không đầy đủ: " + ", ".join(missing))

    print(f"Đã tạo bộ prompt: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
