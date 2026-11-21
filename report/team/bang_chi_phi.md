# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT; bằng 1/p vì k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 (890 phút) | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 (1.132 phút) | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

Cách tính: tử số cộng **mọi** lần chạy (kể cả lần lỗi), mẫu số chỉ đếm 978 yêu cầu `thanh_cong`; 4.373.585 ÷ 978 = 4.472 đ. Hoá đơn chia số yêu cầu: (245.585 + 84.000) ÷ 1.200 = 274,7 đ.

- Chi phí mỗi việc thành công gấp 16,3 lần "hoá đơn chia số yêu cầu" (4.472 ÷ 274,7) [simulated].
- Khoản lớn nhất là làm lại: 51,8% tổng chi phí [simulated]; tiếp theo là xem lại 40,7% [simulated]. Giờ nhân viên (xem lại + làm lại) chiếm 92,5%; token chỉ 5,6%, tool 1,9%.
- So với nhân viên tự làm, cần cộng phần nhân viên làm thay 222 yêu cầu không thành công: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Không viết "rẻ bằng 0,37×" khi chưa cộng phần này.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- `quoc_te` không đáng để trợ lý xử lý: chi phí 22.515 đ = 1,88× của 12.000 đ, thành công chỉ 27,3% [simulated]. Chạy lại tới 3 lần không giúp: tỉ lệ ok của `quoc_te` là 30,0% ở lần 1, 11,4% ở lần 2, 2,2% ở lần 3, lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền (đo từ trace).
- `doi_tac` sát ngưỡng (0,85×, thành công 54,4%) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot [simulated].

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

Cách tính: trong mẫu, `noi_dia` + `hang_nang` có 900 việc thành công trên 1.200 yêu cầu → 45.000 × 900 ÷ 1.200 = 33.750 việc thành công/tháng; 40.000.000 ÷ 33.750 = 1.185 đ. Chi phí mỗi việc thành công trong phạm vi (chưa cố định) là 3.414 đ [simulated].

- Chi phí cố định không đổi kết luận ở khối lượng đầy đủ (0,38× so với 12.000 đ), vẫn rẻ hơn nhân viên; ở một nửa khối lượng tăng lên 0,48× nhưng vẫn dưới 1×. Hồ sơ launch phải ghi rõ con số đã cộng cố định hay chưa, và ở khối lượng nào [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...
