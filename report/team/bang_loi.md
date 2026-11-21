# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

| Loại | Câu hỏi để nhận ra |
| --- | --- |
| Do người dùng | Đầu vào hoặc thao tác của khách có sai không? |
| Hệ thống | Trợ lý làm sai so với thiết kế hoặc chính sách, và lỗi đã lộ ra (khách hoặc nhân viên thấy)? |
| Ngữ cảnh | Kết quả đúng thiết kế và chính sách, chỉ giả định không khớp hoàn cảnh của khách? |
| Giới hạn hệ thống | Trợ lý có làm được không, dù cố gắng (thiếu dữ liệu, ngoài phạm vi, dạng đầu vào không xử lý được)? |
| Ngầm | Có sai (về tiền hoặc chi phí) nhưng không ai nhận ra cho tới khi kiểm tra mẫu? |

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Ngô Gia Bảo · Người gắn nhãn 2: Nguyễn Mạnh Quyền (gắn trong 8 phút, ngồi tách nhau, không trao đổi). Hai cột nhãn chép **nguyên văn** từ file nháp của từng người và không sửa sau khi đã so.

| Ca | Nhãn người 1 (Bảo) | Nhãn người 2 (Quyền) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | (tự gắn) | | Do người dùng |
| 2 | Hệ thống | (tự gắn) | | Hệ thống |
| 3 | Ngữ cảnh | (tự gắn) | | Ngữ cảnh |
| 4 | Giới hạn hệ thống | (tự gắn) | | Giới hạn hệ thống |
| 5 | Ngầm | (tự gắn) | | Ngầm |
| 6 | Do người dùng | (tự gắn) | | Do người dùng |
| 7 | Hệ thống | (tự gắn) | | Hệ thống |
| 8 | Hệ thống | (tự gắn) | | Hệ thống |
| 9 | Do người dùng | (tự gắn) | | Do người dùng |
| 10 | Ngữ cảnh | (tự gắn) | | Ngữ cảnh |
| 11 | Giới hạn hệ thống | (tự gắn) | | Giới hạn hệ thống |
| 12 | Ngầm | (tự gắn) | | Ngầm |
| 13 | Giới hạn hệ thống | (tự gắn) | | Giới hạn hệ thống |
| 14 | Do người dùng | (tự gắn) | | Do người dùng |
| 15 | Hệ thống | (tự gắn) | | Hệ thống |
| 16 | Ngữ cảnh | (tự gắn) | | Ngữ cảnh |
| 17 | Ngầm | (tự gắn) | | Ngầm |
| 18 | Ngữ cảnh | (tự gắn) | | Ngữ cảnh |
| 19 | Giới hạn hệ thống | (tự gắn) | | Giới hạn hệ thống |
| 20 | Hệ thống | (tự gắn) | | Hệ thống |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

> Cột "Nhãn thống nhất" là đáp án chuẩn (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn, 3 Ngầm). Hai cột nhãn cá nhân và cột "Trùng?" phải do Bảo và Quyền tự gắn độc lập rồi điền; tỉ lệ đồng thuận tính sau khi so.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6, 9 — Do người dùng, không phải Hệ thống:** gốc lỗi là khách chọn sai mục (ca 6) hoặc nhập sai loại mã (ca 9). Việc trợ lý không gợi ý thêm nằm ở cột khắc phục, không đổi nguyên nhân gốc.
- **Ca 8, 15 — Hệ thống, không phải Ngầm:** sai đã lộ ra (ca 8 trích dẫn điều khoản không tồn tại, nhìn thấy được; ca 15 nhân viên bắt được khi xem lại). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu.
- **Ca 13 — Giới hạn, không phải Hệ thống:** yêu cầu ngoài phạm vi (sản phẩm của đối tác bảo hiểm) là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời chung chung).
- **Ca 18 — Ngữ cảnh, không phải Hệ thống:** số tiền hoàn 15.000 đ đúng chính sách; chỉ giả định "khách tự hiểu cách tính" là không khớp, nên khách tưởng bị hoàn thiếu.
- **Ca 12 — Ngầm:** kết quả vẫn đúng nhưng chi phí token gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" ở đây là sai về chi phí, không chỉ về câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (reason = ma_khong_hop_le, kèm trace_id); cảnh báo khi > 2% số yêu cầu trong ngày, xem báo cáo hằng ngày | Nhận diện định dạng mã đơn sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hiển thị ảnh mẫu chỉ chỗ lấy mã vận đơn, không dừng im lặng | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: đếm `refund_ledger_write` có cùng mã đơn và ket_qua = ok > 1 lần; ngưỡng 0 ca (1 ca là kích luật dừng an toàn trong `pilot_plan.yaml`) | Bắt buộc idempotency_key = mã đơn + loại hoàn ở mọi lệnh ghi sổ; yêu cầu gửi lại trong lúc đang xử lý thì gộp vào yêu cầu cũ và báo "đang xử lý" | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với reason = so_tien mà kiểm tra lại thấy số tiền đúng, theo tuần; ngưỡng > 1% số yêu cầu đã đóng | Mẫu tin nhắn luôn ghi cách tính và căn cứ: "Phí giao 30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loai mỗi tuần; quoc_te chiếm phần lớn (thành công 27,3%, lần chạy 2 chỉ đúng 11,4% [đo từ trace]) | Giữ cách chuyển nhân viên kèm tóm tắt ngay ở lần chạy đầu, không chạy lại; đưa quoc_te ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra mẫu 100 đơn/tuần, so số tiền hoàn với bảng giá hiện hành; ngưỡng > 1% đơn lệch; kèm cảnh báo khi phiên bản bảng giá trong trace khác bản hiện hành | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào mỗi trace; truy hồi 212 đơn lệch | Kế toán trưởng |
