# Twight Light Frontend Design Kit 1.2 Final

Bộ nguồn UI/UX đã khóa để triển khai Frontend cho **Twight Light**. Gói này chứa `design.md`, 47 đặc tả màn hình, token, route, component/state rules, SVG/PNG Desktop và Mobile, luồng người dùng, gallery độc lập và cổng kiểm tra.

## Bắt đầu

1. Đọc `FRONTEND_START_HERE.md`.
2. Dùng `design.md` làm nguồn UI/UX tổng hợp.
3. Dùng OpenAPI/AsyncAPI và thiết kế hệ thống v3.0 làm nguồn hợp đồng Backend.
4. Kiểm tra `sources/18-backend-contract-gaps.md` trước khi nối một chức năng chưa có hợp đồng.
5. Dùng SVG trong `assets/editable/` làm nguồn chỉnh sửa; PNG trong `assets/preview/` chỉ để đối chiếu.

## Tệp quan trọng

- `design.md`: tài liệu UI/UX cuối cho Frontend.
- `FRONTEND_START_HERE.md`: thứ tự đọc và quy tắc bắt đầu.
- `screens/`: đặc tả từng màn hình.
- `sources/`: quy tắc UI/UX dùng chung và trạng thái hợp đồng.
- `tokens/design-tokens.json`: nguồn token máy đọc được.
- `FRONTEND_IMPLEMENTATION_PLAN.md`: kế hoạch theo P0/P1/P2.
- `DESIGN_TO_CODE_CHECKLIST.md`: cổng hoàn thành giao diện.
- `review/FINAL_REVIEW_GALLERY_STANDALONE.html`: gallery ảnh độc lập.

## Kiểm tra

```bash
python scripts/export_tokens.py
python scripts/render_svg.py
python scripts/build_design.py --final
python scripts/validate_design.py --require-final
```
