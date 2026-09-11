# Chính sách bảo mật

## Báo cáo lỗ hổng

Không mở issue công khai chứa secret, token, dữ liệu cá nhân, nội dung riêng tư hoặc hướng dẫn khai thác hệ thống đang chạy. Gửi báo cáo qua kênh riêng của chủ dự án, gồm:

- phiên bản hoặc commit;
- thành phần và điều kiện xảy ra;
- tác động;
- cách tái hiện an toàn đã loại dữ liệu nhạy cảm;
- bằng chứng và đề xuất khắc phục.

## Quy tắc xử lý

- Không thử khai thác ngoài phạm vi được phép.
- Không truy cập hoặc sao chép dữ liệu người dùng không thuộc quyền.
- Không thực hiện DoS, lừa đảo xã hội hoặc thay đổi môi trường vận hành.
- Secret bị lộ phải được thu hồi hoặc xoay ngay; xóa khỏi commit mới là chưa đủ.
- Bản sửa cần kiểm thử hồi quy và rà soát các đường xử lý tương đương.

Xem thêm `docs/SECURITY_RULES.md` và `docs/reference/SECURITY_THREAT_MODEL.md`.
