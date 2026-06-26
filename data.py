# -*- coding: utf-8 -*-
"""
data.py — Semua data evaluasi program MCB x BRImo.
Edit file ini untuk mengganti angka, teks, atau testimoni tanpa menyentuh app.py
Catatan: field "icon" berisi key yang dipetakan ke SVG line-icon di app.py (lihat ICONS dict),
bukan emoji — sesuai arahan desain corporate/minimalis.
"""

# ============== INFO PROGRAM ==============
PROGRAM_INFO = {
    "nama_program": "MCB x BRImo",
    "nama_panjang": "Mahasiswa Cerdas Bertransaksi x BRImo",
}

# ============== KPI UTAMA ==============
KPI_TARGET = 20
KPI_AKTUAL = 40
KPI_PERSEN = round(KPI_AKTUAL / KPI_TARGET * 100)
BC_RATIO = 4.45
FIRST_TRANSACTION_RATE = 100
JENIS_ACTIVATION = 4
DURASI_HARI = 7

# ============== KONTRIBUSI PER JALUR ==============
JALUR_AKUISISI = [
    {"nama": "Biro Kemahasiswaan Petra", "hasil": 14, "icon": "institution",
     "deskripsi": "Approach resmi ke Biro Kemahasiswaan Petra untuk distribusi info program ke seluruh mahasiswa.",
     "steps": [
         "Felix approach Biro Kemahasiswaan Petra",
         "Biro blast info program ke mahasiswa Petra",
         "Mahasiswa tertarik dan chat langsung ke Felix",
         "Dibantu proses pendaftaran BRImo",
     ]},
    {"nama": "WA Menwa Jatim", "hasil": 19, "icon": "message",
     "deskripsi": "Broadcast dan follow-up personal ke jaringan WhatsApp anggota Menwa lintas kampus Jawa Timur.",
     "steps": [
         "Felix broadcast dan personal WA ke anggota Menwa",
         "Target tertarik dan daftar mandiri",
         "Felix standby membantu proses via WA",
         "Follow up intensif ke seluruh prospek",
     ]},
    {"nama": "Instagram Menwa Hits", "hasil": 7, "icon": "camera",
     "deskripsi": "Konten edukasi dan promosi program melalui akun Instagram komunitas Menwa Hits.",
     "steps": [
         "Felix approach admin Instagram Menwa Hits",
         "Posting program MCB x BRImo di akun resmi",
         "Followers DM Felix untuk info lebih lanjut",
         "Pendaftaran dibantu secara remote",
     ]},
]

# ============== TIMELINE 7 HARI ==============
TIMELINE = [
    {"hari": "H1", "judul": "Persiapan dan Approach", "desc": "Persiapan dan approach Biro Kemahasiswaan Petra untuk mendapat dukungan resmi kampus.", "nasabah_kumulatif": 0},
    {"hari": "H2", "judul": "Aktivasi Digital", "desc": "Aktivasi grup WA Menwa Jatim dan posting program di Instagram Menwa Hits.", "nasabah_kumulatif": 4},
    {"hari": "H3", "judul": "Blast Informasi", "desc": "Blast informasi program ke seluruh mahasiswa Petra melalui Biro Kemahasiswaan.", "nasabah_kumulatif": 10},
    {"hari": "H4", "judul": "Follow Up Personal", "desc": "Follow up personal ke anggota Menwa yang menunjukkan minat melalui WhatsApp.", "nasabah_kumulatif": 17},
    {"hari": "H5", "judul": "Skema Referral", "desc": "Mendorong skema referral, nasabah baru mengajak teman untuk ikut mendaftar.", "nasabah_kumulatif": 24},
    {"hari": "H6", "judul": "Follow Up Masif", "desc": "Follow up masif ke seluruh prospek yang belum menyelesaikan pendaftaran.", "nasabah_kumulatif": 34},
    {"hari": "H7", "judul": "Rekapitulasi", "desc": "Rekapitulasi data nasabah dan penyusunan laporan evaluasi program.", "nasabah_kumulatif": 40},
]

