# KIPM-UP Absensi — Streamlit Deployment

## Struktur File
```
kipmup-streamlit/
├── app.py              ← File utama Streamlit
├── index.html          ← File HTML app absensi kamu (COPY KE SINI)
├── requirements.txt    ← Dependencies
├── .streamlit/
│   └── config.toml    ← Konfigurasi Streamlit
└── README.md
```

## Cara Deploy ke Streamlit Cloud

### 1. Siapkan Repository GitHub (PRIVATE boleh!)
- Buat repo baru di GitHub (boleh private)
- Upload semua file ini + `index.html` kamu ke repo

### 2. Deploy ke Streamlit Cloud
1. Buka https://share.streamlit.io
2. Login dengan akun GitHub
3. Klik **"New app"**
4. Pilih repo kamu
5. Set **Main file path**: `app.py`
6. Klik **Deploy!**

### 3. Selesai!
- App kamu akan dapat URL publik seperti:
  `https://namaapp-xxxxx.streamlit.app`
- URL ini SELALU bisa diakses meski repo GitHub-nya PRIVATE ✅

## Catatan Penting
- File `index.html` WAJIB ada di folder yang sama dengan `app.py`
- Streamlit Cloud gratis untuk repo public maupun private
- URL Streamlit tidak bergantung pada visibilitas repo GitHub
