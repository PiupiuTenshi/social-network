# ADR-010 - Phạm vi P0/P1/P2 và cổng chất lượng

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Khối lượng Tài khoản, Mạng xã hội, Bảng tin, Trò chuyện, Cộng đồng, RTC, Phương tiện, Thương mại và AI có nguy cơ vượt thời gian sáu tháng của một lập trình viên.

## Quyết định

Phân loại P0, P1, P2 và Tương lai. Chỉ mở P1 sau khi P0 đạt cổng tương ứng; chỉ mở P2 khi P0/P1 ổn định. Khi chậm tiến độ, cắt P2 trước, không cắt kiểm thử, bảo mật, backup/restore, quan sát hoặc tài liệu của phần cốt lõi.

## Lý do

Một baseline ít tính năng nhưng hoàn chỉnh, có bằng chứng và khôi phục được có giá trị cao hơn nhiều module dở dang.

## Hệ quả

- Một số chức năng mở rộng có thể không được triển khai.
- Mỗi cổng cần bằng chứng rõ từ test, trace, dashboard và runbook.
- Roadmap phải được cập nhật theo tiến độ thực tế.

## Ràng buộc thực thi

- Không tuyên bố hoàn thành giai đoạn khi tiêu chí bắt buộc còn thất bại.
- Lỗi Critical/High của phạm vi hiện tại chặn chuyển cổng.
- Thay đổi ưu tiên phải ghi rõ lý do, tác động và người quyết định.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
