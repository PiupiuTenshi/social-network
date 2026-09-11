#!/usr/bin/env python3
"""Validate the Vibe Coding kit and final UI/UX design."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
commands = [
    [sys.executable, str(ROOT / "scripts" / "validate_vibe_kit.py")],
    [sys.executable, str(ROOT / "scripts" / "build_execution_plan.py"), "--check"],
    [sys.executable, str(ROOT / "scripts" / "task_gate.py"), "validate"],
    [sys.executable, str(ROOT / "scripts" / "test_task_gate.py")],
    [sys.executable, str(ROOT / "design" / "scripts" / "validate_design.py"), "--require-final"],
]
for command in commands:
    command[1:1] = ["-X", "utf8"]
    print("+", " ".join(command))
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        raise SystemExit(result.returncode)
print("ĐẠT: Vibe Coding kit và UI/UX final đều hợp lệ.")
