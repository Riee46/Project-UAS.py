import os  # Mengimpor modul os untuk menyediakan perintah yang berguna, seperti membersihkan layar.

# Deklarasi list untuk menyimpan data mahasiswa dan nilai tiap mata kuliah.
namamahasiswa = []  # List untuk nama mahasiswa
nilaipemro = []     # List untuk nilai mata kuliah Pemrograman
nilaimatdas = []    # List untuk nilai mata kuliah Matematika Dasar
nilaimatdis = []    # List untuk nilai mata kuliah Matematika Diskrit
matkul = ["PEMRO", "MATDAS", "MATDIS"]  # List nama mata kuliah

# Fungsi untuk membersihkan layar konsol
def clear():
    os.system("cls" if os.name == "nt" else "clear")  # Membersihkan layar konsol, tergantung sistem operasi.

# Fungsi untuk membuat garis pembatas
def garis():
    print("=" * 74)  # Mencetak garis horizontal sepanjang 74 karakter untuk membatasi tampilan.

# Fungsi untuk menampilkan judul program
def cover():
    garis()  # Memanggil fungsi garis sebagai pembatas atas
    print("\t\t       SISTEM PENILAIAN SEDERHANA")  # Menampilkan judul program
    garis()  # Memanggil fungsi garis sebagai pembatas bawah

# Fungsi untuk meminta pengguna menekan ENTER
def enter():
    input("Tekan [ENTER] untuk melanjutkan")  # Menunggu pengguna menekan ENTER sebelum melanjutkan.

# Fungsi menu utama
def menu():
    clear()  # Membersihkan layar
    cover()  # Menampilkan judul program
    print("""
    MENU :
    1. INPUT NILAI MAHASISWA 
    2. DAFTAR NILAI MAHASISWA
    3. NILAI RATA RATA MATAKULIAH KESELURUHAN
    4. LAPORAN AKHIR
    5. TENTANG PEMBUAT PROGRAM
    6. KELUAR PROGRAM   
    """)  # Menampilkan menu pilihan untuk pengguna
    garis()  # Membatasi bagian pilihan menu

    # Input pilihan menu
    try:
        pilih = int(input("Masukkan pilihan program >> "))  # Mengambil pilihan dari pengguna
        if pilih == 1:
            inputan()  # Memanggil fungsi input data mahasiswa
        elif pilih == 2:
            daftar_nilai()  # Memanggil fungsi daftar nilai mahasiswa
        elif pilih == 3:
            rata_rata_mata_kuliah()  # Memanggil fungsi rata-rata nilai tiap mata kuliah
        elif pilih == 4:
            tampilkan_laporan()  # Memanggil fungsi laporan akhir
        elif pilih == 5:
            pembuat()  # Memanggil fungsi tentang pembuat program
        elif pilih == 6:
            clear()
            print("Terima kasih telah menggunakan program ini.")  # Menampilkan pesan keluar program
        else:
            print("Pilihan tidak tersedia!")  # Pesan error jika pilihan tidak ada
            enter()
            menu()
    except ValueError:
        print("Masukkan angka yang valid.")  # Menangani error jika input bukan angka
        enter()
        menu()

# Fungsi untuk input data mahasiswa dan nilai
def inputan():
    while True:
        clear()  # Membersihkan layar
        cover()  # Menampilkan judul program
        namamhs = input("Masukkan nama mahasiswa : ").upper()  # Input nama mahasiswa
        a = int(input("Masukkan nilai PEMRO : "))  # Input nilai mata kuliah Pemrograman
        b = int(input("Masukkan nilai MATDAS : "))  # Input nilai mata kuliah Matematika Dasar
        c = int(input("Masukkan nilai MATDIS : "))  # Input nilai mata kuliah Matematika Diskrit

        # Menyimpan data yang diinputkan ke dalam list
        namamahasiswa.append(namamhs)  # Menyimpan nama mahasiswa
        nilaipemro.append(a)  # Menyimpan nilai Pemrograman
        nilaimatdas.append(b)  # Menyimpan nilai Matematika Dasar
        nilaimatdis.append(c)  # Menyimpan nilai Matematika Diskrit
        
        print("Nilai berhasil diinputkan")  # Menampilkan pesan bahwa nilai berhasil disimpan
        garis()  # Membatasi tampilan

        # Meminta konfirmasi untuk menambah data lagi
        pilih = input("Tambah data lagi atau tidak? [y/t] >> ").lower()  # Konfirmasi untuk mengulang input data
        if pilih != "y":  # Jika jawaban selain 'y', keluar dari loop
            break
    enter()
    menu()

