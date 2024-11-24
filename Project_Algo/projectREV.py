import os
import pandas as pd
from datetime import datetime
from tabulate import tabulate

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "cobalag1"

# Simulasi data obat
data_obat = [
    {"Nama Obat": "Paracetamol", "Tanggal Kadaluarsa": "2024-12-01"},
    {"Nama Obat": "Ibuprofen", "Tanggal Kadaluarsa": "2023-11-15"},
    {"Nama Obat": "Amoxicillin", "Tanggal Kadaluarsa": "2025-05-20"},
    {"Nama Obat": "Aspirin", "Tanggal Kadaluarsa": "2023-09-30"},
]

# Inisialisasi list untuk apoteker dan pasien
apoteker_list = []
pasien_list = []

# Fungsi untuk menyimpan data apoteker ke CSV
def simpan_apoteker_ke_csv():
    df = pd.DataFrame(apoteker_list)
    df.to_csv('apoteker.csv', index=False)

# Fungsi untuk memuat data apoteker dari CSV
def muat_apoteker_dari_csv():
    global apoteker_list
    if os.path.exists('apoteker.csv'):
        apoteker_list = pd.read_csv('apoteker.csv').to_dict(orient='records')

# Fungsi untuk menyimpan data pasien ke CSV
def simpan_pasien_ke_csv():
    df = pd.DataFrame(pasien_list)
    df.to_csv('pasien.csv', index=False)

# Fungsi untuk memuat data pasien dari CSV
def muat_pasien_dari_csv():
    global pasien_list
    if os.path.exists('pasien.csv'):
        pasien_list = pd.read_csv('pasien.csv').to_dict(orient='records')

# Fungsi untuk menyimpan data obat ke CSV
def simpan_obat_ke_csv():
    df = pd.DataFrame(data_obat)
    df.to_csv('obat.csv', index=False)

# Fungsi untuk memuat data obat dari CSV
def muat_obat_dari_csv():
    global data_obat
    if os.path.exists('obat.csv'):
        data_obat = pd.read_csv('obat.csv').to_dict(orient='records')

def tampilan_judul():
    print("=== SISTEK PANASEA ===")

def tampilan_menu():
    print("\n=== Menu Utama ===")
    print(tabulate([
        ["1", "Kelola Data Apoteker"],
        ["2", "Kelola Data Pasien"],
        ["3", "Kelola Data Obat"],
        ["4", "Kelola Pemesanan Obat"],
        ["5", "Kelola Stock Obat"],
        ["6", "Keluar"]
    ], headers=["No", "Menu"], tablefmt="grid"))

# ... (sisa kode tidak berubah) ...

