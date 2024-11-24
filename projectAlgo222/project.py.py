import pandas as pd
import csv
from datetime import datetime
import os

# Konstanta login admin
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "cobalag1"

# Path file absolut (sesuaikan dengan lokasi file Anda)
DATA_OBAT_CSV = os.path.abspath("Users\Lenovo\OneDrive\Documents\Praktikum Pemrograman\Praktikum python 101\Project_Algo\data_obat.csv")
DATA_RACIKAN_CSV = os.path.abspath("Users\Lenovo\OneDrive\Documents\Praktikum Pemrograman\Praktikum python 101\Project_Algo\data_racikan.csv")

# Fungsi untuk memuat data dari CSV
def muat_data():
    global data_obat, data_racikan
    try:
        data_obat = pd.read_csv(DATA_OBAT_CSV)
    except FileNotFoundError:
        data_obat = pd.DataFrame(columns=['Nama Obat', 'Harga', 'Tanggal Kadaluarsa'])

    try:
        data_racikan = pd.read_csv(DATA_RACIKAN_CSV)
    except FileNotFoundError:
        data_racikan = pd.DataFrame(columns=['Nama Racikan', 'Obat', 'Total Harga'])

# Fungsi untuk menyimpan data ke CSV
def simpan_data():
    print(f"Menyimpan data obat ke: {DATA_OBAT_CSV}")
    print(f"Menyimpan data racikan ke: {DATA_RACIKAN_CSV}")

    try:
        data_obat.to_csv(DATA_OBAT_CSV, index=False)
        data_racikan.to_csv(DATA_RACIKAN_CSV, index=False)
        print("Data berhasil disimpan.")
    except PermissionError:
        print("Anda tidak memiliki izin untuk menulis ke file tersebut. Periksa izin file atau lokasi penyimpanan.")
    except OSError as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

# Fungsi untuk menampilkan menu
def tampilan_menu():
    print("\n=== Menu Utama ===")
    print("1. Tambah Data Obat")
    print("2. Hapus Data Obat")
    print("3. Tambah Racikan Obat")
    print("4. Hapus Racikan Obat")
    print("5. Tampilkan Data Obat")
    print("6. Tampilkan Data Racikan Obat")
    print("7. Keluar")

# Fungsi untuk login admin
def login_admin():
    print("=== Login Admin ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login Berhasil")
        return True
    else:
        print("Login gagal! Username atau password salah.")
        return False

# Fungsi untuk menambah data obat
def tambah_data_obat():
    global data_obat
    print("\n=== Tambah Data Obat ===")
    nama = input("Masukkan nama obat: ")
    try:
        harga = float(input("Masukkan harga obat: "))
    except ValueError:
        print("Harga harus berupa angka!")
        return
    tanggal_kadaluarsa = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")

    # Validasi tanggal
    try:
        datetime.strptime(tanggal_kadaluarsa, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal salah! Gunakan format YYYY-MM-DD.")
        return

    # Tambahkan ke DataFrame
    data_obat = pd.concat([data_obat, pd.DataFrame({
        'Nama Obat': [nama],
        'Harga': [harga],
        'Tanggal Kadaluarsa': [tanggal_kadaluarsa]
    })], ignore_index=True)

    simpan_data()  # Simpan data ke CSV
    print(f"Data obat '{nama}' berhasil ditambahkan!\n")

# Fungsi untuk menghapus data obat
def hapus_data_obat():
    global data_obat
    print("\n=== Hapus Data Obat ===")
    nama = input("Masukkan nama obat yang ingin dihapus: ")

    if nama in data_obat['Nama Obat'].values:
        data_obat = data_obat[data_obat['Nama Obat'] != nama]
        simpan_data()  # Simpan data ke CSV
        print(f"Data obat '{nama}' berhasil dihapus!\n")
    else:
        print(f"Obat dengan nama '{nama}' tidak ditemukan!\n")

# Fungsi untuk menambah racikan obat
def tambah_racikan_obat():
    global data_obat, data_racikan
    print("\n=== Tambah Racikan Obat ===")
    nama_racikan = input("Masukkan nama racikan obat: ")

    if data_obat.empty:
        print("Tidak ada data obat untuk diracik. Tambahkan data obat terlebih dahulu.")
        return

    print("\n=== Daftar Obat ===")
    print(data_obat[['Nama Obat', 'Harga']])

    obat_terpilih = []
    total_harga = 0

    while True:
        nama_obat = input("Masukkan nama obat yang ingin ditambahkan ke racikan (atau ketik 'selesai' untuk selesai): ")
        if nama_obat.lower() == 'selesai':
            break
        if nama_obat in data_obat['Nama Obat'].values:
            harga_obat = data_obat.loc[data_obat['Nama Obat'] == nama_obat, 'Harga'].values[0]
            obat_terpilih.append(nama_obat)
            total_harga += harga_obat
            print(f"Obat '{nama_obat}' ditambahkan ke racikan. Total harga saat ini: {total_harga}")
        else:
            print(f"Obat dengan nama '{nama_obat}' tidak ditemukan!")

    if obat_terpilih:
        # Tambahkan ke DataFrame racikan
        data_racikan = pd.concat([data_racikan, pd.DataFrame({
            'Nama Racikan': [nama_racikan],
            'Obat': [', '.join(obat_terpilih)],
            'Total Harga': [total_harga]
        })], ignore_index=True)
        simpan_data()  # Simpan data ke CSV
        print(f"Racikan obat '{nama_racikan}' berhasil ditambahkan!\n")
    else:
        print("Racikan obat tidak memiliki bahan dan tidak akan disimpan.\n")

# Fungsi untuk menghapus racikan obat
def hapus_racikan_obat():
    global data_racikan
    print("\n=== Hapus Racikan Obat ===")
    nama_racikan = input("Masukkan nama racikan yang ingin dihapus: ")

    if nama_racikan in data_racikan['Nama Racikan'].values:
        data_racikan = data_racikan[data_racikan['Nama Racikan'] != nama_racikan]
        simpan_data()  # Simpan data ke CSV
        print(f"Racikan obat '{nama_racikan}' berhasil dihapus!\n")
    else:
        print(f"Racikan dengan nama '{nama_racikan}' tidak ditemukan!\n")

# Main Program
muat_data()  # Memuat data dari CSV
if login_admin():
    print("\nSelamat datang di sistem!")
    while True:
        tampilan_menu()
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == '1':
            tambah_data_obat()
        elif pilihan == '2':
            hapus_data_obat()
        elif pilihan == '3':
            tambah_racikan_obat()
        elif pilihan == '4':
            hapus_racikan_obat()
        elif pilihan == '5':
            print("\n=== Data Obat ===")
            if not data_obat.empty:
                print(data_obat)
            else:
                print("Tidak ada data obat.\n")
        elif pilihan == '6':
            print("\n=== Data Racikan Obat ===")
            if not data_racikan.empty:
                print(data_racikan)
            else:
                print("Tidak ada data racikan obat.\n")
        elif pilihan == '7':
            print("Keluar dari sistem...")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
else:
    print("Akses ditolak.")