# Fungsi untuk menampilkan daftar nilai mahasiswa
def daftar_nilai():
    clear()  # Membersihkan layar
    cover()  # Menampilkan judul program

    # Header tabel untuk daftar nilai
    print(f"| {'NO':>3} | {'NAMA MAHASISWA':<20} | {'NILAI PEMRO':>10} | {'NILAI MATDAS':>10} | {'NILAI MATDIS':>10} |")
    garis()  # Membuat garis pembatas di bawah header

    # Isi tabel dari data mahasiswa
    for i, nama in enumerate(namamahasiswa):  # Loop untuk setiap mahasiswa
        print(f"| {i + 1:>3} | {nama:<20} | {nilaipemro[i]:>10} | {nilaimatdas[i]:>10} | {nilaimatdis[i]:>10} |")
        print("-" * 74)  # Membatasi setiap baris data
    garis()  # Garis pembatas akhir
    enter()
    menu()

# Fungsi untuk menghitung rata-rata nilai per mahasiswa
def hitung_rata_rata():
    # Mengembalikan list yang berisi rata-rata tiap mahasiswa
    return [(nilaipemro[i] + nilaimatdas[i] + nilaimatdis[i]) / 3 for i in range(len(namamahasiswa))]

# Fungsi untuk menentukan grade berdasarkan nilai rata-rata
def tentukan_grade():
    ratamhs = hitung_rata_rata()  # Mengambil list rata-rata tiap mahasiswa
    grademhs = []  # Menyimpan grade tiap mahasiswa
    for rata in ratamhs:
        if rata >= 85:
            grademhs.append("A")
        elif rata >= 70:
            grademhs.append("B")
        elif rata >= 50:
            grademhs.append("C")
        else:
            grademhs.append("D")
    return grademhs

# Fungsi untuk menghitung rata-rata nilai setiap mata kuliah
def rata_rata_mata_kuliah():
    clear()
    cover()

    # Menghitung rata-rata tiap mata kuliah
    rata_pemro = sum(nilaipemro) / len(nilaipemro) if nilaipemro else 0
    rata_matdas = sum(nilaimatdas) / len(nilaimatdas) if nilaimatdas else 0
    rata_matdis = sum(nilaimatdis) / len(nilaimatdis) if nilaimatdis else 0

    # Menampilkan rata-rata tiap mata kuliah dalam tabel
    print(f"| {'NO':>3} | {'MATA KULIAH':<20} | {'NILAI RATA-RATA':>20} |")
    garis()
    for i, matkul in enumerate(["PEMRO", "MATDAS", "MATDIS"]):
        rata = [rata_pemro, rata_matdas, rata_matdis][i]
        print(f"| {i + 1:>3} | {matkul:<20} | {rata:>20.2f} |")
        print("-" * 74)
    garis()
    enter()
    menu()

# Fungsi untuk menampilkan laporan akhir nilai rata-rata dan grade
def tampilkan_laporan():
    clear()
    cover()

    ratamhs = hitung_rata_rata()  # List rata-rata tiap mahasiswa
    grade = tentukan_grade()  # List grade tiap mahasiswa

    # Header tabel
    print(f"| {'NO':>3} | {'NAMA MAHASISWA':<25} | {'NILAI RATA-RATA':>15} | {'GRADE':>6} |")
    garis()

    # Menampilkan nama, rata-rata, dan grade tiap mahasiswa
    for i, nama in enumerate(namamahasiswa):
        print(f"| {i + 1:>3} | {nama:<25} | {ratamhs[i]:>15.2f} | {grade[i]:>6} |")
        print("-" * 74)
    garis()
    enter()
    menu()

# Fungsi untuk menampilkan informasi pembuat program
def pembuat():
    clear()
    cover()
    print("""
PEMBUAT PROGRAM :
NAMA  : ARIEA SAMPOERNA BARUNA WIJAYA
PRODI : TEKNOLOGI INFORMASI - UNIVERSITAS JEMBER
NIM   : 242410102077
""")  # Menampilkan informasi pembuat program
    garis()
    enter()
    menu()

# Fungsi utama untuk menjalankan program
if __name__ == "__main__":
    menu()
