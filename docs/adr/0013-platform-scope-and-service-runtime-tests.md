# ADR-0013: Ranh giới nghiệm thu PH01-BE-PLATFORM-01

- Trạng thái: Accepted
- Ngày: 2026-09-11
- Quyết định: Chủ dự án xác nhận Platform chỉ nghiệm thu framework/harness, Gateway và security policy.

## Quyết định

`PH01-BE-PLATFORM-01` cung cấp envelope, Outbox/Inbox/idempotency primitives, migration reference Account, publisher contract, correlation, Problem Details, rate limit, Gateway YARP/JWT/CORS policy và metrics contracts.

BOLA với resource thật, Kafka ACL/principal runtime, JWT issuer/keys thật, consumer hosted runtime, broker-down/crash-after-publish và end-to-end contract tests thuộc task Account/Social/Chat/Feed sau khi schema, service identity và endpoint đã được khóa. Không tạo resource/identity giả để tuyên bố các kiểm chứng đó đã đạt.

## Hệ quả

Platform vẫn có build, architecture, migration, Inbox duplicate và DB rollback harness. Những task service sau phải bổ sung test BOLA, Kafka ACL, fault/crash và contract vào evidence của chính chúng.
