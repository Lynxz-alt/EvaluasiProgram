# Evaluasi Program MCB x BRImo

Website evaluasi program **MCB x BRImo (Mahasiswa Cerdas Bertransaksi x BRImo)** — BRImo Campus Ambassador 2026,
dibuat dengan [Streamlit](https://streamlit.io).

Desain mengikuti gaya **corporate, minimalis** dengan palet warna resmi identitas BRI hasil rebranding
(Nusantara Blue #0857C3, Cakrawala Blue #307FE2, Mentari Blue #71C5EB). Tidak menggunakan emoji; semua ikon
berupa SVG line-icon yang konsisten dengan gaya laporan korporat.

Halaman dirancang sebagai **satu halaman scroll panjang** (tanpa sidebar/tombol navigasi) — semua section
tampil berurutan saat di-scroll dari atas ke bawah, seperti laporan/landing page korporat. Kartu "Ikhtisar
Laporan" di Beranda berfungsi sebagai anchor link: klik salah satu langsung smooth-scroll ke section terkait.

Tema dipaksa selalu **light mode** (background putih) terlepas dari setting dark mode di browser/OS pengunjung,
supaya kontras warna selalu sesuai desain yang dimaksud.

## Fitur
- Single-page scroll dengan kartu Ikhtisar Laporan yang berfungsi sebagai anchor-link ke setiap section
- Ringkasan KPI: target vs realisasi (20 menjadi 40 nasabah, capaian 200%)
- Timeline aktivasi 7 hari (horizontal swipe-strip di mobile) dan grafik pertumbuhan nasabah kumulatif (Plotly)
- Breakdown kontribusi per jalur akuisisi
- Dokumentasi aktivitas (placeholder, siap diganti foto asli)
- Testimoni peserta
- Analisis SWOT dan lesson learned
- Kesimpulan dan rekomendasi tindak lanjut
- Responsif: layout, ukuran font, dan padding menyesuaikan di layar mobile (lihat media query di `style.css`)

## Menjalankan Secara Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

Lalu buka `http://localhost:8501` di browser.

## Mengedit Konten

Semua teks, angka, dan data ada di file **`data.py`** — edit file itu saja untuk mengganti:
- Info program (nama, periode, contact person)
- Angka KPI (target, aktual, BC ratio)
- Timeline dan jalur akuisisi
- Testimoni
- SWOT dan lesson learned

Tidak perlu menyentuh `app.py` kecuali ingin mengubah layout/desain.

## Mengganti Dokumentasi Placeholder dengan Foto Asli

1. Buat folder `assets/` lalu masukkan foto kamu (misal `assets/wa_broadcast.jpg`)
2. Di `app.py`, cari bagian `render_aktivitas()` pada blok dokumentasi
3. Ganti `<div class="doc-img-area">...</div>` dengan `st.image("assets/wa_broadcast.jpg")`

## Deploy Gratis ke Streamlit Community Cloud

1. Push folder ini ke repository GitHub kamu
2. Buka [share.streamlit.io](https://share.streamlit.io), login dengan GitHub
3. Klik **New app**, pilih repo ini, branch `main`, file utama `app.py`
4. Klik **Deploy** — website otomatis online dengan link publik

## Struktur File

```
.
├── app.py            # Logika, layout, ikon SVG, dan urutan section
├── data.py           # Semua konten/data (edit di sini)
├── style.css         # Styling tema corporate BRI + responsive + force light mode
├── requirements.txt  # Daftar dependency
└── README.md
```

---
Dibuat untuk evaluasi program BRImo Campus Ambassador 2026 — Felix Petra Sanjaya, Universitas Kristen Petra.
