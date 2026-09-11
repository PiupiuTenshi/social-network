#!/usr/bin/env python3
from __future__ import annotations
import re
import sys
from pathlib import Path

PATTERN = re.compile(r'^(feat|fix|refactor|perf|test|docs|build|ci|chore|revert)(\([a-z0-9-]+\))?(!)?: .{5,72}$')
SKIP = ('Merge ', 'Revert "', 'fixup!', 'squash!')

def read_subject(value: str) -> str:
    candidate = Path(value)
    if candidate.is_file():
        lines = candidate.read_text(encoding='utf-8').splitlines()
        return lines[0].strip() if lines else ''
    return value.splitlines()[0].strip()

def main() -> int:
    if len(sys.argv) != 2:
        print('Dùng: validate_commit_message.py <commit-msg-file|commit-subject>')
        return 2
    first = read_subject(sys.argv[1])
    if first.startswith(SKIP) or PATTERN.fullmatch(first):
        return 0
    print('Commit message không đúng: <type>(<scope>): <mô tả 5-72 ký tự>')
    return 1

if __name__ == '__main__':
    raise SystemExit(main())
