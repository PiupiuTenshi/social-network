# Danh mục tài liệu tham chiếu

Các tệp trong thư mục này được chuyển từ **Thiết kế hệ thống chi tiết v3.0** để coding agent có thể đọc Markdown trực tiếp.

- `NFR.md`: mục tiêu phi chức năng.
- `SERVICE_OWNERSHIP.md`: owner, entity, store và event.
- `DATA_MODEL.md`: bảng, trường, index và hạ tầng Outbox/Inbox.
- `API_CATALOG.md`: endpoint và quyền.
- `EVENT_CATALOG.md`: sự kiện, producer, consumer và key.
- `TOPIC_CATALOG.md`: topic, retry, DLQ và versioning.
- `SIGNALR_CATALOG.md`: hub method/event.
- `FUNCTION_SPECIFICATIONS.md`: đặc tả từng function ID.
- `TRACEABILITY_MATRIX.md`: function -> contract/data/event/control/test/priority.
- `SECURITY_THREAT_MODEL.md`: claim, trust boundary, threat và retention.
- `OPERATIONS_BASELINE.md`: backup, RPO/RTO, resource, migration và dependency.
- `QUALITY_GATES.md`: CI, P0/P1/P2, G0-G4, định nghĩa hoàn thành và bàn giao.

Khi source DOCX thay đổi, phải tái sinh hoặc cập nhật các tệp này cùng PR.

- [`SOURCE_BASELINE.md`](SOURCE_BASELINE.md): phiên bản và checksum của tài liệu thiết kế nguồn.
