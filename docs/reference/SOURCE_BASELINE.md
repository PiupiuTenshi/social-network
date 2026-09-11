# Nguồn thiết kế cơ sở

## Tài liệu nguồn

- Tên tệp: `source-documents/SocialPlatform_ThietKeHeThongChiTiet_BanCuoi_v3_0.docx`
- Phiên bản nội dung: `3.0`
- SHA-256 DOCX: `5fb171fd30096c2ced50d8d27d139a07488cf7df918a1ad171f31c839184154d`
- Bản PDF: `source-documents/SocialPlatform_ThietKeHeThongChiTiet_BanCuoi_v3_0.pdf`
- SHA-256 PDF: `e9ae5a404e764738d8c8aa979fcf750aa8048f82e53bfe763d0de49e95028921`
- Vai trò: nguồn thiết kế nghiệp vụ và kỹ thuật để sinh các tài liệu tham chiếu trong thư mục này.

## Quy tắc đồng bộ

1. Không sửa thủ công danh mục trích xuất rồi coi đó là thay đổi thiết kế đã được duyệt.
2. Khi tài liệu nguồn đổi, tạo phiên bản mới, ghi ADR nếu thay đổi kiến trúc và tái sinh các tệp `docs/reference/`.
3. Đối chiếu ít nhất: ownership, API, event, dữ liệu, function specification, traceability, NFR, bảo mật và vận hành.
4. Chạy `python scripts/validate_vibe_kit.py` và review diff trước khi hợp nhất.
5. Không đưa tệp nguồn có dữ liệu nhạy cảm vào repository công khai nếu chưa được phép.
