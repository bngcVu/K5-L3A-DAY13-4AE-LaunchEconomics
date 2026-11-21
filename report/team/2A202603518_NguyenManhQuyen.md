# Báo cáo cá nhân — Nguyễn Mạnh Quyền - 2A202603518

## 1. Thông tin thành viên

- Họ tên: Nguyễn Mạnh Quyền
- MSSV: 2A202603518
- Email: 26ai.quyennm3@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (CP5 · Nhiệm vụ E, duyệt chéo Gate 2a, tổng hợp và nộp bài)

## 2. Phần việc phụ trách

- CP5 · Nhiệm vụ E:
  - `report/team/chi_so.md`: mục E1 (tính thử 3 chỉ số, đề xuất thêm 2 chỉ số), danh sách event có `trace_id` và kiểm tra chéo (giữ nguyên mục E2 của Tô Minh Thành).
  - `report/team/ho_so_launch_v0.md`: tổng hợp hồ sơ launch v0 một trang, đủ 7 mục và đề xuất cuối cùng cho hội đồng Gate 2a.
- Tổng hợp, duyệt chéo và nộp bài:
  - `report/team/phieu_cham.md`: phiếu chấm hội đồng Gate 2a cho nhóm n + 1.
  - `report/team/group_report.md`: báo cáo nhóm ngắn.
  - `TEAM.md`: thông tin nhóm, vai trò, đóng góp và bằng chứng của các thành viên.
  - Rà soát checklist nộp bài (`SUBMISSION.md`) và kiểm tra tính nhất quán số liệu giữa tất cả file hồ sơ.
- CP3 · Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2) vào `report/team/bang_loi.md` để so đồng thuận với Ngô Gia Bảo.

## 3. Đóng góp cụ thể

- **E1 — Đặc tả chỉ số và danh sách event (`report/team/chi_so.md`):**
  - Tính trực tiếp bằng Python trên `src/logix_requests.csv` (`keep_default_na=False`, không dùng cột `_simulated`): chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200; phạm vi `noi_dia` + `hang_nang`: 92,26% = 906/982); tỉ lệ bỏ qua gợi ý là **27,12%** (48/177; trong phạm vi: 21,09% = 27/128); tỉ lệ lỗi lọt đến khách (mở lại 7 ngày) là **4,25%** (51/1.200; trong phạm vi: 3,97% = 39/982).
  - Diễn giải đúng quy tắc: chỉ nêu "chỉ số trong đợt chạy thử là…", không kết luận "trợ lý đã nâng chỉ số" vì đợt chạy thử không có nhóm đối chứng.
  - Đề xuất thêm 1 chỉ số dùng (tỉ lệ mở/sử dụng trợ lý theo nhóm `treatment`/`control` và `staff_id` để kiểm soát ảnh hưởng gián tiếp) và 1 chỉ số an toàn (tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần kết hợp số ca hoàn trùng).
  - Đặc tả **11 event** (mọi event đều có `trace_id`, đồng bộ với các event trong `bang_loi.md` và `pilot_plan.yaml`) và kiểm tra chéo đầy đủ cho mọi chỉ số cũng như chi phí thật thay cột `simulated`.
