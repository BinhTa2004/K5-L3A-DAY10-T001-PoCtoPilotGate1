# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `T001`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-T001-PoCtoPilotGate1`
- Link repo: https://github.com/BinhTa2004/K5-L3A-DAY10-T001-PoCtoPilotGate1
- Trưởng nhóm: Ta Cong Binh — MSSV `2A202603628`.
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Vai và đầu việc bên dưới là phân công đề xuất để nhóm xác nhận. Trưởng nhóm là Ta Cong Binh theo xác nhận của nhóm. Tên của ba thành viên được cung cấp không dấu được giữ không dấu, có tách khoảng trắng.

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
| 1 | Trần Tuấn Đăng | 2A202603618 | Sản phẩm và kinh doanh | |
| 2 | Ta Cong Binh | 2A202603628 | Kỹ sư cổng | Có |
| 3 | Nguyen Tuan Dung | 2A202603608 | Kỹ sư cổng | |
| 4 | Hoang Hai Long | 2A202603670 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công đề xuất

Phân công theo ba vai trong `problem-set.md`: hai Kỹ sư cổng, một Sản phẩm và kinh doanh, một Vận hành và pháp lý. Các đầu việc là kế hoạch thực hiện, chưa phải xác nhận đã hoàn thành.

| Thành viên | Vòng 1 | Vòng 2 và nộp bài | File / mục phụ trách chính |
|---|---|---|---|
| Trần Tuấn Đăng | Mục tiêu, tiêu chí, quy tắc quyết định; soát bản đồ dữ liệu / drift Dũng dự thảo; trần tiền, chi phí, ROI, phạm vi pilot; tổng hợp v1 | Soát specification; phân tích và sửa cổng business; tổng hợp C1, v2 và ba dòng bắt buộc; góp nhánh kinh doanh cho fault tree, trình bày quyết định | Sản phẩm và kinh doanh. A1 câu 1.1, A3–A5; `config/acceptance_criteria.json`; `config/operating_gates.json` mục `business`; B3 (soát và chịu trách nhiệm), B7.4, B8; C1, C5 câu 3.2 (soát), C7 phần kinh doanh, C12; góp nhánh kinh doanh C6 / C9. |
| Ta Cong Binh | Trưởng nhóm, repo / Git, tiến độ; hỗ trợ ranh giới đầu ra A4 và commit/push A5; baseline, trace, guards; cung cấp HAZOP kỹ thuật; chốt và đo prepared | Grade trước sửa; trace, sửa guards; bằng chứng HAZOP / fault tree; eval, grade và --collect sau khi đủ dữ liệu; trình bày ba mốc, đẩy bài | Trưởng nhóm, Kỹ sư cổng. `lab10/guards.py`; hỗ trợ A4–A5; B0–B2, B7.1; dòng kỹ thuật B4 / C4; C0, C2, C7 phần code; bằng chứng C6 / C9; chạy lệnh gom bài để Long kiểm nội dung. |
| Nguyen Tuan Dung | Offline metric; lập bản nháp bản đồ dữ liệu và bằng chứng drift để Đăng soát; hai bước tránh rò rỉ dữ liệu, behavioral test với hai ticket mới; test và hồi quy | Cùng dò lỗi; dự thảo specification; tổng hợp fault tree từ nhánh cả nhóm cung cấp; monitor; trích số report cho Đăng; kiểm hồi quy, đủ report và demo ticket hiểm | Kỹ sư cổng. A2 câu 1.3; B3 (dự thảo), B7.2, B7.3; `lab10/monitors.py`; C2, C5 câu 3.2 (dự thảo để Đăng soát), C6 / C9 (tổng hợp), C8; trích số liệu C12 và kiểm đủ report khi gom bài. |
| Hoang Hai Long | Mục tiêu kế toán / trưởng ca, telemetry; tổng hợp HAZOP, viết phần ngoài kỹ thuật; checklist từ bằng chứng từng người; operations / legal, runbook 1–3 và giờ cao điểm | Số thẻ và phần riêng theo thẻ, giả định môi trường; tổng hợp HAZOP sự cố; sửa operations / legal; risk register, checklist, runbook 4–5; submission.json và kiểm gói nộp Bình gom | Vận hành và pháp lý. A1 câu 1.2, A2 câu 1.4; B4 (tổng hợp và ngoài kỹ thuật), B5, B7.5, B7.6; `config/operating_gates.json` mục `operations`, `legal`; C3, C4 (tổng hợp và ngoài kỹ thuật), C5 câu 3.3, C7 phần vận hành / pháp lý, C10, C11; `submission/submission.json`, kiểm nội dung gói bài. |

