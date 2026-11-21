# Phân công nhóm · Lab 13 LogiX-VN (Gate 2a)

Làm theo kiểu **tiếp sức**, bám đúng lịch của [CHECKPOINTS.md](CHECKPOINTS.md): Vũ xong thì đến Thành, Thành xong thì đến Bảo, Bảo xong thì đến Quyền. Mỗi người giữ riêng một nhóm file (hoặc một khối `TODO` trong `src/lab13.py`), làm xong thì commit và bàn giao kèm các con số chính. Không ai sửa phần của người khác, nên không xung đột khi merge.

```text
14:10 Vũ (CP1·A) ─► 14:53 Thành (CP2·B + E2) ─► 15:35 Bảo (CP3·C + CP4·D) ─► 16:36 Quyền (CP5·E + hồ sơ + duyệt chéo + nộp)
```

Hai việc chạy song song là do đề bắt buộc, không phải do phân công:

- **Gắn nhãn CP3 (15:35–15:43):** đề yêu cầu hai người gắn nhãn độc lập (RULES.md) trong lúc hai người kia hoàn thiện CP2. Bảo và Quyền ngồi tách nhau, mỗi người gắn 20 ca vào file nháp riêng, không trao đổi.
- **Khung hồ sơ:** người giữ hồ sơ "điền dần từ đầu buổi" (CHECKPOINTS CP5). Quyền chỉ ghi số đã được bàn giao vào file riêng của mình, không chờ và không chặn ai.

## Bảng tổng hợp

| Thứ tự | Thành viên | Vai trong TEAM.md | Checkpoint · Nhiệm vụ | Giờ | Phần sở hữu (chỉ người này sửa) | Rubric |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Bùi Ngọc Vũ** | Người viết code (trước giải lao) | Cài đặt + CP1 · A | 14:00–14:53 | `src/lab13.py` khối `TODO CP1`; `bang_chi_phi.md` phần A2–A4 | C1 · 20đ |
| 2 | **Tô Mình Thành** | Người kiểm số | CP2 · B + E2 | 14:53–15:43 | `src/lab13.py` khối `TODO CP2`; `bang_chi_phi.md` phần B1–B4; `chi_so.md` mục E2 | C2 · 15đ, một phần C5 |
| 3 | **Ngô Gia Bảo** | Người gắn nhãn 1; người viết code sau giải lao | CP3 · C + CP4 · D | 15:35–16:36 | `bang_loi.md`; `src/lab13.py` khối `TODO CP4`; `pilot_plan.yaml` | C3 · 10đ, C4 · 15đ |
| 4 | **Nguyễn Mạnh Quyền** | Người gắn nhãn 2, kiêm giữ hồ sơ | CP5 · E + duyệt chéo + nộp | 16:36–18:00 | `chi_so.md` mục E1 và event; `ho_so_launch_v0.md`; `phieu_cham.md`; `group_report.md`; `TEAM.md` | Một phần C5, C6–C8 · 30đ |

Mọi file hồ sơ nằm trong `report/team/`. Cách chia này thoả hai yêu cầu của TEAM.md: đổi người viết code sau giờ giải lao (Vũ trước, Bảo sau), và ít nhất hai người tự tay tính được chi phí (Vũ viết `mo_hinh`, Thành tính tay để kiểm số).

Mỗi người tự tạo báo cáo cá nhân bằng cách **copy** `report/team/MSSV_HoTen.md` (giữ nguyên file mẫu): `MSSV_BuiNgocVu.md`, `MSSV_ToMinhThanh.md`, `MSSV_NgoGiaBao.md`, `MSSV_NguyenManhQuyen.md`.

---

## 1 · Bùi Ngọc Vũ · CP1 · Nhiệm vụ A (14:00 → 14:53)

**Nhận vào:** repo nhóm đã fork, chưa có gì.