- **E3 — Hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`):**
  - Tổng hợp đủ 7 mục trên một trang, khớp hoàn toàn với số liệu từ `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml` và `chi_so.md`.
  - Gắn nhãn `simulated` cho mọi con số phát sinh từ cột `_simulated`, đặt trạng thái đúng quy định (`Giả lập` ở mục 1, 2, 3, 7) và ghi người phụ trách là một vai trò cụ thể.
  - Nêu rõ mọi con số bất lợi (92,5% chi phí là phút `simulated`; xem lại 100% tốn 11.743 đ = 0,98× hoặc 12.415 đ = 1,03× [simulated]; thiết kế 20+20 chỉ đạt MDE 6 điểm với power 0,64 ở mức 5 điểm; lỗi hệ thống ca 7, ca 20) và đưa ra đề xuất **Go có điều kiện** (phạm vi thu hẹp `noi_dia` + `hang_nang`, tối đa 2 lần chạy) kèm 5 điều kiện có người phụ trách và ngày kiểm tra.
- **Tổng hợp và rà soát nộp bài (`report/team/group_report.md`, `TEAM.md`, `report/team/phieu_cham.md`):**
  - Hoàn thiện báo cáo nhóm ngắn, cập nhật bảng thành viên và bằng chứng đóng góp trong `TEAM.md`, chuẩn bị `phieu_cham.md` cho phiên duyệt chéo Gate 2a.
  - Tự kiểm tra chéo toàn bộ số liệu trong phạm vi `noi_dia` + `hang_nang` (3.414 đ cơ sở, 5.147 đ khi làm lại ×2, 3.252 đ khi giới hạn 2 lần chạy [simulated]) và chạy kiểm tra `yaml.safe_load`, không còn dấu `?`, không có từ bị cấm trong hồ sơ.

## 4. Bằng chứng

- Repo nhóm: https://github.com/bngcVu/K5-L3A-DAY13-4AE-LaunchEconomics (nhánh `main`).
- Các file do Quyền trực tiếp hoàn thiện:
  - `report/team/chi_so.md` (mục E1, bảng 11 event có `trace_id`, phần kiểm tra chéo).
  - `report/team/ho_so_launch_v0.md` (hồ sơ 1 trang, 7 mục, đề xuất Go có điều kiện với 5 điều kiện).
  - `report/team/group_report.md` (báo cáo nhóm ngắn đủ 8 mục).
  - `report/team/phieu_cham.md` (thông tin nhóm hội đồng; phần chấm nhóm n + 1 cập nhật tại phiên duyệt chéo).
  - `TEAM.md` (thông tin nhóm, thành viên và tổng hợp bằng chứng đóng góp).
  - `report/team/2A202603518_NguyenManhQuyen.md` (báo cáo cá nhân này).
- Output kiểm chứng:
  - Python tính E1 trực tiếp từ `src/logix_requests.csv`: `994/1.200 = 82,83%`, `48/177 = 27,12%`, `51/1.200 = 4,25%` (lệch 0% so với hướng dẫn).
  - `yaml.safe_load` trên `report/team/pilot_plan.yaml`: hợp lệ, 3 luật dừng, không còn dấu `?` ngoài dòng chú thích.
  - Quét từ bị cấm trên `report/team/*` và `TEAM.md`: 0 kết quả.
- Commit chốt: *(cập nhật sau khi hoàn tất phần gắn nhãn độc lập ở `bang_loi.md`, duyệt chéo `phieu_cham.md` và push lần cuối)*.

## 5. Công cụ AI đã dùng

- **Google Antigravity (Gemini):** hỗ trợ đọc đối chiếu toàn bộ hồ sơ của Vũ, Thành, Bảo; chạy script Python tính và kiểm chứng lại các chỉ số E1 và số liệu trong phạm vi từ `src/logix_requests.csv`, `src/logix_runs.csv`; hỗ trợ biên soạn bảng event, hồ sơ 1 trang `ho_so_launch_v0.md`, `group_report.md` và rà soát checklist nộp bài.
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp Python trên `src/logix_requests.csv` (`keep_default_na=False`) để xác minh 3 chỉ số E1 (82,83%, 27,12%, 4,25%) và các con số trong phạm vi (92,26%, 21,09%, 3,97%, 3.414 đ, 5.147 đ, 3.252 đ), khớp 100% với phần việc của Thành và Bảo.
  - Đối chiếu chéo từng chỉ số E1 và từng ca khắc phục trong `bang_loi.md` với danh sách 11 event để đảm bảo mọi chỉ số đều đo được qua `trace_id`.
  - Kiểm tra `git diff` để chắc chắn không sửa phần sở hữu của thành viên khác (giữ nguyên E2 của Thành, `src/lab13.py`, `bang_chi_phi.md`, `pilot_plan.yaml`).
  - Không dùng AI để bịa số, bịa nhãn lỗi độc lập của CP3 hay bịa kết quả duyệt chéo Gate 2a (tuân thủ `RULES.md`).

## 6. Tự đánh giá

- **Làm được:** ghép nối chặt chẽ toàn bộ kết quả A–E thành một bộ hồ sơ nhất quán, minh bạch các con số `simulated` và điểm bất lợi để tối ưu điểm hội đồng C6–C8.
- **Cần nắm chắc khi bảo vệ trước hội đồng:** vì sao chỉ số không tính được từ danh sách event thì chưa đo được; vì sao không được nói "trợ lý đã nâng chỉ số lên 82,83%" khi chưa có đối chứng; lý do chọn **Go có điều kiện** kèm lộ trình giảm xem lại theo bậc (xử lý rủi ro B4) và ký chấp nhận power 0,64 ở mức 5 điểm.
- **Còn cần hoàn tất trước khi chốt nộp:** điền bộ nhãn độc lập 20 ca của cá nhân vào `report/team/bang_loi.md` để chốt tỉ lệ đồng thuận và cập nhật mục 5 trong `ho_so_launch_v0.md`; hoàn tất phiếu chấm nhóm n + 1 ở `report/team/phieu_cham.md` trong phiên duyệt chéo 17:00; kiểm tra chạy trọn `src/lab13.py` trong môi trường đã cài đủ `requirements.txt` rồi commit & push cuối trước 23h59 GMT+7.
