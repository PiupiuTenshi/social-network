# Bắt đầu triển khai Frontend Twight Light

## Thứ tự đọc bắt buộc

1. `design.md` — nguồn chuẩn UI/UX đã khóa.
2. `tokens/design-tokens.json` — token màu, chữ, khoảng cách, radius và motion.
3. `sources/13-route-map.md` — route và guard.
4. `sources/11-state-matrix.md` — loading, empty, error, offline, forbidden và retry.
5. `sources/18-backend-contract-gaps.md` và `sources/19-frontend-contract-readiness.md` — phần chưa được phép suy đoán API.
6. `FRONTEND_IMPLEMENTATION_PLAN.md` và `DESIGN_TO_CODE_CHECKLIST.md` — thứ tự triển khai và cổng hoàn thành.

## Nguồn hình

- SVG chỉnh sửa: `assets/editable/`.
- PNG đối chiếu: `assets/preview/`.
- Gallery độc lập: `review/FINAL_REVIEW_GALLERY_STANDALONE.html`.
- Contact sheet: `assets/contact-sheets/`.

## Quy tắc quan trọng

- Desktop là nguồn bố cục; Mobile là biến thể responsive có thứ tự ưu tiên riêng, không phải bản thu nhỏ.
- OpenAPI/AsyncAPI quyết định request, response, quyền và lỗi; mockup không tạo endpoint.
- Mọi component phải có trạng thái tải, rỗng, lỗi, không quyền và ngoại tuyến khi có liên quan.
- Không bật tính năng `contract-gap` ở bản phát hành khi chưa có hợp đồng được duyệt.

## Lệnh kiểm tra

```bash
python scripts/export_tokens.py
python scripts/render_svg.py
python scripts/build_design.py --final
python scripts/validate_design.py --require-final
```
