# Quy ước mã nguồn

## Quy tắc chung

- Ưu tiên mã dễ đọc và bất biến rõ hơn abstraction phức tạp.
- Mỗi hàm có một trách nhiệm; tên phản ánh nghiệp vụ.
- Không dùng chuỗi “ma thuật” cho loại sự kiện, mã lỗi, chính sách hoặc header.
- Không dùng trạng thái toàn cục có thể thay đổi.
- Không nuốt exception; phân loại lỗi nghiệp vụ, dữ liệu sai, phân quyền và lỗi tạm thời.
- Thư viện mới phải có lý do, giấy phép phù hợp, kết quả quét bảo mật và cách quay lui.

## C# và .NET

- Tuân theo `.editorconfig` và analyzer thực tế của kho mã.
- Dùng nullable annotations đúng với khả năng xảy ra khi chạy; không dùng `!` để che bất biến chưa chứng minh.
- Dùng `IReadOnlyCollection` hoặc kiểu bất biến khi bên gọi không được sửa.
- Đặt `CancellationToken` ở cuối danh sách tham số và truyền xuyên mọi I/O.
- Dùng `DateTimeOffset` theo UTC cho thời gian nghiệp vụ.
- Tiền tệ dùng `decimal` hoặc value object và luôn có mã tiền tệ rõ.
- Truy vấn EF chỉ chiếu trường cần thiết, phân trang tại cơ sở dữ liệu và kiểm tra SQL cho đường nóng.
- Chỉ dùng `First` hoặc `Single` khi ý nghĩa thật sự yêu cầu exception; phân biệt `null` với tập rỗng.
- Không gọi dịch vụ ngoài trong giao dịch cơ sở dữ liệu, trừ trường hợp có lý do, timeout và cơ chế bù trừ rõ.

## Angular và TypeScript

Phiên bản và mẫu tổ chức phải được khám phá từ kho mã. Nguyên tắc chung:

- Bật chế độ nghiêm ngặt theo cấu hình hiện có.
- Không dùng `any` khi có thể mô hình hóa hợp đồng.
- Component không chứa luồng nghiệp vụ phức tạp; tách service/store theo quy ước hiện tại.
- Hủy subscription hoặc dùng cơ chế quản lý vòng đời của framework.
- Giao diện chỉ hỗ trợ trải nghiệm; backend luôn kiểm tra phân quyền lại.
- Mã hóa/làm sạch nội dung theo chính sách; không bỏ qua cơ chế bảo mật tùy tiện.

## Bình luận và tài liệu

- Bình luận giải thích “vì sao”, bất biến hoặc đánh đổi; không lặp lại điều mã đã thể hiện.
- Hợp đồng công khai và hành vi khó hiểu phải có tài liệu phù hợp.
- Không để bình luận cũ mâu thuẫn với mã hiện tại.
