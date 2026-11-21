# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: **4AE**
- Lớp: **L3A**
- Repo nhóm: [K5-L3A-DAY13-4AE-LaunchEconomics](https://github.com/bngcVu/K5-L3A-DAY13-4AE-LaunchEconomics) (nhánh `main`)
- Thành viên: xem `TEAM.md` (Bùi Ngọc Vũ, Tô Minh Thành, Ngô Gia Bảo, Nguyễn Mạnh Quyền)

## 2. Mục tiêu và cách tiếp cận

Dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí **LogiX-VN** để trình hội đồng **Gate 2a** duyệt kế hoạch pilot (dựa trên dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy trong `src/logix_requests.csv`, `src/logix_runs.csv`). Bộ hồ sơ trả lời bốn câu hỏi cốt lõi: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định.

Nhóm làm việc theo mô hình **tiếp sức** bám sát năm checkpoint trong `CHECKPOINTS.md` và `PHAN_CONG.md`, tách rõ quyền sở hữu từng file và từng khối `TODO` trong `src/lab13.py` để tránh xung đột: Vũ (CP1 · A) → Thành (kiểm số tay + CP2 · B + E2) → Bảo (CP3 · C + CP4 · D) → Quyền (CP3 gắn nhãn độc lập + CP5 · E1, hồ sơ v0, duyệt chéo, tổng hợp và nộp bài). Đổi người viết code sau giờ giải lao (Vũ trước, Bảo sau) và có hai người độc lập tự tính chi phí (Vũ lập `mo_hinh`, Thành tính tay đối chiếu từ CSV).

## 3. Giải pháp

- **Nhiệm vụ A — Mô hình chi phí (`src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md)):** đạt cả ba phép thử A1 (1,20 · 1,25 · 1,25); lập hàm `mo_hinh` với tử số tính mọi lần chạy kể cả lỗi và mẫu số chỉ đếm 978 việc `thanh_cong`; tách chi phí theo bốn loại yêu cầu (A3) và cộng chi phí cố định 40 triệu đ/tháng cho phạm vi thu hẹp `noi_dia` + `hang_nang` (A4).
- **Nhiệm vụ B — Độ nhạy và kiểm số (`src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md)):** Thành tính tay kiểm chứng 4.472 đ từ CSV khớp 0% sai lệch; chạy 9 kịch bản đơn biến (B1), kịch bản cặp (B2), chi phí cả hệ thống theo giới hạn 1–3 lần chạy (B3) và kịch bản xem lại 100% kèm độ nhạy phút làm lại thực tế 15,3 phút/ca (B4).
- **Nhiệm vụ C — Bảng lỗi và khắc phục ([bang_loi.md](bang_loi.md)):** phân loại 20 ca lỗi theo 5 loại Google PAIR dựa trên nguyên nhân gốc; soạn 5 quy tắc phân biệt các ca dễ lẫn và bảng khắc phục 5 ca (9, 20, 18, 4, 17) đủ 5 loại, có cách phát hiện đo được và vai trò phụ trách. *(Đang chờ Quyền bổ sung cột nhãn độc lập để chốt tỉ lệ đồng thuận.)*
- **Nhiệm vụ D — Kế hoạch pilot (`src/lab13.py`, [pilot_plan.yaml](pilot_plan.yaml)):** tính đủ 5 câu cỡ mẫu D1 trước khi chọn cách chia; kiểm tra 5 câu tách tác động D2; tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật dừng an toàn; hoàn thiện `pilot_plan.yaml` hợp lệ với `yaml.safe_load`, không còn dấu `?`, đủ 3 luật dừng theo mẫu NẾU–TRONG–THÌ–KHÔNG THÌ.
- **Nhiệm vụ E — Chỉ số, rủi ro và hồ sơ launch v0 ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất thêm 2 chỉ số (dùng và an toàn), đặc tả 11 event có `trace_id` và kiểm tra chéo; tổng hợp 3 rủi ro kinh tế (E2); ghép thành hồ sơ 1 trang 7 mục kèm đề xuất cuối và điều kiện kiểm tra.

## 4. Kết quả