### Phối hợp để cân khối lượng

Cân cả code, chạy lệnh, phân tích và viết phiếu. Người phụ trách nội dung được hỗ trợ bằng bản nháp và bằng chứng cụ thể. Đây là kế hoạch phân công, chưa xác nhận công việc đã hoàn thành.

| Phần việc | Người chuẩn bị | Người soát / tổng hợp |
|---|---|---|
| B3: dữ liệu và drift | Dũng lập bảng nguồn dữ liệu, thu thập bằng chứng | Đăng phân tích tác động và hoàn thiện kết luận |
| B4 / C4: HAZOP | Bình viết các dòng kỹ thuật từ trace; Long viết phần ngoài kỹ thuật và nhánh chưa thấy trên trace | Long tổng hợp, kiểm đủ yêu cầu từng vòng |
| C5 câu 3.2: specification | Dũng dự thảo quy tắc kiểm được bằng code / report | Đăng soát quy tắc và tác hại; Long viết giả định môi trường ở câu 3.3 |
| C6 / C9: fault tree | Bình cung cấp nhánh code / trace; Đăng nhánh kinh doanh; Long nhánh vận hành / pháp lý | Dũng tổng hợp cây, cả nhóm kiểm bằng chứng và vị trí gate |
| B5 / C10 / C11: checklist và rủi ro | Mỗi người cung cấp bằng chứng, trạng thái, PIC và rủi ro của phần mình | Long tổng hợp và hoàn thiện runbook |
| Gom bài | Bình chạy grade và check_submission --collect đúng thứ tự; Dũng kiểm đủ report / mã lần chạy | Long kiểm submission.json và gói nộp; Đăng soát quyết định và ba dòng bắt buộc |

Khi nhận thẻ, Bình cùng nhóm rà lại khối lượng theo nguyên nhân thực tế. Người đã xong đầu việc nhận thêm phần trích số, định dạng và tổng hợp bằng chứng nếu phần code hoặc vận hành phát sinh nhiều; giữ người chịu trách nhiệm nội dung theo ba vai.

### Việc cả nhóm cùng chốt

- A3: cùng thảo luận kết luận, Đăng tổng hợp. A4: thống nhất ngưỡng và hành động trước khi ký, commit và push tiêu chí, rồi mới chạy đánh giá.
- B6: cùng làm pre-mortem đủ bốn lăng kính, chọn 2–3 lý do thành cổng phòng ngừa.
- C6 và C9: cùng lập fault tree trước và sau sửa, có ít nhất hai nhánh ở hai tầng khác nhau và bằng chứng cho mỗi lá; Dũng tổng hợp, Bình cung cấp trace / vị trí gate, Đăng và Long cung cấp nhánh ngoài kỹ thuật.
- Phần riêng theo thẻ chỉ làm đúng mục tương ứng số đã bốc; nếu là S4, phần riêng nằm ở C1 và B7.6.
- Quyết định v1 và v2 do cả nhóm thống nhất theo tiêu chí đã ký và report thật; người tổng hợp không tự quyết thay nhóm.
- Sau demo, phối hợp trả code / config về bản v2, chạy lại grade và gom bài nếu có thay đổi; kiểm tra đủ thành phần trước khi push.
- Mỗi người tự hoàn thiện đóng góp, bằng chứng, exit ticket và khai báo dùng AI nếu có; mỗi người tự nộp link repo nhóm trên LMS.