**Việc cần làm**
1. 14:00: cài môi trường trong `src/` theo [src/README.md](src/README.md); chạy `python lab13.py`, thấy báo `NotImplementedError` là đúng.
2. Viết ba hàm A1 ở khối `TODO CP1` cho tới khi in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25). **Chưa đạt đủ ba phép thử thì không bàn giao** (quy tắc 1 của lab).
3. Viết `mo_hinh(runs, reqs, …)` (A2): tử số tính **mọi** lần chạy kể cả lần lỗi; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`.
4. Gọi lại `mo_hinh` cho từng giá trị cột `loai` (A3); cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4).
5. Điền vào `bang_chi_phi.md`: bảng A2 đủ 9 dòng (hai dòng tính từ cột `_simulated` ghi nhãn **simulated**), bảng A3 đủ 4 dòng, A4 và các câu trả lời.

**Phải giải thích được:** vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; loại yêu cầu nào không đáng để trợ lý xử lý và vì sao chạy lại tới 3 lần không giúp loại đó.

**Xong khi (điều kiện bàn giao)**
- `python lab13.py` in ĐẠT cả ba phép thử và in bảng A2.
- Chi phí mỗi việc thành công lớn hơn nhiều lần hoá đơn token chia số yêu cầu (chỉ gấp 1–2 lần là đã quên giờ của nhân viên).
- Số khớp slide chữa CP1, lệch không quá 2%.
- Commit, rồi nhắn Thành và Quyền: "CP1 xong, chi phí mỗi việc thành công = …, gấp … lần hoá đơn token; A3: loại đắt nhất là …".

---

## 2 · Tô Mình Thành · CP2 · Nhiệm vụ B + E2 (14:53 → 15:43)

**Nhận vào:** `mo_hinh` đã chạy đúng, do Vũ bàn giao.

**Việc cần làm**
1. **Kiểm số trước tiên:** tính tay một con số trong bảng A2 và ghi cách tính. Nếu lệch, trả lại Vũ sửa; không tự sửa khối `TODO CP1`.
2. Ở khối `TODO CP2`, gọi `mo_hinh` cho:
   - B1: 9 kịch bản, mỗi kịch bản đổi một yếu tố;
   - B2: một kịch bản đổi một cặp yếu tố;
   - B3: giới hạn 1, 2, 3 lần chạy, tính cả chi phí toàn hệ thống;
   - B4: kịch bản xem lại 100% cho `noi_dia` + `hang_nang`.
3. Điền vào `bang_chi_phi.md`: B1 đủ 9 dòng, xếp hạng ba yếu tố ảnh hưởng mạnh nhất, trả lời B3 và B4 (mỗi câu không quá 3 dòng, có số). Xong trước giải lao 15:20.
4. 15:35–15:43, trong lúc Bảo và Quyền gắn nhãn: điền mục **E2 · Rủi ro kinh tế** trong `chi_so.md`. Ít nhất hai dòng, số lấy từ bảng độ nhạy, người phụ trách là một vai trò.

**Phải giải thích được:** vì sao mô hình cộng tuyến tính nên tác động của một cặp bằng tổng hai tác động riêng; vì sao giới hạn số lần chạy rẻ nhất cho công ty có thể khác giới hạn cho chi phí mỗi việc thành công thấp nhất.

**Xong khi**
- Mỗi kịch bản "giảm một nửa" làm chi phí giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" tương ứng.
- B2 bằng tổng hai tác động riêng.
- Số khớp slide chữa CP2, lệch không quá 2%.
- Commit, rồi nhắn Bảo và Quyền: "CP2 xong, ba yếu tố nhạy nhất: …; giới hạn lần chạy chọn …; E2 đã có hai rủi ro …".

---

## 3 · Ngô Gia Bảo · CP3 · Nhiệm vụ C + CP4 · Nhiệm vụ D (15:35 → 16:36)

**Nhận vào:** bộ nhãn độc lập của chính Bảo và của Quyền; số CP1, CP2 đã chốt.

### CP3 · Bảng lỗi (15:35 → 16:08)
1. 15:35–15:43: gắn nhãn độc lập 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi") theo năm loại của Google PAIR, ngồi tách Quyền, không trao đổi.
2. Chép **nguyên văn** hai bộ nhãn (của Bảo và của Quyền) vào `bang_loi.md`. Sau khi đã so thì không sửa hai bộ này.
3. So nhãn, tính tỉ lệ đồng thuận. Dưới 16/20 thì viết lại định nghĩa năm loại trước khi đi tiếp. Với mỗi ca không trùng, cùng Quyền thống nhất nhãn và ghi một câu quy tắc phân biệt.
4. Bảng khắc phục: chọn 5 ca, mỗi loại một ca. Mỗi dòng có cách phát hiện **đo được** (event, ngưỡng, tần suất) và một vai trò phụ trách, không ghi "cả đội".

**Phải giải thích được:** gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa; khác nhau giữa lỗi hệ thống và lỗi ngầm.

### CP4 · pilot_plan.yaml (16:08 → 16:36)
1. Ở khối `TODO CP4`, tính năm câu D1 (cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm) với số cho sẵn: chỉ số chính 0,70, mục tiêu +5 điểm, alpha 0,05, power 0,8, ICC 0,02. Dùng hệ số thiết kế `1 + (m − 1) × ICC` và cỡ mẫu hiệu dụng `c × m ÷ hệ số thiết kế`. Tính D1 **rồi mới** chọn cách chia.
2. Trả lời năm câu D2 "tách được tác động". Ghi kết quả D1 và D2 vào phần chú thích đầu `pilot_plan.yaml`.
3. Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn.
4. Điền mọi dấu `?`. Viết ít nhất ba luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu **NẾU – TRONG – THÌ – KHÔNG THÌ**, mỗi luật có ngưỡng, thời hạn và người có quyền dừng (để lấy đủ C8). Ngưỡng luật chi phí lấy từ bảng độ nhạy của Thành.

**Phải giải thích được:** cách tính cỡ mẫu hiệu dụng khi chia theo cụm; vì sao số cụm quyết định chứ không phải tổng số yêu cầu; đánh đổi nhóm chấp nhận nếu cách chia chưa đủ mẫu.

**Xong khi**
- Đồng thuận từ 16/20 ca; bảng khắc phục đủ năm loại.
- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi.
- `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì.
- Cách chia có ít nhất 20 cụm mỗi nhóm, hoặc ghi rõ đánh đổi.
- Commit, rồi nhắn Quyền: "CP3, CP4 xong; đồng thuận …/20; cỡ mẫu hiệu dụng …; cách chia …; tỉ lệ mở lại 7 ngày = …; ba luật dừng: …".

