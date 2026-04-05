# MASTER_PROJECT_CONTEXT.md - Microsite Transpatriot

## 1. Ringkasan Proyek
Proyek ini adalah microsite untuk **Kementerian Transmigrasi Republik Indonesia** yang berfokus pada **Program Transmigrasi Patriot**. Website ini bertujuan untuk memberikan informasi mengenai profil program, regulasi, dan pendaftaran beasiswa.

## 2. Struktur Proyek
Proyek ini merupakan website statis (HTML/CSS/JS) dengan struktur sebagai berikut:
- `index.html`: Halaman utama dengan hero, profil program, inisiatif utama, dan footer.
- `profil.html`: Informasi detail mengenai program.
- `regulasi.html`: Dokumen dan dasar hukum terkait program.
- `kontakkami.html`: Form kontak dan informasi navigasi kantor.
- `programdetail.html`: Detail dari program-program unggulan.
- `assets/css/style.css`: File CSS utama yang berisi styling global dan responsif.
- `assets/img/`: Folder penyimpanan aset gambar (beberapa link menggunakan Firebase/Storage eksternal).

## 3. Konvensi Styling & UI
- **Font**: Menggunakan Google Fonts ('Inter' dan 'DM Sans').
- **Warna Utama**:
    - `--primary`: `#0d3244` (Deep Blue)
    - `--accent`: `#c08e41` (Gold)
    - `--muted`: `#f3f5f7`
- **Typografi**: Menggunakan blok `<style id="global-typography">` di dalam `index.html` sebagai layer "hot fix" untuk override styling global agar konsisten di mobile.
- **Iconography**: Menggunakan `iconify-icon` (Lucide-based icons).

## 4. Perkembangan Terakhir
- **Mobile Optimization (Section 'Inisiatif & Fokus Utama')**: 
    - Melakukan sinkronisasi visual pada mobile view (Centering icon & text, premium shadow, padding fix).
    - Perbaikan lint error (missing brace) pada media query mobile.
- **Mobile Optimization (Section 'Profil Program')**:
    - Merapatkan section ke atas (mengurangi padding-top) agar flow lebih padat.
    - Merapikan daftar fitur (feature list) agar berada di tengah (centered block) namun teks & ikon tetap rata kiri (left-aligned) dengan alignment yang presisi.

## 5. Deployment / Docker (Optional)
- Karena merupakan web statis, deployment dapat dilakukan via Nginx atau file server statis lainnya.
- Meskipun ada instruksi untuk menggunakan Docker, user telah memberikan konfirmasi bahwa untuk perubahan statis (HTML/CSS) tidak mutlak diperlukan kecuali untuk debugging kompleks.

---
*Dokumen ini diperbarui secara berkala sebagai sumber kebenaran konteks proyek.*
