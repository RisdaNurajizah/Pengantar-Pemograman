k = ""
i = 1

#looping baris
while i <= 6:
    j = i
    
    #looping kolom
    while j > 0:
        k = k + "\U0001f600"
        j = j - 1

    #membuat baris baru
    k = k + "\n"
    i = i + 1

#menampilkan output
print(k)  