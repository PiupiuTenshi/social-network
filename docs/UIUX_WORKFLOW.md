# Quy trình UI/UX đến Frontend — bản đã khóa

UI/UX 1.2 Final nằm trong `design/`. Nguồn triển khai là `design/design.md`; `design.md` ở thư mục gốc là bản tiện dụng được đồng bộ từ nguồn này.

## Bắt đầu một màn hình

1. Dùng `design/data/screen-inventory.json` để tìm mã màn hình và tệp đặc tả.
2. Đọc phần tương ứng trong `design/design.md` và tệp `design/screens/...`.
3. Đối chiếu OpenAPI/AsyncAPI, quyền, mã lỗi và trạng thái nghiệp vụ.
4. Kiểm tra `design/sources/18-backend-contract-gaps.md` và `19-frontend-contract-readiness.md`.
5. Triển khai một vertical slice gồm route, component, state, adapter API, test và accessibility.

## Nguồn hình và token

- SVG chỉnh sửa: `design/assets/editable/`.
- PNG đối chiếu: `design/assets/preview/`.
- Gallery ngoại tuyến: `design/review/FINAL_REVIEW_GALLERY_STANDALONE.html`.
- Token: `design/tokens/design-tokens.json`.

## Khi cần thay đổi thiết kế

1. Ghi `design/DESIGN_CHANGELOG.md`.
2. Đổi màn hình liên quan thành `needs_changes` trong approval.
3. Sửa Markdown/SVG/token nguồn; không sửa trực tiếp `design/design.md`.
4. Render, duyệt Desktop/Mobile, đưa lại `approved`.
5. Chạy từ `design/`:

```bash
python scripts/export_tokens.py
python scripts/render_svg.py
python scripts/build_design.py --final
python scripts/validate_design.py --require-final
```

6. Chạy `python scripts/sync_root_design.py` ở thư mục gốc để cập nhật `design.md` tiện dụng.

## Cổng hoàn thành màn hình

- Route và guard đúng.
- Dữ liệu/hành động khớp hợp đồng.
- Loading, empty, error, permission, offline/reconnect đầy đủ khi liên quan.
- Desktop và Mobile đúng phân cấp, không scale cơ học.
- Keyboard, focus, semantic HTML, accessible name, contrast và reduced motion đạt.
- Test thực tế chạy thành công và có bằng chứng.
