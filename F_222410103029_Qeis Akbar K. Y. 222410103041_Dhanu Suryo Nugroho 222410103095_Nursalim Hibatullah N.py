import os # Memanggil modul operating system
import csv # Memanggil file csv untuk dijalankan dalam program
from datetime import date # Memanggil modul tanggal dan waktu
import time # Memanggil modul waktu

jenispanen = [] # List kosong untuk menampung data jenis tanaman yang dipilih user
jumlahpanen = [] # List kosong untuk menampung data jumlah tanaman yang dipanen user
berattotal = [] # List kosong untuk menampung data berat total panen user
bulanKe = [] # List kosong untuk menampung data bulan yang diinginkan user
tanggal = [] # List kosong untuk menampung data tanggal pemanenan

fileName = "datapanen.csv" # Variabel nama file csv

def clearscreen(): # Fungsi untuk membersihkan terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def awal() :
    clearscreen() # Memenjalankan fungsi clearscreen untuk membersihkan terminal
    print("=" * 100) # Mencetak batas untuk judul
    print("Selamat Datang di 'Panenku'".center(100)) # Mencetak judul dengan posisi center terhadap 100
    print("=" * 100) # Mencetak batas untuk judul
    print(" [1] Login\n [2] Registrasi") # Mencetak pilihan login atau registrasi
    pilihAwal = input(" PILIH MENU [angka]: ") # Menginput pilihan login atau registrasi
    clearscreen() # Memenjalankan fungsi clearscreen untuk membersihkan terminal
    if pilihAwal == "1": # Jika pilihan sama dengan 1 maka diarahkan pada fungsi login
        login() # Program akan menjalankan fungsi login
    elif pilihAwal == "2": # Jika pilihan sama dengan 1 maka akan diarahkan pada fungsi regristasi
        registrasi() # Program akan menjalankan fungsi registrasi
    else: # Jika pilihan selain 1 dan 2 maka diarahkan pada fungsi awal kembali
        print('Nomor yang diinputkan SALAH. Input sesuai NOMOR yang TERSEDIA, ya!') # Mencetak pernyataan bahwa inputan salah dan user diperintahkan untuk menginput nomor yang tersedia
        time.sleep(1.5) # Memberikan jeda selama 1,5 detik sebelum menampilakn fungsi awal
        awal() # Menjalankan fungsi awal

def login(): # Fungsi login
    print(" LOGIN ".center(100,"=")) # Mencetak login dan = yang diposisikan center terhadap 100 
    user = input ("Masukkan Username Anda : ") # Menginputkan username
    sandi = input ("Masukkan Password Anda : ") # Menginputkan password
    if user == "admin" and sandi == "12345": # Jika var. user sama dengan "admin" dan var. sandi sama dengan "12345", maka user akan dinyatakan berhasil login
        print (" Anda BERHASIL Login ".center(100, "-")) # Mencetak pernyataan berhasil login dan "-" yang diposisikan center terhadap 100 bulan 
        print("=" *100) # Mencetak batas berupa"=" sebanyak 100 kali
        time.sleep(1.5) # Memberikan jeda selama 1,5 detik sebelum perintah selanjutnya
        menu() # Menjalankan fungsi menu
    else : # Jika selain var. user sama dengan "admin" dan var. sandi sama dengan "12345", maka user dinyatakan gagal login
        print ("USERNAME atau PASSWORD yang Anda masukkan SALAH".center(100, "-")) # Mencetak pernyataan bahwa username atau password salah dan "-" yang diposisikan center terhadap 100 bulan
        print("=" *100) # Mencetak batas berupa"=" sebanyak 100 kali
        time.sleep(1.5) # Memberikan jeda selama 1,5 detik sebelum menampilkan fungsi awal
        awal() # Menjalankan fungsi awal

