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

| Ca | Nhãn người 1 (Bảo) | Nhãn người 2 (Quyền) | Trùng? | Nhãn thống nhất | Lý do |
| --: | --- | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng | Đầu vào sai (thiếu hai chữ số), lỗi xuất phát từ khách. |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống | Gọi sai tham số tool so với thiết kế, lỗi đã lộ (hoàn thiếu, khách mở lại). |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Đúng thiết kế (ví LogiX), chỉ giả định không khớp kỳ vọng nhận tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Thiếu dữ liệu chặng nước ngoài; trợ lý nói rõ và chuyển nhân viên. |
| 5 | Ngầm | Ngầm | Có | Ngầm | Thừa tiền hệ thống, chỉ phát hiện nhờ kiểm tra mẫu. |
| 6 | Do người dùng | Hệ thống | **Không** | Do người dùng | Trợ lý không nhận ra nội dung mô tả (hàng vỡ) mâu thuẫn với mục đã chọn, xử lý sai luồng. Cách gắn khác: ND, vì khách chọn nhầm mục. |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống | Lỗi ghi sổ cái nhưng vẫn báo thành công, trái thiết kế và đã lộ ra. |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống | Dẫn điều khoản không tồn tại; số tiền đúng nên không phải Ngầm. |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng | Khách nhập sai loại mã. Việc không gợi ý chỉ là chỗ cải thiện. |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Từ chối đúng chính sách; giả định "cam kết 24 giờ" không khớp hoàn cảnh bão. |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Không xử lý được âm thanh, ngoài khả năng kỹ thuật. |
| 12 | Ngầm | Ngầm | Có | Ngầm | Sai chi phí (token gấp 3) kéo dài 3 tuần mà không ai thấy. |
| 13 | Giới hạn hệ thống | Hệ thống | **Không** | Giới hạn hệ thống | Ngoài phạm vi là đúng, nhưng trả lời chung chung thay vì nói rõ không xử lý được, nên lỗi nằm ở cách xử lý. |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng | Thao tác nhầm của khách. |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống | Tính 100% thay vì 50%, trái chính sách; lỗi lộ ra nhờ nhân viên xem lại. |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Đúng thiết kế "gửi ngay", chỉ giả định không tính đến giờ khách nghỉ. |
| 17 | Ngầm | Ngầm | Có | Ngầm | Dùng bảng giá cũ, lệch nhỏ, không ai mở lại trong 9 ngày. |
| 18 | Ngữ cảnh | Hệ thống | **Không** | Ngữ cảnh | Tin nhắn thiếu cách tính khiến khách hiểu sai, là khiếm khuyết thiết kế đầu ra. Cách gắn khác: NC, vì tính toán đúng chính sách. |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Dữ liệu chỉ 12 tháng; trợ lý nói rõ và chuyển kèm tóm tắt. |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống | Khách gửi lại là hành vi bình thường; gốc là lệnh hoàn thiếu khoá chống trùng. |

**Tỉ lệ đồng thuận:** 17 / 20 = 85% (≥ 80%, không cần viết lại định nghĩa). Ba ca không trùng: ca 6, ca 13, ca 18.

> Nhãn thống nhất sau khi so: 4 Do người dùng (1, 6, 9, 14), 5 Hệ thống (2, 7, 8, 15, 20), 4 Ngữ cảnh (3, 10, 16, 18), 4 Giới hạn hệ thống (4, 11, 13, 19), 3 Ngầm (5, 12, 17).
>
> Bộ nhãn người 2 (Quyền) gắn độc lập trong file nháp riêng (3 Do người dùng, 8 Hệ thống, 3 Ngữ cảnh, 3 Giới hạn hệ thống, 3 Ngầm), không trao đổi với người 1, chép nguyên văn vào cột trên và không sửa sau khi so.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 — Do người dùng, không phải Hệ thống (không trùng, Bảo: Do người dùng · Quyền: Hệ thống):** Quyền gắn Hệ thống vì trợ lý không nhận ra mô tả "hàng vỡ" mâu thuẫn với mục đã chọn; thống nhất là Do người dùng vì nguyên nhân gốc là khách chọn nhầm mục (tương tự ca 9 khách nhập sai loại mã), còn việc kiểm tra chéo mô tả hay gợi ý nằm ở cột khắc phục.
- **Ca 13 — Giới hạn hệ thống, không phải Hệ thống (không trùng, Bảo: Giới hạn · Quyền: Hệ thống):** Quyền gắn Hệ thống vì trợ lý trả lời chung chung thay vì nói rõ không xử lý được như ca 4, 11, 19; thống nhất là Giới hạn hệ thống vì nguyên nhân gốc là yêu cầu ngoài phạm vi (sản phẩm của đối tác bảo hiểm), còn cách phản hồi kém là chỗ cần sửa.
- **Ca 18 — Ngữ cảnh, không phải Hệ thống (không trùng, Bảo: Ngữ cảnh · Quyền: Hệ thống):** Quyền gắn Hệ thống vì tin nhắn thiếu cách tính khiến khách hiểu sai; thống nhất là Ngữ cảnh vì số tiền hoàn 15.000 đ đúng thiết kế và chính sách, chỉ giả định "khách tự hiểu cách tính" không khớp hoàn cảnh.
- **Ca 8, 15 — Hệ thống, không phải Ngầm:** sai đã lộ ra (ca 8 trích dẫn điều khoản không tồn tại, trái thiết kế và nhìn thấy được, số tiền đúng nên không phải Ngầm; ca 15 nhân viên bắt được khi xem lại). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu.
- **Ca 20 — Hệ thống, không phải Do người dùng:** khách gửi lại là hành vi bình thường; nguyên nhân gốc là lệnh hoàn thiếu khoá chống trùng (`idempotency_key`) nên hoàn hai lần.
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