### Ghi nhận hỗ trợ AI trong bước chuẩn bị

Nhóm đã dùng Codex để điền danh sách thành viên theo thông tin cung cấp và soạn phân công đề xuất. Các mục cá nhân bên dưới là khung để từng người hoàn thiện theo việc thực tế, chưa phải xác nhận đã làm xong.

## Cá nhân

Mỗi thành viên tự hoàn thiện mục của mình. Phần việc được điền theo phân công đề xuất; đóng góp, bằng chứng và exit ticket phải phản ánh công việc thực tế.

## TranTuanDang-2A202603618

### Phần việc phụ trách

Sản phẩm và kinh doanh. A1 câu 1.1, A3–A5; `config/acceptance_criteria.json`; `config/operating_gates.json` mục `business`; B3 (soát và chịu trách nhiệm), B7.4, B8; C1, C5 câu 3.2 (soát), C7 phần kinh doanh, C12; góp nhánh kinh doanh C6 / C9.

### Đóng góp cụ thể

Chờ thành viên tự ghi công việc thực tế đã hoàn thành.

### Bằng chứng

Chờ thành viên bổ sung mã commit, mã lần chạy và vị trí trong phiếu.

### Exit ticket

Chờ thành viên tự viết một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Thành viên tự ghi phần việc đã dùng AI và cách kiểm tra lại, nếu có.

## TaCongBinh-2A202603628

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng. `lab10/guards.py`; hỗ trợ A4–A5; B0–B2, B7.1; dòng kỹ thuật B4 / C4; C0, C2, C7 phần code; bằng chứng C6 / C9; chạy lệnh gom bài để Long kiểm nội dung.

### Đóng góp cụ thể

Chờ thành viên tự ghi công việc thực tế đã hoàn thành.

### Bằng chứng

Chờ thành viên bổ sung mã commit, mã lần chạy và vị trí trong phiếu.

### Exit ticket

Chờ thành viên tự viết một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Thành viên tự ghi phần việc đã dùng AI và cách kiểm tra lại, nếu có.

## NguyenTuanDung-2A202603608

### Phần việc phụ trách

Kỹ sư cổng. A2 câu 1.3; B3 (dự thảo), B7.2, B7.3; `lab10/monitors.py`; C2, C5 câu 3.2 (dự thảo để Đăng soát), C6 / C9 (tổng hợp), C8; trích số liệu C12 và kiểm đủ report khi gom bài.

### Đóng góp cụ thể

Chờ thành viên tự ghi công việc thực tế đã hoàn thành.

### Bằng chứng

Chờ thành viên bổ sung mã commit, mã lần chạy và vị trí trong phiếu.

### Exit ticket

Chờ thành viên tự viết một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Thành viên tự ghi phần việc đã dùng AI và cách kiểm tra lại, nếu có.

## HoangHaiLong-2A202603670

### Phần việc phụ trách

Vận hành và pháp lý. A1 câu 1.2, A2 câu 1.4; B4 (tổng hợp và ngoài kỹ thuật), B5, B7.5, B7.6; `config/operating_gates.json` mục `operations`, `legal`; C3, C4 (tổng hợp và ngoài kỹ thuật), C5 câu 3.3, C7 phần vận hành / pháp lý, C10, C11; `submission/submission.json`, kiểm nội dung gói bài.

### Đóng góp cụ thể

Chờ thành viên tự ghi công việc thực tế đã hoàn thành.

### Bằng chứng

Chờ thành viên bổ sung mã commit, mã lần chạy và vị trí trong phiếu.

### Exit ticket

Chờ thành viên tự viết một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Thành viên tự ghi phần việc đã dùng AI và cách kiểm tra lại, nếu có.
