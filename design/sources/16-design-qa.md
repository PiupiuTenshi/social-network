# 16. Kiểm tra chất lượng thiết kế

## Visual QA

- Không cắt text ở 320, 390, 768, 1024 và 1440 px.
- Không có hành động chính ngoài viewport mà không có chỉ dẫn cuộn.
- Nút/field cùng loại có cùng chiều cao.
- Modal không vượt 90vh; nội dung có scroll nội bộ hợp lý.
- Mobile keyboard không che composer/submit.

## UX QA

- Mỗi thao tác có phản hồi.
- Lỗi giữ dữ liệu người dùng.
- Back/refresh/deep link không phá luồng.
- Double-click/retry không tạo side effect trùng.
- Stale data 412 có đường giải quyết.
- Offline/reconnect có hành vi xác định.
- Feature flag không để link chết.

## Accessibility QA

- Keyboard-only pass.
- Screen-reader smoke pass cho auth/feed/chat.
- Contrast audit.
- Reduced motion.
- 200% zoom/reflow.
- Touch target.

## Contract QA

- Route/API/function mapping đầy đủ.
- Không gọi API không có trong source mà không đánh dấu “cần khóa hợp đồng”.
- Mã lỗi và trạng thái UI phù hợp.

## Kiểm tra được bổ sung ở vòng cuối

- Toast top-end không chồng tiêu đề, input, menu hoặc CTA ở 390 px và 1440 px.
- Checklist mật khẩu có cả biểu tượng, chữ và thông báo `aria-live`; không chỉ dựa vào màu.
- Modal OTP giữ focus, đóng bằng nút rõ ràng và không để OTP tiếp tục chỉnh sửa sau xác minh.
- Video không bị thu hẹp để dành action rail; action bar nằm dưới media trên desktop và mobile.
- Rich text toolbar có nhóm điều khiển, trạng thái active và tên truy cập; không dùng icon mơ hồ không có nhãn.
- Trạng thái xử lý video và trạng thái thất bại không xuất hiện mâu thuẫn trong cùng một thời điểm.

