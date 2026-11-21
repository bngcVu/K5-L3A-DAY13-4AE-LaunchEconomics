# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994 / 1.200); phạm vi `noi_dia` + `hang_nang`: **92,26%** (906 / 982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` (41) hoặc `bo` (7), chia số yêu cầu được xem lại (`duoc_xem_lai == 1`: 177) | **27,12%** (48 / 177); phạm vi `noi_dia` + `hang_nang`: **21,09%** (27 / 128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51 / 1.200); phạm vi `noi_dia` + `hang_nang`: **3,97%** (39 / 982) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ mở/sử dụng trợ lý theo nhóm thí nghiệm | Số yêu cầu thuộc phạm vi có event `agent_suggestion_shown` chia tổng số yêu cầu thuộc phạm vi, tách theo `arm` (`treatment` / `control`) và `staff_id` | Không cần tính (đo trong pilot; kiểm soát ảnh hưởng gián tiếp nhóm `control` = 0%) |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (và số ca hoàn trùng) | Số đơn có `so_tien_da_hoan != so_tien_dung` chia 100 đơn mẫu kiểm tra/tuần (bắt lỗi ngầm ca 5, 17); kết hợp đếm mã đơn có > 1 `refund_ledger_write` với `ket_qua = ok` (bắt ca 20, ngưỡng 0 ca) | Không cần tính (đo hằng tuần / đối soát sổ cái mỗi giờ trong pilot) |

Cách tính: đọc `src/logix_requests.csv` với `keep_default_na=False` (không dùng cột `_simulated`, nên cả ba chỉ số trên là số đo trực tiếp từ mẫu đợt chạy thử). Kết luận đúng: **chỉ số chính trong đợt chạy thử là 82,83% (994/1.200), tỉ lệ bỏ qua gợi ý là 27,12% (48/177), tỉ lệ mở lại trong 7 ngày là 4,25% (51/1.200)** — không viết "trợ lý đã nâng chỉ số từ 70%" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười một event (vượt mức tối thiểu sáu), mọi event đều có `trace_id` để nối với trace của agent và khớp với `bang_loi.md`, `pilot_plan.yaml`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / Hệ thống ticket | `request_id`, `loai`, `depot`, `staff_id`, `arm`, `so_tien`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Cổng tiếp nhận yêu cầu | `request_id`, `reason` (vd: `ma_khong_hop_le`), `trace_id` | Khi đầu vào của khách sai định dạng (ca 9) |
| `agent_run_completed` | Trợ lý (agent) | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` (`ok`/`loi`), `phien_ban_bang_gia`, `trace_id` | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `arm`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu sai |
| `handoff_to_staff` | Trợ lý (agent) | `request_id`, `loai`, `reason` (`thieu_du_lieu`, `vuot_gioi_han_chay`, `rollback`), `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang hàng đợi nhân viên (ca 4, rollback) |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `ma_don`, `so_tien`, `ket_qua` (`ok`/`loi`), `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái (ca 7, ca 20) |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | App khách / Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu đã đóng (ca 18) |
| `audit_sample_checked` | Hệ thống / Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `phien_ban_bang_gia`, `trace_id` | Khi kế toán kiểm tra mẫu 100 đơn hằng tuần (ca 5, ca 17) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, nối các event theo `trace_id` (và `request_id`):

- **Chỉ số chính (% đóng trong 24 giờ và không mở lại trong 7 ngày):** ghép `refund_request_created.created_at` với `ticket_closed.closed_at` (≤ 24 giờ) và kiểm tra không có `ticket_reopened` trong 7 ngày sau `closed_at`, tách theo `arm`. → **Đo được.**
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** đếm `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số `staff_review_decision`. → **Đo được.**
- **Chỉ số an toàn — Tỉ lệ lỗi lọt đến khách:** đếm yêu cầu có `ticket_reopened` trong 7 ngày sau `ticket_closed.closed_at`, chia tổng `refund_request_created`, tách theo `arm`. → **Đo được.**
- **Chỉ số dùng tự đề xuất — Tỉ lệ mở/sử dụng trợ lý theo nhóm:** đếm yêu cầu từ `refund_request_created` (trong phạm vi) có `agent_suggestion_shown`, tách theo `arm` và `staff_id` (giám sát nhóm `control` = 0%). → **Đo được.**
- **Chỉ số an toàn tự đề xuất — Tỉ lệ đơn hoàn sai tiền và số ca hoàn trùng:** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung`, đối chiếu `phien_ban_bang_gia` với `agent_run_completed`) và đối soát `refund_ledger_write` theo `ma_don`, `ket_qua = ok` (> 1 lần là hoàn trùng). → **Đo được.**
- **Bổ sung cho luật dừng chi phí (thay cột `simulated`):** `agent_run_completed` (token, tool mọi lần chạy) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai` (đo thật) cho phép tính chi phí mỗi việc thành công thật ngay sau tuần 1. → **Đo được** khi bật đủ event trước ngày bắt đầu pilot.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ mỗi việc thành công (B1) [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu (B4) [simulated] | % yêu cầu được xem lại còn > 50% khi kết thúc bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa (A4) [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
