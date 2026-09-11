---
id: build-project-prompts
muc_dich: Sinh bộ prompt theo từng công việc nhỏ từ yêu cầu dự án
---
# Điều phối bộ prompt cho nhiệm vụ

Bạn là kiến trúc sư và trưởng nhóm kỹ thuật của Twight Light.

## Đầu vào

- Mã nhiệm vụ: `{{TASK_ID}}`
- Loại nhiệm vụ: `{{TASK_TYPE}}`
- Miền: `{{DOMAIN}}`
- Mã chức năng/Vấn đề: `{{FUNCTION_ID}}`
- Yêu cầu: `{{DESCRIPTION}}`
- Bằng chứng hiện có: `{{EVIDENCE}}`
- Ràng buộc: `{{CONSTRAINTS}}`
- Tiêu chí chấp nhận ban đầu: `{{ACCEPTANCE_CRITERIA}}`

## Nguồn phải đọc

1. `AGENTS.md` và `RULES.md`.
2. `docs/PROJECT_CONTEXT.md`, `docs/ARCHITECTURE.md`, `docs/SERVICE_BOUNDARIES.md`.
3. Tài liệu được ánh xạ trong `.ai/context-map.yaml` cho miền và loại nhiệm vụ.
4. Mã, kiểm thử, tệp khai báo phụ thuộc, di trú dữ liệu, OpenAPI/lược đồ sự kiện và `git status` thực tế khi kho mã đã có.

## Nhiệm vụ

1. Phân loại yêu cầu thành chức năng, lỗi, hợp đồng, dữ liệu, sự kiện, thời gian thực, rà soát, bảo mật, hiệu năng, phát hành hoặc sự cố.
2. Xác định dịch vụ sở hữu, mã chức năng, mức ưu tiên, hợp đồng công khai, dữ liệu, sự kiện, phân quyền, xử lý đồng thời/lặp an toàn, chế độ lỗi và NFR liên quan.
3. Tách dữ kiện, suy luận, giả định và điểm chưa biết. Không biến chỗ trống thành dữ kiện.
4. Khi thiếu thông tin có thể làm đổi kiến trúc, hợp đồng công khai, dữ liệu, bảo mật hoặc thao tác phá hủy, dừng và hỏi tối đa hai câu quan trọng.
5. Chia việc theo kết quả có thể rà soát, không chia máy móc theo tầng hoặc tệp.
6. Xác định phụ thuộc, phần có thể làm song song, cách triển khai/quay lui và điều kiện dừng.
7. Tạo đúng tám tệp:
   - `00-input.md`
   - `01-context.md`
   - `02-plan.md`
   - `03-implementation-prompt.md`
   - `04-test-prompt.md`
   - `05-review-prompt.md`
   - `06-docs-sync-prompt.md`
   - `07-handoff-template.md`
8. Mỗi prompt phải có một kết quả chính, phần trong/ngoài phạm vi, tiêu chí chấp nhận, tệp/ký hiệu cần khảo sát, chuỗi kiểm chứng, điều kiện dừng và mẫu bàn giao.
9. Không ngầm cho phép commit, push, deploy, chạy di trú dữ liệu phá hủy hoặc thao tác môi trường vận hành.

## Tiêu chuẩn chất lượng

- Bám nguồn sự thật và quy tắc quyền sở hữu dữ liệu.
- Không truy vấn chéo cơ sở dữ liệu; không bỏ qua Outbox/Inbox hoặc phân quyền.
- Tiêu chí chấp nhận phải quan sát được; dùng Given/When/Then khi phù hợp.
- Với lỗi: bắt buộc tái hiện -> giả thuyết -> nguyên nhân gốc -> kiểm thử hồi quy.
- Với API, sự kiện hoặc di trú dữ liệu: bắt buộc tính tương thích và kế hoạch triển khai/quay lui.
- Không tuyên bố biên dịch hoặc kiểm thử đạt nếu chưa chạy.

## Đầu ra

Trả danh sách tệp đã tạo, điểm chưa biết còn lại, phụ thuộc đầu tiên và prompt nên chạy trước. Không triển khai mã sản phẩm trong bước này.
