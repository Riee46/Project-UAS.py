import pandas as pd
from tabulate import tabulate
import os

DATA_OBAT_CSV = "data_obat.csv"

# Fungsi untuk membaca data dari file CSV menggunakan pandas
def baca_data_obat():
    if not os.path.exists(DATA_OBAT_CSV):
        return []  # Jika file tidak ada, kembalikan list kosong

    try:
        df = pd.read_csv(DATA_OBAT_CSV)
        return df.to_dict(orient="records")  # Konversi DataFrame ke list of dictionaries
    except pd.errors.EmptyDataError:
        return []  # Jika file kosong, kembalikan list kosong

# Fungsi untuk menulis data ke file CSV menggunakan pandas
def tulis_data_obat(data):
    df = pd.DataFrame(data)  # Konversi list of dictionaries ke DataFrame
    df.to_csv(DATA_OBAT_CSV, index=False)  # Simpan ke file CSV tanpa menulis index

# Fungsi untuk menambah stok obat
def tambah_stok_obat():
    os.system('clear')
    print("=== Pemasukan Stok Obat ===")
    nama_obat = input("Masukkan nama obat: ")
    jumlah_stok = input("Masukkan jumlah obat yang ditambahkan: ")
    tanggal_kadaluarsa = input("Masukkan tanggal kadaluarsa obat (YYYY-MM-DD): ")

    try:
        jumlah_stok = int(jumlah_stok)  # Validasi jumlah stok sebagai angka
        if jumlah_stok <= 0:
            raise ValueError("Jumlah stok harus lebih dari 0.")

        data_obat = baca_data_obat()

        # Cek apakah obat sudah ada
        obat_ditemukan = False
        for obat in data_obat:
            if obat["Nama Obat"] == nama_obat:
                obat["stok"] += jumlah_stok  # Tambahkan ke stok yang ada
                obat_ditemukan = True
                break

        # Jika obat tidak ditemukan, tambahkan sebagai data baru
        if not obat_ditemukan:
            data_obat.append({
                "Nama Obat": nama_obat,
                "stok": jumlah_stok,
                "Tanggal Kadaluarsa": tanggal_kadaluarsa
            })

        tulis_data_obat(data_obat)
        os.system('clear')
        print("Stok obat berhasil diperbarui!")

    except ValueError as e:
        os.system('clear')
        print(f"Kesalahan: {e}")

# Fungsi untuk menampilkan daftar obat
def tampilkan_daftar_obat():
    os.system('clear')
    print("=== Daftar Obat ===")
    data_obat = baca_data_obat()
    if not data_obat:
        print("Belum ada data obat.")
    else:
        print(tabulate(data_obat, headers="keys", tablefmt="grid"))
        input("Tekan Enter untuk keluar...")
        os.system('clear')

# Fungsi utama untuk menu aplikasi
os.system('clear')
while True:
    print("\n=== Aplikasi Pemasukan Stok Obat ===")
    print("1. Tambah Stok Obat")
    print("2. Tampilkan Daftar Obat")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_stok_obat()
    elif pilihan == "2":
        tampilkan_daftar_obat()
    elif pilihan == "3":
        print("Keluar dari aplikasi. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
