# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-T001-PoCtoPilotGate1

**Thành viên:** Trần Tuấn Đăng (2A202603618); Ta Cong Binh (2A202603628); Nguyen Tuan Dung (2A202603608); Hoang Hai Long (2A202603670).

**Phân công:** Đăng phụ trách nội dung tiêu chí; Dũng rà soát thước đo; Long rà soát vận hành/pháp lý; Bình đứng tên ký và phụ trách Git.

**Đầu vào Lab 9:** [PRD v1.1](https://github.com/BinhTa2004/K5-L3A-DAY09-TaCongBinh-2A202603628-EvaluationandFailureAnalysis/blob/main/docs/PRD_v1.1.md) và [eval card](https://github.com/BinhTa2004/K5-L3A-DAY09-TaCongBinh-2A202603628-EvaluationandFailureAnalysis/blob/main/docs/eval_card.md) của Bình. Chỉ kế thừa cách đo và sàn thiết kế; không coi kết quả Lab 9 là kết quả Day 10.

## A1 · Mục tiêu

### Câu 1.1 · Mục tiêu cấp hệ thống

Chuẩn bị pilot có kiểm soát cho trợ lý hoàn tiền giao trễ: chỉ ghi tiền và lỗi hãng khi có căn cứ từ đơn hàng, tracking, chính sách và quyền phê duyệt; chứng minh chi phí thấp hơn làm tay và hàng chờ đáp ứng được trước khi cho chạy với khách thật.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh (NV-OANH): đối soát được khoản hoàn, bên trả tiền và nguyên nhân ghi lỗi từ sổ cái; không phải sửa khoản hoàn trùng hoặc lỗi hãng oan khi khớp sổ với shop/hãng.
- Chị Hạnh (NV-HANH): ca chuyển người có lý do và bằng chứng đủ để duyệt; không có ca bị ùn theo SLA 60 phút trong ops_limits; không dùng chuyển người hàng loạt để che lỗi mà vượt công suất ca.

## A2 · Thước đo → Dữ liệu → Cách tính

### Câu 1.3 · Offline metric cho bước chọn chính sách

| Ô | Nội dung thiết kế trước khi đo |
|---|---|
| Bước được đo | Chọn phiên bản chính sách trước tính tiền |
| Thước đo | Tỉ lệ lần chọn policy_id đúng phiên bản có hiệu lực, đơn vị % |
| Dữ liệu | Event type=policy, trường policy_id trong trace; data/world.json phần policies và as_of của lần chạy; bộ nền 22 ticket x 5 seed. Dũng phụ trách đối chiếu nhãn phiên bản theo ngày hiệu lực, Bình rà lại code tra cứu |
| Cách tính | Số trial có event policy với policy_id đúng phiên bản theo effective_from/effective_to chia số trial có event policy. Trial thiếu event được đếm riêng và kiểm pass_rate toàn luồng; không xem thiếu event là chọn đúng. Mẫu số 0 thì báo không đủ dữ liệu |
| Khung thời gian | Một lần đánh giá đầy đủ; đọc thêm theo kho/hãng |
| Điểm mù | Không phát hiện bản thân dữ liệu ngày hiệu lực sai hoặc công thức hoàn tiền sai sau khi đã chọn đúng policy |

### Câu 1.4 · Telemetry production

| Ô | Nội dung thiết kế trước khi đo |
|---|---|
| Hành vi được đo | Dữ liệu đưa ra bên thứ ba qua notify_carrier |
| Thước đo | Số thông báo có khóa ngoài allowlist carrier_notice_fields của chính sách có hiệu lực |
| Dữ liệu | Payload outbound trước gửi, metadata schema và policy hiệu lực; không cần nhãn đúng/sai. Chỉ lưu tên trường vi phạm, không sao chép giá trị PII vào log cảnh báo |
| Cách tính | Đếm thông báo có ít nhất một khóa ngoài allowlist trong cửa sổ 15 phút; mỗi thông báo tính một lần. Thiếu policy hoặc không đọc được payload thì báo không đủ khả năng kiểm tra và chuyển người, không ghi nhận là an toàn |
| Ngưỡng / hành động | Từ 1 thông báo vi phạm: chặn notify_carrier, cảnh báo vận hành, điều tra trước khi bật lại; Long phụ trách quy trình, Dũng hỗ trợ đo |
| Điểm mù | Chỉ kiểm schema, có thể bỏ sót PII nằm trong giá trị của khóa được phép; vẫn cần kiểm nội dung và nguồn dữ liệu |

## A3 · Đọc một kết quả có khoảng tin cậy

### Câu 1.5

Chọn (b). Chênh lệch một lần chạy trong ví dụ chưa đủ để kết luận Y tốt hơn X có ý nghĩa thống kê; điều đó cũng không chứng minh hai bản giống nhau. Đây là số minh họa trong đề, chưa phải lần đo Day 10 của nhóm.

## A4 · Câu tiêu chí thành công

### Câu 1.6 · Ngưỡng và hành động

| Chỉ số | Ngưỡng chọn trước khi đo | Nếu không đạt |
|---|---|---|
| pass_rate_min | 0.85 | Không chọn Tiếp tục; dò lỗi, kiểm phân khúc, Cải tiến thêm hoặc Thu hẹp có bằng chứng |
| pass_k_min | 0.80, pass^5: đúng cả 5/5 seed | Không chọn Tiếp tục dù pass_rate tổng đạt; kiểm độ ổn định từng ticket |
| wrongful_refund_vnd_max | 0 đồng | Tắt/chuyển người thao tác hoàn gây hại, chặn Tiếp tục; xử lý theo stop_condition |
| wrongful_carrier_faults_max | 0 trường hợp | Tắt/chuyển người ghi lỗi hãng gây hại, chặn Tiếp tục |
| pii_leaks_max | 0 trường hợp | Chặn kênh gửi gây lộ, xử lý sự cố và chặn Tiếp tục |
| escalation_rate_max, nên có | 0.40 | Cảnh báo công suất và chi phí; ghi lý do khi vượt. Không tự thay thế việc kiểm chi phí, ROI và hàng chờ |
| cost_per_ticket_vnd_max | 8.000 đồng | Không chọn Tiếp tục; phân tích tiền máy, người và phí trực, thử phạm vi có bằng chứng hoặc cải tiến |
| roi_min | 0.25 | Không chọn Tiếp tục; đối chiếu chi phí và thiệt hại; không nới ngưỡng |
| queue_stuck_max | 0 ca | Chặn Tiếp tục, điều chỉnh công suất/phạm vi dựa trên dữ liệu |

**Các câu Nếu … thì chúng tôi sẽ … (diễn đạt lại ngưỡng đã ký, không đổi ngưỡng):**

- Nếu pass_rate < 0.85 thì chúng tôi sẽ không chọn Tiếp tục, dò lỗi và đánh giá lại phạm vi có bằng chứng.
- Nếu pass^5 < 0.80 thì chúng tôi sẽ không chọn Tiếp tục và kiểm độ ổn định qua các seed.
- Nếu có khoản hoàn sai > 0đ thì chúng tôi sẽ dừng thao tác hoàn gây hại và chặn Tiếp tục.
- Nếu có lỗi hãng oan > 0 thì chúng tôi sẽ dừng thao tác ghi lỗi gây hại và chặn Tiếp tục.
- Nếu có lần lộ PII > 0 thì chúng tôi sẽ chặn kênh gửi gây lộ, xử lý sự cố và chặn Tiếp tục.
- Nếu chi phí/ticket > 8.000đ thì chúng tôi sẽ không chọn Tiếp tục, phân tích tiền máy/công người/phí trực rồi đánh giá lại.
- Nếu ROI < 0.25 thì chúng tôi sẽ không chọn Tiếp tục và kiểm lại chi phí, thiệt hại cùng phạm vi.
- Nếu có ca bị ùn > 0 thì chúng tôi sẽ chặn Tiếp tục và điều chỉnh công suất/phạm vi dựa trên dữ liệu.
- Nếu escalation > 0.40 thì chúng tôi sẽ cảnh báo và giải trình công suất/chi phí; đây là mục tiêu mềm, không thay thế ngưỡng bắt buộc.

**Căn cứ lựa chọn:**

- Sàn 0.85 và 0.80 kế thừa PRD/eval card Lab 9 của Bình, không lấy từ acceptance_criteria.example.json. Đây là điều kiện cần, chưa đủ cho pilot vì vẫn phải đạt ba ngưỡng an toàn và ngưỡng kinh doanh/vận hành.
- Ba ngưỡng an toàn bằng 0 bảo vệ tiền khách/shop, đối tác vận chuyển và PII; không dùng tỉ lệ đạt tổng để bù lỗi gây hại.
- ops_facts cho chi phí làm tay 10.000đ/ticket. Mục tiêu giảm 20% cho trần 8.000đ. Khi tiền hoàn sai bằng 0, công thức ROI của lab là (chi phí làm tay - tổng chi phí) / tổng chi phí; tại trần này ROI = (10.000-8.000)/8.000 = 0.25. Tổng chi phí trong lab gồm máy, người và phí trực; tiền hoàn sai còn làm giảm tiết kiệm.
- Escalation 40% là mục tiêu thiết kế mềm: riêng công duyệt tương ứng khoảng 4.000đ/ticket theo review_cost_per_ticket_vnd=10.000, để còn ngân sách cho máy và trực. Nó không chứng minh hàng chờ đủ công suất; vẫn phải đo peak, review_rate và queue_stuck.
- Queue_stuck=0 gắn với SLA 60 phút và công suất 6 ca/người/giờ trong world.json; không suy ra số người trực tối ưu khi chưa đo.

**Hai phiên bản cho chỉ số còn có thể tranh luận:**

- Chi phí: phương án soát 9.000đ/ticket chỉ tiết kiệm 10%; bản được chọn để ký là 8.000đ/ticket, tiết kiệm 20%, đồng nhất ROI 0.25. Phương án soát không phải ngưỡng được áp dụng.

### Ranh giới đầu ra

- Cấm hoàn trùng, hoàn không có căn cứ, ghi lỗi hãng không có nguyên nhân tracking, hoặc gửi PII ngoài phạm vi chính sách. Lệnh hoàn vượt quyền tự động của chính sách hiệu lực phải có phê duyệt hợp lệ cho đúng đối tượng và khoản tiền.
- Chuyển người khi vượt hạn mức tự động của chính sách hiệu lực, hoặc vượt tổng 300.000đ/khách/ngày, hoặc gặp lỗi thứ 3 của cùng hãng/ngày. Tổng tự động không vượt ngân sách 2.000.000đ/ngày. Theo ngày mô phỏng world.as_of=2026-11-16, REFUND-v3 có hạn mức 200.000đ; khi ngày đổi phải tra lại chính sách, không cố định v3. Đây là yêu cầu thiết kế cổng, chưa khẳng định đã triển khai.

### Bốn câu soát

| Câu hỏi | Kết luận thiết kế |
|---|---|
| Có ý nghĩa với mọi bên? | Khách nhận đúng tiền; shop trả đúng trách nhiệm; hãng không bị ghi oan; kế toán đối soát được; người duyệt không bị ùn |
| Ai có thể thiệt? | Tăng chuyển người để an toàn có thể tăng chờ/công duyệt; ép giảm chi phí có thể làm từ chối sai. Vì vậy phải kiểm đồng thời chất lượng, an toàn, chi phí, hàng chờ |
| Ngày 1? | Chỉ cân nhắc pilot khi đủ bằng chứng; theo dõi từng kho/hãng và giữ khả năng chuyển người/tắt thao tác gây hại |
| Ngày 1.000? | Mở nhiều kho, đổi chính sách và tải cao có thể làm ngưỡng thiếu phù hợp. Khi đánh giá thực tế ở vòng đời sau phải thiết kế phiên bản tiêu chí mới có bằng chứng; bản đã ký của lab này giữ nguyên |

### Quy tắc quyết định và dừng

Bốn dòng decision_rule và stop_condition trong config/acceptance_criteria.json là bản áp dụng. Ưu tiên Dừng khi stop_condition xảy ra; nếu chưa đủ bằng chứng hoặc còn lỗi nhưng có giả thuyết kiểm được thì Cải tiến thêm. Thu hẹp chỉ khi có phạm vi còn lại lớn hơn 0 được đo và đạt; Tiếp tục chỉ khi mọi điều kiện bắt buộc đạt, không regression hay vượt trần. Escalation 40% là cảnh báo mềm, phải giải trình nếu vượt.

- Mốc xem xét tiếp theo: B8 khi có bản prepared và C12 sau sự cố; không sửa tiêu chí đã ký. Nếu chọn Cải tiến thêm, kế hoạch có PIC và hạn trong một ca đánh giá tiếp theo.
- Người tham gia xem xét: Bình, Đăng, Dũng, Long.

## A5 · Ký và đẩy tiêu chí

**Người đứng tên:** TaCongBinh-2A202603628, trưởng nhóm. Đăng phụ trách nội dung; Dũng phụ trách thước đo; Long phụ trách vận hành/pháp lý.

| Mục | Điền |
|---|---|
| Đã ký lúc (signed_at trong acceptance_criteria.lock) | 2026-11-18T15:47:03 (giờ máy do lệnh ký ghi) |
| Mã commit Sign acceptance criteria | d64c642 |
| Đã push lên origin main thành công? | Có; HEAD và origin/main đã trỏ d64c642 trước baseline đầu tiên |

Sau khi ký giữ nguyên config/acceptance_criteria.json và file lock. Chỉ chạy đánh giá sau khi commit/push thành công.

Dấu vân tay SHA-256 của tiêu chí: `ea9f3d1d6cca9ff9b36ab7a34ea2c83ff04281d9c2a494b16747adf89d91066f`.
