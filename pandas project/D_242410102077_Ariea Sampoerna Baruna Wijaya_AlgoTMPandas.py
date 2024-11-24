import pandas as pd
import numpy as np

# Informasi pemilik program
print(f"Pemilik Program\nNAMA: Ariea Sampoerna Baruna Wijaya\nNIM: 242410102077\nKELAS: ALGO D")
print(" ")

# Menghasilkan 10 nilai acak antara 70 hingga 90 dan disimpan ke dalam list
np.random.seed(0)
nilai_acak = list(np.random.randint(70, 91, size=10))

# Menentukan status nilai dan menyimpannya dalam list
status = ["Sangat memuaskan" if nilai >= 75 else "Cukup" for nilai in nilai_acak]

# Membuat data untuk kolom NIM, nilai, dan status nilai
data = {
    'nim': [f'2424101020{i+1}' for i in range(10)],  # Membuat NIM untuk 10 data
    'nilai': nilai_acak,
    'status_nilai': status
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)
print("Data Frame Awal:")
print(df)
print(" ")

# Mengurutkan DataFrame berdasarkan kolom nilai dari yang terbesar
df_urut = df.sort_values(by='nilai', ascending=False)
print("Data Frame yang urut Berdasarkan Nilai:")
print(df_urut)
