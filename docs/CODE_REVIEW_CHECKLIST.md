# Danh sách rà soát mã nguồn

## Ý định và phạm vi

- [ ] Phần khác biệt đúng mục tiêu của issue hoặc pull request.
- [ ] Không có tái cấu trúc hoặc nâng cấp thư viện ngoài phạm vi.
- [ ] Hành vi hiện tại, hành vi mong muốn và phần ngoài mục tiêu rõ.

## Kiến trúc

- [ ] Đúng dịch vụ sở hữu; không truy vấn hoặc khóa ngoại xuyên cơ sở dữ liệu.
- [ ] Đúng hướng phụ thuộc; API không truy cập `DbContext` trực tiếp.
- [ ] Mã dùng chung không mang quy tắc nghiệp vụ riêng của một miền.

## Hợp đồng và dữ liệu

- [ ] Mã trạng thái, lược đồ và lỗi đúng hợp đồng API.
- [ ] Vỏ sự kiện, khóa phân vùng, phiên bản và bên nhận đúng danh mục.
- [ ] Di trú tương thích; chỉ mục, ràng buộc và concurrency token bảo vệ bất biến.
- [ ] Thử lại hoặc phát lại không nhân đôi tác dụng phụ.

## .NET

- [ ] Nullability đúng; không dùng `!` để che bất biến.
- [ ] Async và `CancellationToken` đúng; không sync-over-async.
- [ ] LINQ/EF không tải thừa, đánh giá phía máy khách hoặc N+1.
- [ ] Vòng đời DI và cách dùng `DbContext` an toàn.

## Bảo mật

- [ ] Xác thực và phân quyền được áp dụng trên mọi đường.
- [ ] Không có BOLA/IDOR, injection, XSS, SSRF hoặc rò rỉ secret.
- [ ] Log và dữ liệu quan sát không chứa PII hoặc token.

## Kiểm thử và vận hành

- [ ] Kiểm thử hành vi quan sát được và tình huống lỗi/tranh chấp phù hợp.
- [ ] Có kiểm thử hồi quy cho lỗi.
- [ ] Metric, log, trace, cảnh báo và runbook được cập nhật khi cần.
- [ ] Lệnh kiểm chứng có kết quả thật.

Mỗi phát hiện phải có mức độ, vị trí, kịch bản lỗi, tác động, bằng chứng và cách khắc phục. Tránh nhận xét chỉ về phong cách đã có công cụ tự động xử lý.
