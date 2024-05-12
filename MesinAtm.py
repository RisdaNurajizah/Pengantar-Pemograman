pin_atm = "070705"
saldo = 50000000

def verifikasi_pin(pin_atm):
    while True:
        pin = input("Silahkan masukkan 4 digit pin anda : ")
        print("\t")
        if pin == pin_atm:
            print("Pin Anda Benar")
            print("\t")
            return True
        else:
            konfirmasi_pin = input("Pin Anda Salah. Apakah ingin coba lagi ? [Y/T] => ").lower()
            if konfirmasi_pin != "y":
                return False
            print("\t")
            
def tampilkan_menu():
    print("1. Silahkan tekan 1 untuk informasi Saldo")
    print("2. Silahkan tekan 2 untuk penarikan uang")
    print("3. Silahkan tekan 3 untuk menabung")
    print("4. Silahkan tekan 4 untuk keluar")


print("Selamat Datang di program ATM, Bank Syariah Indonesia")
print("\t")

hasil_verifikasi=verifikasi_pin(pin_atm)
if hasil_verifikasi:
    while True:
        tampilkan_menu()
        print("\t")

        pilihan = input("Silahkan pilih menu yang anda inginkan => ")
        print("======================================================")

        if pilihan == "1":
            print("Isi saldo anda : Rp.",saldo)
    
            konfirmasi_saldo = input("Apakah anda ingin kembali ke menu awal ? [Y/T]  =>  ").lower()
            if konfirmasi_saldo != "y":
                break
            print("\t")

        elif pilihan == "2":
            batas_penarikan = (50000, 100000, 250000, 500000, 1000000)
            tarik_uang = int(input("Silahkan, masukan nominal uang penarikan anda : "))
            print("\t")

            if tarik_uang in batas_penarikan and tarik_uang <= saldo:
                saldo -= tarik_uang
                print("Penarikan berhasil. Sisa saldo anda sekarang : Rp.",saldo)
                print("\t")
                konfirmasi_tarik_uang = input("Apakah anda ingin kembali ke menu awal ? [Y/T] => ").lower()
                if konfirmasi_tarik_uang != "y":
                    break
                print("\t")
            else:
                print("Nominal yang anda masukan tidak tersedia atau saldo anda tidak mencukupi.")
                print("\t")
                konfirmasi_tarik_uang = input("Apakah anda ingin kembali ke menu awal ? [Y/T] => ").lower()
                if konfirmasi_tarik_uang != "y":
                    break
                print("\t")
                
        elif pilihan == "3":
            nabung_uang = int(input("Silahkan, masukan nominal uang yang ingin anda tabung : "))
            print("\t")
            saldo += nabung_uang    
            print("Saldo anda sekarang: Rp.",saldo)
            print("\t")
            konfirmasi_nabung_uang = input("Apakah anda ingin kembali ke menu awal ? [Y/T] => ").lower()
            if konfirmasi_nabung_uang != "y":
                break
            print("\t")

        elif pilihan == "4":
            print("Kartu anda akan keluar dari mesin ATM....")
            print("\t")
            print("Terima Kasih sudah menggunakan layanan Bank ABCXYZ")
            print("\t")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih kembali")
            print("\t")








    