# ==========================================
# Mini Program Perpustakaan (CRUD + Peminjaman)
# ==========================================

# Data awal: 10 daftar buku
buku = [
    {"id": 1, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "stok": 3},
    {"id": 2, "judul": "Bumi", "penulis": "Tere Liye", "stok": 5},
    {"id": 3, "judul": "Negeri 5 Menara", "penulis": "A. Fuadi", "stok": 2},
    {"id": 4, "judul": "Pulang", "penulis": "Tere Liye", "stok": 4},
    {"id": 5, "judul": "Dilan 1990", "penulis": "Pidi Baiq", "stok": 3},
    {"id": 6, "judul": "Koala Kumal", "penulis": "Raditya Dika", "stok": 6},
    {"id": 7, "judul": "Cantik Itu Luka", "penulis": "Eka Kurniawan", "stok": 3},
    {"id": 8, "judul": "Ronggeng Dukuh Paruk", "penulis": "Ahmad Tohari", "stok": 2},
    {"id": 9, "judul": "Bumi Manusia", "penulis": "Pramoedya A. Toer", "stok": 4},
    {"id": 10, "judul": "Filosofi Kopi", "penulis": "Dewi Lestari", "stok": 5},
]

# Menampilkan daftar buku
def read_buku():
    print("\n=== Daftar Buku ===")
    for b in buku:
        print(f"ID: {b['id']} | {b['judul']} - {b['penulis']} | Stok: {b['stok']}")
    print()

# Menambah buku
def create_buku():
    print("\n=== Tambah Buku ===")
    id_baru = buku[-1]["id"] + 1 if buku else 1
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    stok = int(input("Stok: "))

    buku.append({"id": id_baru, "judul": judul, "penulis": penulis, "stok": stok})
    print("Buku berhasil ditambahkan!\n")

# Mengubah data buku
def update_buku():
    print("\n=== Update Buku ===")
    read_buku()
    id_buku = int(input("Masukkan ID buku yang ingin diupdate: "))

    for b in buku:
        if b["id"] == id_buku:
            b["judul"] = input("Judul baru: ")
            b["penulis"] = input("Penulis baru: ")
            b["stok"] = int(input("Stok baru: "))
            print("Buku berhasil diperbarui!\n")
            return
    print("ID buku tidak ditemukan!\n")

# Menghapus buku
def delete_buku():
    print("\n=== Hapus Buku ===")
    read_buku()
    id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))

    for b in buku:
        if b["id"] == id_buku:
            buku.remove(b)
            print("Buku berhasil dihapus!\n")
            return
    print("ID buku tidak ditemukan!\n")

# Peminjaman buku
def pinjam_buku():
    print("\n=== Peminjaman Buku ===")
    read_buku()
    id_buku = int(input("Masukkan ID buku yang ingin dipinjam: "))

    for b in buku:
        if b["id"] == id_buku:
            if b["stok"] > 0:
                b["stok"] -= 1
                print(f"Anda berhasil meminjam '{b['judul']}'\n")
            else:
                print("Stok buku habis!\n")
            return
    print("ID buku tidak ditemukan!\n")


# Menu utama
def menu():
    while True:
        print("===== MENU PERPUSTAKAAN =====")
        print("1. Lihat Daftar Buku")
        print("2. Tambah Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Pinjam Buku")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_buku()
        elif pilihan == "2":
            create_buku()
        elif pilihan == "3":
            update_buku()
        elif pilihan == "4":
            delete_buku()
        elif pilihan == "5":
            pinjam_buku()
        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")


# Jalankan program
menu()
