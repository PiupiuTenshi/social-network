# Hướng dẫn làm việc cho Twight Light

Tệp này là nguồn hướng dẫn canonical ở root. Dùng đúng tên `AGENTS.md`; không tạo alias chỉ khác hoa/thường vì Windows và Linux xử lý tên tệp khác nhau.

## Trước khi thay đổi

Đọc theo thứ tự:

1. `AGENTS.md`
2. `RULES.md`
3. `docs/START_HERE.md`
4. Tài liệu phù hợp trong `.ai/context-map.yaml`
5. Hướng dẫn cục bộ gần nhất nếu có.

Xác định ID task/chức năng, dịch vụ sở hữu, hợp đồng/dữ liệu/sự kiện bị ảnh hưởng, tiêu chí chấp nhận và lệnh kiểm chứng. Không suy đoán phiên bản, API, schema, quyền hoặc lệnh chưa có bằng chứng.

## Cổng thực thi

Với ID trong `docs/execution/plan.json`, đọc `docs/execution/PROMPT_ORDER.md` để biết thứ tự và luôn chạy `python -X utf8 scripts/task_gate.py check ID` trước khi làm. Chỉ thực hiện khi READY hoặc đang tiếp tục đúng ID IN_PROGRESS. Không bỏ qua dependency, DoR, acceptance, evidence hoặc review; không sửa `state.json` bằng tay.

Khi nguồn mâu thuẫn hoặc thiếu quyết định về ownership, API/event, schema, phân quyền, PII, concurrency, migration hay thao tác phá hủy: dừng, ghi blocker/ADR cần thiết và không tự chọn phương án. UI approved không tự chứng minh Backend contract approved.

## Quy tắc bắt buộc

- Dịch vụ sở hữu aggregate và dữ liệu nguồn; không truy vấn/ghi chéo DB. Dùng API hoặc projection sự kiện.
- Giữ hướng phụ thuộc `API -> Application -> Domain`; Domain không phụ thuộc framework, HTTP, DB hoặc Kafka.
- Bên phát dùng Outbox; bên nhận dùng Inbox hoặc cơ chế idempotency. Không giả định exactly-once.
- Kiểm phân quyền ở dịch vụ sở hữu; không tin identity, role hoặc owner từ client.
- Không đưa secret, token, OTP hay PII thô vào code, log, prompt, issue hoặc evidence.
- Mọi thay đổi có kiểm thử/bằng chứng phù hợp; không báo build/test đạt nếu chưa chạy.
- Không tự commit, push, merge, tag, deploy, đổi production, chạy migration phá hủy hoặc thêm dependency khi chưa được yêu cầu/phê duyệt rõ.

## Bàn giao

Ghi tệp đã đổi, nguồn/ADR/hợp đồng liên quan, từng acceptance → evidence, lệnh thực tế cùng kết quả, giả định, blocker và rủi ro. Đồng bộ tài liệu/hợp đồng khi chúng bị ảnh hưởng.
