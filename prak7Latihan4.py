# Menginput string
m_string = input("Masukkan string : ")
m_langkah = int(input("Masukkan berapa langkah : "))

# fungsi untuk enkripsi caesar cipher
def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        # Periksa apakah karakter adalh huruf
        if char.isalpha():
            # Tentukan apakah karakter adalah huruf besar atau kecil
            if char.isupper():
                # Enkripsi huruf besar
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Enkripsi huruf kecil
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Tambahkan kararter non-huruf tanpa perubahan
            encrypted_char = char

        # Tambahkan karakter yang telah dienkripsi ke hasil akhir
        encrypted_text += encrypted_char

    return encrypted_text

# Penggunaan
original_text = m_string
langkah = m_langkah
encrypted_text = caesar_cipher(original_text, langkah)

# Cetak hasil
print ("Original string : ",original_text)
print ("Setelah dienkripsi : ",encrypted_text)