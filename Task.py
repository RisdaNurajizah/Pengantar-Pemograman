# Meminta input dari pengguna
inputan = input("Inputan : ")

# Inisialisasi variabel untuk menghitung huruf dan angka
jumlah_huruf = 0
jumlah_angka = 0

# Menghitung jumlah huruf dan angka
for char in inputan:
    if char.isalpha():
        jumlah_huruf += 1
    elif char.isdigit():
        jumlah_angka += 1

# Cetak hasil
print(f"Jumlah huruf: {jumlah_huruf}")
print(f"Jumlah angka: {jumlah_angka}")