- **Kinh tế (A, B):** chi phí mỗi việc thành công toàn mẫu **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token+tool/yêu cầu (274,7 đ, đo từ trace); giờ nhân viên chiếm **92,5%** (làm lại 51,8%, xem lại 40,7%) [simulated]. So công bằng cả hệ thống (cộng 222 ca không thành công × 12.000 đ): **5.865 đ/yc = 0,49×** [simulated]. Trong phạm vi thu hẹp `noi_dia` + `hang_nang` (982/1.200 = 81,8% khối lượng): **3.414 đ** chưa cố định, **4.599 đ (0,38×)** ở 45.000 yc/tháng và **5.784 đ (0,48×)** ở một nửa khối lượng [simulated]. Loại `quoc_te` (22.515 đ = 1,88×, thành công 27,3%) và `doi_tac` (10.215 đ = 0,85×) [simulated].
- **Độ nhạy (B):** ba yếu tố mạnh nhất là số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%) và lương nhân viên (+23,1%); giới hạn **2 lần chạy** rẻ nhất toàn hệ thống (6.901.220 đ) [simulated]. Điểm bất lợi B4: xem lại 100% tốn **11.743 đ (0,98×)** (9 phút làm lại) hoặc **12.415 đ (1,03×)** (15,3 phút thực tế) [simulated].
- **Chỉ số và pilot (D, E):** trong đợt chạy thử (không đối chứng), chỉ số chính là **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200; phạm vi 3,97%). Thiết kế pilot chia ngẫu nhiên **20 + 20 nhân viên**, chấp nhận **MDE 6 điểm** (n = 859, m ≥ 299 yc/người, DE = 6,96; power 0,64 nếu tác động thật chỉ 5 điểm), ngày quyết định `2027-01-12`.
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang` với 5 điều kiện bắt buộc (vá ca 7 và ca 20, ký chấp nhận MDE 6 điểm, bật 11 event thay số `simulated` sau tuần 1, lộ trình giảm xem lại theo bậc, bật kiểm tra mẫu 100 đơn/tuần).
- **Kết quả duyệt chéo Gate 2a ([phieu_cham.md](phieu_cham.md)):** *(cập nhật sau phiên duyệt chéo lúc 17:00 với nhóm hội đồng và nhóm được chấm).*

## 5. Khó khăn và cách xử lý

- **Lỗi phạm vi phép tính so sánh 12.000 đ ở CP1:** lần chạy đầu chỉ cộng 12.000 đ cho 148 ca `chuyen_nhan_vien` ra 5.125 đ; nhóm đối chiếu slide/hướng dẫn và sửa thành cộng đủ 222 yêu cầu không thành công ra **5.865 đ (0,49×)** [simulated].
- **Giới hạn cỡ mẫu với 40 nhân viên ở CP4:** trần cỡ mẫu hiệu dụng `20 / 0,02 = 1.000 < 1.251` nên không cách chia cụm nào đủ mẫu cho mức chênh 5 điểm. Nhóm chọn chia theo nhân viên 20 + 20 để đảm bảo tách tác động (20 cụm/nhóm), chấp nhận MDE 6 điểm và ghi rõ rủi ro power 0,64 vào hồ sơ để Giám đốc vận hành ký duyệt.
- **Môi trường Python và encoding Windows:** khi chạy `src/lab13.py` trên Windows cần đặt `PYTHONUTF8=1` để in tiếng Việt không lỗi font, và cần kích hoạt đúng môi trường ảo đã cài `requirements.txt` (có `statsmodels` và `pyyaml`) để chạy trọn vẹn phần tính power ở `chay_nhiem_vu_d`.

## 6. Tổng hợp đóng góp

Chi tiết phần việc, đóng góp và bằng chứng (commit, file, kiểm tra) của từng thành viên nằm trong `TEAM.md` và các báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- **Phụ thuộc dữ liệu giả lập:** 92,5% tổng chi phí đến từ hai cột `phut_xem_lai_simulated` và `phut_lam_lai_simulated`. Cần bật đủ event `staff_review_decision`, `staff_rework_completed` và tính lại toàn bộ bảng chi phí sau tuần đầu pilot.
- **Giả định thiết kế chưa kiểm chứng trên dữ liệu thật:** `baseline = 0,70` và `ICC = 0,02` là giả định của đề; nếu ICC thực tế cao hơn 0,02 thì cần kéo dài bước 0,50 để đủ cỡ mẫu hiệu dụng.
- **Rủi ro ảnh hưởng gián tiếp trong cùng depot:** chia theo nhân viên giúp đủ 20 cụm/nhóm nhưng nhân viên cùng depot vẫn có thể trao đổi; cần giám sát chặt `agent_suggestion_shown` ở nhóm đối chứng (mục tiêu 0%).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`).
- Đề bài và hướng dẫn Lab 13 LogiX-VN (`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
