#!/usr/bin/env python3
"""Write or verify SHA-256 manifests without Git/build/cache content."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

EXCLUDED = {".git", "node_modules", "bin", "obj", "dist", ".angular", "__pycache__", ".venv", "cache"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.root.is_dir():
        raise SystemExit(f"Artifact root is missing: {args.root}")
    files = [
        path for path in args.root.rglob("*")
        if path.is_file() and path.resolve() != args.output.resolve() and not set(path.relative_to(args.root).parts) & EXCLUDED
    ]
    if not files:
        raise SystemExit("No eligible artifacts to checksum")
    lines = [f"{digest(path)}  {path.relative_to(args.root).as_posix()}" for path in sorted(files)]
    content = "\n".join(lines) + "\n"
    if args.verify:
        if not args.output.is_file() or args.output.read_text(encoding="utf-8") != content:
            raise SystemExit("SHA-256 manifest is absent or does not match artifacts")
        print(f"Verified SHA-256 manifest: {args.output}")
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(f"Wrote SHA-256 manifest for {len(files)} artifacts: {args.output}")


if __name__ == "__main__":
    main()
