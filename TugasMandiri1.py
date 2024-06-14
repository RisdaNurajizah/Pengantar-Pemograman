import random

# List pilihan yang valid
pilihan = ['gunting', 'batu', 'kertas']

while True:
    # Input pemain 1
    pemain1 = input("Pemain 1: Silahkan anda pilih : Gunting, Batu, Kertas -> ").strip().lower()
    while pemain1 not in pilihan:
        pemain1 = input("Pilihan tidak valid. Silahkan anda pilih lagi : Gunting, Batu, Kertas -> ").strip().lower()

    # Input pemain 2
    pemain2 = input("Pemain 2 : Silahkan anda pilih : Gunting, Batu, Kertas -> ").strip().lower()
    while pemain2 not in pilihan:
        pemain2 = input("Pilihan tidak valid. Silahkan anda pilih lagi : Gunting, Batu, Kertas -> ").strip().lower()

    # Menentukan pemenang
    if pemain1 == pemain2:
        print("Seri")
    elif (pemain1 == 'gunting' and pemain2 == 'kertas') or \
       (pemain1 == 'batu' and pemain2 == 'gunting') or \
       (pemain1 == 'kertas' and pemain2 == 'batu'):
       print("Pemain 1 Menang")
    else:
        print("Pemain 2 Menang")


    # Main lagi Ya atau Tidak
    main_lagi = input("Apakah anda ingin memulai Permainan Awal lagi [Y/T] -> ").strip().lower()
    if main_lagi == "t":
        print("GAME OVER")
        break
    elif main_lagi != "y":
     print("Permainan Baru akan dimulai")
     break