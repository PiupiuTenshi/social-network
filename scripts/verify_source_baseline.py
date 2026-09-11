#!/usr/bin/env python3
"""So sánh SHA-256 của tài liệu nguồn với baseline dùng để sinh bộ tài liệu."""
from __future__ import annotations
import argparse
from hashlib import sha256
from pathlib import Path

EXPECTED = "5fb171fd30096c2ced50d8d27d139a07488cf7df918a1ad171f31c839184154d"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='Đường dẫn tới DOCX thiết kế hệ thống v3.0')
    args = parser.parse_args()
    path = Path(args.source)
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != EXPECTED:
        print(f'Không khớp baseline. expected={EXPECTED} actual={actual}')
        return 1
    print(f'Baseline hợp lệ: {actual}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