# Proses login
if login_admin():
    muat_apoteker_dari_csv()
    muat_pasien_dari_csv()
    muat_obat_dari_csv()
    
    tampilan_judul()
    print("Selamat datang di sistem!")
    while True:
        tampilan_menu()
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            while True:
                tampilan_menu_apoteker()
                sub_pilihan = input("Pilih submenu (1-4): ")
                if sub_pilihan == '1':
                    print("Menambah Apoteker...")
                    # Logika untuk menambah apoteker
                    nama_apoteker = input("Masukkan nama apoteker: ")
                    alamat_apoteker = input("Masukkan alamat apoteker: ")
                    no_telepon_apoteker = input("Masukkan no telepon apoteker: ")

                    # Simpan data apoteker ke dalam dictionary
                    apoteker_data = {
                        "nama": nama_apoteker,
                        "alamat": alamat_apoteker,
                        "no_telepon": no_telepon_apoteker
                    }

                    # Tambahkan data apoteker ke dalam list
                    apoteker_list.append(apoteker_data)
                    simpan_apoteker_ke_csv()  # Simpan ke CSV

                    print("Apoteker berhasil ditambahkan!")
                    print("Data Apoteker:")
                    print("Nama:", nama_apoteker)
                    print("Alamat:", alamat_apoteker)
                    print("No Telepon:", no_telepon_apoteker)
                elif sub_pilihan == '2':
                    print("Menghapus Apoteker...")
                    # Logika untuk menghapus apoteker
                    nama_apoteker = input("Masukkan nama apoteker yang akan dihapus: ")
                    apoteker_found = False

                    for apoteker in apoteker_list:
                        if apoteker["nama"] == nama_apoteker:
                            apoteker_found = True
                            apoteker_list.remove(apoteker)
                            simpan_apoteker_ke_csv()  # Simpan ke CSV
                            print("Apoteker berhasil dihapus!")
                            break

                    if not apoteker_found:
                        print("Apoteker tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Apoteker...")
                    if not apoteker_list:
                        print("Tidak ada apoteker yang terdaftar.")
                    else:
                        print("Daftar Apoteker:")
                        for apoteker in apoteker_list:
                            print("Nama:", apoteker["nama"])
                            print("Alamat:", apoteker["alamat"])
                            print("No Telepon:", apoteker["no_telepon"])
                            print("-------------------------")
                elif sub_pilihan == '4':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")
        
        elif pilihan == '2':
            while True:
                tampilan_menu_pasien()
                sub_pilihan = input("Pilih submenu (1-4): ")
                if sub_pilihan == '1':
                    print("Menambah Pasien...")
                    # Logika untuk menambah pasien
                    nama_pasien = input("Masukkan nama pasien: ")
                    alamat_pasien = input("Masukkan alamat pasien: ")
                    no_telepon_pasien = input("Masukkan no telepon pasien: ")
                    umur_pasien = input("Masukkan umur pasien: ")

                    # Simpan data pasien ke dalam dictionary
                    pasien_data = {
                        "nama": nama_pasien,
                        "alamat": alamat_pasien,
                        "no_telepon": no_telepon_pasien,
                        "umur": umur_pasien
                    }

                    # Tambahkan data pasien ke dalam list
                    pasien_list.append(pasien_data)
                    simpan_pasien_ke_csv()  # Simpan ke CSV

                    print("Pasien berhasil ditambahkan!")
                    print("Data Pasien:")
                    print("Nama:", nama_pasien)
                    print("Alamat:", alamat_pasien)
                    print("No Telepon:", no_telepon_pasien)
                    print("Umur:", umur_pasien)
                elif sub_pilihan == '2':
                    print("Menghapus Pasien...")
                    # Logika untuk menghapus pasien
                    nama_pasien = input("Masukkan nama pasien yang akan dihapus: ")
                    pasien_found = False

                    for pasien in pasien_list:
                        if pasien["nama"] == nama_pasien:
                            pasien_found = True
                            pasien_list.remove(pasien)
                            simpan_pasien_ke_csv()  # Simpan ke CSV
                            print("Pasien berhasil dihapus!")
                            break

                    if not pasien_found:
                        print("Pasien tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Pasien...")
                    if not pasien_list:
                        print("Tidak ada pasien yang terdaftar.")
                    else:
                        print("Daftar Pasien:")
                        for pasien in pasien_list:
                            print("Nama:", pasien["nama"])
                            print("Alamat:", pasien["alamat"])
                            print("No Telepon:", pasien["no_telepon"])
                            print("Umur:", pasien["umur"])
                            print("-------------------------")
                elif sub_pilihan == '4':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '3':
            while True:
                tampilan_menu_obat()
                sub_pilihan = input("Pilih submenu (1-5): ")
                if sub_pilihan == '1':
                    print("Menambah Obat...")
                    # Logika untuk menambah obat
                    nama_obat = input("Masukkan nama obat: ")
                    dosis_obat = input("Masukkan dosis obat: ")
                    jumlah_obat = input("Masukkan jumlah obat: ")
                    tanggal_kadaluarsa = input("Masukkan tanggal kadaluarsa (DD-MM-YYYY): ")

                    # Simpan data obat ke dalam dictionary
                    obat_data = {
                        "Nama Obat": nama_obat,
                        "Dosis": dosis_obat,
                        "Jumlah ": jumlah_obat,
                        "Tanggal Kadaluarsa": tanggal_kadaluarsa
                    }

                    # Tambahkan data obat ke dalam list
                    data_obat.append(obat_data)
                    simpan_obat_ke_csv()  # Simpan ke CSV

                    print("Obat berhasil ditambahkan!")
                    print("Data Obat:")
                    print("Nama:", nama_obat)
                    print("Dosis:", dosis_obat)
                    print("Jumlah:", jumlah_obat)
                    print("Tanggal Kadaluarsa:", tanggal_kadaluarsa)
                elif sub_pilihan == '2':
                    print("Menghapus Obat...")
                    # Logika untuk menghapus obat
                    nama_obat = input("Masukkan nama obat yang akan dihapus: ")
                    obat_found = False

                    for obat in data_obat:
                        if obat["Nama Obat"] == nama_obat:
                            obat_found = True
                            data_obat.remove(obat)
                            simpan_obat_ke_csv()  # Simpan ke CSV
                            print("Obat berhasil dihapus!")
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Obat...")
                    if not data_obat:
                        print("Tidak ada obat yang terdaftar.")
                    else:
                        print("Daftar Obat:")
                        for obat in data_obat:
                            print("Nama Obat:", obat["Nama Obat"])
                            print("Dosis:", obat["Dosis"])
                            print("Jumlah:", obat["Jumlah"])
                            print("Tanggal Kadaluarsa:", obat["Tanggal Kadaluarsa"])
                            print("-------------------------")
                elif sub_pilihan == '4':
                    filter_tanggal_kadaluarsa()
                elif sub_pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '4':
            while True:
                tampilan_menu_pemesanan()
                sub_pilihan = input("Pilih submenu (1-3): ")
                if sub_pilihan == '1':
                    pemesanan = buat_pemesanan()
                    print("Pemesanan berhasil dibuat.")
                elif sub_pilihan == '2':
                    if 'pemesanan' in locals():
                        cetak_struk(pemesanan)
                    else:
                        print("Belum ada pemesanan yang dibuat.")
                elif sub_pilihan == '3':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '5':
            while True:
                tampilan_menu_stock()
                sub_pilihan = input("Pilih submenu (1-3): ")
                if sub_pilihan == '1':
                    print("Cek Stock Obat...")
                    nama_obat = input("Masukkan nama obat yang ingin dicek: ")
                    obat_found = False

                    for obat in data_obat:
                        if obat["Nama Obat"].lower() == nama_obat.lower():
                            obat_found = True
                            print("Detail Obat:")
                            print("Nama Obat:", obat["Nama Obat"])
                            print("Dosis:", obat["Dosis"])
                            print("Jumlah Tersedia:", obat["Jumlah"])
                            print("Tanggal Kadaluarsa:", obat["Tanggal Kadaluarsa"])
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '2':
                    print("Cek Tanggal Kadaluarsa...")
                    nama_obat = input("Masukkan nama obat yang ingin dicek: ")
                    obat_found = False

                    for obat in data_obat:
                        if obat["Nama Obat"].lower() == nama_obat.lower():
                            obat_found = True
                            print("Detail Obat:")
                            print("Nama Obat:", obat["Nama Obat"])
                            print("Tanggal Kadaluarsa:", obat["Tanggal Kadaluarsa"])
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '3':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '6':
            print("Keluar dari sistem")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
else:
     print("Akses ditolak.")