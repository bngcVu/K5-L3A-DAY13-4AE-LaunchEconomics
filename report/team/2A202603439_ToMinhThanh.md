# Báo cáo cá nhân — ToMinhThanh-2A202603439

## 1. Thông tin thành viên

- Họ tên: Tô Minh Thành
- MSSV: 2A202603439
- Email: tominhthanh75@gmail.com
- Vai trong nhóm: người kiểm số

## 2. Phần việc phụ trách

CP2 · Nhiệm vụ B (bảng độ nhạy) và mục E2 (rủi ro kinh tế), nhận bàn giao `mo_hinh` từ Vũ. Phần sở hữu: khối `TODO CP2` trong `src/lab13.py`; `bang_chi_phi.md` phần B1–B4; `chi_so.md` mục E2.

## 3. Đóng góp cụ thể

- Kiểm số trước khi làm tiếp: tính tay từ `logix_requests.csv` được 890 phút xem lại và 1.132 phút làm lại, tức 1.780.000 đ và 2.264.000 đ [simulated]. Cộng token 245.585 và tool 84.000 ra 4.373.585 đ, chia 978 việc thành công = 4.472 đ. Khớp bảng A2 của Vũ nên không phải trả lại.
- B1: gọi lại `mo_hinh` cho 9 kịch bản, mỗi kịch bản đổi một yếu tố. Mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (tỉ số −0,500).
- B2: token gấp đôi cộng xem lại gấp đôi ra 6.543 đ (+46,3%), bằng tổng hai tác động riêng (5,6% + 40,7%) vì mô hình cộng tuyến tính. Ba yếu tố nhạy nhất: số ca làm lại +51,8%, tỉ lệ xem lại +40,7%, lương nhân viên +23,1%.
- B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ); giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) nhưng đẩy thêm 85 yêu cầu sang nhân viên.
- B4: xem lại 100% ra 11.743 đ (0,98× của 12.000 đ), hoặc 12.415 đ (1,03×) nếu làm lại 15,3 phút/ca như dữ liệu. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút hoặc ≤ 4,8 phút.
- E2: ba dòng rủi ro (làm lại gấp đôi, xem lại 100% kéo dài, khối lượng thấp), số lấy từ B1, B4, A4, người phụ trách là vai trò.

Mọi số tính từ cột `_simulated` đều ghi nhãn simulated.

## 4. Bằng chứng

- `src/lab13.py`: khối `CP2 · Nhiệm vụ B`; chạy `python lab13.py` in B1, B2, B3, B4.
- `report/team/bang_chi_phi.md`: mục "Kiểm số A2", B1–B4.
- `report/team/chi_so.md`: mục E2.
- Số khớp slide chữa CP2, lệch không quá 2%.

## 5. Công cụ AI đã dùng

Claude Code, dùng để đọc đề và hướng dẫn, viết khối code CP2 và điền các bảng. Cách tự kiểm tra: chạy lại `lab13.py` và đối chiếu từng số với hướng dẫn chi tiết; tính tay con số 4.472 đ từ file CSV thô, độc lập với `mo_hinh`; kiểm tra tỉ số −0,500 giữa các cặp "gấp đôi/giảm một nửa" và kiểm tra B2 bằng tổng hai tác động riêng. Không dùng AI để bịa số.

## 6. Tự đánh giá

Hoàn thành đúng phạm vi CP2: số khớp, không phải trả lại phần của Vũ. Hạn chế: toàn bộ số B dựa trên phút simulated nên chưa phản ánh phút đo thật; cần thay bằng số đo sau tuần đầu của pilot.
