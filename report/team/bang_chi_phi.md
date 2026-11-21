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

## Kiểm số A2 (người kiểm số tính tay)

Tính tay từ `logix_requests.csv` (không qua `mo_hinh`): tổng phút xem lại = 890, tổng phút làm lại = 1.132 → 890 × 2.000 = 1.780.000 đ và 1.132 × 2.000 = 2.264.000 đ [simulated]. Cộng token 245.585 và tool 84.000 (5.600 lần × 15 đ) ra 4.373.585 đ; chia 978 việc thành công = 4.472 đ. Khớp bảng A2 của Vũ, không lệch.

## B1 · Đổi từng yếu tố

Gốc (A2) = 4.472 đ mỗi việc thành công. Mọi số trong B là [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9); `lab13.py` in tỉ số −0,500 cho cả ba cặp.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính: token và tiền xem lại là hai khoản cộng với nhau, không nhân nhau.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%). Giá token chỉ +5,6%, nên pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải hoá đơn token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). [simulated]

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ (rẻ nhất) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), nhưng không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ).
- Lý do: giới hạn 1 lần đẩy thêm 85 yêu cầu (319 − 234) sang nhân viên, mỗi yêu cầu 12.000 đ, nên tổng hệ thống tăng 548.561 đ so với 2 lần dù chi phí mỗi việc thành công giảm.

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang` (982 yêu cầu): 948 yêu cầu có ít nhất một lần chạy ok × 5 phút × 2.000 đ = 9.480.000 đ; 48 ca làm lại × 9 phút × 2.000 đ = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công. [simulated]

- Xem lại 100%: **11.743 đ = 0,98× của 12.000 đ**. Nếu dùng phút làm lại thật của dữ liệu (15,3 phút/ca thay vì 9): **12.415 đ = 1,03×**, tức đắt hơn nhân viên tự làm. Mức hoà vốn: mỗi lần xem lại phải ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút).
- Tiền xem lại chiếm khoảng 90% chi phí nên xem lại 100% thì trợ lý gần như không tiết kiệm được gì. Pilot phải học được tỉ lệ xem lại giảm an toàn xuống mức nào và mỗi lần xem lại có ngắn hơn 5 phút được không.