def registrasi(): #fungsi registrasi
    print(" REGISTRASI ".center(100,"=")) # Mencetak registrasi dan = yang diposisikan center terhadap 100
    nama = input("Masukkan Nama Anda      : " ) # Menginputkan nama
    telepon = int(input ("Masukkan No. Telp. Anda : ")) # Menginputkan nomor telpon
    user = input ("Masukkan Username Anda  : ") # Menginputkan username
    sandi = input ("Masukkan Password Anda  : ") # Menginputkan password
    if nama != "" and telepon != "" and user != "" and sandi != "" and user != "admin" and sandi != "12345" : # Jika nama, no telp, user, dan, sandi tidak sama dengan kosong dan user tidak sama dengan "admin" dan sandi tidak sama dengan "12345", maka...
        print (" Registrasi akun Anda BERHASIL ".center(100, "-")) # Mencetak pernyataan registrasi berhasil dan "-" yang diposisikan center terhadap 100 bulan 
        print("=" *100) # Mencetak batas berupa "=" sebanyak 100 kali
        time.sleep(1.5) # Memberikan jeda selama 1,5 detik sebelum menampilkan fungsi awal
        menu() # Menjalankan fungsi menu
    else :
        print(" Registrasi akun Anda GAGAL. Masukkan DATA dengan BENAR ".center(100, "-")) # Mencetak pernyataan bahwa registrasi gagal dan "-" yang diposisikan center terhadap 100 bulan
        print("=" *100) # Mencetak batas berupa "=" sebanyak 100 kali
        time.sleep(1.5) # Memberikan jeda selama 1,5 detik sebelum menampilkan fungsi awal
        awal() # Menjalankan fungsi awal

def menu(): #fungsi menu
    clearscreen() # Menjalankan fungsi clearscreen untuk membersihkan terminal
    print("="*100) # Mencetak batas berupa "=" sebanyak 100 kali
    print(" Selamat Datang 'Farms'! ".center(100,"-")) # Mencetak judul dan "-" dengan posisi center terhadap 100 bulan
    print("="*100) # Mencetak batas berupa "=" sebanyak 100 kali
    print(" [1] Daftar Tanaman\n [2] Menghitung Jumlah Panen\n [3] Hapus Jumlah Panen\n [4] Riwayat\n [5] Logout") # Mencetak pilihan menu
    pesan = input('PILIH MENU [angka] \n>>> ') # Menginputkan pilihan menu
    clearscreen() # Menjalankan fungsi clearscreen untuk membersihkan terminal
    if pesan == '1': # Jika pesan sama dengan 1, maka akan diarahkan pada fungsi daftar_tanaman
        daftar_tanaman() # Program akan menjalankan fungsi daftar tanaman
        input("Tekan ENTER untuk mulai menghitung") # Meminta inputan enter untuk kemudian user diarahkan pada pemesanan sesuai menu
        panen() # Fungsi panen dijalankan
    elif pesan == '2': # Jika pesan sama dengan 1, maka akan diarahkan pada fungsi pesnanan
        panen() # Program akan menjalankan fungsi panen
    elif pesan == '3': # Jika pesan sama dengan 1, maka akan diarahkan pada fungsi hapus
        hapus() # Program akan menjalankan fungsi hapus
    elif pesan == '4': # Jika pesan sama dengan 1, maka akan diarahkan pada fungsi riwayatPanen
        riwayatPanen() # Program akan menjalankan fungsi daftar tanaman
        kembaliTampilan() # Menjalankan fungsi kembaliTampilan untuk kembali ke tampilan menu 
    elif pesan == "5": # Jika pesan sama dengan 1, maka akan diarahkan pada fungsi logout
        logout() # Program akan menjalankan fungsi logout
    else: # Jika pesan tidak sama dengan 1, 2, 3, 4, atau 5, maka diarahkan pada tampilan awal menu
        print("-" *100) # Mencetak batas berupa "-" sebanyak 100 kali
        print('MENU yang dipilih TIDAK TERSEDIA. NOMOR yang diinputkan SALAH!')
        print("=" *100) # Mencetak batas berupa "=" sebanyak 100 kali
        time.sleep(1.5) # Memberikan jeda selama 1,5 detik sebelum menampilakn fungsi awal
        menu() # Menjalankan fungsi menu

