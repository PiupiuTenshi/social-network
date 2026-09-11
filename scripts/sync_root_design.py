#!/usr/bin/env python3
"""Synchronize root design.md from design/design.md with adjusted relative links."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "design" / "design.md"
out = ROOT / "design.md"
text = src.read_text(encoding="utf-8")
text = text.replace("](assets/", "](design/assets/")
text = text.replace("](screens/", "](design/screens/")
text = text.replace("`review/FINAL_REVIEW_GALLERY_STANDALONE.html`", "`design/review/FINAL_REVIEW_GALLERY_STANDALONE.html`")
for prefix in ["sources/", "screens/", "tokens/", "assets/", "review/"]:
    text = text.replace(f"`{prefix}", f"`design/{prefix}")
for name in ["FRONTEND_IMPLEMENTATION_PLAN.md", "FRONTEND_IMPLEMENTATION_PROMPT.md", "DESIGN_TO_CODE_CHECKLIST.md", "FRONTEND_START_HERE.md"]:
    text = text.replace(f"`{name}`", f"`design/{name}`")
text = text.replace(
    "<!-- Tệp được sinh tự động. Không sửa trực tiếp; hãy sửa sources/, screens/, tokens/ hoặc review/approval-status.yaml. -->",
    "<!-- Bản tiện dụng ở thư mục gốc. Nguồn sinh là design/design.md; không sửa trực tiếp. -->",
)
out.write_text(text, encoding="utf-8")
print(f"Đã đồng bộ {out.relative_to(ROOT)} từ {src.relative_to(ROOT)}")
