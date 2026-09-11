# Kế hoạch triển khai Frontend

## Giai đoạn 0 - Nền tảng giao diện

- App shell, route guard, error boundary, token, typography, icon và accessibility primitives.
- HTTP client, Problem Details mapper, auth refresh coordinator, SignalR adapter và feature flag.

## Giai đoạn 1 - P0

1. Xác thực cơ sở: AUTH-01 đến AUTH-03.
2. Bảng tin và bài viết: FEED-01 đến FEED-04.
3. Hồ sơ và thiết lập cơ sở.
4. Chat, notification và trạng thái hệ thống.

## Giai đoạn 2 - P1

- Khôi phục mật khẩu, xóa tài khoản, cộng đồng, RTC, media, video và điều hành nội dung.

## Giai đoạn 3 - P2

- Marketplace, AI, tóm tắt và các chức năng chỉ được bật khi hợp đồng Backend tương ứng đã khóa.

## Cổng hoàn thành mỗi màn hình

- Route và quyền đúng.
- Desktop + mobile đúng thứ tự ưu tiên.
- Loading/empty/error/offline/forbidden được xử lý.
- Keyboard, focus, aria và độ tương phản đạt.
- Test tối thiểu cho happy path, validation, authorization và retry/idempotency khi liên quan.
- Không còn dữ liệu giả nằm trên đường chạy production.
