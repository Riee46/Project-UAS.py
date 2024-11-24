import os  # Mengimpor modul 'os' untuk mengakses fungsi sistem, seperti membersihkan layar konsol

# Daftar kosong untuk menyimpan data mahasiswa dan nilai setiap mata kuliah
namamahasiswa = []  
nilaipemror = []  
nilaimatdis = []  
nilaibing = []  
matkul = ["PEMROR", "MATDIS", "BING"]  # Daftar nama mata kuliah

def clear_screen():  # Fungsi untuk membersihkan layar
    os.system("cls")  # Memanggil perintah sistem 'cls' untuk membersihkan layar (Windows)

def print_line():  # Fungsi untuk mencetak garis pemisah
    print("=" * 75)  # Mencetak '=' sebanyak 75 karakter untuk garis pemisah

def cover():  # Fungsi untuk menampilkan judul program
    print_line()  # Mencetak garis
    print("\t\t SISTEM PENILAIAN SEDERHANA")  # Judul program
    print_line()  # Mencetak garis

def pause():  # Fungsi untuk menghentikan sementara eksekusi program
    input("press [ENTER] to continue..")  # Menunggu pengguna menekan ENTER untuk melanjutkan

# Fungsi utama untuk menampilkan menu program
def menu():
    clear_screen()  # Membersihkan layar
    cover()  # Menampilkan judul program
    print("""
    MENU :
    1. INPUT NILAI MAHASISWA
    2. DAFTAR NILAI MAHASISWA
    3. NILAI RATA RATA MATAKULIAH KESELURUHAN
    4. LAPORAN AKHIR
    5. TENTANG PEMBUAT PROGRAM
    6. KELUAR PROGRAM
    """)
print_line()  # Mencetak garis pemisah

pilih = int(input("masukan pilihan program >>"))  # Meminta input dari pengguna untuk memilih menu

# Percabangan untuk menentukan tindakan berdasarkan pilihan pengguna
if pilih == 1 :
    inputan ()  # Memanggil fungsi 'inputan' jika pilihan adalah 1
elif pilih == 2 :
    daftar_nilai()  # Memanggil fungsi 'daftar_nilai' jika pilihan adalah 2
elif pilih == 3 :
    rata_rata_mata_kuliah()  # Memanggil fungsi 'rata_rata_mata_kuliah' jika pilihan adalah 3
elif pilih == 4 :
    tampilkan_laporan()  # Memanggil fungsi 'tampilkan_laporan' jika pilihan adalah 4
elif pilih == 5 :
    pembuat()  # Memanggil fungsi 'pembuat' jika pilihan adalah 5
else :
    clear_screen()  # Membersihkan layar
    print("terima kasih telah menggunakan program ini")  # Pesan penutup jika pengguna memilih keluar

