#Program 1: perhitungan sederhana
BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100
RumusPenjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan = BilanganPertama - BilanganKedua - BilanganKetiga
RumusPerkalian = BilanganPertama * BilanganKedua * BilanganKetiga
print(f"Penjumlahan = {BilanganPertama} + {BilanganKedua} + {BilanganKetiga} = ",RumusPenjumlahan)
print(f"Pengurangan = {BilanganPertama} - {BilanganKedua} - {BilanganKetiga} = ",RumusPengurangan)
print(f"Perkalian   = {BilanganPertama} * {BilanganKedua} * {BilanganKetiga} = ",RumusPerkalian)

#Program2: menghitung luas bangun datar
#1. Luas persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi
print(luas_persegi)

#2. Luas persegi panjang
panjang_pp = 50
lebar_pp = 15.5
luas_pp = panjang_pp * lebar_pp
print(luas_pp)

#3. luas segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
print(luas_segitiga)

#4. Luas lingkaran
jari_jari = 4
luas_lingkaran = 3.14 * jari_jari**2
print(luas_lingkaran)

#5. luas jajar genjang
alas = 10
tinggi = 4
luas_jajargenjang = alas * tinggi
print(luas_jajargenjang)

#6. luas trapesium
jumlah_rusuk_sejajar1 = 5
jumlah_rusuk_sejajar2 = 20
tinggi_trapesium = 5
luas_trapesium = 0.5 * (jumlah_rusuk_sejajar1 + jumlah_rusuk_sejajar2) * tinggi_trapesium
print(luas_trapesium)

#program 3
a = -11
b = 13
result_and = a & b
result_or = a | b
result_not_a = ~a
result_xor = a ^ b

print("a & b =", result_and)
print("a | b =", result_or)
print("~a =", result_not_a)
print("a ^ b =", result_xor)