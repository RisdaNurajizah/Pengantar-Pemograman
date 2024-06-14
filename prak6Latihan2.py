# input angka dari keyboard
angka = input("Input sebuah angka : ")

# Ubah menjadi tipe data integer
angka = int(angka)

# Pengulangan perkalian menggunakan For Loop
i = 1
while i <= 10:
    hasil = angka * i
    print(angka, "x", i, "=", hasil)
    i += 1