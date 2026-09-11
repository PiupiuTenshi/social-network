# Phát triển cục bộ

Tệp này chỉ chứa lệnh đã được xác minh trong kho mã. Các chỗ trống phải được điền sau khi tạo solution và ứng dụng; không đoán phiên bản hoặc đường dẫn.

## Yêu cầu

- .NET SDK: lấy từ `global.json`.
- Node/npm: lấy từ `.nvmrc`, `package.json` và lockfile.
- Docker/Compose: lấy từ tài liệu hoặc pipeline đã kiểm chứng.
- Secret phát triển: dùng user-secrets hoặc `.env` không commit.

## Lệnh chuẩn

```bash
# Khởi động hạ tầng
[CHUA_XAC_MINH_TU_KHO_MA]

# Khôi phục gói và biên dịch backend
[CHUA_XAC_MINH_TU_KHO_MA]

# Chạy kiểm thử đơn vị và tích hợp
[CHUA_XAC_MINH_TU_KHO_MA]

# Cài đặt và chạy Angular
[CHUA_XAC_MINH_TU_KHO_MA]

# Chạy di trú có kiểm soát
[CHUA_XAC_MINH_TU_KHO_MA]
```

## Kiểm tra sức khỏe

Liệt kê endpoint và lệnh thực tế sau khi triển khai. Không ghi “đã kiểm chứng” khi chưa chạy trên môi trường sạch.
