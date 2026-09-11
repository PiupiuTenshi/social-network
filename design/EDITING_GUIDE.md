# Hướng dẫn chỉnh sửa sau khi khóa bản cuối

## Nguồn được phép sửa

- Nội dung và tiêu chí: `sources/` và `screens/`.
- Token: `tokens/design-tokens.json`.
- Hình: SVG trong `assets/editable/`.
- Trạng thái duyệt: `review/approval-status.yaml`.

Không sửa trực tiếp `design.md`; tệp này được sinh tự động.

## Chỉnh hình

- Desktop giữ frame `1440 x 1024`.
- Mobile giữ frame logic `390 x 844`; PNG preview được xuất ở mật độ 2x.
- Không chỉ sửa PNG vì PNG bị ghi đè khi render.
- Không chuyển chữ thành path khi còn cần chỉnh microcopy.

Sau khi sửa SVG:

```bash
python scripts/render_svg.py
```

## Chỉnh token

```bash
python scripts/export_tokens.py
```

## Quy trình thay đổi bản đã khóa

1. Ghi lý do trong `DESIGN_CHANGELOG.md`.
2. Đổi màn hình liên quan sang `needs_changes` trong `review/approval-status.yaml`.
3. Sửa Markdown/SVG/token nguồn.
4. Render và kiểm tra Desktop/Mobile.
5. Đưa trạng thái về `approved` sau khi duyệt.
6. Chạy:

```bash
python scripts/build_design.py --final
python scripts/validate_design.py --require-final
```

Trạng thái hợp lệ: `draft`, `needs_changes`, `approved`, `deferred`.
