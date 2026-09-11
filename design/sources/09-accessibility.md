# 09. Accessibility

Mục tiêu tối thiểu: WCAG 2.2 AA cho luồng P0/P1.

## Bàn phím

- Mọi chức năng dùng được bằng bàn phím.
- Focus order theo bố cục và không nhảy vào nội dung ẩn.
- Focus ring luôn nhìn thấy.
- Dialog giữ focus và trả focus sau khi đóng.
- Drag/drop có thao tác thay thế bằng nút.

## Trình đọc màn hình

- Một H1 trên mỗi route.
- Landmark rõ: header, nav, main, complementary.
- Tin nhắn realtime dùng `role=log`; không đọc từng token AI.
- Thông báo trạng thái dùng live region phù hợp.
- Icon-only button có tên truy cập.

## Hình ảnh và media

- Ảnh nội dung có alt hoặc cơ chế nhập alt khi phù hợp.
- Avatar có tên người dùng trong text lân cận.
- Video có điều khiển chuẩn.
- Live captions là phần tương lai; UI không tuyên bố đã hỗ trợ.
- Audio tin nhắn có transcript khi job thành công, nhưng audio vẫn là nguồn gốc.

## Màu và tương phản

- Text thường tối thiểu 4.5:1.
- Text lớn tối thiểu 3:1.
- Focus/component boundary tối thiểu 3:1 khi áp dụng.
- Không dùng màu duy nhất để biểu đạt trạng thái.

## Form

- Label luôn tồn tại.
- Error gắn trường.
- Error summary tập trung sau submit.
- Không xóa dữ liệu người dùng khi lỗi.