# ============== OBJECTIVE ==============
BUSINESS_OBJECTIVES = [
    {"judul": "Akuisisi Nasabah Baru", "desc": "Menambah jumlah nasabah aktif BRImo baru dari segmen mahasiswa secara terukur dalam waktu singkat (7 hari)."},
    {"judul": "Aktivasi dan First Transaction", "desc": "Memastikan nasabah baru tidak hanya mendaftar, tetapi benar-benar melakukan transaksi pertama di BRImo."},
    {"judul": "Channel Akuisisi Baru", "desc": "Membuka dan membuktikan efektivitas jaringan Menwa Jatim sebagai kanal akuisisi non-konvensional."},
    {"judul": "Brand Awareness Kampus", "desc": "Memperkenalkan BRImo sebagai solusi transaksi utama mahasiswa lintas kampus Jawa Timur."},
]

TARGET_KOMUNITAS = [
    {"judul": "Mahasiswa Universitas Kristen Petra", "icon": "institution", "desc": "Basis utama dengan dukungan resmi pihak kampus, responsif terhadap program institusional."},
    {"judul": "Anggota Menwa Jatim Lintas Kampus", "icon": "users", "desc": "Struktur organisasi hierarkis dan kepercayaan internal tinggi, keputusan dipengaruhi senioritas."},
    {"judul": "Mahasiswa Umum di Kampus Ber-Menwa", "icon": "network", "desc": "Jangkauan sekunder melalui efek jejaring sosial dari anggota Menwa di kampus masing-masing."},
]

# ============== LATAR BELAKANG ==============
LATAR_BELAKANG = [
    {"judul": "Kondisi Digital Banking", "icon": "trend", "desc": "Penetrasi mobile banking terus meningkat, namun segmen mahasiswa di kampus belum tergarap optimal."},
    {"judul": "Tantangan Akuisisi BRImo", "icon": "alert", "desc": "BRImo belum jadi pilihan utama mahasiswa karena minimnya edukasi personal dari figur tepercaya di kampus."},
    {"judul": "Peluang Belum Dimanfaatkan", "icon": "spark", "desc": "Menwa Jatim punya ribuan anggota aktif lintas kampus dengan struktur hierarkis kuat, channel akuisisi yang belum tersentuh."},
]

TUJUAN_PROGRAM = [
    "Membuka channel akuisisi baru melalui jaringan terpusat Menwa Jatim",
    "Membangun brand awareness BRImo secara masif di lintas kampus Jawa Timur",
    "Menciptakan referral chain organik yang berkelanjutan di kalangan mahasiswa",
    "Meletakkan fondasi operasional untuk scaling ke seluruh Menwa Jatim dan nasional",
]

# ============== DAMPAK PROGRAM ==============
DAMPAK_PROGRAM = [
    {"judul": "Akuisisi 2x Lipat Target", "icon": "trophy", "desc": "40 nasabah baru BRImo aktif tercapai, 2x dari target awal 20 nasabah dalam periode yang sama."},
    {"judul": "Engagement Aktif Menwa", "icon": "trend", "desc": "Jaringan Menwa Jatim terbukti menjadi kanal akuisisi baru yang responsif dan dapat direplikasi."},
    {"judul": "Dukungan Resmi Kampus", "icon": "handshake", "desc": "Biro Kemahasiswaan Petra turut mendukung distribusi informasi program ke mahasiswa."},
    {"judul": "Referral Chain Terbentuk", "icon": "network", "desc": "Sejumlah nasabah baru mengajak rekan sejawat, menandai awal pertumbuhan organik."},
]

# ============== DOKUMENTASI (placeholder) ==============
DOKUMENTASI = [
    {"judul": "Broadcast WA Menwa Jatim", "icon": "message",
     "desc": "Pesan ajakan dan panduan pendaftaran ke grup Menwa lintas kampus."},
    {"judul": "Story dan Feed Instagram", "icon": "camera",
     "desc": "Konten edukasi program di Instagram pribadi Felix dan Menwa Hits."},
    {"judul": "Approach Biro Kemahasiswaan", "icon": "institution",
     "desc": "Koordinasi langsung dengan Biro Kemahasiswaan Petra untuk dukungan resmi."},
    {"judul": "Sesi Pendampingan Pendaftaran", "icon": "users",
     "desc": "Felix mendampingi proses pendaftaran BRImo nasabah baru secara langsung."},
]

