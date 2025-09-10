# Penerapan Core Flask

1. Install dulu Flask
```bash
pip instal Flask
```

2. Buat struktur foldernya

# Penerapan Tailwind

# 🔹 Fungsi umum sidebar

1. Navigasi utama atau tambahan
    * Menu menuju halaman lain (Dashboard, Laporan, Settings, dll).
    * Biasanya dipakai di aplikasi web (admin panel, CMS, sistem internal).

2. Filter / kategori
    * E-commerce: filter produk (harga, kategori, brand).
    * Blog: kategori artikel, tag.

3. Informasi profil pengguna
    * Foto profil, nama, status login.
    * Shortcut ke pengaturan akun.

4. Akses cepat ke fitur penting
    * Notifikasi, pesan terbaru, daftar tugas.
    * Shortcut ke "Create New", "Upload", "Search", dll.

5. Widget atau informasi tambahan
    * Kalender, jam, daftar teman online, iklan, dll.


# 🔹 Contoh penggunaan sidebar sesuai jenis web

1. Dashboard Admin → menu navigasi (Home, Users, Reports, Settings).
2. E-Commerce → filter produk (harga, brand, ukuran).
3. Blog / News Portal → kategori, arsip, artikel populer.
4. SaaS / App → menu utama untuk berpindah antar fitur.


# 🔹 Solusi umum sidebar di mobile

1. Diubah jadi off-canvas menu
    * Sidebar disembunyikan, lalu bisa ditampilkan dengan tombol (biasanya ☰ hamburger).
    * Muncul dari kiri/kanan saat user klik tombol.

2. Diubah jadi bottom navigation
    * Untuk aplikasi sederhana, menu sidebar diganti ke baris ikon di bawah (seperti aplikasi mobile).

3. Collapse jadi ikon
    * Sidebar hanya menampilkan ikon, tanpa teks. Saat di-tap bisa expand.

4. Dropdown menu di header
    * Kalau menunya sedikit, pindahkan ke menu dropdown di header.

# Note

1. penggunaan hover pada mobile sebaiknya tidak diterapkan