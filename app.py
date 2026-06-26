# -*- coding: utf-8 -*-
"""
app.py — Website Evaluasi Program MCB x BRImo (BRImo Campus Ambassador 2026)
Desain: corporate, minimalis, palet warna resmi BRI (Nusantara/Cakrawala/Mentari Blue).
Jalankan dengan: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

import data as d

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Evaluasi Program MCB x BRImo",
    page_icon=None,
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
# COLOR CONSTANTS — Official BRI 2025 rebrand palette
# ============================================================
NUSANTARA = "#0857C3"   # primary
CAKRAWALA = "#307FE2"   # secondary
MENTARI = "#71C5EB"     # accent
INK = "#0B1E3D"
SLATE = "#5B6B85"
LINE = "#E3E8F0"
SURFACE = "#F7F9FC"

# ============================================================
# LINE-ICON LIBRARY (SVG, stroke-based, no emoji)
# ============================================================
ICONS = {
    "institution": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 10l9-6 9 6"/><path d="M5 10v9M19 10v9M9 10v9M15 10v9"/><path d="M3 19h18"/></svg>',
    "message": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 11.5a8.4 8.4 0 0 1-1.1 4.2L21 20l-4.3-1.1a8.5 8.5 0 1 1 4.3-7.4z"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 8h3l1.5-2h7L17 8h3a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3 2.7-5 6-5s6 2 6 5"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14c2 .3 3.7 1.8 3.7 3.6"/></svg>',
    "network": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="6" cy="6" r="2.3"/><circle cx="18" cy="6" r="2.3"/><circle cx="12" cy="18" r="2.3"/><path d="M7.8 7.5L11 16M16.2 7.5L13 16M8.3 6h7.4"/></svg>',
    "trend": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 17l5-5 4 4 8-9"/><path d="M15 7h5v5"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17.5v.1"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2l1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8z"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 6H4v2a3 3 0 0 0 3 3M17 6h3v2a3 3 0 0 1-3 3"/><path d="M10 16h4v3h-4z"/><path d="M8 21h8"/></svg>',
    "handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 12l4-4 4 3 2-2 4 4-3 3-3-2-2 2-4-2z"/><path d="M11 11l3 3M16 8l3 3-3 3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 3v6c0 4.5-3.4 7.5-8 9-4.6-1.5-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 3h9l3 3v15H6z"/><path d="M15 3v3h3"/><path d="M9 13h6M9 16.5h6M9 9.5h3"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="0.8" fill="currentColor"/></svg>',
    "balance": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3v18M5 7h14"/><path d="M5 7l-2.5 5a2.5 2.5 0 0 0 5 0zM19 7l-2.5 5a2.5 2.5 0 0 0 5 0z"/><path d="M8 21h8"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12l5 5L20 6"/></svg>',
}

def icon_svg(key, size=24):
    raw = ICONS.get(key, ICONS["doc"])
    return raw.replace("<svg ", f'<svg width="{size}" height="{size}" ')

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
SECTIONS = [
    "Beranda",
    "1. Summary Program",
    "2. Objective Program",
    "3. Target dan KPI",
    "4. Aktivitas Program",
    "5. Dampak Program",
    "6. Testimoni Peserta",
    "7. SWOT dan Lesson Learned",
    "Kesimpulan",
]

with st.sidebar:
    st.markdown(
        f"""
        <div style="padding: 0.3rem 0 1.1rem 0; border-bottom: 1px solid {LINE}; margin-bottom: 1.1rem;">
            <div style="font-weight:700; color:{INK}; font-size:1.0rem; line-height:1.35;">
                MCB x BRImo
            </div>
            <div style="color:{SLATE}; font-size:0.78rem; margin-top:0.2rem;">Laporan Evaluasi Program</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    choice = st.radio(
        "Navigasi",
        options=SECTIONS,
        label_visibility="collapsed",
    )
    st.markdown(f"<div style='height:1px;background:{LINE};margin:1.2rem 0;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="font-size:0.78rem; color:{SLATE}; line-height:1.7;">
            <div style="font-weight:600; color:{INK};">{d.PROGRAM_INFO['penyelenggara']}</div>
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
    <div class="kicker-rule"></div>
    """
    if desc:
        html += f'<div class="section-desc">{desc}</div>'
    st.markdown(html, unsafe_allow_html=True)

def card(icon_key, title, desc):
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">{icon_svg(icon_key)}</div>
            <div class="card-title">{title}</div>
            <div class="card-desc">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def card_dark(icon_key, title, desc):
    st.markdown(
        f"""
        <div class="card-dark">
            <div class="card-icon" style="color:{MENTARI};">{icon_svg(icon_key)}</div>
            <div class="card-title white">{title}</div>
            <div class="card-desc light">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
            <div class="hero-meta-row">
                <div>
                    <div class="hero-meta-label">Periode Program</div>
                    <div class="hero-meta-value">{d.PROGRAM_INFO['periode']}</div>
                </div>
                <div>
                    <div class="hero-meta-label">Disusun Oleh</div>
                    <div class="hero-meta-value">{d.PROGRAM_INFO['penyelenggara']}</div>
                </div>
                <div>
                    <div class="hero-meta-label">Institusi</div>
                    <div class="hero-meta-value">{d.PROGRAM_INFO['kampus']}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:0.8rem;'>Sorotan Hasil Program</p>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f"""<div class="kpi-box">
                <div class="kpi-label">Target Awal</div>
                <div class="kpi-number">{d.KPI_TARGET}</div>
                <div class="kpi-sub">nasabah baru</div>
            </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(
            f"""<div class="kpi-box emphasis">
                <div class="kpi-label on-dark">Realisasi Akhir</div>
                <div class="kpi-number on-dark">{d.KPI_AKTUAL}</div>
                <div class="kpi-sub on-dark">nasabah baru</div>
            </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(
            f"""<div class="kpi-box">
                <div class="kpi-label">Capaian</div>
                <div class="kpi-number accent">{d.KPI_PERSEN}%</div>
                <div class="kpi-sub">dari target</div>
            </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(
            f"""<div class="kpi-box">
                <div class="kpi-label">BC Ratio</div>
                <div class="kpi-number accent">{d.BC_RATIO}</div>
                <div class="kpi-sub">manfaat ekonomi</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Gunakan menu navigasi di sidebar kiri untuk menjelajahi setiap bagian evaluasi secara detail.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:1rem;'>Daftar Isi</p>", unsafe_allow_html=True)
    toc_items = [
        ("doc", "Summary Program", "Gambaran umum dan tujuan"),
        ("target", "Objective Program", "Business objective dan target komunitas"),
        ("trend", "Target dan KPI", "Target vs realisasi"),
        ("network", "Aktivitas Program", "Timeline dan dokumentasi"),
        ("trophy", "Dampak Program", "Hasil dan manfaat"),
        ("message", "Testimoni Peserta", "Suara nasabah baru"),
        ("balance", "SWOT Analysis", "Analisis dan lesson learned"),
        ("check", "Kesimpulan", "Rekomendasi tindak lanjut"),
    ]
    cols = st.columns(4)
    for i, (icon, title, desc) in enumerate(toc_items):
        with cols[i % 4]:
            card(icon, title, desc)
            st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SECTION 1: SUMMARY PROGRAM
# ============================================================
def render_summary():
    section_header("01 — Summary Program", "Apa itu Program MCB x BRImo")

    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.markdown(
            f"""
            <p style="font-size:0.96rem; line-height:1.75; color:{INK};">
            <b>{d.PROGRAM_INFO['nama_program']}</b> ({d.PROGRAM_INFO['nama_panjang']}) adalah program akuisisi nasabah
            baru BRImo yang dijalankan secara mandiri oleh Campus Ambassador melalui jaringan kampus dan organisasi
            mahasiswa. Program ini menyasar mahasiswa aktif Universitas Kristen Petra dan anggota Resimen Mahasiswa
            (Menwa) Jawa Timur lintas kampus, dengan pendekatan peer-to-peer yang personal dan organik.
            </p>
            <p style="font-size:0.96rem; line-height:1.75; color:{INK};">
            Berbeda dari kampanye digital konvensional, program ini memanfaatkan figur tepercaya di lingkungan kampus
            sebagai jembatan edukasi sekaligus fasilitator pendaftaran, sehingga proses akuisisi terasa lebih
            personal, cepat, dan terpercaya.
            </p>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        info_rows = [
            ("Periode Program", f"{d.PROGRAM_INFO['periode']} ({d.PROGRAM_INFO['durasi']})"),
            ("Penyelenggara", f"{d.PROGRAM_INFO['penyelenggara']}, {d.PROGRAM_INFO['jabatan']} - {d.PROGRAM_INFO['kampus']}"),
            ("Cakupan Komunitas", d.PROGRAM_INFO['cakupan']),
            ("Jalur Akuisisi", "3 jalur paralel: Biro Kemahasiswaan, WA Menwa Jatim, Instagram Menwa Hits"),
        ]
        rows_html = "".join(
            f'<div class="info-row"><div class="info-label">{label}</div><div class="info-value">{val}</div></div>'
            for label, val in info_rows
        )
        st.markdown(f'<div class="card">{rows_html}</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:1rem;'>Latar Belakang Program</p>", unsafe_allow_html=True)
    cols = st.columns(3)
    for col, item in zip(cols, d.LATAR_BELAKANG):
        with col:
            card(item["icon"], item["judul"], item["desc"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="card-dark">
            <div style="color:{MENTARI}; font-weight:600; font-size:0.75rem; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:1rem;">
                Tujuan Program
            </div>
        """,
        unsafe_allow_html=True,
    )
    for t in d.TUJUAN_PROGRAM:
        st.markdown(
            f'<div class="check-item" style="color:white;"><span class="check-mark">{icon_svg("check", 14)}</span><span>{t}</span></div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# SECTION 2: OBJECTIVE PROGRAM
# ============================================================
def render_objective():
    section_header("02 — Objective Program", "Business Objective dan Target Komunitas")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""<div class="card-flat" style="padding:1.6rem;">
            <div style="color:{NUSANTARA}; font-weight:600; font-size:0.78rem; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:1.2rem;">
                Business Objective
            </div>""",
            unsafe_allow_html=True,
        )
        for i, obj in enumerate(d.BUSINESS_OBJECTIVES):
            st.markdown(
                f"""
                <div class="numbered-item">
                    <div class="numbered-index">0{i+1}</div>
                    <div>
                        <div style="font-weight:700; color:{INK}; font-size:0.92rem;">{obj['judul']}</div>
                        <div style="color:{SLATE}; font-size:0.82rem; margin-top:0.2rem; line-height:1.5;">{obj['desc']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            f"""<div class="card-dark" style="padding:1.6rem;">
            <div style="color:{MENTARI}; font-weight:600; font-size:0.78rem; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:1.2rem;">
                Komunitas yang Disasar
            </div>""",
            unsafe_allow_html=True,
        )
        for komunitas in d.TARGET_KOMUNITAS:
            st.markdown(
                f"""
                <div style="display:flex; gap:0.9rem; margin-bottom:1.3rem;">
                    <div style="min-width:30px; color:{MENTARI};">{icon_svg(komunitas['icon'], 26)}</div>
                    <div>
                        <div style="font-weight:700; color:white; font-size:0.9rem;">{komunitas['judul']}</div>
                        <div style="color:#C9D9F0; font-size:0.8rem; margin-top:0.2rem; line-height:1.5;">{komunitas['desc']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# SECTION 3: TARGET DAN KPI
# ============================================================
def render_kpi():
    section_header(
        "03 — Target dan Capaian KPI",
        "Realisasi Melampaui Target",
        "Perbandingan target awal program dengan hasil akhir yang dicapai dalam periode akuisisi.",
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""<div class="kpi-box">
                <div class="kpi-label">Target Awal</div>
                <div class="kpi-number">{d.KPI_TARGET}</div>
                <div class="kpi-sub">nasabah baru</div>
            </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(
            f"""<div class="kpi-box emphasis">
                <div class="kpi-label on-dark">Realisasi Akhir</div>
                <div class="kpi-number on-dark">{d.KPI_AKTUAL}</div>
                <div class="kpi-sub on-dark">nasabah baru</div>
            </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(
            f"""<div class="kpi-box">
                <div class="kpi-label">Capaian</div>
                <div class="kpi-number accent">{d.KPI_PERSEN}%</div>
                <div class="kpi-sub">dari target</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    sec_kpi = [
        (c1, f"{d.FIRST_TRANSACTION_RATE}%", "First Transaction Rate", "dari seluruh nasabah baru bertransaksi pertama kali"),
        (c2, f"{d.JENIS_ACTIVATION} Jenis", "Activation Type", "Welcome, Campus, Community, dan Referral activation"),
        (c3, f"{d.DURASI_HARI} Hari", "Durasi Pencapaian", "target tercapai 2x lipat dalam waktu yang sama"),
    ]
    for col, num, title, desc in sec_kpi:
        with col:
            st.markdown(
                f"""
                <div style="border-left:2px solid {LINE}; padding-left:1rem;">
                    <div style="font-size:1.55rem; font-weight:700; color:{NUSANTARA};">{num}</div>
                    <div style="font-weight:700; color:{INK}; font-size:0.88rem; margin:0.2rem 0 0.3rem 0;">{title}</div>
                    <div style="color:{SLATE}; font-size:0.78rem; line-height:1.4;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:1rem;'>Kontribusi Capaian per Jalur Akuisisi</p>", unsafe_allow_html=True)

    col_chart, col_table = st.columns([1.3, 1])
    with col_chart:
        df = pd.DataFrame(d.JALUR_AKUISISI)
        fig = go.Figure(
            go.Bar(
                x=df["nama"],
                y=df["hasil"],
                text=df["hasil"],
                textposition="outside",
                marker_color=NUSANTARA,
                width=0.5,
            )
        )
        fig.update_layout(
            height=380,
            margin=dict(t=20, b=10, l=10, r=10),
            plot_bgcolor="white",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(gridcolor=LINE, title=None),
            xaxis=dict(title=None),
            font=dict(family="Source Sans Pro", color=INK, size=12.5),
            showlegend=False,
        )
        st.plotly_chart(fig, width="stretch")

    with col_table:
        rincian = [
            ("Target nasabah baru aktif", d.KPI_TARGET, d.KPI_AKTUAL, f"{d.KPI_PERSEN}%"),
            ("First transaction rate", "100%", "100%", "Tercapai"),
            ("Jenis activation digabung", 4, 4, "Tercapai"),
            ("Data nasabah terlengkapi", d.KPI_TARGET, d.KPI_AKTUAL, f"{d.KPI_PERSEN}%"),
        ]
        rows_html = "".join(
            f"<tr><td>{label}</td><td style='text-align:center;color:{SLATE};'>{target}</td>"
            f"<td style='text-align:center;font-weight:700;color:{NUSANTARA};'>{aktual}</td>"
            f"<td style='text-align:center;font-weight:700;color:{INK};'>{pct}</td></tr>"
            for label, target, aktual, pct in rincian
        )
        st.markdown(
            f"""
            <div class="card-flat" style="padding:1.5rem;">
                <table class="kpi-table">
                    <tr><th>Indikator</th><th style="text-align:center;">Target</th><th style="text-align:center;">Aktual</th><th style="text-align:center;">Hasil</th></tr>
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
            key_class = "is-key" if t["hari"] == "H5" else ""
            st.markdown(
                f"""
                <div class="timeline-card {key_class}">
                    <div class="timeline-day">{t['hari']}</div>
                    <div class="timeline-title">{t['judul']}</div>
                    <div class="timeline-desc">{t['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        f'<p class="muted-note">Catatan: skema referral di H5 menjadi titik balik akselerasi pendaftaran, '
        f'mendorong lonjakan nasabah baru di H6.</p>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:1rem;'>Pertumbuhan Nasabah Kumulatif</p>", unsafe_allow_html=True)
    df_growth = pd.DataFrame(d.TIMELINE)
    fig = go.Figure(
        go.Scatter(
            x=df_growth["hari"],
            y=df_growth["nasabah_kumulatif"],
            mode="lines+markers",
            line=dict(color=NUSANTARA, width=2.5),
            marker=dict(size=7, color=NUSANTARA),
            fill="tozeroy",
            fillcolor="rgba(8,87,195,0.06)",
        )
    )
    fig.add_hline(y=d.KPI_TARGET, line_dash="dash", line_color=SLATE,
                   annotation_text="Target: 20", annotation_position="top left")
    fig.update_layout(
        height=300,
        margin=dict(t=20, b=10, l=10, r=10),
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(gridcolor=LINE, title="Jumlah Nasabah"),
        xaxis=dict(title=None),
        font=dict(family="Source Sans Pro", color=INK, size=12.5),
    )
    st.plotly_chart(fig, width="stretch")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:1rem;'>Tiga Jalur Paralel Akuisisi Nasabah</p>", unsafe_allow_html=True)
    cols = st.columns(3)
    for col, jalur in zip(cols, d.JALUR_AKUISISI):
        with col:
            steps_html = "".join(
                f'<div class="step-item"><span class="step-num">{i+1}</span><span>{s}</span></div>'
                for i, s in enumerate(jalur["steps"])
            )
            st.markdown(
                f"""
                <div class="card-dark" style="padding:1.5rem;">
                    <div style="color:{MENTARI}; margin-bottom:0.7rem;">{icon_svg(jalur['icon'], 28)}</div>
                    <div style="font-weight:700; color:white; font-size:0.98rem; margin-bottom:1.1rem;">{jalur['nama']}</div>
                    <div style="color:#C9D9F0;">{steps_html}</div>
                    <div style="margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(255,255,255,0.15);">
                        <span style="font-weight:700; color:{MENTARI}; font-size:1.3rem;">{jalur['hasil']}</span>
                        <span style="color:#C9D9F0; font-size:0.82rem;"> nasabah</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{SLATE}; font-size:0.8rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:0.3rem;'>Dokumentasi Aktivitas Akuisisi</p>", unsafe_allow_html=True)
    st.caption("Slot dokumentasi di bawah masih placeholder. Ganti dengan tangkapan layar atau foto asli sebelum presentasi final.")
    cols = st.columns(4)
    for col, doc in zip(cols, d.DOKUMENTASI):
        with col:
            st.markdown(
                f"""
                <div class="doc-card">
                    <div class="doc-img-area">{icon_svg(doc['icon'], 30)}</div>
                    <div class="doc-placeholder-label">Placeholder dokumentasi</div>
                    <div class="doc-body">
                        <div class="doc-title">{doc['judul']}</div>
                        <div class="doc-desc">{doc['desc']}</div>
                    </div>
                </div>
                """,
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
            <div class="card-dark" style="padding:1.8rem; min-height:380px;">
                <div style="color:{MENTARI}; margin-bottom:0.8rem;">{icon_svg('balance', 32)}</div>
                <div style="color:{MENTARI}; font-weight:600; font-size:0.75rem; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:0.4rem;">
                    BC Ratio
                </div>
                <div style="font-size:2.8rem; font-weight:700; color:white;">{d.BC_RATIO}</div>
                <p style="color:#C9D9F0; font-size:0.86rem; line-height:1.65; margin-top:1rem;">
                    Setiap Rp1 biaya yang dikeluarkan menghasilkan Rp{d.BC_RATIO} manfaat ekonomi bagi BRI. Program
                    dinilai layak dan menguntungkan untuk dijalankan, dan dengan capaian {d.KPI_AKTUAL} nasabah,
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
    section_header("06 — Testimoni Peserta", "Suara Langsung dari Nasabah Baru")
    st.caption("Testimoni di bawah merupakan ilustrasi gambaran umpan balik peserta. Disarankan dilengkapi dengan kutipan asli sebelum dipublikasikan.")

    cols = st.columns(3)
    for col, t in zip(cols, d.TESTIMONI):
        with col:
            st.markdown(
                f"""
                <div class="testi-card">
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

    swot_colors = {"Strength": NUSANTARA, "Weakness": "#B07A1E", "Opportunity": "#1E7A4D", "Threat": "#B0392B"}
    quads = list(d.SWOT.items())
    for row_start in [0, 2]:
        cols = st.columns(2)
        for col, (title, data) in zip(cols, quads[row_start:row_start+2]):
            with col:
                color = swot_colors.get(title, NUSANTARA)
                items_html = "".join(f'<div class="swot-item">{it}</div>' for it in data["items"])
                st.markdown(
                    f"""
                    <div class="swot-card" style="--swot-color:{color};">
                        <div class="swot-header" style="color:{color};">{title}</div>
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
                card(item["icon"], item["judul"], item["desc"])
                st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SECTION: KESIMPULAN
# ============================================================
def render_kesimpulan():
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown(
            f"""
            <div class="section-kicker">Kesimpulan dan Rekomendasi</div>
            <div class="section-title">Program Terbukti Layak untuk Diskalakan</div>
            <div class="kicker-rule"></div>
            <p style="color:{SLATE}; font-size:0.95rem; line-height:1.75; margin-top:0.6rem; margin-bottom:1.3rem;">
            Dengan capaian {d.KPI_AKTUAL} nasabah baru ({d.KPI_PERSEN}% dari target) dan BC Ratio {d.BC_RATIO},
            program {d.PROGRAM_INFO['nama_program']} membuktikan bahwa jaringan komunitas kampus berbasis kepercayaan
            adalah kanal akuisisi yang efektif dan efisien secara biaya.
            </p>
            """,
            unsafe_allow_html=True,
        )
        for r in d.REKOMENDASI:
            st.markdown(
                f'<div class="check-item"><span class="check-mark">{icon_svg("check", 14)}</span><span style="color:{INK};">{r}</span></div>',
                unsafe_allow_html=True,
            )

    with col2:
        st.markdown(
            f"""
            <div class="contact-card">
                <div style="font-size:0.72rem; font-weight:600; color:{SLATE}; letter-spacing:1px; text-transform:uppercase;">Contact Person</div>
                <div style="font-size:1.1rem; font-weight:700; color:{INK}; margin-top:0.5rem;">{d.PROGRAM_INFO['penyelenggara']}</div>
                <div style="color:{SLATE}; font-size:0.83rem; margin-top:0.2rem; line-height:1.5;">{d.PROGRAM_INFO['jabatan']}<br>{d.PROGRAM_INFO['kampus']}</div>
                <div class="divider-line"></div>
                <div style="font-size:0.88rem; color:{INK}; margin-bottom:0.5rem;">{d.PROGRAM_INFO['telp']}</div>
                <div style="font-size:0.88rem; color:{INK};">{d.PROGRAM_INFO['email']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='text-align:center; color:{SLATE}; font-size:0.88rem;'>Terima kasih.</p>",
        unsafe_allow_html=True,
    )

# ============================================================
# ROUTER
# ============================================================
ROUTES = {
    "Beranda": render_beranda,
    "1. Summary Program": render_summary,
    "2. Objective Program": render_objective,
    "3. Target dan KPI": render_kpi,
    "4. Aktivitas Program": render_aktivitas,
    "5. Dampak Program": render_dampak,
    "6. Testimoni Peserta": render_testimoni,
    "7. SWOT dan Lesson Learned": render_swot,
    "Kesimpulan": render_kesimpulan,
}

ROUTES[choice]()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    f"<div style='border-top:1px solid {LINE}; padding-top:1.2rem;'>"
    f"<p style='text-align:center; color:{SLATE}; font-size:0.76rem;'>"
    f"Dibuat untuk Evaluasi Program BRImo Campus Ambassador 2026 — {d.PROGRAM_INFO['penyelenggara']}</p></div>",
    unsafe_allow_html=True,
)
