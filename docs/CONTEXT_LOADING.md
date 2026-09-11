# Quản lý bối cảnh

## Ba lớp bối cảnh

1. **Ổn định:** `AGENTS.md`, `RULES.md`, `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`.
2. **Theo miền và nhiệm vụ:** ranh giới, API, sự kiện, dữ liệu, bảo mật và đặc tả chức năng liên quan.
3. **Tức thời:** issue, phần khác biệt, log, kiểm thử thất bại, bản bàn giao và trạng thái Git.

Không sao chép toàn bộ lớp ổn định vào mọi prompt. Tham chiếu đường dẫn và chỉ nạp nội dung thật sự cần thiết.

## Quy tắc nạp

- Backend chức năng: cơ sở + ranh giới dịch vụ + đặc tả chức năng + API/dữ liệu/sự kiện liên quan + kiểm thử.
- Lỗi: cơ sở + xử lý lỗi + mã/kiểm thử/log bằng chứng.
- Di trú dữ liệu: cơ sở + mô hình dữ liệu + quy tắc cơ sở dữ liệu + vận hành + ADR khi phá vỡ.
- Kafka: cơ sở + danh mục sự kiện + topic/thử lại/phiên bản.
- Bảo mật: cơ sở + quy tắc bảo mật + mô hình đe dọa + hợp đồng tài nguyên.
- Rà soát: cơ sở + hành vi dự kiến + toàn bộ phần khác biệt + mã/kiểm thử xung quanh.

## Khi chưa có kho mã

Giữ chỗ trống rõ cho phiên bản, đường dẫn, lệnh và hành vi hiện tại. Không biến giả định thành dữ kiện.

## Khi tài liệu mâu thuẫn với mã

Dừng thay đổi hành vi công khai và ghi:

- hai nguồn đang mâu thuẫn;
- bằng chứng cụ thể;
- tác động;
- phương án đề xuất;
- quyết định cần người dùng hoặc ADR.

Ánh xạ máy đọc được nằm trong `.ai/context-map.yaml`.
## Nhiệm vụ UI/UX và Frontend

- Rà soát thiết kế: nạp `docs/UIUX_WORKFLOW.md`, `design/AGENTS.md`, `design/DESIGN_RULES.md`, màn hình liên quan và contract tương ứng.
- Triển khai Frontend: dùng `design/design.md` làm nguồn UI/UX đã khóa và kiểm tra OpenAPI/AsyncAPI trước khi nối dữ liệu.
- Không nạp toàn bộ 47 màn hình khi nhiệm vụ chỉ liên quan một route; dùng `design/data/screen-inventory.json` để định vị.
- Với tính năng gap, nạp `design/sources/18-backend-contract-gaps.md` và `19-frontend-contract-readiness.md`.

