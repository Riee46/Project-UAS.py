# Input string
message = "saya sangat senang menjadi manusia"

# Remove spaces for counting characters
message = message.replace(" ", "")

# Initialize dictionary to store frequency of characters
char_frequency = {}

# Count frequency of each character
for char in message:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Print the results
for char, frequency in char_frequency.items():
    print(f"Huruf: {char} : Jumlah: {frequency}")



    pesan = "kapal laud"
pesan = pesan.replace(" ", "")

frekuensi_chara = {}

for chara in pesan:
    if chara in frekuensi_chara :
        frekuensi_chara[chara] += 1
    else:
        frekuensi_chara[chara] = 1

for chara, frekuensi in frekuensi_chara.items():
    print(f"Huruf: {chara} : Jumlah: {frekuensi}")

    pesan = "aku siapa"
pesan = pesan.replace(" ", "")

frekuensi_chara = {}

for chara in pesan:
    if chara in frekuensi_chara :
        frekuensi_chara[chara] += 1
    else:
        frekuensi_chara[chara] = 1

for chara, frekuensi in frekuensi_chara.items():
    print(f"Huruf: {chara} : Jumlah: {frekuensi}")