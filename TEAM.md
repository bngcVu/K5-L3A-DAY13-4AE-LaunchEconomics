# Team

## Thông tin nhóm

- Tên nhóm: **4AE**
- Lớp: **L3A**
- Repo nhóm: `K5-L3A-DAY13-4AE-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/bngcVu/K5-L3A-DAY13-4AE-LaunchEconomics · nhánh `main` · commit chốt *(cập nhật sau khi hoàn tất commit cuối trước 23h59)*

Phân công chi tiết và điều kiện bàn giao: [PHAN_CONG.md](PHAN_CONG.md).

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Bùi Ngọc Vũ | 2A202603463 | buingocvuuu@gmail.com | https://github.com/bngcVu | Người viết code (trước giải lao): CP1 · A |
|   2 | Tô Minh Thành | 2A202603439 | tominhthanh75@gmail.com | https://github.com/thanhtmhe186559 | Người kiểm số: CP2 · B và E2 |
|   3 | Ngô Gia Bảo | 2A2026033482 | 26ai.baong4@vinuni.edu.vn | https://github.com/b-baocode | Người gắn nhãn 1, người viết code sau giải lao: CP3 · C và CP4 · D |
|   4 | Nguyễn Mạnh Quyền | 2A202603518 | 26ai.quyennm3@vinuni.edu.vn | https://github.com/manhquyenkma | Người gắn nhãn 2, kiêm giữ hồ sơ: CP5 · E, duyệt chéo, nộp bài |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí. Nhóm đáp ứng điều này như sau: Vũ viết `mo_hinh` (trước giải lao), Thành tính tay để kiểm số rồi viết CP2, Bảo viết CP4 (sau giải lao).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## Bùi Ngọc Vũ - MSSV 2A202603463

### Phần việc phụ trách

- Cài môi trường và CP1 · Nhiệm vụ A (mô hình chi phí mỗi việc thành công): `src/lab13.py` (ba hàm A1, `mo_hinh`, đoạn in A2, A3, A4) và `report/team/bang_chi_phi.md` (A1–A4).

### Đóng góp cụ thể

- Viết ba hàm A1; `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
- Viết `mo_hinh` (tử số cộng mọi lần chạy, mẫu số chỉ đếm 978 việc thành công) và tính A2: chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu [simulated].
- Tách theo loại yêu cầu (A3): `quoc_te` 22.515 đ = 1,88× của 12.000 đ, không đáng để trợ lý xử lý [simulated].
- Cộng chi phí cố định 40 triệu đ/tháng (A4): 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng; 5.784 đ = 0,48× ở một nửa khối lượng [simulated].

### Bằng chứng

- Commit: `7c31b5a` (code CP1 và `bang_chi_phi.md`), `ea964cb` (`PHAN_CONG.md`), `c1d24bb`, `696fb20` (`TEAM.md` và báo cáo cá nhân `report/team/2A202603463_BuiNgocVu.md`), nhánh `main`.
- Output `python lab13.py` (UTF-8): ba phép thử ĐẠT; bảng A2, A3, A4 khớp đáp án trong hướng dẫn, lệch dưới 2%.
- Công cụ AI đã dùng và cách tự kiểm tra: ghi trong `report/team/2A202603463_BuiNgocVu.md`.

## Tô Minh Thành - MSSV 2A202603439

### Phần việc phụ trách

- CP2 · Nhiệm vụ B (bảng độ nhạy B1–B4) và mục E2 (rủi ro kinh tế) trong `report/team/chi_so.md`; kiểm số của CP1 bằng cách tính tay.

### Đóng góp cụ thể

- Kiểm số A2 bằng cách tính tay từ `logix_requests.csv` (890 phút xem lại, 1.132 phút làm lại → tổng 4.373.585 đ ÷ 978 = 4.472 đ [simulated]), khớp 0% sai lệch với bảng của Vũ.
- Viết khối `TODO CP2` trong `src/lab13.py` và điền B1–B4 trong `report/team/bang_chi_phi.md`: 9 kịch bản đơn biến (tỉ số cặp gấp đôi/giảm nửa = −0,500), cặp token ×2 + xem lại ×2 = 6.543 đ (+46,3%), xếp hạng 3 yếu tố mạnh nhất (làm lại +51,8%, xem lại +40,7%, lương +23,1%) [simulated].
- B3: giới hạn 2 lần chạy rẻ nhất toàn hệ thống (6.901.220 đ) [simulated]; B4: xem lại 100% ra 11.743 đ (0,98×) hoặc 12.415 đ (1,03× với 15,3 phút làm lại thực tế), hoà vốn ≤ 5,1 hoặc ≤ 4,8 phút/lần xem [simulated].
- Điền mục E2 (`report/team/chi_so.md`): 3 dòng rủi ro kinh tế (làm lại ×2, xem lại 100% kéo dài, khối lượng thấp) lấy số từ B1, B4, A4.

### Bằng chứng

- Commit: `656c2e6` (code CP2, `bang_chi_phi.md`, `chi_so.md` mục E2, báo cáo cá nhân `report/team/2A202603439_ToMinhThanh.md`), merge `265d59c`, nhánh `main`.
- Output `python lab13.py` in đủ B1–B4, tỉ số kiểm tra −0,500 khớp, số lệch dưới 2%.
- Công cụ AI đã dùng và cách tự kiểm tra: ghi trong `report/team/2A202603439_ToMinhThanh.md`.

