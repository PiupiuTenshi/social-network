#!/usr/bin/env python3
"""Render editable SVG files to review PNG files and rebuild contact sheets."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

from common import ROOT, load_inventory


def render_all() -> None:
    mappings = [
        (ROOT / "assets/editable/svg/desktop", ROOT / "assets/preview/png/desktop", 1),
        (ROOT / "assets/editable/svg/mobile", ROOT / "assets/preview/png/mobile", 2),
        (ROOT / "assets/editable/flows", ROOT / "assets/preview/flows", 1),
        (ROOT / "assets/editable/boards", ROOT / "assets/preview/boards", 1),
    ]
    total = 0
    for src_dir, out_dir, scale in mappings:
        out_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(src_dir.glob("*.svg")):
            out = out_dir / f"{src.stem}.png"
            cairosvg.svg2png(url=str(src), write_to=str(out), scale=scale)
            total += 1
    print(f"Đã render {total} SVG thành PNG.")


def fonts():
    regular = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    bold = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    try:
        return (
            ImageFont.truetype(str(regular), 15),
            ImageFont.truetype(str(bold), 18),
            ImageFont.truetype(str(regular), 12),
        )
    except Exception:
        f = ImageFont.load_default()
        return f, f, f


def wrapped(draw: ImageDraw.ImageDraw, text: str, font, width: int, max_lines: int = 2) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if draw.textlength(test, font=font) <= width or not current:
            current = test
        else:
            lines.append(current)
            current = word
            if len(lines) == max_lines - 1:
                break
    if current and len(lines) < max_lines:
        remaining_used = " ".join(lines + [current])
        if len(remaining_used) < len(text) and len(lines) == max_lines - 1:
            current = current.rstrip("…") + "…"
        lines.append(current)
    return lines


def make_screen_sheets(kind: str, per_sheet: int, cols: int) -> None:
    inventory = load_inventory()
    out_dir = ROOT / "assets/contact-sheets"
    out_dir.mkdir(parents=True, exist_ok=True)
    font, font_b, font_s = fonts()
    thumb_w = 300 if kind == "desktop" else 220
    thumb_h = 214 if kind == "desktop" else 476
    label_h = 62
    gap = 22
    margin = 28
    rows = math.ceil(per_sheet / cols)
    sw = margin * 2 + cols * thumb_w + (cols - 1) * gap
    sh = margin * 2 + 48 + rows * (thumb_h + label_h) + (rows - 1) * gap
    pages = math.ceil(len(inventory) / per_sheet)
    for batch_idx in range(pages):
        batch = inventory[batch_idx * per_sheet : (batch_idx + 1) * per_sheet]
        canvas = Image.new("RGB", (sw, sh), "#F8FAFC")
        draw = ImageDraw.Draw(canvas)
        draw.text((margin, margin), f"Twight Light · {kind.capitalize()} · {batch_idx + 1}/{pages}", font=font_b, fill="#0F172A")
        draw.text((sw - margin, margin + 2), f"{len(batch)} màn hình", font=font_s, fill="#64748B", anchor="ra")
        for i, item in enumerate(batch):
            row, col = divmod(i, cols)
            x = margin + col * (thumb_w + gap)
            y = margin + 48 + row * (thumb_h + label_h + gap)
            slug = Path(item["file"]).stem
            image_path = ROOT / "assets/preview/png" / kind / f"{slug}.png"
            image = Image.open(image_path).convert("RGB")
            image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            bg = Image.new("RGB", (thumb_w, thumb_h), "white")
            bg.paste(image, ((thumb_w - image.width) // 2, (thumb_h - image.height) // 2))
            canvas.paste(bg, (x, y))
            draw.rectangle((x, y, x + thumb_w, y + thumb_h), outline="#CBD5E1", width=1)
            title = f"{item['id']} · {item['title']}"
            for line_no, line in enumerate(wrapped(draw, title, font, thumb_w, 2)):
                draw.text((x, y + thumb_h + 7 + line_no * 18), line, font=font, fill="#0F172A")
            draw.text((x, y + thumb_h + 45), f"{item['priority']} · {item['group']}", font=font_s, fill="#64748B")
        canvas.save(out_dir / f"{kind}-{batch_idx + 1:02d}.jpg", quality=90, optimize=True)


def make_gallery(src_dir: Path, out_name: str, title: str, cols: int, thumb: tuple[int, int]) -> None:
    paths = sorted(src_dir.glob("*.png"))
    font, font_b, font_s = fonts()
    tw, th = thumb
    gap, margin, label_h = 20, 28, 40
    rows = math.ceil(len(paths) / cols)
    sw = margin * 2 + cols * tw + (cols - 1) * gap
    sh = margin * 2 + 48 + rows * (th + label_h) + (rows - 1) * gap
    canvas = Image.new("RGB", (sw, sh), "#F8FAFC")
    draw = ImageDraw.Draw(canvas)
    draw.text((margin, margin), title, font=font_b, fill="#0F172A")
    for i, path in enumerate(paths):
        row, col = divmod(i, cols)
        x, y = margin + col * (tw + gap), margin + 48 + row * (th + label_h + gap)
        image = Image.open(path).convert("RGB")
        image.thumbnail((tw, th), Image.Resampling.LANCZOS)
        bg = Image.new("RGB", (tw, th), "white")
        bg.paste(image, ((tw - image.width) // 2, (th - image.height) // 2))
        canvas.paste(bg, (x, y))
        draw.rectangle((x, y, x + tw, y + th), outline="#CBD5E1", width=1)
        draw.text((x, y + th + 8), path.stem.replace("-", " ").title(), font=font_s, fill="#0F172A")
    canvas.save(ROOT / "assets/contact-sheets" / out_name, quality=90, optimize=True)


def build_contact_sheets() -> None:
    out_dir = ROOT / "assets/contact-sheets"
    for old in out_dir.glob("*.jpg"):
        old.unlink()
    make_screen_sheets("desktop", per_sheet=12, cols=4)
    make_screen_sheets("mobile", per_sheet=9, cols=3)
    make_gallery(ROOT / "assets/preview/flows", "flows.jpg", "Twight Light · Các luồng người dùng", 3, (360, 205))
    make_gallery(ROOT / "assets/preview/boards", "boards.jpg", "Twight Light · Bảng thiết kế dùng chung", 2, (560, 315))
    print(f"Đã tạo {len(list(out_dir.glob('*.jpg')))} contact sheet.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-render", action="store_true", help="Chỉ tạo lại contact sheet.")
    parser.add_argument("--skip-contact-sheets", action="store_true", help="Chỉ render PNG.")
    args = parser.parse_args()
    if not args.skip_render:
        render_all()
    if not args.skip_contact_sheets:
        build_contact_sheets()


if __name__ == "__main__":
    main()
