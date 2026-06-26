# -*- coding: utf-8 -*-
"""
app.py — Website Evaluasi Program MCB x BRImo (BRImo Campus Ambassador 2026)
Dibuat dengan Streamlit. Jalankan dengan: streamlit run app.py
"""

import time
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

import data as d

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Evaluasi Program MCB x BRImo",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# LOAD CSS
# ============================================================
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ============================================================
# COLOR CONSTANTS (Python side, untuk Plotly)
# ============================================================
NAVY = "#16327A"
BLUE = "#0B5FCC"
ORANGE = "#F58220"
GREEN = "#1E9E6B"
SLATE = "#5B6B8C"
SKY = "#EAF1FC"

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
SECTIONS = [
    ("🏠", "Beranda"),
    ("📋", "1. Summary Program"),
    ("🎯", "2. Objective Program"),
    ("📊", "3. Target & KPI"),
    ("🗺️", "4. Aktivitas Program"),
    ("💥", "5. Dampak Program"),
    ("💬", "6. Testimoni Peserta"),
    ("🧭", "7. SWOT & Lesson Learned"),
    ("✅", "Kesimpulan"),
]

with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
            <div style="font-size:2.2rem;">📱</div>
            <div style="font-weight:800; color:{NAVY}; font-size:1.05rem; line-height:1.3;">
                MCB x BRImo
            </div>
            <div style="color:{SLATE}; font-size:0.8rem;">Laporan Evaluasi Program</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    choice = st.radio(
        "Navigasi",
        options=[s[1] for s in SECTIONS],
        format_func=lambda x: f"{[s[0] for s in SECTIONS if s[1]==x][0]}  {x}",
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(
        f"""
        <div style="font-size:0.78rem; color:{SLATE}; line-height:1.6;">
            <b>{d.PROGRAM_INFO['penyelenggara']}</b><br>
            {d.PROGRAM_INFO['jabatan']}<br>
            {d.PROGRAM_INFO['kampus']}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# HELPER COMPONENTS
# ============================================================
def section_header(kicker, title, desc=None):
    html = f"""
    <div class="section-kicker">{kicker}</div>
    <div class="section-title">{title}</div>
    """
    if desc:
        html += f'<div class="section-desc">{desc}</div>'
    st.markdown(html, unsafe_allow_html=True)

def card(icon, title, desc, icon_bg="blue"):
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon-circle {icon_bg}">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-desc">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def animated_number(placeholder, target, suffix="", duration=0.6, prefix=""):
    """Animasi hitung naik untuk angka KPI."""
    steps = 20
    for i in range(steps + 1):
        val = int(target * (i / steps))
        placeholder.markdown(
            f'<div class="kpi-number" style="color:{BLUE};">{prefix}{val}{suffix}</div>',
            unsafe_allow_html=True,
        )
        time.sleep(duration / steps)

# ============================================================
# SECTION: BERANDA
# ============================================================
def render_beranda():
    st.markdown(
        f"""
        <div class="hero-wrap">
            <div class="hero-kicker">BRImo Campus Ambassador 2026</div>
            <div class="hero-title">Laporan Evaluasi Program<br>{d.PROGRAM_INFO['nama_program']}</div>
            <div class="hero-subtitle">{d.PROGRAM_INFO['nama_panjang']}</div>
            <div class="hero-meta">📅 <b>Periode:</b> {d.PROGRAM_INFO['periode']} ({d.PROGRAM_INFO['durasi']})</div>
            <div class="hero-meta">👤 <b>Disusun oleh:</b> {d.PROGRAM_INFO['penyelenggara']} — {d.PROGRAM_INFO['kampus']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### ✨ Sorotan Hasil Program")

    col1, col2, col3, col4 = st.columns(4)
    highlight_data = [
        (col1, "TARGET AWAL", d.KPI_TARGET, "nasabah baru", False),
        (col2, "REALISASI AKHIR", d.KPI_AKTUAL, "nasabah baru", True),
        (col3, "CAPAIAN", d.KPI_PERSEN, "% dari target", "green"),
        (col4, "BC RATIO", d.BC_RATIO, "manfaat ekonomi", "orange"),
    ]
    for col, label, val, sub, style in highlight_data:
        with col:
            if style is True:
                color = BLUE
                box_class = "white"
            elif style == "green":
                color = GREEN
                box_class = "dark"
            elif style == "orange":
                color = ORANGE
                box_class = "dark"
            else:
                color = "#9FB3D9"
                box_class = "dark"
            label_class = "dark-muted" if box_class == "white" else "muted"
            suffix = "%" if label == "CAPAIAN" else ("x" if label == "BC RATIO" else "")
            display_val = f"{val}{suffix}" if label != "BC RATIO" else val
            st.markdown(
                f"""
                <div class="kpi-box {box_class}">
                    <div class="kpi-label {label_class}">{label}</div>
                    <div class="kpi-number" style="color:{color};">{display_val}</div>
                    <div class="kpi-sub" style="color:{'#1B2A4D' if box_class=='white' else '#DCE8FB'};">{sub}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Gunakan menu navigasi di sidebar kiri untuk menjelajahi setiap bagian evaluasi secara detail.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 🗂️ Daftar Isi")
    cols = st.columns(4)
    toc_items = [
        ("📋", "Summary Program", "Gambaran umum & tujuan"),
        ("🎯", "Objective Program", "Business objective & target komunitas"),
        ("📊", "Target & KPI", "Target vs realisasi"),
        ("🗺️", "Aktivitas Program", "Timeline & dokumentasi"),
        ("💥", "Dampak Program", "Hasil & manfaat"),
        ("💬", "Testimoni Peserta", "Suara nasabah baru"),
        ("🧭", "SWOT Analysis", "Analisis & lesson learned"),
        ("✅", "Kesimpulan", "Rekomendasi tindak lanjut"),
    ]
    for i, (icon, title, desc) in enumerate(toc_items):
        with cols[i % 4]:
            card(icon, title, desc, icon_bg="navy" if i % 2 == 0 else "blue")
            st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SECTION 1: SUMMARY PROGRAM
# ============================================================
def render_summary():
    section_header("01 — Summary Program", "Apa itu Program MCB x BRImo?")

    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.markdown(
            f"""
            <p style="font-size:0.97rem; line-height:1.7; color:{NAVY};">
            <b>{d.PROGRAM_INFO['nama_program']}</b> ({d.PROGRAM_INFO['nama_panjang']}) adalah program akuisisi nasabah
            baru BRImo yang dijalankan secara mandiri oleh Campus Ambassador melalui jaringan kampus dan organisasi
            mahasiswa. Program ini menyasar mahasiswa aktif Universitas Kristen Petra dan anggota Resimen Mahasiswa
            (Menwa) Jawa Timur lintas kampus, dengan pendekatan <i>peer-to-peer</i> yang personal dan organik.
            </p>
            <p style="font-size:0.97rem; line-height:1.7; color:{NAVY};">
            Berbeda dari kampanye digital konvensional, program ini memanfaatkan figur tepercaya di lingkungan kampus
            (peer influencer) sebagai jembatan edukasi sekaligus fasilitator pendaftaran, sehingga proses akuisisi
            terasa lebih personal, cepat, dan terpercaya.
            </p>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        info_rows = [
            ("PERIODE PROGRAM", f"{d.PROGRAM_INFO['periode']} ({d.PROGRAM_INFO['durasi']})"),
            ("PENYELENGGARA", f"{d.PROGRAM_INFO['penyelenggara']}, {d.PROGRAM_INFO['jabatan']} - {d.PROGRAM_INFO['kampus']}"),
            ("CAKUPAN KOMUNITAS", d.PROGRAM_INFO['cakupan']),
            ("JALUR AKUISISI", "3 jalur paralel: Biro Kemahasiswaan, WA Menwa Jatim, Instagram Menwa Hits"),
        ]
        for label, val in info_rows:
            st.markdown(
                f"""
                <div class="card-sky" style="margin-bottom:0.7rem; padding:1rem 1.1rem;">
                    <div style="font-size:0.72rem; font-weight:700; color:{BLUE}; letter-spacing:1px;">{label}</div>
                    <div style="font-size:0.85rem; color:{NAVY}; margin-top:0.25rem;">{val}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Latar Belakang Program")
    cols = st.columns(3)
    for col, item in zip(cols, d.LATAR_BELAKANG):
        with col:
            card(item["icon"], item["judul"], item["desc"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="card-navy">
            <div style="color:{ORANGE}; font-weight:700; font-size:0.78rem; letter-spacing:1.5px; margin-bottom:0.7rem;">
                TUJUAN PROGRAM
            </div>
        """,
        unsafe_allow_html=True,
    )
    for t in d.TUJUAN_PROGRAM:
        st.markdown(
            f'<div style="color:white; font-size:0.92rem; margin-bottom:0.55rem;">✅&nbsp;&nbsp;{t}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# SECTION 2: OBJECTIVE PROGRAM
# ============================================================
def render_objective():
    section_header("02 — Objective Program", "Business Objective & Target Komunitas")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""<div class="card-sky" style="padding:1.5rem;">
            <div style="color:{BLUE}; font-weight:700; font-size:0.8rem; letter-spacing:1.5px; margin-bottom:1rem;">
                BUSINESS OBJECTIVE
            </div>""",
            unsafe_allow_html=True,
        )
        for i, obj in enumerate(d.BUSINESS_OBJECTIVES):
            st.markdown(
                f"""
                <div style="display:flex; gap:0.8rem; margin-bottom:1.1rem;">
                    <div style="font-weight:800; font-size:1.4rem; color:{ORANGE}; min-width:38px;">0{i+1}</div>
                    <div>
                        <div style="font-weight:700; color:{NAVY}; font-size:0.95rem;">{obj['judul']}</div>
                        <div style="color:{SLATE}; font-size:0.83rem; margin-top:0.15rem; line-height:1.45;">{obj['desc']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            f"""<div class="card-navy" style="padding:1.5rem;">
            <div style="color:{ORANGE}; font-weight:700; font-size:0.8rem; letter-spacing:1.5px; margin-bottom:1rem;">
                KOMUNITAS YANG DISASAR
            </div>""",
            unsafe_allow_html=True,
        )
        for komunitas in d.TARGET_KOMUNITAS:
            st.markdown(
                f"""
                <div style="display:flex; gap:0.8rem; margin-bottom:1.1rem;">
                    <div class="card-icon-circle blue" style="margin-bottom:0; min-width:46px;">{komunitas['icon']}</div>
                    <div>
                        <div style="font-weight:700; color:white; font-size:0.92rem;">{komunitas['judul']}</div>
                        <div style="color:#DCE8FB; font-size:0.82rem; margin-top:0.15rem; line-height:1.45;">{komunitas['desc']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# SECTION 3: TARGET & KPI
# ============================================================
def render_kpi():
    section_header(
        "03 — Target & Capaian KPI",
        "Realisasi Jauh Melampaui Target",
        "Perbandingan target awal program dengan hasil akhir yang dicapai dalam periode akuisisi.",
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""<div class="kpi-box dark">
                <div class="kpi-label muted">TARGET AWAL</div>
                <div class="kpi-number" style="color:#9FB3D9;">{d.KPI_TARGET}</div>
                <div class="kpi-sub" style="color:#DCE8FB;">nasabah baru</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""<div class="kpi-box white">
                <div class="kpi-label dark-muted">REALISASI AKHIR</div>
                <div class="kpi-number" style="color:{BLUE};">{d.KPI_AKTUAL}</div>
                <div class="kpi-sub" style="color:{NAVY};">nasabah baru</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""<div class="kpi-box dark">
                <div class="kpi-label muted">CAPAIAN</div>
                <div class="kpi-number" style="color:{GREEN};">{d.KPI_PERSEN}%</div>
                <div class="kpi-sub" style="color:#DCE8FB;">dari target</div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    sec_kpi = [
        (c1, f"{d.FIRST_TRANSACTION_RATE}%", "First Transaction Rate", "dari seluruh nasabah baru bertransaksi pertama kali"),
        (c2, f"{d.JENIS_ACTIVATION} Jenis", "Activation Type", "Welcome, Campus, Community & Referral activation"),
        (c3, f"{d.DURASI_HARI} Hari", "Durasi Pencapaian", "target tercapai 2x lipat dalam waktu yang sama"),
    ]
    for col, num, title, desc in sec_kpi:
        with col:
            st.markdown(
                f"""
                <div style="font-size:1.7rem; font-weight:800; color:{ORANGE};">{num}</div>
                <div style="font-weight:700; color:{NAVY}; font-size:0.9rem; margin-bottom:0.2rem;">{title}</div>
                <div style="color:{SLATE}; font-size:0.78rem;">{desc}</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("##### 📊 Kontribusi Capaian per Jalur Akuisisi")

    col_chart, col_table = st.columns([1.3, 1])
    with col_chart:
        df = pd.DataFrame(d.JALUR_AKUISISI)
        fig = go.Figure(
            go.Bar(
                x=df["nama"],
                y=df["hasil"],
                text=df["hasil"],
                textposition="outside",
                marker_color=BLUE,
                width=0.55,
            )
        )
        fig.update_layout(
            height=380,
            margin=dict(t=20, b=10, l=10, r=10),
            plot_bgcolor="white",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(gridcolor="#E5EAF5", title=None),
            xaxis=dict(title=None),
            font=dict(family="Source Sans Pro", color=NAVY, size=13),
            showlegend=False,
        )
        st.plotly_chart(fig, width='stretch')

    with col_table:
        rincian = [
            ("Target nasabah baru aktif", d.KPI_TARGET, d.KPI_AKTUAL, f"{d.KPI_PERSEN}%"),
            ("First transaction rate", "100%", "100%", "Tercapai"),
            ("Jenis activation digabung", 4, 4, "Tercapai"),
            ("Data nasabah terlengkapi", d.KPI_TARGET, d.KPI_AKTUAL, f"{d.KPI_PERSEN}%"),
        ]
        rows_html = ""
        for label, target, aktual, pct in rincian:
            rows_html += f"""
            <tr>
                <td style="padding:0.55rem 0; color:{NAVY}; font-size:0.85rem;">{label}</td>
                <td style="padding:0.55rem 0; color:{SLATE}; text-align:center; font-size:0.9rem;">{target}</td>
                <td style="padding:0.55rem 0; color:{BLUE}; text-align:center; font-weight:700; font-size:0.9rem;">{aktual}</td>
                <td style="padding:0.55rem 0; color:{GREEN}; text-align:center; font-weight:700; font-size:0.85rem;">{pct}</td>
            </tr>
            <tr><td colspan="4" style="border-bottom:1px solid #E2E8F5;"></td></tr>
            """
        st.markdown(
            f"""
            <div class="card-sky" style="padding:1.3rem;">
                <div style="color:{BLUE}; font-weight:700; font-size:0.78rem; letter-spacing:1px; margin-bottom:0.6rem;">
                    RINCIAN KPI
                </div>
                <table style="width:100%; border-collapse:collapse;">
                    <tr style="border-bottom:1px solid #C9D6F0;">
                        <th style="text-align:left; font-size:0.72rem; color:{SLATE}; padding-bottom:0.4rem;">Indikator</th>
                        <th style="font-size:0.72rem; color:{SLATE}; padding-bottom:0.4rem;">Target</th>
                        <th style="font-size:0.72rem; color:{SLATE}; padding-bottom:0.4rem;">Aktual</th>
                        <th style="font-size:0.72rem; color:{SLATE}; padding-bottom:0.4rem;">%</th>
                    </tr>
                    {rows_html}
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# SECTION 4: AKTIVITAS PROGRAM
# ============================================================
def render_aktivitas():
    section_header("04 — Aktivitas Program", "Timeline Aktivasi 7 Hari")

    cols = st.columns(7)
    for col, t in zip(cols, d.TIMELINE):
        with col:
            highlight = "highlight" if t["hari"] == "H5" else ""
            st.markdown(
                f"""
                <div class="timeline-card">
                    <div class="timeline-badge {highlight}">{t['hari']}</div>
                    <div class="timeline-title">{t['judul']}</div>
                    <div class="timeline-desc">{t['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        f'<p class="muted-note">📌 Catatan: skema referral di H5 menjadi titik balik akselerasi pendaftaran, '
        f'mendorong lonjakan nasabah baru di H6.</p>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 📈 Pertumbuhan Nasabah Kumulatif")
    df_growth = pd.DataFrame(d.TIMELINE)
    fig = go.Figure(
        go.Scatter(
            x=df_growth["hari"],
            y=df_growth["nasabah_kumulatif"],
            mode="lines+markers",
            line=dict(color=BLUE, width=3),
            marker=dict(size=9, color=ORANGE),
            fill="tozeroy",
            fillcolor="rgba(11,95,204,0.08)",
        )
    )
    fig.add_hline(y=d.KPI_TARGET, line_dash="dash", line_color=SLATE,
                   annotation_text="Target: 20", annotation_position="top left")
    fig.update_layout(
        height=320,
        margin=dict(t=20, b=10, l=10, r=10),
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(gridcolor="#E5EAF5", title="Jumlah Nasabah"),
        xaxis=dict(title=None),
        font=dict(family="Source Sans Pro", color=NAVY, size=13),
    )
    st.plotly_chart(fig, width='stretch')

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 🛤️ 3 Jalur Paralel Akuisisi Nasabah")
    cols = st.columns(3)
    for col, jalur in zip(cols, d.JALUR_AKUISISI):
        with col:
            steps_html = "".join(
                f'<div class="step-item"><span class="step-num">{i+1}</span><span>{s}</span></div>'
                for i, s in enumerate(jalur["steps"])
            )
            st.markdown(
                f"""
                <div class="card-navy" style="padding:1.3rem;">
                    <div class="card-icon-circle orange" style="margin-bottom:0.6rem;">{jalur['icon']}</div>
                    <div style="font-weight:700; color:white; font-size:1rem; margin-bottom:0.9rem;">{jalur['nama']}</div>
                    <div style="color:#DCE8FB;">{steps_html}</div>
                    <div style="margin-top:1rem; text-align:center; background:{BLUE}; border-radius:30px; padding:0.5rem; font-weight:700; color:white; font-size:0.9rem;">
                        Hasil: {jalur['hasil']} nasabah
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 📸 Dokumentasi Aktivitas Akuisisi")
    st.caption("Slot dokumentasi di bawah masih placeholder — ganti dengan screenshot/foto asli kamu.")
    cols = st.columns(4)
    for col, doc in zip(cols, d.DOKUMENTASI):
        with col:
            st.markdown(
                f"""
                <div class="doc-card">
                    <div class="doc-img-area" style="background:{doc['color']}1A;">
                        <div style="width:55px; height:55px; border-radius:50%; background:{doc['color']};
                                    display:flex; align-items:center; justify-content:center; font-size:1.6rem;">
                            {doc['icon']}
                        </div>
                    </div>
                    <div class="doc-placeholder-label">[ Placeholder dokumentasi ]</div>
                    <div class="doc-body">
                        <div class="doc-title">{doc['judul']}</div>
                        <div class="doc-desc">{doc['desc']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown(
        "<br><p class='muted-note'>💡 Tip: Ganti placeholder ini dengan upload gambar — lihat komentar "
        "<code>DOKUMENTASI</code> di file <code>data.py</code> dan tambahkan st.image() jika sudah ada file aslinya.</p>",
        unsafe_allow_html=True,
    )

# ============================================================
# SECTION 5: DAMPAK PROGRAM
# ============================================================
def render_dampak():
    section_header("05 — Dampak Program", "Dampak yang Dihasilkan Program")

    col1, col2 = st.columns([1, 1.6])
    with col1:
        st.markdown(
            f"""
            <div class="card-navy" style="padding:1.6rem; min-height:380px;">
                <div style="font-size:1.8rem;">⚖️</div>
                <div style="color:{ORANGE}; font-weight:700; font-size:0.8rem; letter-spacing:1.5px; margin:0.8rem 0 0.3rem 0;">
                    BC RATIO
                </div>
                <div style="font-size:3rem; font-weight:800; color:white;">{d.BC_RATIO}</div>
                <p style="color:#DCE8FB; font-size:0.88rem; line-height:1.6; margin-top:0.8rem;">
                    Setiap Rp1 biaya yang dikeluarkan menghasilkan Rp{d.BC_RATIO} manfaat ekonomi bagi BRI — program
                    dinilai sangat layak dan menguntungkan untuk dijalankan, dan dengan capaian {d.KPI_AKTUAL} nasabah,
                    efisiensi biaya akuisisi per kepala menjadi lebih baik dari proyeksi awal.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        rows = [d.DAMPAK_PROGRAM[i:i+2] for i in range(0, len(d.DAMPAK_PROGRAM), 2)]
        for row in rows:
            cols = st.columns(2)
            for col, item in zip(cols, row):
                with col:
                    card(item["icon"], item["judul"], item["desc"])
                    st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SECTION 6: TESTIMONI
# ============================================================
def render_testimoni():
    section_header(
        "06 — Testimoni Peserta",
        "Suara Langsung dari Nasabah Baru",
    )
    st.caption("*Testimoni di bawah merupakan ilustrasi gambaran umpan balik peserta — disarankan dilengkapi dengan kutipan asli sebelum dipublikasikan.")

    cols = st.columns(3)
    for col, t in zip(cols, d.TESTIMONI):
        with col:
            st.markdown(
                f"""
                <div class="testi-card">
                    <div class="testi-quote-mark">&ldquo;</div>
                    <div class="testi-text">{t['quote']}</div>
                    <div class="divider-line"></div>
                    <div class="testi-name">{t['nama']}</div>
                    <div class="testi-role">{t['peran']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ============================================================
# SECTION 7: SWOT
# ============================================================
def render_swot():
    section_header("07 — SWOT Analysis", "Analisis SWOT Program")

    quads = list(d.SWOT.items())
    for row_start in [0, 2]:
        cols = st.columns(2)
        for col, (title, data) in zip(cols, quads[row_start:row_start+2]):
            with col:
                items_html = "".join(f'<div class="swot-item" style="color:{NAVY};">{it}</div>' for it in data["items"])
                st.markdown(
                    f"""
                    <div class="swot-card" style="background:{data['color']}14;">
                        <div class="swot-header" style="color:{data['color']};">
                            <span>{data['icon']}</span><span>{title.upper()}</span>
                        </div>
                        {items_html}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    section_header("07 — Lesson Learned", "Pembelajaran untuk Tahap Selanjutnya")
    rows = [d.LESSON_LEARNED[i:i+2] for i in range(0, len(d.LESSON_LEARNED), 2)]
    for row in rows:
        cols = st.columns(2)
        for col, item in zip(cols, row):
            with col:
                card(item["icon"], item["judul"], item["desc"], icon_bg="navy")
                st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SECTION: KESIMPULAN
# ============================================================
def render_kesimpulan():
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown(
            f"""
            <div class="section-kicker">Kesimpulan & Rekomendasi</div>
            <div class="section-title">Program Terbukti Layak untuk Diskalakan</div>
            <p style="color:{SLATE}; font-size:0.97rem; line-height:1.7; margin-top:0.6rem;">
            Dengan capaian {d.KPI_AKTUAL} nasabah baru ({d.KPI_PERSEN}% dari target) dan BC Ratio {d.BC_RATIO},
            program {d.PROGRAM_INFO['nama_program']} membuktikan bahwa jaringan komunitas kampus berbasis kepercayaan
            adalah kanal akuisisi yang efektif dan efisien secara biaya.
            </p>
            """,
            unsafe_allow_html=True,
        )
        for r in d.REKOMENDASI:
            st.markdown(
                f'<div style="margin-bottom:0.6rem; font-size:0.92rem; color:{NAVY};">✅&nbsp;&nbsp;{r}</div>',
                unsafe_allow_html=True,
            )

    with col2:
        st.markdown(
            f"""
            <div class="contact-card">
                <div style="font-size:0.75rem; font-weight:700; color:{SLATE}; letter-spacing:1px;">CONTACT PERSON</div>
                <div style="font-size:1.15rem; font-weight:800; color:{NAVY}; margin-top:0.4rem;">{d.PROGRAM_INFO['penyelenggara']}</div>
                <div style="color:{SLATE}; font-size:0.85rem; margin-top:0.2rem;">{d.PROGRAM_INFO['jabatan']}<br>{d.PROGRAM_INFO['kampus']}</div>
                <div class="divider-line"></div>
                <div style="font-size:0.9rem; color:{NAVY};">📞 {d.PROGRAM_INFO['telp']}</div>
                <div style="font-size:0.9rem; color:{NAVY}; margin-top:0.4rem;">✉️ {d.PROGRAM_INFO['email']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='text-align:center; color:{ORANGE}; font-style:italic; font-size:1.1rem;'>Terima kasih. 🙏</p>",
        unsafe_allow_html=True,
    )

# ============================================================
# ROUTER
# ============================================================
ROUTES = {
    "Beranda": render_beranda,
    "1. Summary Program": render_summary,
    "2. Objective Program": render_objective,
    "3. Target & KPI": render_kpi,
    "4. Aktivitas Program": render_aktivitas,
    "5. Dampak Program": render_dampak,
    "6. Testimoni Peserta": render_testimoni,
    "7. SWOT & Lesson Learned": render_swot,
    "Kesimpulan": render_kesimpulan,
}

ROUTES[choice]()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align:center; color:{SLATE}; font-size:0.78rem;'>"
    f"Dibuat untuk Evaluasi Program BRImo Campus Ambassador 2026 — {d.PROGRAM_INFO['penyelenggara']}</p>",
    unsafe_allow_html=True,
)