## Ngô Gia Bảo - MSSV 2A2026033482

### Phần việc phụ trách

- CP3 · Nhiệm vụ C (bảng lỗi `report/team/bang_loi.md`, gắn nhãn 20 ca độc lập) và CP4 · Nhiệm vụ D (`src/lab13.py` khối `TODO CP4`, `report/team/pilot_plan.yaml`, cỡ mẫu D1, tách tác động D2, luật dừng).

### Đóng góp cụ thể

- Viết `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `chay_nhiem_vu_d` trong `src/lab13.py`: năm câu D1 khớp đáp án (1.251 · 3.103 / DE 2,48 · tối đa 1.000 · tối đa 300 · m ≥ 299; power 0,64 ở mức 5 điểm), tính tỉ lệ mở lại 7 ngày hiện tại 4,25% toàn mẫu và 3,97% trong phạm vi.
- Điền hoàn chỉnh `report/team/pilot_plan.yaml`: chia ngẫu nhiên 20 + 20 nhân viên, phạm vi `noi_dia` + `hang_nang`, MDE 6 điểm, 3 luật dừng đủ bốn vế NẾU–TRONG–THÌ–KHÔNG THÌ, không còn dấu `?`, đọc được bằng `yaml.safe_load`.
- Gắn nhãn độc lập 20 ca lỗi (người 1), soạn 5 quy tắc phân biệt ca dễ lẫn và lập bảng khắc phục 5 ca (9, 20, 18, 4, 17) đủ 5 loại Google PAIR trong `report/team/bang_loi.md`.

### Bằng chứng

- Commit: `e10b5a7` (CP4 `src/lab13.py` và `pilot_plan.yaml`), `b3b3e80` (CP3 `bang_loi.md` và `report/team/2A2026033482_NgoGiaBao.md`), `42694e9`, nhánh `main`.
- Kiểm tra `yaml.safe_load` hợp lệ, không còn dấu `?` ngoài dòng chú thích.
- Công cụ AI đã dùng và cách tự kiểm tra: ghi trong `report/team/2A2026033482_NgoGiaBao.md`.

## Nguyễn Mạnh Quyền - MSSV 2A202603518

### Phần việc phụ trách

- CP5 · Nhiệm vụ E: mục E1 và danh sách event trong `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`; duyệt chéo Gate 2a (`report/team/phieu_cham.md`); `report/team/group_report.md`; `TEAM.md`; rà soát checklist và nộp bài cuối. Gắn nhãn 20 ca độc lập (người 2) ở CP3.

### Đóng góp cụ thể

- Điền mục E1 và danh sách event trong `report/team/chi_so.md`: tính trực tiếp từ `src/logix_requests.csv` 3 chỉ số (chính 82,83% = 994/1.200; bỏ qua gợi ý 27,12% = 48/177; mở lại 7 ngày 4,25% = 51/1.200), đề xuất thêm 2 chỉ số (dùng và an toàn), đặc tả 11 event có `trace_id` và kiểm tra chéo với mọi chỉ số.
- Hoàn thiện hồ sơ 1 trang `report/team/ho_so_launch_v0.md` đủ 7 mục với nhãn `simulated` đầy đủ, nêu rõ các con số bất lợi (phút `simulated`, xem lại 100% tốn 0,98×–1,03×, power 0,64 ở mức 5 điểm, lỗi ca 7 và ca 20) và đề xuất **Go có điều kiện** kèm 5 điều kiện, vai trò phụ trách và ngày kiểm tra.
- Hoàn thiện `report/team/group_report.md`, cập nhật `TEAM.md`, tạo báo cáo cá nhân `report/team/2A202603518_NguyenManhQuyen.md`, chuẩn bị `report/team/phieu_cham.md` cho phiên duyệt chéo Gate 2a và kiểm tra các điều kiện nộp bài (`yaml.safe_load`, không còn dấu `?`, không có từ bị cấm).
- CP3: gắn nhãn độc lập 20 ca (người 2) kèm lý do từng ca trong file nháp riêng, không trao đổi với Bảo; đồng thuận 17/20 = 85%, thống nhất 3 ca không trùng (ca 6: Hệ thống → Do người dùng; ca 13: Hệ thống → Giới hạn hệ thống; ca 18: Hệ thống → Ngữ cảnh) theo nguyên nhân gốc và ghi quy tắc phân biệt trong `bang_loi.md`.
- *(Đang chờ hoàn tất tại lớp: chấm nhóm n+1 vào `phieu_cham.md` và commit/push chốt.)*

### Bằng chứng

- Các file đã tạo/cập nhật: `report/team/chi_so.md` (E1 + 11 event + kiểm tra chéo), `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`, `report/team/2A202603518_NguyenManhQuyen.md`, `TEAM.md`.
- Kiểm chứng số E1 trực tiếp bằng Python trên `src/logix_requests.csv` (`keep_default_na=False`), kiểm chứng `yaml.safe_load` trên `pilot_plan.yaml` và quét từ bị cấm trên toàn bộ `report/team/`.
- Công cụ AI đã dùng và cách tự kiểm tra: ghi trong `report/team/2A202603518_NguyenManhQuyen.md`. Commit chốt cập nhật sau khi commit/push cuối.
