# Mức ưu tiên và lộ trình

## Quy tắc cắt phạm vi

- Không bắt đầu P1 khi G1 chưa đạt.
- Không bắt đầu P2 khi G2 chưa đạt.
- P2 là phần bị cắt đầu tiên khi chậm tiến độ.
- Không cắt kiểm thử, phân quyền, Outbox/Inbox, sao lưu/khôi phục, khả năng quan sát hoặc tài liệu để giữ một chức năng P2.

## Cổng chất lượng

- **G0 - Kiến trúc:** ownership, lược đồ, API/sự kiện, mô hình lỗi và ADR đã khóa.
- **G1 - Luồng P0:** Tài khoản -> Bài viết -> Kafka -> Bảng tin và Trò chuyện chạy xuyên suốt; lỗi broker/cơ sở dữ liệu được xử lý.
- **G2 - P1:** Cộng đồng, Phương tiện, xóa tài khoản và điều hành có phân quyền, thử lại, bảo mật và bằng chứng khôi phục.
- **G3 - P2:** chức năng P2 đạt NFR riêng, có phương án suy giảm và không ảnh hưởng P0/P1.
- **G4 - Phát hành:** không còn lỗi nghiêm trọng; hợp đồng, khôi phục, quay lui và kịch bản trình diễn đã diễn tập.

## Lộ trình sáu tháng

1. **Tuần 1-2:** nền tảng, Tài khoản, BuildingBlocks, CI/CD và hạ tầng.
2. **Tuần 3-8:** Mạng xã hội, Bảng tin, Trò chuyện, SignalR, phân quyền và xử lý lặp an toàn.
3. **Tuần 9-14:** Cộng đồng/RTC, Phương tiện, OTP, xóa tài khoản và điều hành; chỉ bắt đầu Thương mại khi P0 đạt.
4. **Tuần 15-18:** Thương mại, AI/tìm kiếm và củng cố hệ thống theo năng lực.
5. **Tuần 19-22:** NFR, hợp đồng, tình huống lỗi, bảo mật, di trú, khôi phục và tài liệu.
6. **Tuần 23-24:** dashboard, cảnh báo, runbook, diễn tập phát hành và bàn giao.

Chi tiết cổng và bằng chứng nằm trong `docs/reference/QUALITY_GATES.md`.
