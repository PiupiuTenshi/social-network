# Ranh giới dịch vụ

## Tài khoản

Sở hữu danh tính, hồ sơ, refresh token, thiết lập tài khoản, OAuth, OTP và vòng đời xóa tài khoản. Không sở hữu quan hệ theo dõi, bài viết, thành viên cộng đồng, tin nhắn hoặc đơn hàng.

## Mạng xã hội

Sở hữu theo dõi, chặn, bài viết, bình luận, phản ứng, chia sẻ và metadata báo cáo/điều hành. `user_id` chỉ là tham chiếu danh tính ngoài, không có khóa ngoại sang `account_db`.

## Cộng đồng

Sở hữu cộng đồng, thành viên, vai trò, quyền, kênh và lời mời. Đây là nguồn quyền cho kênh cộng đồng và RTC.

## Trò chuyện

Sở hữu cuộc trò chuyện, thành viên, tin nhắn, phản ứng tin nhắn, trạng thái đọc và thông báo. Kênh văn bản cộng đồng là bản chiếu hoặc tham chiếu; không có khóa ngoại sang `community_db`.

## Bảng tin

Sở hữu các mô hình đọc `FeedEntry`, `FeedUserSummary` và `FeedPostSummary`. Không sửa bài viết gốc. Dữ liệu phải dựng lại được từ dữ liệu xuất của nguồn và phần chênh lệch Kafka.

## Phương tiện

Sở hữu phiên tải lên và metadata phương tiện. Dữ liệu nhị phân nằm trong SeaweedFS. Dịch vụ khác chỉ lưu `media_id` và kiểm tra trạng thái/quyền qua hợp đồng hoặc bản chiếu.

## Thương mại

Sở hữu tin đăng, tồn kho, đơn hàng, thanh toán giả lập và lịch sử trạng thái. Trong bản cơ sở, đây là một đơn vị triển khai nên một số bước dùng giao dịch cục bộ; state machine vẫn được duy trì để minh họa bù trừ và tách dịch vụ về sau.

## AI và tìm kiếm

Sở hữu embedding, chunk, job và metadata bản chép lời. Không truy cập trực tiếp cơ sở dữ liệu của dịch vụ nguồn. Mọi dữ liệu đưa vào mô hình phải có phạm vi và bằng chứng phân quyền.

Xem ma trận đầy đủ tại `docs/reference/SERVICE_OWNERSHIP.md` và `docs/reference/DATA_MODEL.md`.
