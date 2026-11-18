# Ghi nhận lỗi kiểm gói khi nhóm chỉ được phát S1

Nhóm T001 được giao S1. Chỉ chạy S1 và bộ nền theo quy trình; không cần giải, chạy hoặc đọc thẻ S2–S8.

Lệnh tái hiện:

```powershell
python -X utf8 -m lab10.grade --incident S1
```

Report `R-S1-grade-20261118-172005-e13c24` có visible, regression, criteria, monitor đạt; checkpoint nguyên vẹn. S1 65/65 và nền 110/110 đạt; không hoàn sai, lỗi hãng oan, PII. Hidden tests không có trên máy.

Tổng grade FAIL do hàm integrity trong bộ chấm đọc toàn bộ `lab10/MANIFEST.json`, yêu cầu cả các thẻ không được phát. Có 28 đường dẫn thiếu (4 file mỗi S2–S8); toàn bộ file khóa thực sự có mặt, gồm 4 file S1, đều đúng hash. Đây là khác biệt giữa yêu cầu kiểm gói và cách phát riêng S1, không phải lỗi hash nội dung S1 hoặc yêu cầu làm thêm 7 thẻ.

Giữ nguyên manifest và bộ chấm. Cần Coach xác nhận bản phát hành/manifest chính thức phù hợp nhận riêng S1 hoặc cách xử lý ô integrity này; nhóm không tự tạo manifest thay thế, giả file, hay tuyên bố grade PASS. Không có liên hệ với Coach được tự động gửi.

Quyết định v2 hiện là Cải tiến thêm do thiếu xác nhận kiểm gói. `check_submission` báo ĐỦ THÀNH PHẦN chỉ xác nhận gói nộp đã đủ thành phần, không thay kết luận grade.
