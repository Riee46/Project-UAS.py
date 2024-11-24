import pandas as pd
from datetime import datetime

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "cobalag1"

def tampilan_menu():
    print("=== Menu Utama ===")
    print("1. Tambah Data Obat")
    print("2. Tambah Racikan Obat")
    print("3. Tampilkan Data Obat")
    print("4. Cek Tanggal Harga Obat")
    print("5. Cek Tanggal Kadaluarsa Obat")
    print("6. Keluar")

def login_admin():
    print("=== Login Admin ===")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login Berhasil")
        return True
    else:
        print("Login gagal! Username atau password salah.")
        return False

# Proses login
if login_admin():
    print("Selamat datang di sistem!")
    while True:
        tampilan_menu()
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            print("Menambah Data Obat...")
            # Tambahkan logika untuk menambah data obat di sini
        elif pilihan == '2':
            print("Menambah Racikan Obat...")
            # Tambahkan logika untuk menambah racikan obat di sini
        elif pilihan == '3':
            print("Menampilkan Data Obat...")
            # Tambahkan logika untuk menampilkan data obat di sini
        elif pilihan == '4':
            print("Cek Tanggal Harga Obat...")
            # Tambahkan logika untuk cek tanggal harga obat di sini
        elif pilihan == '5':
            print("Cek Tanggal Kadaluarsa Obat...")
            # Tambahkan logika untuk cek tanggal kadaluarsa obat di sini
        elif pilihan == '6':
            print("Keluar dari sistem...")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
else:
    print("Akses ditolak.")