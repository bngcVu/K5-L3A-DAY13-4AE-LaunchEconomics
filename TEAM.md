# Team

## Thông tin nhóm

- Tên nhóm: ……… (điền; dùng đúng tên này trong tên repo)
- Lớp: L3A hoặc L3B (điền)
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: ……… (Quyền điền lúc nộp bài)

Phân công chi tiết và điều kiện bàn giao: [PHAN_CONG.md](PHAN_CONG.md).

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Bùi Ngọc Vũ | 2A202603463 | buingocvuuu@gmail.com | https://github.com/bngcVu | Người viết code (trước giải lao): CP1 · A |
|   2 | Tô Mình Thành | ……… | ……… | ……… | Người kiểm số: CP2 · B và E2 |
|   3 | Ngô Gia Bảo | ……… | ……… | ……… | Người gắn nhãn 1, người viết code sau giải lao: CP3 · C và CP4 · D |
|   4 | Nguyễn Mạnh Quyền | ……… | ……… | ……… | Người gắn nhãn 2, kiêm giữ hồ sơ: CP5 · E, duyệt chéo, nộp bài |

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

## Bùi Ngọc Vũ - MSSV ………

### Phần việc phụ trách

- Cài môi trường và CP1 · Nhiệm vụ A (mô hình chi phí mỗi việc thành công): `src/lab13.py` (ba hàm A1, `mo_hinh`, đoạn in A2, A3, A4) và `report/team/bang_chi_phi.md` (A1–A4).

### Đóng góp cụ thể

- Viết ba hàm A1; `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
- Viết `mo_hinh` (tử số cộng mọi lần chạy, mẫu số chỉ đếm 978 việc thành công) và tính A2: chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu [simulated].
- Tách theo loại yêu cầu (A3): `quoc_te` 22.515 đ = 1,88× của 12.000 đ, không đáng để trợ lý xử lý [simulated].
- Cộng chi phí cố định 40 triệu đ/tháng (A4): 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng; 5.784 đ = 0,48× ở một nửa khối lượng [simulated].

### Bằng chứng

- Commit: `7c31b5a` (code CP1 và `bang_chi_phi.md`), `ea964cb` (`PHAN_CONG.md`), `c1d24bb` (`TEAM.md` và báo cáo cá nhân), nhánh `main`.
- Output `python lab13.py` (UTF-8): ba phép thử ĐẠT; bảng A2, A3, A4 khớp đáp án trong hướng dẫn, lệch dưới 2%.
- Công cụ AI đã dùng và cách tự kiểm tra: ghi trong `report/team/MSSV_BuiNgocVu.md` (Vũ tự điền).

## Tô Mình Thành - MSSV ………

### Phần việc phụ trách

- CP2 · Nhiệm vụ B (bảng độ nhạy B1–B4) và mục E2 (rủi ro kinh tế) trong `report/team/chi_so.md`; kiểm số của CP1 bằng cách tính tay.

### Đóng góp cụ thể

- (Thành điền sau khi làm xong.)

### Bằng chứng

- (Thành điền: commit, output, công cụ AI đã dùng và cách tự kiểm tra.)

## Ngô Gia Bảo - MSSV ………

### Phần việc phụ trách

- CP3 · Nhiệm vụ C (bảng lỗi `report/team/bang_loi.md`, gắn nhãn 20 ca độc lập) và CP4 · Nhiệm vụ D (`report/team/pilot_plan.yaml`, cỡ mẫu D1, tách tác động D2, luật dừng).

### Đóng góp cụ thể

- (Bảo điền sau khi làm xong.)

### Bằng chứng

- (Bảo điền: commit, output, công cụ AI đã dùng và cách tự kiểm tra.)

## Nguyễn Mạnh Quyền - MSSV ………

### Phần việc phụ trách

- CP5 · Nhiệm vụ E: mục E1 và danh sách event trong `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`; duyệt chéo Gate 2a (`report/team/phieu_cham.md`); `report/team/group_report.md`; `TEAM.md`; commit và push cuối. Gắn nhãn 20 ca độc lập ở CP3.

### Đóng góp cụ thể

- (Quyền điền sau khi làm xong.)

### Bằng chứng

- (Quyền điền: commit, output, công cụ AI đã dùng và cách tự kiểm tra.)
