# Hướng dẫn cho trợ lý triển khai và chỉnh sửa UI/UX

Phạm vi của tệp này là toàn bộ bộ thiết kế Twight Light.

## Nguồn chuẩn

1. Thiết kế hệ thống v3.0, OpenAPI và AsyncAPI quyết định API, dữ liệu, quyền, sự kiện và trạng thái nghiệp vụ.
2. `design.md` là nguồn UI/UX tổng hợp đã khóa.
3. `sources/` quyết định quy tắc UI/UX dùng chung.
4. `screens/` quyết định mục tiêu, hành động, trạng thái và tiêu chí của từng màn hình.
5. `tokens/design-tokens.json` quyết định token.
6. SVG trong `assets/editable/` là nguồn hình; PNG chỉ để đối chiếu.

## Quy tắc bắt buộc

- Không tự tạo endpoint, field, claim, quyền hoặc trạng thái Backend chỉ vì mockup cần dữ liệu.
- Kiểm tra `sources/18-backend-contract-gaps.md` và `sources/19-frontend-contract-readiness.md` trước khi code tính năng gap.
- Giữ mã màn hình, mã chức năng và route đã khóa; thay đổi phá vỡ cần changelog và quyết định hợp đồng.
- Mỗi màn hình phải xử lý Desktop, Mobile, loading, empty, error, unauthorized/forbidden và kết nối khi liên quan.
- Không dùng màu làm tín hiệu duy nhất; điều khiển phải dùng được bằng bàn phím và có focus nhìn thấy.
- Touch target tối thiểu 44 x 44 px.
- Không sửa trực tiếp `design.md`.
- Không tuyên bố render/build/validator đạt khi chưa chạy lệnh thật.

## Lệnh bàn giao

```bash
python scripts/export_tokens.py
python scripts/render_svg.py
python scripts/build_design.py --final
python scripts/validate_design.py --require-final
```

## Báo cáo thay đổi

- Màn hình/tài liệu đã đổi.
- Lý do và quyết định UX.
- Hợp đồng Backend bị ảnh hưởng hay không.
- SVG/PNG đã render.
- Lệnh kiểm tra và kết quả thật.
