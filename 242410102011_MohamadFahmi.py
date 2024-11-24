# Nama : mohammad Fahmi Nazmuddin
# NIM  : 242410102011
# Kelas : D (tatap muka)
# TUGAS MANDIRI SISTEM PENILAIAN SEDERHANA



def input_siswa():
    while True: # disini memakai while true untuk  memastikan loop terus dijalankan hingga inputan valid didapat

        ulang = input("Masukkan jumlah mahasiswa: ") # input ulang dimasukkan sebagai string, kemudian diubah menjadi integer
        try:
            ulang = int(ulang)
            if ulang <1:
                print("Minimal input 1 data") # jika input kurang dari 1, pesan akan menampilkan dan meminta input ulang
                continue
            return ulang
        except ValueError: # jika input tidak dapat diubah menjadi integer, maka menghasilkan ValueError, dan program akan menampilkan pesan (inputan harus berupa angka)
            print("inputan harus berupa angka")
def input_nama():
    while True:
        nama = input("Nama: ")
        if nama.isalpha():  # pengecekan nama menggunakan huruf, hanya memastikan jika nama hanya berisi huruf saja
            return nama
        else:
            print("Nama hanya boleh huruf")

def input_nilai(mata_kuliah):
     while True:
        try:
            nilai = float(input(f"Nilai {mata_kuliah}: "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 dan 100")
        except ValueError:
            print("Inputan harus berupa angka")

def hitung_rata_rata(a,b,c):
    avgNilai = (a+b+c)/3
    return avgNilai

def rata_rata_mata_kuliah (data):
    # menjabarkan nilai awal variabel rata-rata
    rata_Mat = rata_Bing = rata_Pemro = 0  
    # memakai perulangan yang berguna untuk menghitung total nilai setiap mata kuliah
    for i in data:
        rata_Mat += i[1]
        rata_Bing += i[2]
        rata_Pemro += i[3]
    # total rata-rata setiap mata kuliah (rumus jumlah data dibagi banyak data)
    rata_Mat /= len(data)
    rata_Bing /= len(data)
    rata_Pemro /= len(data)
    # setelah total rata-rata kemudian menyimpan nilai rata-rata mata kuliah pada list avgKuliah
    rata_kuliah = [rata_Mat, rata_Bing, rata_Pemro]
    return rata_kuliah

def tentukan_grade (avgNilai):
    if 85 <= avgNilai <= 100:
        grade = "A"
    elif 70 <= avgNilai < 85:
        grade = "B"
    elif 50 <= avgNilai < 70:
        grade = "C"
    elif 0 <= avgNilai < 50:
        grade = "D"
    return grade

def tampilkan_laporan(avgKuliah,data):
    # menggunakan perulangan untuk print nama mahasiswa, matkul, dan nilai masing-masing mahasiswa
    for i in data:
        print("Nama Mahasiswa:",i[0])
        print("Mata Kuliah: Matematika, Bahasa Inggris, Pemrograman")
        print(f"Nilai: {i[1]}, {i[2]}, {i[3]}\n")

    print("Laporan Nilai Mahasiswa:")
    print("-"*40)
    print("Nama Mahasiswa\t| Rata-rata\t| Grade")
    print("-"*40)

    # perulangan untuk print rata-rata dan grade masing-masing mahasiswa
    for i in data:
        # memanggil fungsi untuk menghitung rata-rata mahasiswa
        # menggunakan argumen nilai setiap matkul yang tersimpan dalam list data
        rata_siswa = hitung_rata_rata(i[1], i[2], i[3])  
        # memanggil fungsi untuk penentuan grade mahasiswa
        # menggunakan argumen nilai rata-rata mahasiswa, variabel hasil dari fungsi hitung_rata_rata
        grade = tentukan_grade(rata_siswa)
        print(f"{i[0]}\t\t| {rata_siswa:.2f}\t\t| {grade}")
        # ( :.2f ) digunakan memastikan hanya dua angka desimal yang ditampilkan

    # menampilkan rata-rata tiap matkul yang tersimpan pada list avgKuliah
    print("\nRata-rata Nilai Per Mata Kuliah:")
    print("-"*40)
    print(f"Matematika\t| {avgKuliah[0]:.2f}")
    print(f"Bahasa Inggris\t| {avgKuliah[1]:.2f}")
    print(f"Pemrograman\t| {avgKuliah[2]:.2f}")

data = [] # penjabaran untuk list kosong

# memanggil fungsi untuk proses inputan
ulang = input_siswa() # memanggil fungsi untuk menentukan jumlah mahasiswa yang akan diinput
for i in range(ulang): # loop for meminta data nama dan nilai setiap mahasiswa
    nama = input_nama()
    Mat = input_nilai("Matematika")
    Bing = input_nilai("Bahasa Inggris")
    Pemro = input_nilai("Pemrograman")
    print()
    # memasukkan semua inputan kedalam satu list data
    data.append([nama, Mat, Bing, Pemro])

avgKuliah = rata_rata_mata_kuliah(data) 
tampilkan_laporan(avgKuliah,data) # Setelah semua data diinputkan, (rata_rata_mata_kuliah(data)) menghitung rata-rata nilai tiap mata kuliah, dan (tampilkan_laporan(avgKuliah, data)) menampilkan laporan lengkap