def daftar_tanaman(): # Fungsi daftar tanaman
    clearscreen() # Menjalankan fungsi clearscreen untuk membersihkan terminal
    print(" DAFTAR TANAMAN ".center(100,"=")) # Mencetak judul daftar tanaman dan "=" dengan posisi center terhadap 100 bulan
    print(            
        " [1] Padi\n"
        " [2] Jagung\n"
        " [3] Tembakau") # Mencetak daftar pilihan tanaman dengan tambahan tab dan enter untuk memberi tampilan yang rapi
    print("-" *100) # Mencetak batas berupa "-" sebanyak 100 kali
    print("-" *100) # Mencetak batas berupa "-" sebanyak 100 kali

def panen(): # Fungsi panen
    daftar_tanaman() # Menjalankan fungsi daftar tanaman
    no = input("Panen Ke\t\t\t\t\t: ") # Menginputkan urutan panen user
    item = input("Pilih Nama Tanaman [angka sesuai DAFTAR]\t: ") # Menginputkan pilihan tanaman
    if item == "1": # Jika item sama dengan 1, maka pilihan nomor 1 pada menu akan diinputkan pada data
        tanaman = "Padi" # Var tanaman berisi "Padi"
        berat = 33 # Var berat berisi 33
    elif item == "2": # Jika item sama dengan 2, maka pilihan nomor 2 pada menu akan diinputkan pada data
        tanaman = "Jagung" # Var tanaman berisi "Jagung"
        berat = 25 # Var berat berisi 25
    elif item == "3": # Jika item sama dengan 3, maka pilihan nomor 3 pada menu akan diinputkan pada data
        tanaman = "Tembakau" # Var tanaman berisi "Tembakau"
        berat = 6 # Var berat berisi 6
    else : # Jika item tidak sama dengan 1, 2, atau 3, maka user akan diarahkan pada menu awal
        print("-" *100) # Mencetak batas berupa "-" sebanyak 100 kali
        print("Maaf, PILIHAN Anda TIDAK TERSEDIA. Silakan PILIH SESUAI DAFTAR yang ada.")
        print("=" *100) # Mencetak batas berupa "=" sebanyak 100 kali
        time.sleep(2) # Memberikan jeda selama 2 detik sebelum menampilkan fungsi menu
        menu() # Menjalankan fungsi menu

    jumlah = int(input("Jumlah Karung\t\t\t\t\t: ")) # Menginputkan jumlah tanaman yang diperoleh, yang akan dikalikan dengan berat rata-rata perkarung
    bulan = input("Bulan\t\t\t\t\t\t: ") # Menginputkan bulan yang diinginkan sebagai tanda kapan diperolehnya
    totalberat = jumlah * berat

    jenispanen.append(tanaman) # Menambahkan isi dari var tanaman ke dalam list jenispanen
    jumlahpanen.append(int(jumlah)) # Menambahkan isi dari var jumlah ke dalam list jumlahpanen
    bulanKe.append(bulan) # Menambahkan isi dari var bulan ke dalam list bulanKe
    berattotal.append(int(totalberat)) # Menambahkan isi dari var totalberat ke dalam list berattotal
    tanggal.append(dates())
    print(
        f'\nAnda menambahkan tanaman {tanaman} sebanyak {jumlah} pada {bulan} dengan total berat {totalberat} \nke dalam daftar panen') # Memberikan penjelasan kembali apa yang telah user pilih pada menu

    with open(fileName, 'a', newline='') as file: # Membuka dan menambahkan data pada file csv
        kolom = ['NO', 'TANGGAL', 'NAMA TANAMAN',  'BULAN', 'KARUNG', 'BERAT'] # Variabel dengan nama kolom yang berisi key dari data
        writer = csv.DictWriter(file, delimiter=",", fieldnames=kolom) # Variabel writer yang berisi pembacaan data pada file csv
        list_baru = {'NO' : no, 'TANGGAL' : dates(), 'NAMA TANAMAN' : tanaman, 'BULAN' : bulan, 'KARUNG' : jumlah, 'BERAT' : totalberat } # Variabel berisi key dan valuenya
        writer.writerow(list_baru) # Variabel berisi data key
    riwayatPanen() # Menjalankan fungsi riwayatPanen untuk menampilkan daftar tanaman yang dipanen
    kembaliTampilan() # Menjalankan fungsi kembaliTampilan untuk kembali ke menu 

