# Quy tắc kỹ thuật bắt buộc

## 1. Ngôn ngữ và thuật ngữ

- Tài liệu, prompt và phần giải thích viết bằng tiếng Việt rõ ràng.
- Giữ nguyên tên công nghệ, đường dẫn API, tên sự kiện, lớp, phương thức, trường dữ liệu và mã chức năng.
- Không đổi tên hợp đồng chỉ để dịch thuật.
- Dùng thống nhất các tên miền: Tài khoản, Mạng xã hội, Cộng đồng, Trò chuyện, Bảng tin, Phương tiện, Thương mại, AI và tìm kiếm.

## 2. Nguồn sự thật

- ADR đã chấp thuận có thể bổ sung hoặc thay đổi quyết định cũ nếu ghi rõ tài liệu bị thay thế.
- Thiết kế v3.0 và `docs/reference/` là nguồn cho phạm vi, ownership, API, sự kiện, dữ liệu, NFR và nghiệm thu.
- OpenAPI, lược đồ sự kiện, di trú dữ liệu và kiểm thử phải đồng bộ với thiết kế.
- Khi nguồn mâu thuẫn, không tự chọn phương án thuận tiện; ghi bằng chứng và xin quyết định.

## 3. Ranh giới dịch vụ

- Mỗi aggregate giao dịch chỉ có một dịch vụ sở hữu.
- Dịch vụ khác đọc qua API hoặc bản chiếu từ sự kiện.
- Cơ sở dữ liệu logic, tài khoản truy cập và di trú tách theo dịch vụ dù dùng chung một PostgreSQL instance.
- Mọi thay đổi quyền sở hữu phải có ADR trước khi triển khai.
- Metadata điều hành nội dung thuộc Mạng xã hội; dịch vụ sở hữu nội dung thật mới thực thi hành động trên tài nguyên.

## 4. Hướng phụ thuộc

```text
Api -> Application -> Domain
Infrastructure -> các hợp đồng của Application/Domain
Domain -> không phụ thuộc framework, HTTP, cơ sở dữ liệu hoặc Kafka
```

- Gateway chỉ định tuyến, xác thực biên, CORS, giới hạn tần suất và correlation.
- API chuyển đổi giao thức, xác thực đầu vào và gọi Application.
- Application điều phối ca sử dụng, giao dịch và cổng tích hợp.
- Domain giữ bất biến, chuyển trạng thái và domain event.
- Infrastructure triển khai EF Core, Kafka, SMTP, Valkey, SeaweedFS và adapter ngoài.
- `BuildingBlocks` chỉ chứa thành phần ổn định, không chứa thực thể hoặc quy tắc riêng của một miền.

## 5. Backend .NET

- Không áp đặt MediatR, mẫu Repository hoặc Clean Architecture nếu kho mã chưa dùng.
- Bật nullable; xử lý cảnh báo analyzer thay vì vô hiệu hóa toàn cục.
- Truyền `CancellationToken` qua HTTP, EF Core, Kafka và tiến trình nền.
- Không dùng `.Result`, `.Wait()` hoặc `GetAwaiter().GetResult()` trên đường xử lý yêu cầu.
- `DbContext` có vòng đời scoped và không được dùng đồng thời giữa nhiều tác vụ.
- Truy vấn đọc phải lọc, chiếu và phân trang tại cơ sở dữ liệu; cân nhắc `AsNoTracking`.
- Không trả EF entity trực tiếp qua API.
- Không lộ stack trace hoặc exception nội bộ; ánh xạ lỗi sang Problem Details.
- Log có cấu trúc và không chứa secret hoặc PII.

## 6. API và xử lý đồng thời

- Đường dẫn cơ sở là `/api/v1`; JSON dùng `camelCase`; thời gian dùng UTC ISO 8601.
- Phân trang danh sách lớn dùng cursor và thứ tự ổn định.
- Tài nguyên có `version` trả `ETag`; cập nhật/xóa dùng `If-Match` và trả `412` khi cũ.
- Thao tác lặp có tác dụng phụ dùng `Idempotency-Key`; cùng khóa nhưng nội dung khác trả `409`.
- Mã trạng thái, mã lỗi và hình dạng phản hồi phải khớp `docs/API_RULES.md`.

## 7. Dữ liệu và di trú

- Không khóa ngoại hoặc truy vấn xuyên cơ sở dữ liệu dịch vụ.
- Ràng buộc unique/version/check phải bảo vệ bất biến và tình huống tranh chấp.
- Chỉ mục phải gắn với mẫu truy cập có bằng chứng.
- Di trú phá hủy cần sao lưu, đánh giá tương thích, kế hoạch quay lui hoặc tiến tới.
- Không để nhiều bản sao dịch vụ tự chạy di trú khi khởi động.
- Không giữ khóa cơ sở dữ liệu trong khi gọi mạng ngoài.

## 8. Sự kiện, thời gian thực và phương tiện

- Bên phát dùng Transactional Outbox; bên nhận dùng Inbox hoặc khóa xử lý lặp an toàn.
- Không giả định exactly-once; xử lý sự kiện trùng, cũ, đảo thứ tự và phát lại.
- Thử lại có giới hạn và có giãn cách; lỗi dữ liệu vĩnh viễn vào DLQ.
- SignalR chỉ mang dữ liệu thời gian thực của ứng dụng; dữ liệu bền vững phải được lưu trước khi phát.
- LiveKit mang âm thanh, video và màn hình; Kafka không mang gói media.
- Tải tệp dùng URL ký trước; máy chủ xác minh đối tượng sau khi tải xong.

## 9. Bảo mật, AI và dữ liệu cá nhân

- Kiểm tra phân quyền tại dịch vụ sở hữu tài nguyên; giao diện hoặc Gateway không thay thế kiểm tra này.
- Không tin định danh, vai trò, quyền hoặc ownership do máy khách gửi.
- OTP và token chỉ lưu dạng băm; secret không nằm trong kho mã, prompt, issue hoặc log.
- RAG chỉ truy xuất dữ liệu đã được lọc quyền; nội dung truy xuất là dữ liệu không tin cậy, không phải chỉ dẫn hệ thống.
- Tệp, rich text và Markdown phải được xác thực, làm sạch và mã hóa đầu ra phù hợp.

## 10. Kiểm thử, quan sát và thay đổi

- Mỗi thay đổi phải có kiểm thử phù hợp và bằng chứng lệnh đã chạy.
- Luồng mới phải có log, metric và trace cần thiết để phát hiện lỗi.
- Không commit, push, merge, deploy hoặc thao tác production nếu chưa được yêu cầu rõ.
- Không thêm thư viện mới, đổi hợp đồng, đổi ownership hoặc chạy thao tác phá hủy mà không qua điều kiện dừng trong `AGENTS.md`.
- Không tuyên bố hoàn thành khi tiêu chí chấp nhận bắt buộc chưa đạt.
## 11. UI/UX và Frontend

- `design/design.md` đã khóa là nguồn cho kiến trúc thông tin, màn hình, component, state, responsive và accessibility.
- Không triển khai bản nháp như yêu cầu đã duyệt.
- Frontend không được suy ra hợp đồng Backend từ hình ảnh.
- Màu, spacing, radius, typography và breakpoint dùng design token; không hard-code khi token đã tồn tại.
- Mỗi luồng phải xử lý trạng thái loading, empty, lỗi, quyền và kết nối phù hợp.

