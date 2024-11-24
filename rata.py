import os 

# Data Kosong
list_mahasiswa = []
list_matakuliah = ["Matematika", "Etika Profesi", "Pemrograman"]
list_nilaimtk = []
list_nilaietika = []
list_nilaipemro = []

def garis():
    print("-"*50)

# inputan Data Mahasiswa
def data_mahasiswa():
    while True:
        mahasiswa = input("Masukkan nama mahasiswa: ",)
        mahasiswa = mahasiswa.title().strip()
        list_mahasiswa.append(mahasiswa)

        while True:
            try:
                ana = int(input("Masukkan Nilai Matematika: "))
                ani = int(input("Masukkan Nilai Etika Profesi: "))
                anu = int(input("Masukkan Nilai Pemrograman: ")) 
                break
            except ValueError:
                print("Masukkan Nilai yang benar")

        list_nilaimtk.append(ana)
        list_nilaietika.append(ani)
        list_nilaipemro.append(anu)
        choice = input("Tambahkan data mahasiswa lain? [y/n]: ")

        while True:
            try:
                if choice == "y":
                    break
                elif choice == "n":
                    return
            except TypeError:
                print("Pilih [y] atau [n]")

def rata_individu():
    rataind = []
    for i in range (len(list_nilaimtk)):
        total = list_nilaimtk[i] + list_nilaietika[i] + list_nilaietika[i]
        rata = total/len(list_matakuliah)
        rataind.append(rata)
    return rataind

def penentuan_grade(nilai):
    if nilai >= 85:
        grade = "A"
    elif nilai >= 70 < 85:
        grade = "B"
    elif nilai >= 50 < 70:
        grade = "C"
    elif nilai < 50:
        grade = "D"

    return grade

def rata_matkul():
    ratamatkul = []
    ratamtk = sum(list_nilaimtk)/len(list_nilaimtk)
    rataetika = sum(list_nilaietika)/len(list_nilaietika)
    ratapemro = sum(list_nilaipemro)/len(list_nilaipemro)

    ratamatkul.append(ratamtk)
    ratamatkul.append(rataetika)
    ratamatkul.append(ratapemro)

def tampilkan_laporan():
    garis()
    print("Nama Mahasiswa", "|", "Rata-rata", "|", "Grade")
    garis()

    

while True:
    print("""
    Hai Mahasiswa!!
    1. Tambahkan Data Mahasigma
    2. Tampilkan Rapot Mahasigma
    3. Exit
    """)
    try:
        pilih = int(input("Silahkan pilih menu [1/2/3]: "))
    except ValueError:
        print("Dimohon memasukkan pilihan yang benar")
    else:
        if pilih == 1:
            data_mahasiswa()
        # elif pilih == 2:
        #     tampilkan_laporan()
        # elif pilih == 3:
        #     exit()