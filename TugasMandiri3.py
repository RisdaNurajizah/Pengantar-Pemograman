i = ""
j = 5

while j > 0:
    l = j
    while l > 0:
        i += " " + str(l) 
        l -= 1
    
    i += "\n"
    j -= 1

print(i)