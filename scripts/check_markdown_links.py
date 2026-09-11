#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')

def main() -> int:
    errors = []
    for md in ROOT.rglob('*.md'):
        if any(part in {'.git','node_modules','work'} for part in md.parts):
            continue
        text = md.read_text(encoding='utf-8')
        for target in PATTERN.findall(text):
            target = target.strip().split()[0].strip('<>')
            if not target or target.startswith(('#','http://','https://','mailto:')):
                continue
            path = unquote(target.split('#',1)[0])
            if path and not (md.parent/path).resolve().exists():
                errors.append(f'{md.relative_to(ROOT)} -> {target}')
    if errors:
        print('Liên kết Markdown không tồn tại:')
        print('\n'.join('- '+e for e in errors))
        return 1
    print('Markdown links: OK')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