# ============== TESTIMONI ==============
TESTIMONI = [
    {"quote": "Prosesnya gampang banget, tinggal chat Felix terus dibantu sampai selesai. Sekarang transfer iuran organisasi jadi lebih praktis.",
     "nama": "R. Andika", "peran": "Anggota Menwa Jatim"},
    {"quote": "Awalnya cuma ikut-ikutan temen, tapi pas dicoba ternyata BRImo memang lebih lengkap buat kebutuhan harian mahasiswa.",
     "nama": "S. Wulandari", "peran": "Mahasiswa Universitas Kristen Petra"},
    {"quote": "Seneng ada yang bantu daftar langsung, jadi nggak perlu antre ke bank. Reward cashback-nya juga lumayan buat anak kos.",
     "nama": "M. Firmansyah", "peran": "Anggota Menwa Jatim"},
]

# ============== SWOT ==============
SWOT = {
    "Strength": {
        "items": [
            "Jaringan Menwa Jatim solid dan hierarkis, mempercepat penyebaran info",
            "Pendekatan peer-to-peer personal meningkatkan trust calon nasabah",
            "Dukungan resmi Biro Kemahasiswaan Petra memperkuat kredibilitas",
        ],
    },
    "Weakness": {
        "items": [
            "Sangat bergantung pada satu Campus Ambassador (Felix) sebagai PIC tunggal",
            "Kapasitas follow up manual terbatas saat volume prospek meningkat tajam",
            "Belum ada sistem tracking otomatis untuk progres pendaftaran",
        ],
    },
    "Opportunity": {
        "items": [
            "Potensi scaling ke seluruh satuan Menwa Jatim (50 kampus) dan nasional",
            "Skema BRImo Officer berinsentif dapat mereplikasi model ini secara luas",
            "Referral chain organik berpotensi tumbuh tanpa biaya akuisisi tambahan",
        ],
    },
    "Threat": {
        "items": [
            "Ketergantungan pada relasi personal berisiko jika Campus Ambassador berganti",
            "Kompetitor e-wallet/bank lain dapat mereplikasi strategi serupa di kampus",
            "Minat mahasiswa terhadap reward dapat menurun jika tidak diperbarui",
        ],
    },
}

LESSON_LEARNED = [
    {"judul": "Peer Trust adalah Kunci", "icon": "spark",
     "desc": "Pendekatan personal dari figur tepercaya (senior Menwa, Campus Ambassador) jauh lebih efektif dibanding iklan digital konvensional untuk segmen mahasiswa."},
    {"judul": "Referral Mempercepat Growth", "icon": "trend",
     "desc": "Skema First Transaction, Reward, Ajak Teman di H5 terbukti menjadi akselerator utama lonjakan akuisisi di hari-hari berikutnya."},
    {"judul": "Multi-Channel Saling Memperkuat", "icon": "network",
     "desc": "Kombinasi WA personal, broadcast komunitas, dan Instagram menciptakan touchpoint berlapis yang meningkatkan konversi dibanding satu kanal saja."},
    {"judul": "Perlu Sistem, Bukan Hanya Individu", "icon": "shield",
     "desc": "Keberhasilan yang bertumpu pada satu Campus Ambassador perlu didukung sistem (tracking, SOP, tim) agar dapat diskalakan secara berkelanjutan."},
]

# ============== REKOMENDASI ==============
REKOMENDASI = [
    "Lanjutkan ke Fase 2: tempatkan BRImo Officer berinsentif di setiap satuan Menwa",
    "Bangun sistem tracking pendaftaran agar tidak bergantung pada follow up manual",
    "Replikasi model peer-to-peer ini ke kampus lain dengan organisasi mahasiswa aktif",
]
