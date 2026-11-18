# TEAM · LAB 10 · T001

- Lớp: L3A.
- Repo: https://github.com/BinhTa2004/K5-L3A-DAY10-T001-PoCtoPilotGate1
- Trưởng nhóm: Ta Cong Binh — 2A202603628.
- Thẻ đã bốc: **S1**. Nhóm chỉ phân tích và chạy S1; bộ nền dùng để kiểm hồi quy.

## Thành viên và phân công

| Thành viên | MSSV | Vai | Nội dung phụ trách |
|---|---|---|---|
| Trần Tuấn Đăng | 2A202603618 | Sản phẩm và kinh doanh | A1, A3–A5; soát B3; business gates, B7.4, B8; C1, soát specification, C12 và ba dòng bắt buộc; nhánh kinh doanh của fault tree |
| Ta Cong Binh | 2A202603628 | Trưởng nhóm, kỹ sư cổng | Repo/Git và tiêu chí ký; B0–B2, guards, HAZOP kỹ thuật; checkpoint, grade/trace/eval, C0/C2/C7; gom bài |
| Nguyen Tuan Dung | 2A202603608 | Kỹ sư cổng | A2 offline metric, dự thảo B3, B7.2–B7.3; specification, C6/C9, monitors/C8; số liệu và hồi quy |
| Hoang Hai Long | 2A202603670 | Vận hành và pháp lý | A1 góc nhìn người vận hành, telemetry; B4–B5, operations/legal, B7.5–B7.6; C3–C5 phần môi trường, C10–C11 và submission.json |

Các thành viên phụ trách nội dung theo bảng phân công. Mã lần chạy và báo cáo đánh giá là bằng chứng chung của nhóm.

## TranTuanDang-2A202603618

### Đóng góp cụ thể

- Xây dựng mục tiêu, tiêu chí chất lượng/an toàn, chi phí/ROI và bốn quy tắc quyết định; soát Phiếu A và bản đồ dữ liệu/drift B3.
- Giải trình trần hoàn ngày 2.000.000đ, ngân sách LLM 1.500đ/ticket, ROI tối thiểu 0.25 tại B7.4.
- Tổng hợp quyết định v1 tại B8; phụ trách đối chiếu kết quả v2 với ngưỡng đã ký, đọc phân khúc xấu nhất và ba dòng bắt buộc ở C12.

### Bằng chứng

- Commit `94f4aaa`: chốt cổng vòng 1/quyết định v1; bản tiêu chí của nhóm được ký bằng commit `d64c642`.
- Phiếu A; B3, B7.4, B8; C1, C5, C12 và `config/operating_gates.json` mục business.
- B8 gốc dẫn một run prepared cũ chưa có report trên máy; phụ lục B ghi rõ và bổ sung kết quả kiểm chứng `R-base-prepared-20261118-165612-591bdf`, không tạo giả report cũ.

### Exit ticket

- Điều học được: phải kiểm đồng thời chất lượng, an toàn và hiệu quả kinh tế; pass_rate cao không bù được một khoản hoàn sai. S1 sau sửa đạt 65/65, chi phí 6.008đ/ticket và ROI 0.66 vẫn cần đọc cùng các giới hạn của dữ liệu mock.
- Điều còn chưa chắc: chi phí/ROI và chất lượng tracking ngoài thực tế có giữ được khi mở rộng tải, kho và thay chính sách hay không; nhóm thiếu kho trên bộ nền còn tốn 10.359đ/ticket.

## TaCongBinh-2A202603628

### Đóng góp cụ thể

- Trưởng nhóm, chuẩn bị repo và điều phối; tự commit/push tiêu chí trước baseline, phối hợp tích hợp bài của nhóm.
- Phân tích T-002@55, xây dựng guards, bổ sung HAZOP kỹ thuật; đối chiếu checkpoint vòng 1 với bản hiện tại.
- Chạy grade trước sửa S1, dò các nguyên nhân khác nhau, sửa kiểm ngày giao, nhánh từ chối hoàn và trần lỗi hãng/ngày; chạy lại đánh giá/hồi quy và gom bài.

### Bằng chứng

- Commit ký `d64c642`; snapshot `ba703106`; commit `6742d56` cho guards và các commit tích hợp bài của nhóm.
- B0–B2, B4/B6 phần kỹ thuật, B7.1; C0, C2, C7; `lab10/guards.py`.
- Grade cuối: R-S1-grade-20261118-173517-e13c24; report ba mốc và nhật ký đầy đủ trong submission/runs/.

### Exit ticket

