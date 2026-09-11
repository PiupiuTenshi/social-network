"""Danh mục tệp của kit, loại Git metadata và artifact phát triển."""
from pathlib import Path

IGNORED_PARTS = {".git", "work", "__pycache__", "node_modules", ".venv", "venv", "bin", "obj", "dist", ".angular", "TestResults", "coverage", ".adapter-harness"}


def kit_files(root: Path):
    return sorted((p for p in root.rglob("*") if p.is_file()
                   and not IGNORED_PARTS.intersection(p.relative_to(root).parts)
                   and p.suffix not in {".pyc", ".tmp"}
                   and p != root / "docs/execution/state.json.lock"), key=lambda p: p.relative_to(root).as_posix())
