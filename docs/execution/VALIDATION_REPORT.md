# Kiểm chứng bộ kế hoạch và cổng READY

Ngày: **07/09/2026**. Kết luận: bộ kế hoạch, gate và validator kit/UI/UX đã chạy đạt trên Windows. Không có bằng chứng nghiệm thu sản phẩm được tạo từ các kết quả này.

## Môi trường và phạm vi

- Windows/PowerShell, Python **3.11.9**, PyYAML **6.0.3**.
- Lần đầu `validate_all.py` dừng ở validator thiết kế do thiếu `PIL`; không ghi lần đó là PASS.
- Đã cài **Pillow 12.3.0**, nằm trong dải có sẵn `Pillow>=10,<13` của `design/requirements.txt`, vào `work/document-audit/python-deps`. Tiến trình kiểm chứng dùng `PYTHONPATH` tới thư mục này; không cài vào Python toàn máy.
- Không cần thư viện ngoài cho bộ sinh/gate/33 tests. Không chạy .NET/Angular/product integration vì chưa có ứng dụng.
- Log tổng hợp tại [validation/validate-all.txt](validation/validate-all.txt); chỉ thay đường dẫn tuyệt đối workspace/interpreter bằng `$REPO`/`$PYTHON` để bàn giao gọn.

## Kiểm tra đã chạy

| Lệnh/kiểm tra | Kết quả thực tế |
|---|---|
| `python -X utf8 scripts/build_execution_plan.py --check` | Exit 0; 9 phase, 158 task, 318 subtask; file sinh khớp bộ sinh |
| `python -X utf8 scripts/task_gate.py validate` | Exit 0; 318 node, không ID trùng/dependency thiếu/vòng lặp, plan/state hợp lệ |
| `python -X utf8 scripts/test_task_gate.py` | **34/34 tests PASS** |
| `python -X utf8 scripts/validate_vibe_kit.py` | Exit 0; cấu trúc, Unicode, biên dịch script, context-map, manifest và liên kết đạt |
| `python -X utf8 design/scripts/validate_design.py --require-final` | Exit 0; 47 màn hình, 110 SVG, 110 PNG; metadata, links, tokens, approval và cấu trúc ảnh đạt |
| `python -X utf8 scripts/validate_all.py` với môi trường trên | Exit 0; chạy liên tiếp toàn bộ các bước trên |
| `verify_source_baseline.py` với DOCX gốc | Exit 0; SHA-256 khớp baseline |
| Hash PDF và đối chiếu mã DOCX/PDF | PDF SHA-256 khớp hồ sơ; 84 trang, cùng 66 mã chức năng |

34 tests gồm 26 ca gate và 8 ca kế hoạch thực tế: DoR/evidence thiếu hoặc sai; không được bỏ bước; review đúng completion; artifact/path/hash; evidence và nguồn bị sửa; STALE lan truyền; lock/WIP; JSON trùng khóa; DAG; coverage 66 chức năng và 47 màn hình; P1 sau G1, P2 sau G2; G1/G2 không phụ thuộc ngược ưu tiên; chỉ mục thứ tự có đủ 318 ID và không đặt task trước dependency.

## Thử từ chối qua CLI thật

Kết quả đầy đủ tại [validation/gate-cli.json](validation/gate-cli.json). Đây là kiểm thử **từ chối như mong đợi**; exit khác 0 trong bảng dưới không phải test thất bại.

| Lệnh `task_gate.py …` | Exit mong đợi/thực tế | Hành vi |
|---|---|---|
| `check PH00-GOV-AUDIT-01` | 1 / 1 | NOT_READY; chưa có DoR |
| `start PH00-GOV-AUDIT-01` | 2 / 2 | Không bắt đầu khi chưa READY |
| `check PH03-BE-SOC-03-01` | 1 / 1 | Tiền nhiệm chưa DONE |
| `start PH03-BE-SOC-03-01` | 2 / 2 | Từ chối task phía sau |
| `prompt PH03-BE-SOC-03-01` | 1 / 1 | Không cấp prompt thực thi cho task bị chặn |
| `check NOT-A-TASK` | 2 / 2 | Từ chối ID không tồn tại |
| `prompt PH00-GOV-AUDIT-01 --preview` | 0 / 0 | Chỉ xem, có nhãn PREVIEW |

Hash `state.json` trước/sau các lệnh trên không đổi: `a6406368c7b712bf892b56c97c368db03891b05420f57ec38382a98c21510ac0`. `tasks` và `history` vẫn rỗng. Tests thành công dùng fixture trong thư mục tạm; không ghi DONE vào kế hoạch thật.

## Phân bố bàn giao

| Phase | Task | Subtask |
|---|---:|---:|
| PH00 | 5 | 5 |
| PH01 | 4 | 5 |
| PH02 | 11 | 22 |
| PH03 | 40 | 81 |
| PH04 | 49 | 102 |
| PH05 | 14 | 34 |
| PH06 | 32 | 63 |
| PH07 | 1 | 4 |
| PH08 | 2 | 2 |
| Tổng | **158** | **318** |

Theo nhóm subtask: Backend 146, Data 44, Frontend 116, Governance 6, Gate 6.

## Chưa được kết luận

- Chưa có subtask sản phẩm READY/DONE, G0–G4 chưa đạt; task đầu là `PH00-GOV-AUDIT-01: NEEDS_READY`.
- Validator ảnh đạt không thay visual review từng pixel, browser E2E hoặc kiểm accessibility runtime.
- Chưa có Git/remote/PR/branch protection thực tế; workflow mới chưa chạy trên hosting. BL-01 về file quy tắc trên Linux và BL-18 về product CI còn trong backlog.
- Chưa có build/test ứng dụng, migration/restore drill, load/security scan sản phẩm hay release/deploy. Không dùng báo cáo này để bỏ qua các task đó.
