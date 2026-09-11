# Cài Git hooks

Chạy một lần trong thư mục gốc của kho mã:

```bash
git config core.hooksPath .githooks
```

Hook chỉ kiểm tra thông điệp commit và tính toàn vẹn của bộ tài liệu. Biên dịch và kiểm thử sản phẩm vẫn phải chạy theo CI cùng Definition of Done.
