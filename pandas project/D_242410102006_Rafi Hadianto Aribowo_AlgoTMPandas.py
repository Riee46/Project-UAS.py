import pandas as pd
import numpy as np

print(f"Pemilik Program\nNAMA: Rafi Hadianto Aribowo\nNIM:242410102006\nKELAS:ALGO D")
print(" ")

np.random.seed(0)
nilai_acak = list(np.random.randint(70, 91, size = 10)) #Menghasilkan 10 nilai acak antara 70 hingga 90 dan disimpan ke dalam list

#Menentukan status nilai dan disimpan ke dalam list
status = [] 
for nilai in nilai_acak:
    if nilai >= 75:
        status.append('Sangat memuaskan')
    else:
        status.append('Cukup')
#perulangan membuat NIM1 hingga 10
data = {
    'nim': [f'2424101020{i+1}' for i in range(10)],
    'nilai': nilai_acak,
    'status_nilai': status
} 

#membuat dataframe dari list
df = pd.DataFrame(data)
print("data frame:")
print(df)
print(" ")

#Mengurutkan dataframe berdasarkan kolom nilai yang terbesar
df_urut = df.sort_values(by='nilai', ascending=False) 
print("data frame sorted")
print(df_urut)