def kembaliTampilan(): # Fungsi kembali ke tampilan menu
    input("\nSilakan tekan ENTER untuk kembali ke Menu.") #menginput enter agar kemudian dapat diarahkan pada fungsi menu
    menu() # Menjalankan fungsi menu

def dates(): # Fungsi tanggal
    objek = date.today() 
    hari = (str(objek.day)+"-"+str(objek.month)+"-"+str(objek.year)) 
    return hari

def riwayatPanen(): # Fungsi riwayatPanen untuk menampilkan daftar tanaman yang dipanen
    print('=' * 100) # Mencetak batas berupa "=" sebanyak 100 kali
    tanggal = dates() 
    ket = ["NO", "TANGGAL", "NAMA TANAMAN", "BULAN", "KARUNG", "BERAT"]  # Variabel dengan nama ket yang berisi key dari data
    print(f'|| {ket[0]:<3}| {ket[1]:<13}| {ket[2]:<25}| {ket[3]:<25}| {ket[4]:<8}|{ket[5]:>11} ||') # Mencetak key setiap indeks
    print('='*100)
    for x in range(len(jenispanen)): # Untuk setiap x dalam range panjang list jenispanen
        print(
            f'|| {x+1:<3}| {tanggal:<13}| {jenispanen[x]:<25}| {bulanKe[x]:<25}| {jumlahpanen[x]:<8}|{berattotal[x]:>11} ||') # Mencetak value setiap indeks sesuai keynya
    print('='*100) # Mencetak batas berupa "=" sebanyak 100 kali

def hapus(): # Fungsi hapus
    riwayatPanen() # Menjalankan fungsi riwayatPanen untuk menampilkan daftar tanaman yang dipanen
    tanggal = dates()
    with open(fileName, mode='w', newline='') as file: # Membuka serta menulis pada fule csv
        writer = csv.writer(file, delimiter=',') # Variabel writer yang berisi pembacaan data pada file csv
        hapus = int(input('Pilih nomor: ')) - 1 # Menginputkan nomor yang akan dihapus dengan pengurangan -1 karena indeks sistem dimulai dari nol
        jenispanen.pop(hapus) # Menghapus indeks ke "hapus" dari list jenispanen
        jumlahpanen.pop(hapus) # Menghapus indeks ke "hapus" dari list jumlahpanen
        bulanKe.pop(hapus) # Menghapus indeks ke "hapus" dari list bulanKe
        berattotal.pop(hapus) # Menghapus indeks ke "hapus" dari list berattotal
        for i in range(len(jenispanen)): # Untuk setiap i dalam range panjang list jenispanen
            newFile = [i+1, tanggal, jenispanen[i], bulanKe[i], jumlahpanen[i], berattotal[i]]
            writer.writerow(newFile)
        file.close() # Menutup file
        print('Hapus Jumlah Panen'.center(100,"-")) # Mencetak kalimat bahwa penghapusan yang dilakukan telah berhasil
        kembaliTampilan() # Menjalankan fungsi kembaliTampilan untuk kembali ke tampilan menu 

def logout(): # Fungsi logout untuk menghentikan program
    keluar = input("Apakah Anda yakin keluar dari program? [y/t] : ") # Menginput y atau t
    if keluar == "y" or keluar == "Y":  # Jika keluar sama dengan y atau Y, maka user diarahkan pada pemberhentian program
        print("-" * 100) # Mencetak batas berupa "-" sebanyak 100 kali
        print(" ANDA BERHASIL LOGOUT ".center(100, "=")) # Mencetak pernyataan dan "=" dengan posisi center terhadap 100 bulan
        quit # Menghentikan program
    elif keluar == "t" or keluar == "T": # Jika keluar sama dengan t atau T, maka usr akan diarahkan pada tampilan menu awal program
        time.sleep(1.5)
        menu() # Program akan menjalankan fungsi menu
    else: # Jika keluar selain y, Y, t, atau T, maka user akan diarahkan pada menu tampilan awal
        print("MENU yang Anda pilih TIDAK TERSEDIA") # Mencetak pernyataan dari inputan user yang tidak sesuai
        kembaliTampilan() # Menjalankan fungsi kembaliTampilan untuk kembali ke tampilan menu 

awal() # Memanggil atau menampilkan fungsi awal