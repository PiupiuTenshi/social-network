# Quy tắc thiết kế giao diện

## Phân cấp

- Một màn hình có một hành động chính rõ ràng.
- Hành động nguy hiểm không được đặt ngang cấp thị giác với hành động thường.
- Nội dung quan trọng xuất hiện trước thông tin bổ trợ trên mobile.
- Không thêm thanh điều hướng hoặc mô hình tương tác mới khi chưa cập nhật kiến trúc thông tin.

## Trạng thái

- Mọi vùng tải bất đồng bộ phải có loading, empty, success và error.
- Lỗi có thể thử lại phải giữ dữ liệu người dùng đã nhập.
- 401 dẫn về luồng xác thực; 403 không tiết lộ dữ liệu; 404 có thể dùng để ẩn tài nguyên; 409/412 phải giải thích xung đột; 429 hiển thị thời gian thử lại khi có; 503 phải có fallback hoặc thông báo suy giảm.
- Reconnect không tạo side effect lặp; UI phải phản ánh trạng thái đang gửi/đang đồng bộ.

## Responsive

- Không thu nhỏ desktop theo tỷ lệ để tạo mobile.
- Split view chuyển thành route con, drawer hoặc stacked layout.
- Bảng chuyển thành card/list khi cột không còn đọc được.
- Navigation desktop và mobile giữ cùng ý nghĩa, không nhất thiết cùng hình thức.

## Accessibility

- Semantic HTML trước ARIA.
- Focus order theo thứ tự đọc; focus được chuyển có chủ đích khi mở/đóng dialog.
- Icon-only control có accessible name.
- Form có label, mô tả lỗi và liên kết `aria-describedby` phù hợp.
- Hỗ trợ `prefers-reduced-motion`.
- Contrast văn bản và điều khiển phải đạt WCAG AA.

## Token và component

- Không hard-code màu, spacing, radius, shadow hoặc breakpoint khi đã có token.
- Component dùng chung phải có API nhỏ, trạng thái rõ và không chứa quy tắc nghiệp vụ của màn hình.
- Variant chỉ được thêm khi có ít nhất một use case thật trong tài liệu.
