# Inisialisasi String
a = "Hello, World!"
ori_string = "orang jahat adalah orang baik yang tersakiti"

# Ubah menjadi Lowercase dan Uppercase
lowercase_string = a.lower()
uppercase_string = a.upper()

# Mengganti character vocal (a, o dan e) menjadi i
new_string = ""
for char in ori_string:
    if char in 'aoe':
        new_string += 'i'
    else:
        new_string += char

# Cetak hasil
print ("Original string  :",a)
print ("Lowercase string :",lowercase_string)
print ("Uppercase string :",uppercase_string)
print ("Original string  :",ori_string)
print ("Menggantikan karakter a,o,e menjadi i:",new_string)