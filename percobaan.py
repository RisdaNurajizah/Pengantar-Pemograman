pin_atm = "070705"
saldo = 5000000

def verifikasi_pin(pin_atm):
    while True:
        try:
            pin = input("Silahkan masukkan 4 digit pin anda : ")
            if pin == pin_atm:
                print("Pin Anda Benar")
                return True
            else:
                konfirmasi_pin = input("Pin Anda Salah. Apakah ingin coba lagi ? [Y/T] => ").lower()
                if konfirmasi_pin != "y":
                    return False
        except ValueError:
            print("Mohon masukkan pin dengan benar.")

def tampilkan_menu():
    print("1. Silahkan tekan 1 untuk informasi Saldo")
    print("2. Silahkan tekan 2 untuk penarikan uang")
    print("3. Silahkan tekan 3 untuk menabung")
    print("4. Silahkan tekan 4 untuk keluar")

def informasi_saldo():
    print("Isi saldo anda : Rp.", saldo)
    konfirmasi_saldo = input("Apakah anda ingin kembali ke menu awal ? [Y/T] => ").lower()
    if konfirmasi_saldo != "y":
        return False
    return True

def penarikan_uang():
    batas_penarikan = (50000, 100000, 250000, 500000, 1000000)
    try:
        tarik_uang = int(input("Silahkan, masukan nominal uang penarikan anda : "))
        if tarik_uang in batas_penarikan and tarik_uang <= saldo:
            saldo -= tarik_uang
            print("Penarikan berhasil. Sisa saldo anda sekarang : Rp.", saldo)
            return True
        else:
            print("Nominal yang anda masukan tidak tersedia atau saldo anda tidak mencukupi.")
            return False
    except ValueError:
        print("Mohon masukkan nominal penarikan dengan benar.")
        return False

def menabung_uang():
    try:
        tabung_uang = int(input("Silahkan, masukan nominal uang yang akan dimasukkan : "))
        saldo += tabung_uang
        print("Tabungan berhasil. Sisa saldo anda sekarang : Rp.", saldo)
        return True
    except ValueError:
        print("Mohon masukkan nominal tabungan dengan benar.")
        return False

print("Selamat Datang di program ATM, Bank Syariah Indonesia")
print("\t")

hasil_verifikasi = verifikasi_pin(pin_atm)
if hasil_verifikasi:
    while True:
        tampilkan_menu()
        print("\t")

        pilihan = input("Silahkan pilih menu yang anda inginkan => ")
        print("======================================================")

        if pilihan == "1":
            if not informasi_saldo():
                break

        elif pilihan == "2":
            if penarikan_uang():
                konfirmasi_penarikan = input("Apakah anda ingin kembali ke menu awal ? [Y/T] => ").lower()
                if konfirmasi_penarikan != "y":
                    break