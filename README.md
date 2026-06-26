# 📱 Evaluasi Program MCB x BRImo

Website evaluasi program **MCB x BRImo (Mahasiswa Cerdas Bertransaksi x BRImo)** — BRImo Campus Ambassador 2026,
dibuat dengan [Streamlit](https://streamlit.io).

## ✨ Fitur
- Ringkasan KPI: target vs realisasi (20 → 40 nasabah, capaian 200%)
- Timeline aktivasi 7 hari & grafik pertumbuhan nasabah kumulatif (interaktif, Plotly)
- Breakdown kontribusi per jalur akuisisi
- Dokumentasi aktivitas (placeholder, siap diganti foto asli)
- Testimoni peserta
- Analisis SWOT & lesson learned
- Kesimpulan & rekomendasi tindak lanjut

## 🛠️ Menjalankan Secara Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

Lalu buka `http://localhost:8501` di browser.

## ✏️ Mengedit Konten

Semua teks, angka, dan data ada di file **`data.py`** — edit file itu saja untuk mengganti:
- Info program (nama, periode, contact person)
- Angka KPI (target, aktual, BC ratio)
- Timeline & jalur akuisisi
- Testimoni
- SWOT & lesson learned

Tidak perlu menyentuh `app.py` kecuali ingin mengubah layout/desain.

## 🖼️ Mengganti Dokumentasi Placeholder dengan Foto Asli

1. Buat folder `assets/` lalu masukkan foto kamu (misal `assets/wa_broadcast.jpg`)
2. Di `app.py`, cari bagian `render_aktivitas()` pada blok dokumentasi
3. Ganti `<div class="doc-img-area">...</div>` dengan `st.image("assets/wa_broadcast.jpg")`

## 🚀 Deploy Gratis ke Streamlit Community Cloud

1. Push folder ini ke repository GitHub kamu
2. Buka [share.streamlit.io](https://share.streamlit.io), login dengan GitHub
3. Klik **New app**, pilih repo ini, branch `main`, file utama `app.py`
4. Klik **Deploy** — website otomatis online dengan link publik

## 📂 Struktur File

```
.
├── app.py            # Logika & layout halaman
├── data.py           # Semua konten/data (edit di sini)
├── style.css         # Styling tampilan
├── requirements.txt  # Daftar dependency
└── README.md
```

---
Dibuat untuk evaluasi program BRImo Campus Ambassador 2026 — Felix Petra Sanjaya, Universitas Kristen Petra.
