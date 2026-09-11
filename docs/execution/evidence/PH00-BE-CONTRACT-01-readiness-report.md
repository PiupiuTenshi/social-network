# Definition of Ready — PH00-BE-CONTRACT-01

- Task: `PH00-BE-CONTRACT-01`
- Ngày UTC: `2026-09-07`
- Môi trường: workspace tài liệu Windows/PowerShell, chưa có solution, lockfile sản phẩm, remote hoặc migration.
- Tiền nhiệm: `PH00-GOV-AUDIT-01` đã DONE hợp lệ.

## Phạm vi đã khóa cho planning

Task chỉ tạo contract P0, schema/fixture và ADR để giải quyết BL-02 đến BL-06. Không tạo code nghiệp vụ, DB schema/migration, dependency, remote hoặc triển khai.

Các quy ước đã có nguồn và được áp dụng trong contract mới:

1. `412` là stale ETag/`If-Match`; `409` là xung đột nghiệp vụ hoặc cùng `Idempotency-Key` với request khác. Đây là áp dụng thống nhất `API_RULES.md`, không đổi semantics sản phẩm.
2. Kafka là integration contract (`MessageEdited`); SignalR là client realtime contract (`MessageUpdated`). Các event persistent được lưu trước khi broadcast; realtime không là nguồn dữ liệu chuẩn.
3. Topic lifecycle Cộng đồng partition theo `communityId`; `ChannelCreated` mang `channelId` trong payload. Replay giữ `correlationId` gốc, thêm metadata replay riêng.
4. P0 `POST /posts` chỉ nhận text, không `mediaRefs`; P1 Media/Video và toàn bộ P1/P2 contract-gap mặc định tắt/hoãn.
5. Privacy/block propagation dùng event versioned và consumer fail-closed; dữ liệu hiển thị luôn kiểm policy ở owner/projection được cập nhật.

## Điều kiện và bằng chứng

| DoR | Kết luận | Nguồn/artifact |
|---|---|---|
| DOR01 | Goal, phạm vi, 3 AC và ngoài phạm vi rõ | Prompt task, báo cáo này |
| DOR02 | Ownership/hợp đồng đầu vào đã xác định; quyết định final được ghi ADR/contract trong task | `API_RULES.md`, `EVENT_RULES.md`, catalogs, `BLOCKERS.md` |
| DOR03 | Quyền, PII, stale/idempotency, delivery/replay và privacy được đặt thành bắt buộc trong schema/fixture | Báo cáo này, `SECURITY_RULES.md`, `REALTIME_RULES.md` |
| DOR04 | Audit tiền nhiệm DONE, không có dependency khác | `state.json` |
| DOR05 | Chỉ dùng JSON parse/contract validator, generator/gate/test thật; không bịa product build | `scripts/validate_p0_contracts.py` sẽ được tạo trong task |
| DOR06 | Không có migration/rollback trong planning contract; việc đó thuộc DATA/TOOLCHAIN sau | `PROMPT_ORDER.md`, `BLOCKERS.md` |
| DOR07 | Chủ dự án giao Codex thực hiện; điều kiện dừng giữ nguyên khi gặp contract vượt P0 | `AGENTS.md`, `READY_GATE.md` |

Các decision P1/P2 không được chốt trong task này vẫn giữ owner ở PH04/PH06. Khi tìm thấy nguồn trái với năm quy ước trên, dừng và mở ADR thay thế thay vì đổi lặng lẽ.
