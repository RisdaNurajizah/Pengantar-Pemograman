# List angka
list = [13, 15, 30, 41, 45, 55, 75, 95, 102, 135, 139, 151, 193, 200]
print(list)
print ("\n")
# List untuk menyimpan hasil akhir
result = []
# Loop melalui setiap angka dalam list
for number in list:
    # Periksa apakah angka habis dibagi 3 dan tidak lebih dari 151
    if number % 3 == 0 and number <= 151:
        # Jika kondisi terpenuhi, tambahkan angka ke dalam list result
        result.append(number)

# Cetak list hasil yang berisi angka-angka yang memenuhi kriteria
for number in result:
    print(number)