# List angka
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List angka :",angka)

# Inisialisasi
genap = 0
ganjil = 0

# Menentukan apakah bilangan genap atau ganjil  
for bilangan in angka:
    if bilangan % 2 == 0:
        genap += 1
    else:
        ganjil += 1

# Cetak hasil
print("Jumlah bilangan genap : ", genap)
print("Jumlah bilangan ganjil : ",ganjil)