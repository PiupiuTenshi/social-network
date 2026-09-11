# Hồ sơ đọc và đối chiếu tài liệu

Ngày thực hiện: **07/09/2026**. Mục tiêu: chuyển bộ thiết kế thành phase → Backend/Data/Frontend → task/subtask → prompt theo ID, cùng điều kiện READY và Git flow. Đây là khảo sát để lập kế hoạch, chưa phải nghiệm thu sản phẩm.

## Phạm vi nguồn

Manifest đầu vào liệt kê 505 mục, trong đó 216 mục Markdown. Trên Windows, `AGENTS.md` và `agents.md` cùng trỏ vào một file; không tính chúng là hai bộ quy tắc độc lập. [SOURCE_INVENTORY.json](SOURCE_INVENTORY.json) lưu 236 mục nguồn văn bản/cấu hình/DOCX/PDF cùng kích thước và SHA-256 quan sát trong lúc khảo sát, trước khi bổ sung các liên kết điều hướng execution. Đây là snapshot truy vết; hash tài liệu được sửa sau đó có thể khác. MANIFEST/checksums ở root mô tả bộ bàn giao hiện tại.

| Nhóm | Phạm vi đã đọc/đối chiếu | Tác động vào kế hoạch |
|---|---|---|
| Quy tắc và điều phối | Entry AGENTS, RULES, START_HERE, context-map, hướng dẫn công cụ, CONTRIBUTING, SECURITY | Ngôn ngữ, ownership, điều kiện dừng, workflow và quyền thực hiện |
| Tài liệu dự án | 55 Markdown trong `docs/`, gồm ADR và reference | Kiến trúc, 66 chức năng, dữ liệu/API/events, NFR, ưu tiên, kiểm thử và vận hành |
| Prompt/biểu mẫu | 28 Markdown trong `prompts/`, 13 trong `templates/`, command aliases và PR/issue templates | Hình thức prompt, acceptance, chứng cứ, review và bàn giao |
| UI/UX chuẩn | 20 nguồn dùng chung (00–19), 47 screen specs, inventory, tokens, routes, state/contract-readiness, implementation/QA guides và bản tổng hợp | 47 màn hình, các phần P0/P1/P2, dependency API, responsive và accessibility |
| Lịch sử thiết kế | Archive, feedback/history, changelog và trạng thái approved hiện tại | Phân biệt quyết định cuối với bản bị loại; không khôi phục màn AI-03 độc lập |
| Nguồn DOCX | Trích 4.437 đoạn văn bản/XML, gồm bảng và đặc tả | Đối chiếu nguồn gốc, ownership, hợp đồng, lifecycle và nghiệm thu |
| Nguồn PDF | Trích văn bản đủ 84 trang, rà cấu trúc 33 chương và đối chiếu danh mục mã | PDF và DOCX cùng có 66 mã chức năng; không có mã chỉ xuất hiện ở một bản |
| Công cụ/hạ tầng kit | Scripts, Git hooks, workflow, gitignore/gitattributes, inventory và source verifier | Cơ chế READY, kiểm DAG, CI kế hoạch và các blocker công cụ hiện có |

Phần văn bản trùng giữa prompt aliases, screen specs và bản tổng hợp được đối chiếu theo nội dung chung cùng các dòng khác biệt. Không xem văn bản lặp là yêu cầu mới. `design.md` ở root khác `design/design.md` về đường dẫn tương đối và chú thích bản tiện dụng theo `scripts/sync_root_design.py`; nguồn UI vẫn là bản trong `design/`.

## Baseline tài liệu gốc

| Tệp | SHA-256 |
|---|---|
| `SocialPlatform_ThietKeHeThongChiTiet_BanCuoi_v3_0.docx` | `5fb171fd30096c2ced50d8d27d139a07488cf7df918a1ad171f31c839184154d` |
| `SocialPlatform_ThietKeHeThongChiTiet_BanCuoi_v3_0.pdf` | `e9ae5a404e764738d8c8aa979fcf750aa8048f82e53bfe763d0de49e95028921` |

DOCX/PDF không bị chỉnh sửa. Có thể kiểm lại DOCX bằng `scripts/verify_source_baseline.py` và hash cả hai bằng `Get-FileHash`. Văn bản trích xuất tạm nằm trong `work/document-audit/`, được loại khỏi Git và danh mục phân phối; không cần PyMuPDF/DOCX parser để chạy gate hoặc tái sinh kế hoạch.

## Các kết luận ảnh hưởng thứ tự triển khai

1. Đây là kit tài liệu/thiết kế; chưa có sản phẩm có thể build/test. Không dùng CI tài liệu xanh để báo G0–G4 đạt.
2. Giữ 8 dịch vụ nghiệp vụ, Gateway/BuildingBlocks riêng; Data là nhóm công việc, không phải một dịch vụ sở hữu mọi DB.
3. Giữ main và nhánh ngắn theo ADR/Git flow hiện có. Luồng phase theo ưu tiên: khóa nền → P0 → G1 → P1 → G2 → P2 được chọn → gia cố → G4.
4. UI có nhiều khả năng ngoài contract baseline. Tách màn hình thành các lát cắt ưu tiên; phần chưa khóa không được tự tạo API hoặc đưa vào nghiệm thu như đã triển khai.
5. Media text-only P0, phân tách OAuth/OTP, deletion participants theo dịch vụ đang bật và phạm vi OpenSearch cần được chốt tại task contract tương ứng. Kế hoạch thể hiện cách tránh phụ thuộc vòng; không thay ADR bằng suy luận của người lập kế hoạch.
6. Tập hợp 18 nhóm vấn đề có nguồn, tác động, owner và đầu ra xử lý tại [BLOCKERS.md](BLOCKERS.md). Task GOV/contract đi trước phần sản phẩm bị ảnh hưởng.

## Giới hạn của lần khảo sát

- SVG/PNG/gallery và các hình nhúng được kiểm kê, liên kết với spec và dùng làm nguồn cho task QA sau này. Không tuyên bố đã kiểm bằng mắt từng ảnh, render lại toàn bộ hình hoặc kiểm từng pixel của PDF.
- Kiểm đủ văn bản/mã chức năng không chứng minh mọi đoạn DOCX/PDF giống nhau từng chữ; khác biệt hợp đồng vẫn cần quyết định ở đúng owner.
- Approval UI 47/47 là trạng thái có sẵn trong bộ thiết kế, không phải phê duyệt mới của lần lập kế hoạch và không chứng minh Backend ready.
- Không có Git repository/remote ở workspace lúc khảo sát. Chưa tạo branch/tag, commit, push, PR, ruleset hay deploy. Playbook là hướng dẫn thao tác có điều kiện.
- Tại thời điểm khảo sát ban đầu, `agents.md` là shim tự trỏ. PH00-GOV-AUDIT-01 đã thay nó bằng `AGENTS.md` canonical, có nội dung quy tắc và không giữ alias chỉ khác hoa/thường. Cần kiểm lại tên tệp sau `git init`/checkout Linux; xem audit report.
- Không chọn/bịa phiên bản .NET/Angular/package hay kết quả test sản phẩm. PH00-BE-TOOLCHAIN và PH01-BE-CI phải xác minh chúng bằng tệp khai báo và lệnh chạy thật.

Kết quả kiểm tra **bộ kế hoạch và công cụ** được ghi tại [VALIDATION_REPORT.md](VALIDATION_REPORT.md). `state.json` chưa chứa hồ sơ READY/DONE; các báo cáo của lần lập kế hoạch không tự mở cổng cho task sản phẩm.
