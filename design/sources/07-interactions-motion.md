# Tương tác và chuyển động

- Vùng auth có avatar vector chuyển động ngang, chéo và theo đường cong; tôn trọng `prefers-reduced-motion`.
- Toast xuất hiện ở vị trí top-end trên cả desktop và mobile, có bù safe-area; không che tiêu đề, trường nhập hoặc CTA.
- Composer bảng tin dùng `position: sticky` nhưng không che nội dung khi bàn phím hoặc thanh trình duyệt mobile thay đổi.
- Tin nhắn đang gửi: chấm động; lỗi: nhãn “Gửi lỗi” kèm nút thử lại.
- Enter gửi, Shift+Enter xuống dòng; phải cấu hình được cho accessibility.
- Bài viết chi tiết mở ở layer trên desktop và route toàn màn hình trên mobile. Thích, Bình luận và Đăng lại luôn nằm dưới phương tiện.
