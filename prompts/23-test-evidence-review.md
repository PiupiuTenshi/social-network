---
id: test-evidence-review
ket_qua_chinh: Ma trận kiểm thử và khoảng trống bằng chứng
---
# Rà soát bằng chứng kiểm thử

## Chế độ thực hiện

Chỉ đọc, phân tích và đề xuất. Không chỉnh mã sản phẩm, mã kiểm thử hoặc cấu hình.

## Đầu vào

- Mã nhiệm vụ: `{{TASK_ID}}`
- Loại nhiệm vụ: `{{TASK_TYPE}}`
- Mã chức năng hoặc vấn đề: `{{FUNCTION_ID}}`
- Miền: `{{DOMAIN}}`
- Yêu cầu: {{DESCRIPTION}}
- Bằng chứng hiện có: {{EVIDENCE}}
- Ràng buộc: {{CONSTRAINTS}}
- Tiêu chí chấp nhận: {{ACCEPTANCE_CRITERIA}}

## Nhiệm vụ

1. Đọc tiêu chí chấp nhận, mã liên quan, kiểm thử hiện có và kết quả CI đã cung cấp.
2. Lập ma trận: tiêu chí hoặc rủi ro -> cấp kiểm thử -> tệp/test hiện có -> kết quả -> khoảng trống.
3. Kiểm tra luồng thành công, dữ liệu sai, phân quyền, lỗi phụ thuộc, xử lý đồng thời, xử lý lặp an toàn, thử lại, tính tương thích và NFR khi liên quan.
4. Phân biệt kiểm thử đã chạy thành công, chỉ tồn tại trong mã và chưa được xác minh.
5. Đề xuất kiểm thử bổ sung theo thứ tự ưu tiên, nêu dữ liệu, assertion và lệnh dự kiến.
6. Không báo đạt chỉ vì có tệp kiểm thử; cần kết quả lệnh hoặc tệp bằng chứng phù hợp.

## Đầu ra

- Ma trận kiểm thử và bằng chứng.
- Khoảng trống chặn hoàn thành.
- Kiểm thử đề xuất theo mức ưu tiên.
- Lệnh cần chạy nhưng chưa xác minh.
- Rủi ro còn lại.
