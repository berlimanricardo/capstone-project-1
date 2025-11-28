Project Capstone Python – Sistem Manajemen Perpustakaan (CRUD + Peminjaman)

Project ini adalah program sederhana berbasis console untuk mengelola data buku di perpustakaan. Fitur utama yang disediakan adalah:

Melihat daftar buku
2. Menambah buku
3. Mengubah data buku
4. Menghapus buku
5. Meminjam buku

Program berjalan menggunakan perintah input dari pengguna.


Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer.
2. Simpan file program sebagai perpustakaan.py.
3. Jalankan melalui terminal atau cmd:
	" python perpustakaan.py "
4. Program akan menampilkan menu utama.


Struktur Data Buku

Data buku disimpan dalam list of dictionary seperti berikut:
	" {"id": 1, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "stok": 3} "

Setiap buku memiliki:
id → angka unik
2. judul → judul buku
3. penulis → nama penulis
4. stok → jumlah buku yang tersedia


Penjelasan Fitur Program

Lihat Daftar Buku
Menampilkan seluruh buku beserta ID, judul, penulis, dan stok.
--->	Dipanggil dengan memilih menu 1.

Tambah Buku
Pengguna dapat menambahkan buku baru dengan mengisi:

Judul
2. Penulis
3. Stok

ID buku akan dibuat otomatis.
--->	Dipanggil dengan menu 2.

Update Buku
Mengubah informasi buku berdasarkan ID yang dipilih.

Pengguna dapat mengganti:
Judul baru
2. Penulis baru
3. Stok baru
--->	Dipanggil dengan menu 3.

Hapus Buku

Menghapus data buku dari daftar.

Pengguna hanya perlu memasukkan ID buku yang ingin dihapus.
--->	Dipanggil dengan menu 4.

5️⃣ Peminjaman Buku

Meminjam buku akan mengurangi stok sebanyak 1.

Jika stok habis → program memberi pesan bahwa stok kosong.

Jika ID tidak ditemukan → pesan error muncul.
--->	Dipanggil dengan menu 5.

Keluar Program

Menutup aplikasi.
--->	Menu 6.


Flow Program (Menu Utama)

Setiap kali selesai menggunakan fitur, program akan kembali ke menu utama:

===== MENU PERPUSTAKAAN =====
1. Lihat Daftar Buku
2. Tambah Buku
3. Update Buku
4. Hapus Buku
5. Pinjam Buku
6. Keluar

Pengguna cukup memilih angka menu.


Catatan Penting

Program bersifat sederhana dan tidak menggunakan database.
2. Semua data tersimpan sementara selama program berjalan.
3. Bila program ditutup, data yang diinput tidak akan tersimpan permanen.


Selesai!

Dengan panduan ini, pengguna bisa memahami cara kerja program dan menjalankannya tanpa kebingungan.

