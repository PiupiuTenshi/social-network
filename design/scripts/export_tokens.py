#!/usr/bin/env python3
"""Export design-tokens.json to CSS custom properties and a TypeScript object."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from common import ROOT

SOURCE = ROOT / "tokens/design-tokens.json"


def walk(node: Any, prefix: list[str] | None = None):
    prefix = prefix or []
    if isinstance(node, dict) and "$value" in node:
        yield prefix, node["$value"]
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$") or key == "meta":
                continue
            yield from walk(value, prefix + [str(key)])


def css_name(parts: list[str]) -> str:
    joined = "-".join(parts)
    joined = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", joined).lower()
    return f"--sp-{joined}"


def css_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    light: list[tuple[list[str], Any]] = []
    dark: list[tuple[list[str], Any]] = []
    general: list[tuple[list[str], Any]] = []
    for parts, value in walk(data):
        if len(parts) >= 2 and parts[0] == "color" and parts[1] == "light":
            light.append((parts[2:], value))
        elif len(parts) >= 2 and parts[0] == "color" and parts[1] == "dark":
            dark.append((parts[2:], value))
        else:
            general.append((parts, value))

    lines = [":root {"]
    for parts, value in general:
        lines.append(f"  {css_name(parts)}: {css_value(value)};")
    for parts, value in light:
        lines.append(f"  {css_name(['theme'] + parts)}: {css_value(value)};")
    lines.append("}")
    lines.append("")
    lines.append('[data-theme="dark"] {')
    for parts, value in dark:
        lines.append(f"  {css_name(['theme'] + parts)}: {css_value(value)};")
    lines.append("}")
    lines.append("")
    lines.append(":focus-visible { outline: 3px solid var(--sp-color-light-focus, #4F46E5); outline-offset: 2px; }")
    (ROOT / "tokens/tokens.generated.css").write_text("\n".join(lines) + "\n", encoding="utf-8")

    json_text = json.dumps(data, ensure_ascii=False, indent=2)
    ts = "// Sinh từ design-tokens.json. Không sửa trực tiếp.\nexport const designTokens = " + json_text + " as const;\n"
    (ROOT / "tokens/theme.generated.ts").write_text(ts, encoding="utf-8")
    print("Đã tạo tokens/tokens.generated.css và tokens/theme.generated.ts.")


if __name__ == "__main__":
    main()