# Fungsi untuk memasukkan data nilai mahasiswa
def inputan ():
    while true :  # Mengulang proses input data
        clear_screen()  # Membersihkan layar
        cover()  # Menampilkan judul program
        namamahasiswa = input("masukan nama mahasiswa :").upper()  # Meminta nama mahasiswa, diubah menjadi huruf besar
        pemror = int(input("Masukan nilai PEMROR"))  # Meminta nilai PEMROR dari pengguna
        matdis = int(input("Masukan nilai MATDIS"))  # Meminta nilai MATDIS dari pengguna
        bing = int(input("Masukan nilai BING"))  # Meminta nilai BING dari pengguna

        mahasiswa.append(name)  # Menambahkan nama mahasiswa ke dalam list 'namamahasiswa'
        nilai_pemror.append(pemror)  # Menambahkan nilai PEMROR ke dalam list 'nilaipemror'
        nilai_matdis.append(matdis)  # Menambahkan nilai MATDIS ke dalam list 'nilaimatdis'
        nilai_bing.append(bing)  # Menambahkan nilai BING ke dalam list 'nilaibing'

        print("nilai berhasil di inputkan")  # Menampilkan pesan bahwa nilai berhasil diinputkan
        print_line()  # Mencetak garis pemisah

        # Meminta pengguna untuk memasukkan data lagi atau tidak
        if input("Tambah data lagi atau tidak ? [yes]/[no]").lower() == "n":
            break  # Keluar dari loop jika pengguna memasukkan 'n'

        pause()  # Menghentikan sementara eksekusi program
        menu()  # Kembali ke menu utama

        # Fungsi untuk menampilkan daftar nilai mahasiswa
        def daftar_nilai():
            clear_screen()  # Membersihkan layar
            cover()  # Menampilkan judul program
            print_line()  # Mencetak garis pemisah
            print(f"| {'NO':>3} | {'NAMA':>20} | {'PEMROR':>15} | {'MATDIS':>15} | {'BING':>15} |")  # Header tabel
            print_line()  # Mencetak garis pemisah

            for i, nama in enumerate(siswa):  # Looping untuk menampilkan data mahasiswa dan nilai
                print(f"| {i + 1:>3} | {nama:>20} | {nilaipemror[i]:>15} | {nilaimatdis[i]:>15} | {nilaibing[i]:>15} |")  # Menampilkan data mahasiswa
                print("-" * 74)  # Mencetak garis pemisah
            print_line()  # Mencetak garis pemisah
            pause()  # Menghentikan sementara eksekusi program
            menu()  # Kembali ke menu utama
            
# Fungsi untuk menghitung rata-rata nilai per mahasiswa
def hitung_rata_rata():
    return [(nilaipemror[i] + nilaimatdis[i] + nilaibing[i]) / 3 for i in range(len(namamahasiswa))]  # Menghitung rata-rata setiap mahasiswa

# Fungsi untuk menentukan grade berdasarkan rata-rata
def tentukan_grade():
    ratamhs = hitung_rata_rata()  # Memanggil fungsi 'hitung_rata_rata' untuk mendapatkan rata-rata setiap mahasiswa
    grademhs = []  # Daftar kosong untuk menyimpan grade
    for rata in ratamhs:  # Looping untuk menentukan grade berdasarkan rata-rata
        if rata >= 85:
            grademhs.append("A")
        elif rata >= 70:
            grademhs.append("B")
        elif rata >= 50:
            grademhs.append("C")
        else:
            grademhs.append("D")
    return grademhs  # Mengembalikan daftar grade

# Fungsi untuk menampilkan rata-rata setiap mata kuliah
def rata_rata_mata_kuliah():
    clear_screen()  # Membersihkan layar
    cover()  # Menampilkan judul program
    rata_pemror = sum(nilaipemror) / len(nilaipemror) if nilaipemror else 0  # Menghitung rata-rata PEMROR
    rata_matdis = sum(nilaimatdis) / len(nilaimatdis) if nilaimatdis else 0  # Menghitung rata-rata MATDIS
    rata_bing = sum(nilaibing) / len(nilaibing) if nilaibing else 0  # Menghitung rata-rata BING

    # Menampilkan tabel rata-rata nilai per mata kuliah
    print(f"| {'NO':>3} | {'MATA KULIAH':<20} | {'NILAI RATA-RATA':>20} |")
    garis()
    for i, matkul in enumerate(["PEMROR", "MATDIS", "BING"]):  # Looping untuk setiap mata kuliah
        rata = [rata_pemror, rata_matdis, rata_bing][i]  # Mengambil rata-rata untuk mata kuliah saat ini
        print(f"| {i + 1:>3} | {matkul:<20} | {rata:>20.2f} |")  # Menampilkan data
        print("-" * 74)  # Garis pemisah antar baris
    garis()
    pause()  # Menghentikan sementara eksekusi program
    menu()  # Kembali ke menu utama

# Fungsi utama untuk memulai program
if __name__ == "__main__":
    menu()  # Menampilkan menu utama program
