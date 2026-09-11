# Danh sách kiểm tra phát hành

## Trước phát hành

- [ ] Commit/tag bất biến; changelog và ghi chú phát hành đã cập nhật.
- [ ] Đạt G4; không còn lỗi Critical/High hoặc ngoại lệ chưa phê duyệt.
- [ ] OpenAPI, lược đồ sự kiện, di trú dữ liệu và tài liệu đồng bộ.
- [ ] Biên dịch, kiểm thử đơn vị, tích hợp, hợp đồng, kiến trúc, bảo mật và smoke test đạt.
- [ ] SBOM, quét thư viện/container và kiểm tra giấy phép đạt.
- [ ] Bản sao lưu hoặc snapshot cần thiết đã tạo và kiểm chứng.
- [ ] Di trú đã được thử trên cơ sở dữ liệu mới và đường nâng cấp từ phiên bản trước.
- [ ] Phương án quay lui hoặc tiến tới và cờ chức năng đã sẵn sàng.
- [ ] Cấu hình và secret của môi trường được xác minh, không in ra log.

## Triển khai

- [ ] Chạy di trú bằng job có kiểm soát.
- [ ] Khi đổi sự kiện, nâng bên nhận trước bên phát theo kế hoạch tương thích.
- [ ] Health check, readiness và smoke test đạt.
- [ ] Theo dõi tỷ lệ lỗi, p95, Outbox chờ, consumer lag, DLQ và pool cơ sở dữ liệu.

## Sau phát hành

- [ ] Đối chiếu tiêu chí chấp nhận và dữ liệu quan trọng.
- [ ] Xác nhận không có cảnh báo bất thường.
- [ ] Ghi phiên bản, thời gian, người thực hiện và bằng chứng.
- [ ] Xóa log bổ sung hoặc cờ tạm đúng thời hạn.
