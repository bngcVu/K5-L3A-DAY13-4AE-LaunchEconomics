"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai  # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai  # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai  # mẫu số KHÁC tử số: tử số cộng mọi lần chạy
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()           # mẫu số chỉ đếm việc thành công
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ D · Cỡ mẫu và thiết kế pilot ----------
P1, P2, ALPHA, POWER, ICC = 0.70, 0.75, 0.05, 0.80, 0.02


def co_mau(p1, p2, alpha=ALPHA, power=POWER):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức z, làm tròn lên)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m − 1) × ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc=ICC):
    """c cụm × m yêu cầu ÷ DE; luôn nhỏ hơn c ÷ ICC."""
    return c * m / he_so_thiet_ke(m, icc)


def chay_nhiem_vu_d(reqs):
    n_a = co_mau(P1, P2)
    print('\nD1 · Cỡ mẫu (baseline 0,70 → 0,75; alpha 0,05; power 0,8; ICC 0,02)')
    print(f'  a) chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')

    de_b = he_so_thiet_ke(75)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / 75)
    print(f'  b) theo nhân viên, m = 75: DE = {de_b:.2f}; n = {n_b:,} mỗi nhóm → {nv_b} nhân viên mỗi nhóm, '
          f'tổng {2 * nv_b} > 40 → {"không đủ người" if 2 * nv_b > 40 else "đủ người"}')

    tran_c = 20 / ICC
    print(f'  c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa = 20 / 0,02 = {tran_c:,.0f} '
          f'{"<" if tran_c < n_a else "≥"} {n_a:,} → {"không đạt" if tran_c < n_a else "đạt"}')

    print(f'  d) 6 depot mỗi nhóm: tối đa = 6 / 0,02 = {6 / ICC:,.0f}')

    n_e = co_mau(P1, 0.76)
    # 20m / (1 + (m − 1)·ICC) ≥ n_e  ⇔  m ≥ n_e·(1 − ICC) / (20 − n_e·ICC)
    m_e = math.ceil(n_e * (1 - ICC) / (20 - n_e * ICC))
    print(f'  e) mức chênh 6 điểm: {n_e:,} mỗi nhóm; 20 người mỗi nhóm cần m ≥ {m_e} yêu cầu/người '
          f'(DE = {he_so_thiet_ke(m_e):.2f}; hiệu dụng {co_mau_hieu_dung(20, m_e):,.0f}); '
          f'tổng {2 * 20 * m_e:,} yêu cầu ≈ {2 * 20 * m_e / 1500:.1f} ngày khối lượng toàn công ty')

    # Power bất lợi: thiết kế cho 6 điểm nhưng tác động thật chỉ 5 điểm
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    pw = NormalIndPower().power(effect_size=proportion_effectsize(P2, P1), nobs1=n_e, alpha=ALPHA)
    print(f'  power nếu tác động thật chỉ +5 điểm với n = {n_e} mỗi nhóm: {pw:.2f}')

    # D3 · tỉ lệ mở lại hiện tại trước khi đặt luật an toàn
    mo_lai = reqs['mo_lai_trong_7_ngay'].astype(int)
    pv = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    print('\nD3 · Tỉ lệ mo_lai_trong_7_ngay trong đợt chạy thử')
    print(f'  toàn bộ: {mo_lai.mean() * 100:.2f}% ({mo_lai.sum()}/{len(reqs)})')
    print(f'  phạm vi noi_dia + hang_nang: {mo_lai[pv].mean() * 100:.2f}% ({mo_lai[pv].sum()}/{pv.sum()})')
    lam_lai_pv = (reqs.loc[pv, 'ket_qua'] == 'lam_lai').mean()
    print(f'  tỉ lệ lam_lai trong phạm vi: {lam_lai_pv * 100:.1f}%')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    goc = ket_qua['cps']
    print(f"\nA2: cps / hoa_don_moi_yc = {goc / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for khoan in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f"  {khoan:8s} {ket_qua[khoan] / ket_qua['tong'] * 100:5.1f}% tổng chi phí")
    print(f"  gio nhan vien (xem_lai + lam_lai) {(ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100:5.1f}%")
    khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']  # 222 yêu cầu nhân viên phải tự làm
    he_thong = (ket_qua['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    print(f"  cả hệ thống / yêu cầu (cộng {BASELINE:,}đ cho {khong_thanh_cong} yêu cầu không thành công) = "
          f"{he_thong:,.0f} = {he_thong / BASELINE:.2f}x của 12.000đ [simulated]")

    # A3: tách theo loại yêu cầu (có cột simulated nên mọi cps là simulated)
    print('\nA3: loai | so_yc | ti_le_thanh_cong | lan_chay/yc | cps [simulated] | so voi 12.000d')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        so_run = runs['request_id'].isin(r['request_id']).sum()
        print(f"  {loai:10s} {len(r):5d} {m['thanh_cong'] / len(r) * 100:6.1f}% "
              f"{so_run / len(r):5.2f} {m['cps']:10,.0f} {m['cps'] / BASELINE:5.2f}x")

    # A4: cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    m = mo_hinh(runs, pham_vi)
    print('\nA4: phạm vi noi_dia + hang_nang [simulated]')
    print(f"  cps trong phạm vi (chưa cố định) = {m['cps']:,.0f} ({m['thanh_cong']} việc thành công / mẫu)")
    for ten, yc_thang in (('45.000 yc/tháng', 45000), ('một nửa khối lượng', 22500)):
        viec_thang = yc_thang * m['thanh_cong'] / len(reqs)
        co_dinh = 40_000_000 / viec_thang
        print(f"  {ten:20s} viec_thanh_cong/thang={viec_thang:8,.0f}  co_dinh/viec={co_dinh:6,.0f}  "
              f"cps+co_dinh={m['cps'] + co_dinh:6,.0f}  {(m['cps'] + co_dinh) / BASELINE:4.2f}x")
    # ---------- CP2 · Nhiệm vụ B: bảng độ nhạy ----------
    # B1: mỗi kịch bản đổi một yếu tố (mọi số là simulated)
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    print('\nB1: kich ban | cps [simulated] | thay doi')
    tac_dong = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        tac_dong[ten] = cps - goc
        print(f'  {ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')
    for gd, gn in (('Giá token gấp đôi', 'Giá token giảm một nửa'),
                   ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
                   ('Làm lại gấp đôi', 'Làm lại giảm một nửa')):
        print(f'  kiem tra: {gn} = {tac_dong[gn] / tac_dong[gd]:.3f} x tac dong {gd} (ky vong -0,5)')

    # B2: một cặp = giá token gấp đôi + xem lại gấp đôi
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = tac_dong['Giá token gấp đôi'] + tac_dong['Xem lại gấp đôi']
    print(f'\nB2: cap token x2 + xem lai x2 = {cap:,.0f} ({(cap / goc - 1) * 100:+.1f}%); '
          f'tong hai tac dong rieng = {goc + tong_rieng:,.0f} ({tong_rieng / goc * 100:+.1f}%)')

    # B3: giới hạn số lần chạy; cả hệ thống = tổng trợ lý + 12.000đ × yêu cầu không thành công
    print('\nB3: gioi han | tong tro ly | khong thanh cong | ca he thong | cps [simulated]')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        kt = len(reqs) - m['thanh_cong']
        print(f"  {k} lan {m['tong']:12,.0f} {kt:5d} {m['tong'] + kt * BASELINE:12,.0f} {m['cps']:8,.0f}")

    # B4: xem lại 100% cho noi_dia + hang_nang (5 phút/lần xem, 9 phút/ca làm lại theo đề)
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    token_tool = ((runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA).sum()
                  + (runs_pv['tool_calls'] * GIA_TOOL).sum())
    so_xem = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()   # yêu cầu có ít nhất một lần chạy ok
    ca_lam_lai = (pv['phut_lam_lai_simulated'] > 0).sum()
    viec_ok = (pv['ket_qua'] == 'thanh_cong').sum()
    phut_thuc = reqs.loc[reqs['phut_lam_lai_simulated'] > 0, 'phut_lam_lai_simulated'].mean()  # trung bình trên toàn bộ ca làm lại của mẫu
    print(f'\nB4: {len(pv)} yc, {so_xem} yc duoc xem lai, {ca_lam_lai} ca lam lai, {viec_ok} viec thanh cong, '
          f'token+tool={token_tool:,.0f}, phut lam lai trung binh thuc = {phut_thuc:.1f}')
    for nhan, phut_lam in (('9 phut/ca (de bai)', 9), (f'{phut_thuc:.1f} phut/ca (du lieu)', phut_thuc)):
        tong4 = token_tool + so_xem * 5 * LUONG_PHUT + ca_lam_lai * phut_lam * LUONG_PHUT
        hoa_von = (BASELINE * viec_ok - token_tool - ca_lam_lai * phut_lam * LUONG_PHUT) / (so_xem * LUONG_PHUT)
        print(f'  {nhan:24s} tong={tong4:12,.0f} cps={tong4 / viec_ok:7,.0f} = {tong4 / viec_ok / BASELINE:.2f}x'
              f'  hoa von: xem lai <= {hoa_von:.1f} phut')
    # CP4 · Nhiệm vụ D: cỡ mẫu và thiết kế pilot.
    chay_nhiem_vu_d(reqs)