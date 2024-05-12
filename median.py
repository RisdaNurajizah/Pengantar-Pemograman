pertama = float(input("Masukan nilai pertama : "))
kedua = float(input("Masukan nilai kedua : "))
ketiga =float(input("Masukan nilai ketiga : "))

list = [pertama, kedua, ketiga]
list.sort()

if len(list) % 2 == 0:
    median = (list[len(list) // 2 -1] + list[len(list) // 2] / 2)
else:
    median = list[len(list) // 2]

print("Median : ",median)

