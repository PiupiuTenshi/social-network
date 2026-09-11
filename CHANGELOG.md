# Nhật ký thay đổi

Tài liệu dùng định dạng gần với Keep a Changelog. Phiên bản phần mềm dùng Semantic Versioning khi bắt đầu phát hành.

## [3.0.0] - 2026-09-07

### Kế hoạch thực thi bổ sung

- Thêm `docs/execution/`: 9 phase, 158 task, 318 subtask/prompt, phân chia Backend/Data/Frontend và truy vết 66 chức năng, 47 màn hình.
- Thêm roadmap, blocker register, cổng G0–G4, Git playbook và hồ sơ phạm vi đối chiếu tài liệu.
- Thêm `task_gate.py` để kiểm DoR, dependency, acceptance, artifact/hash và review; state ban đầu chưa có task sản phẩm READY/DONE.
- Thêm bộ sinh có `--check`, kiểm thử hành vi gate/đồ thị, workflow CI kế hoạch và công cụ đồng bộ MANIFEST/checksums.
- Sửa ignore runtime `/data/` để giữ `design/data/`, bỏ cache/build/.git khỏi inventory và giữ bytes evidence qua checkout. Các kết quả kiểm chứng được ghi riêng trong `docs/execution/VALIDATION_REPORT.md`; không phải kết quả test sản phẩm.

### Thêm

- UI/UX Twight Light 1.2 Final với 47 màn hình Desktop/Mobile đã duyệt.
- `design.md` ở thư mục gốc và `design/design.md` làm nguồn triển khai Frontend.
- Gallery độc lập, SVG/PNG, design token, route/state/component rules và kế hoạch triển khai.
- Ma trận khoảng trống/sẵn sàng hợp đồng để ngăn Frontend tự suy đoán API.
- Tài liệu nguồn DOCX/PDF v3.0 và script kiểm tra toàn bộ gói.

### Sửa

- Áp dụng phản hồi cuối cho xác thực và bài viết/video.
- Cập nhật prompt, context map và quy trình UI/UX sang bản đã khóa.

## [1.0.0] - 2026-09-05

### Thêm

- Bộ quy tắc `AGENTS.md` và `RULES.md` dành cho người phát triển và trợ lý lập trình.
- Bối cảnh dự án, kiến trúc, ranh giới dịch vụ, quy ước API, dữ liệu, sự kiện, thời gian thực, bảo mật, kiểm thử và vận hành.
- Danh mục tham chiếu được chuyển hóa từ Thiết kế hệ thống chi tiết v3.0.
- Bộ prompt chuyên biệt cho khảo sát, lập kế hoạch, triển khai, sửa lỗi, kiểm thử, rà soát, bảo mật, hiệu năng, phát hành và sự cố.
- Script ghép bối cảnh, sinh bộ prompt tám tệp, kiểm tra prompt, liên kết Markdown, thông điệp commit và dấu vân tay tài liệu nguồn.
- Git flow tinh gọn, lệnh Git an toàn, hook cục bộ và quy trình làm việc song song bằng worktree.
- Tệp tích hợp cho Cursor, Claude, Windsurf, GitHub Copilot và công cụ đọc `AGENTS.md`.
- Biểu mẫu ADR, chức năng, API, sự kiện, lỗi, kế hoạch, pull request, phát hành, sự cố, bằng chứng kiểm thử và bàn giao.

### Bảo đảm chất lượng

- Kiểm tra liên kết Markdown và cấu trúc bộ tài liệu.
- Kiểm tra cú pháp Python và YAML.
- Kiểm tra sinh thử bộ prompt và xác minh đúng tám tệp đầu ra.
- Kiểm tra dấu vân tay SHA-256 của tài liệu thiết kế cơ sở.
