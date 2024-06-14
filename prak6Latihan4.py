# menghitung perkalian 1 - 100
def perkalian():
    for i in range(1, 11):
        line = []
        for j in range(1, 11):
            line.append(i * j)
        print(" ".join(map(str, line)))

perkalian()