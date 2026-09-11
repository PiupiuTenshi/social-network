# 11. Ma trận trạng thái

## Trạng thái dùng chung

| Trạng thái | Thành phần | Hành vi |
|---|---|---|
| loading | Skeleton/Spinner | Không thay đổi layout lớn |
| empty | EmptyState | Giải thích + CTA hữu ích |
| error-retryable | InlineAlert/ErrorState | Giữ dữ liệu người dùng + Thử lại |
| forbidden | ErrorState | Không tiết lộ tài nguyên |
| not-found | ErrorState | Quay về nơi an toàn |
| offline | OfflineBanner | Cho biết thao tác nào vẫn dùng được |
| reconnecting | StatusChip | Không nhân đôi dữ liệu |
| rate-limited | InlineAlert | Đọc Retry-After nếu có |
| service-unavailable | ErrorState | Chỉ ảnh hưởng mô-đun tương ứng |
| stale-version | ConflictDialog | Tải bản mới/so sánh, không ghi đè |

## Trạng thái theo miền

### Bài viết video

`draft -> uploaded -> processing -> ready/published` hoặc `failed`.

### Tin nhắn

`local-pending -> persisted -> delivered -> read`; có nhánh `failed`.

### Đơn hàng

`Pending -> AwaitingPayment -> Paid -> Processing -> Completed` hoặc `Cancelled`.

### Báo cáo

`Pending -> InReview -> ActionPending -> Actioned -> Closed`, hoặc `Rejected`.

### Xóa tài khoản

`none -> requested/grace-period -> processing -> completed`; có nhánh `cancelled`.

## Trạng thái xác thực bổ sung

| Trạng thái | Hiển thị | Hành động |
|---|---|---|
| `toast_success` | Toast top-end, không che form | Tự đóng hoặc mở đích an toàn |
| `password_criteria_invalid` | Dấu X + tiêu chí chưa đạt dưới trường mật khẩu | Giữ dữ liệu, focus tiêu chí đầu tiên chưa đạt |
| `verification_success` | Modal giữa màn hình, focus bị giữ trong modal | Chọn OK để chuyển sang form mật khẩu mới |
| `password_reset_ready` | Chỉ hiện mật khẩu mới và xác nhận; không hiện OTP | Đổi mật khẩu một lần, khóa gửi lặp |

## Trạng thái bài viết bổ sung

- Media luôn dùng toàn bộ chiều rộng khả dụng của PostCard.
- Action bar nằm dưới media theo thứ tự: Thích, Bình luận, Đăng lại, Lưu, Chia sẻ.
- Khi video xử lý nền, toast top-end chỉ báo tiến trình; lỗi chi tiết nằm trong vùng có nút Thử lại hoặc Lưu bản nháp.

