# Checklist chuyển thiết kế thành mã

- [ ] Đã đọc `design.md` và đặc tả màn hình liên quan.
- [ ] Đã kiểm tra OpenAPI/AsyncAPI, không suy đoán endpoint.
- [ ] Đã tái sử dụng token và component hiện có.
- [ ] Đã triển khai desktop và mobile theo thiết kế, không scale cơ học.
- [ ] Đã có loading, empty, error, offline và unauthorized khi liên quan.
- [ ] Toast top-end không che UI; lỗi cần xử lý có bản inline/bền vững.
- [ ] Focus, keyboard, aria-label, aria-live và reduced-motion đạt.
- [ ] Đã xử lý hủy request, reconnect và gửi lặp khi liên quan.
- [ ] Đã chạy format/lint/build/test thật.
- [ ] Đã đối chiếu screenshot với SVG/PNG nguồn và ghi lại sai khác có chủ đích.