- Điều học được: kiểm lệnh hoàn tiền chưa đủ, vì nhánh từ chối có thể không gọi issue_refund; cũng cần kiểm trước phản hồi khi DB cho thấy khách còn quyền lợi.
- Điều còn chưa chắc: dữ liệu đúng cấu trúc có đúng thực tế không và bộ đếm trần có giữ được tính nguyên tử khi nhiều worker ghi đồng thời không; mock tuần tự chưa trả lời được.

## NguyenTuanDung-2A202603608

### Đóng góp cụ thể

- Phụ trách offline metric A2, dự thảo bản đồ dữ liệu/drift B3 để Đăng soát.
- Phụ trách hai bước chống rò rỉ dữ liệu đánh giá và behavioral test hai ticket tự viết ở B7.2–B7.3.
- Phối hợp specification C5, tổng hợp fault tree trước/sau C6/C9; phụ trách ba monitor ở C8, trích số liệu và kiểm hồi quy để hoàn thiện C12.

### Bằng chứng

- Phiếu A mục A2; B3, B7.2–B7.3; C5–C6, C8–C9; `lab10/monitors.py`.
- Grade R-S1-grade-20261118-173517-e13c24: monitor và regression đạt; ba metric tracking_claim_mismatch_rate, tracking_date_invalid_rate, carrier_strike_cap_block_rate sáng đèn trên S1 so với bộ nền.
- Kết quả chung sau sửa: S1 65/65, nền 110/110 và 13/13 test công khai đạt. Kết quả đánh giá được dùng chung cho nhóm.

### Exit ticket

- Điều học được: monitor dùng trong production phải tính từ dữ kiện/sự kiện không nhãn; sự kiện do ctx.log có type=guard và tên nằm ở kind, đọc sai trường sẽ làm metric không báo dù guard đã chặn.
- Điều còn chưa chắc: khi log bị mất hoặc DB sai nhưng hợp lệ, ba monitor hiện tại có thể bỏ sót; cần đo độ đầy đủ log, độ trễ cảnh báo và false alarm trên pilot thật.

## HoangHaiLong-2A202603670

### Đóng góp cụ thể

- Phụ trách góc nhìn vận hành/pháp lý, HAZOP ngoài kỹ thuật và checklist 9 nhóm có PIC; hoàn thiện B4–B7.6, quy trình người trực, chi phí/công suất và điều kiện dừng.
- Phụ trách phần riêng S1 ở C3.5, tổng hợp HAZOP C4, giả định môi trường C5; bổ sung risk register, checklist và runbook 4–5 ở C10–C11.
- Phụ trách thông tin bàn/thành viên/thẻ/quyết định/ba dòng trong submission.json; rà gói nộp Bình gom theo submission/README.md.

### Bằng chứng

- Commit `be4ae69`: cập nhật B4–B7.6 theo số base, kênh báo tin khớp bản chụp vòng 1.
- B4–B5, B7.5–B7.6; C3.5, C4–C5, C10–C11; `config/operating_gates.json` mục operations/legal và `submission/submission.json`.
- Grade R-S1-grade-20261118-173517-e13c24: S1 không còn lỗi hãng oan/PII, reviewer 1 người ×6 ca/giờ, không ùn ở tải mock; hạn chế về cao điểm và thực tế ghi tại runbook.

### Exit ticket

- Điều học được: nhiều hành động có vẻ đúng riêng lẻ vẫn có thể vượt quyền khi cộng dồn theo hãng/ngày; cổng phải đi kèm PIC, đối soát và quy trình xử lý phần bị chặn.
- Điều còn chưa chắc: một reviewer có đáp ứng giờ cao điểm thật và bên hãng có tin quyết định tự động không; cần diễn tập tải, kiểm thời gian chờ và lấy phản hồi người liên quan.

## Trạng thái bàn giao

- Chỉ làm thẻ S1. Grade R-S1-grade-20261118-173517-e13c24: visible, criteria, regression, monitor đạt; snapshot và tiêu chí còn nguyên. Hidden tests không có trên máy.
- Kết quả tổng: FAIL tại integrity do thiếu 28 file khóa S2–S8 của bộ phát hành. Visible, criteria, regression và monitor đạt; phạm vi phân tích của nhóm là S1.
- Quyết định v1: Tiếp tục. Quyết định v2: Cải tiến thêm; căn cứ và kế hoạch tiếp theo trình bày tại C12.
- Gói nộp chỉ giữ danh sách tại submission/README.md: code/config, ba phiếu, report gần nhất, ba mốc, nhật ký mọi lần chạy, submission.json và manifest. Không kèm probe, trace rời, readiness hay bản sao phiếu.
