import csv
import os
import pandas as pd

# Cek keberadaan file pengguna
if not os.path.exists("users.csv"):
    header = ["username", "password", "role"]
    with open("users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(["admin", "admin123", "admin"])  # Admin default
        writer.writerow(["user", "user123", "user"])    # User default

# Cek keberadaan file obat
if not os.path.exists("obat.csv"):
    header = ["kode_obat", "nama_obat", "stok", "harga"]
    with open("obat.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(["OBT001", "Paracetamol", 50, 5000])
        writer.writerow(["OBT002", "Amoxicillin", 30, 10000])
        writer.writerow(["OBT003", "Vitamin C", 100, 3000])

# Fungsi utama menu
def main_menu(user_role):
    print("-----------------------------------------------")
    print("=== Selamat Datang di Sistem Pemesanan Obat ===")
    print("-----------------------------------------------")
    print(f"Halo, Anda login sebagai {'Admin' if user_role == 'admin' else 'User'}")
    print("\nPilih menu berikut:")

    if user_role == "admin":
        print("1. Kelola Obat")
        print("2. Approve Transaksi")
        print("3. Rekap Data")
        print("4. Logout")
    elif user_role == "user":
        print("1. Cek Data Obat")
        print("2. Pesan Obat")
        print("3. Riwayat Pesanan")
        print("4. Logout")
    else:
        print("Peran tidak dikenali.")
        return

    # Meminta input dari pengguna
    pilihan = input("\nMasukkan nomor pilihan: ")

    # Menangani pilihan berdasarkan peran
    if user_role == "admin":
        if pilihan == "1":
            kelola_obat()
        elif pilihan == "2":
            approve_transaksi()
        elif pilihan == "3":
            rekap_data()
        elif pilihan == "4":
            logout()
        else:
            print("Pilihan tidak valid.")
            main_menu(user_role)  # Ulang menu
    elif user_role == "user":
        if pilihan == "1":
            cek_data_obat()
        elif pilihan == "2":
            pesan_obat()
        elif pilihan == "3":
            riwayat_pesanan()
        elif pilihan == "4":
            logout()
        else:
            print("Pilihan tidak valid.")
            main_menu(user_role)  # Ulang menu

# Fungsi CRUD Simulasi
def kelola_obat():
    print("\n--- Kelola Obat ---")
    print("1. Tambah Obat")
    print("2. Hapus Obat")
    print("3. Kembali")
    pilihan = input("\nMasukkan nomor pilihan: ")

    if pilihan == "1":
        kode = input("Masukkan kode obat: ")
        nama = input("Masukkan nama obat: ")
        stok = int(input("Masukkan stok: "))
        harga = int(input("Masukkan harga: "))

        with open("obat.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([kode, nama, stok, harga])
        print("Obat berhasil ditambahkan.")
    elif pilihan == "2":
        kode = input("Masukkan kode obat yang ingin dihapus: ")
        df = pd.read_csv("obat.csv")
        df = df[df["kode_obat"] != kode]
        df.to_csv("obat.csv", index=False)
        print("Obat berhasil dihapus.")
    elif pilihan == "3":
        return
    else:
        print("Pilihan tidak valid.")
    kelola_obat()

def approve_transaksi():
    print("\n--- Approve Transaksi ---")
    print("Fitur ini akan membantu admin menyetujui transaksi.")
    # Simulasi: Tambahkan logika approve transaksi di sini

def rekap_data():
    print("\n--- Rekap Data ---")
    print("Fitur ini akan membantu admin melihat rekap data.")
    # Simulasi: Tambahkan logika rekap data di sini

def cek_data_obat():
    print("\n--- Cek Data Obat ---")
    if os.path.exists("obat.csv"):
        df = pd.read_csv("obat.csv")
        print(df)
    else:
        print("Data obat belum tersedia.")

def pesan_obat():
    print("\n--- Pesan Obat ---")
    kode = input("Masukkan kode obat yang ingin dipesan: ")
    jumlah = int(input("Masukkan jumlah: "))
    
    df = pd.read_csv("obat.csv")
    if kode in df["kode_obat"].values:
        obat = df[df["kode_obat"] == kode]
        stok = int(obat["stok"])
        if jumlah <= stok:
            df.loc[df["kode_obat"] == kode, "stok"] = stok - jumlah
            df.to_csv("obat.csv", index=False)
            print("Pesanan berhasil!")
        else:
            print("Stok tidak mencukupi.")
    else:
        print("Kode obat tidak ditemukan.")

def riwayat_pesanan():
    print("\n--- Riwayat Pesanan ---")
    print("Fitur ini akan membantu user melihat riwayat pesanan.")
    # Simulasi: Tambahkan logika riwayat pesanan di sini

def logout():
    print("\nAnda telah logout. Sampai jumpa!")
    exit()

# Program Utama
if __name__ == "__main__":
    # Login sederhana
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Verifikasi pengguna
    users = pd.read_csv("users.csv")
    user = users[(users["username"] == username) & (users["password"] == password)]

    if not user.empty:
        role = user.iloc[0]["role"]
        main_menu(role)
    else:
        print("Login gagal! Username atau password salah.")
