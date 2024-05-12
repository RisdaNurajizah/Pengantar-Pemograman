#definisi fungsi
def print_vertical(kata):
    #fungsi untuk mencetak string secara vertical atau mengurut ke bawah
    for character in kata:
        print(character)

#meminta input dari user
input_kata = input("Kata yang tersedia adalah: ")

#memanggil fungsi dan memberikan string sebagai argumen
print_vertical(input_kata)
