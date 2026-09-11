# Bắt đầu triển khai Frontend Twight Light

Task và prompt theo từng màn hình/lát cắt ưu tiên nằm tại [backlog Frontend](docs/execution/FRONTEND.md). Kiểm [cổng READY](docs/execution/READY_GATE.md) trước thực thi; một màn hình có thể có subtask P0/P1/P2 riêng để giữ đúng phụ thuộc Backend/Data.

## Nguồn bắt buộc

1. `design.md` — bản tổng hợp tiện dụng ở thư mục gốc.
2. `design/design.md` — nguồn UI/UX chính trong bộ thiết kế.
3. `design/tokens/design-tokens.json` — token máy đọc được.
4. `design/sources/13-route-map.md` và `design/data/screen-inventory.json` — route/màn hình.
5. `design/sources/11-state-matrix.md` — loading, empty, error, offline và retry.
6. `design/sources/18-backend-contract-gaps.md` và `design/sources/19-frontend-contract-readiness.md` — phần không được tự suy đoán API.
7. `prompts/25-uiux-to-frontend.md` — prompt triển khai từng vertical slice.

## Lệnh kiểm tra thiết kế

```bash
cd design
python scripts/export_tokens.py
python scripts/render_svg.py
python scripts/build_design.py --final
python scripts/validate_design.py --require-final
```

## Thứ tự triển khai

- P0: xác thực, bảng tin, hồ sơ/thiết lập cơ sở, chat, thông báo và trạng thái hệ thống.
- P1: khôi phục mật khẩu, xóa tài khoản, cộng đồng, RTC, media/video và điều hành nội dung.
- P2: marketplace, AI/tóm tắt và chức năng mở rộng chỉ sau khi hợp đồng Backend được khóa.

Không coi mockup là nguồn tạo endpoint, field, quyền hoặc trạng thái nghiệp vụ mới.
