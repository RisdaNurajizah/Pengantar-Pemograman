# Meminta input dari pengguna
inputan = input("Inputan : ")

# Memeriksa apakah input hanya berisi angka
if inputan.isdigit():
    # Menghitung jumlah karakter dalam input
    jumlah_angka = len(inputan)
    # Cetak hasil
    print(f"Jumlah angka = {jumlah_angka}")
else:
    # Menampilkan pesan jika input tidak hanya berisi angka
    print("Input tidak valid. Harap masukkan string yang hanya berisi angka.")