---

## 4 · Nguyễn Mạnh Quyền · CP5 · Nhiệm vụ E + duyệt chéo + nộp bài (16:36 → 18:00)

**Nhận vào:** toàn bộ số đã chốt của Vũ, Thành, Bảo.

**Việc làm trước 16:36 (chỉ trong file của mình, không chặn ai)**
- 14:00: điền thông tin nhóm, bốn thành viên và vai vào `TEAM.md`.
- Mở khung `ho_so_launch_v0.md`, ghi dần số mỗi khi nhận được tin nhắn bàn giao.
- 15:35–15:43: gắn nhãn độc lập 20 ca vào file nháp riêng, đưa cho Bảo; sau đó chỉ tham gia thống nhất các ca không trùng.

**Việc cần làm (16:36 → 17:00)**
1. Điền mục **E1** trong `chi_so.md`: tính thử ba chỉ số (chính, dùng, an toàn) trên 1.200 yêu cầu, bằng script hoặc tính tay có ghi cách tính; đề xuất thêm một chỉ số dùng và một chỉ số an toàn; liệt kê ít nhất sáu event, mỗi event có `trace_id`; kiểm tra chéo từng chỉ số với event dùng để tính nó.
2. Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số" (đợt chạy thử không có nhóm đối chứng).
3. Hoàn thiện `ho_so_launch_v0.md`: một trang, bảy mục. Mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và người phụ trách là một vai trò. Dòng cuối chọn **một** trong ba đề xuất Go · Go có điều kiện · No-go. Phải nêu cả con số bất lợi và cách xử lý (C6), và thu hẹp phạm vi có lý do bằng số (C7).

**Duyệt chéo và nộp (17:00 → 18:00, sau đó đến 23h59)**
4. 17:00: gửi hồ sơ cho nhóm hội đồng. Cả bốn người có mặt; ai phụ trách phần nào thì trả lời câu hỏi về phần đó.
5. Chấm nhóm n + 1 vào `phieu_cham.md` (nhóm cuối chấm nhóm 1).
6. 17:45: điền `group_report.md`, cập nhật `TEAM.md` (đóng góp và bằng chứng của từng người), nhắc ba bạn kia commit báo cáo cá nhân, rồi commit và push lần cuối trước **23h59 GMT+7**.

**Xong khi**
- Ba chỉ số tính thử khớp slide chữa; đủ sáu event có `trace_id`; đủ hai dòng rủi ro (E2 của Thành).
- `grep -rni production ../report/team` không in gì.
- Mọi số tính từ cột `_simulated` trong hồ sơ đều có nhãn **simulated**.
- Đủ sáu file hồ sơ trong `report/team/` với đúng tên: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`.

---

## Sau khi bàn giao

Vũ, Thành và Bảo không ngồi không sau khi bàn giao:
- Viết báo cáo cá nhân: phần việc, đóng góp, bằng chứng (commit, file), công cụ AI đã dùng và cách tự kiểm tra.
- Ôn lại phần của mình để trả lời hội đồng lúc 17:00.
- Có mặt khi người sau nhắn hỏi về số mình đã bàn giao.

## Quy tắc chung

1. Chỉ sửa file hoặc khối `TODO` mình sở hữu. Thấy sai ở phần người khác thì nhắn người đó sửa.
2. Bàn giao bằng commit cộng một tin nhắn có các con số chính, để người sau không phải đọc lại code.
3. Đối chiếu ngay khi slide chữa hiện lên; lệch quá 2% thì người sở hữu phần đó sửa trước khi người sau dùng số.
4. Mọi con số do `src/lab13.py` tính ra hoặc tính tay có ghi cách tính. Không dùng AI để bịa số, nhãn lỗi hay kết quả duyệt chéo.
5. Mỗi câu trả lời không quá 3 dòng, có ít nhất một con số. Không dùng từ "production". Người phụ trách luôn là một vai trò, không ghi "cả đội".
6. Không sửa `src/logix_runs.csv`, `src/logix_requests.csv`; không commit `.venv/` hoặc `.env`.
