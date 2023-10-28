import os   # Library dipakai untuk meng-clear terminal sistem operasi WINDOWS / LINUX
import time  # Library untuk waktu delay
import segno    # Library genarate QRCode
from termcolor import colored   # Library untuk hasil ada warnanya

# Sebuah variable info dan exit
info = colored("Dalam pengembangan", "red")
exit_ = colored("Good Bye..", "red", attrs=["blink"])

# Banner
print("""
░█▀█░█░█░█▀▀░█▀▀░█▀█░▀█▀░█░█░░░░░▀▀█
░█▀▀░░█░░█░█░█▀▀░█░█░░█░░█░█░▄▄▄░▄▀░
░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░░░▀▀▀ 
""")

# Animasi delay, seakan - akan loading
print("Menu akan tampil dalam 3 detik")
time.sleep(1)
print("Menu akan tampil dalam 2 detik")
time.sleep(1)
print("Menu akan tampil dalam 1 detik")
time.sleep(1)

# Setelah animasi, maka perintah ini akan meng-clear animasi tersebut
os.system("clear")
os.system("cls")

# Sebuah variable penyambut user
title = colored("SELAMAT DATANG PyGENIU-Z", "red")
descrip = colored("\nSilakan kunjungi link untuk source code nya.", "red")
link = colored("https://github.com/zidan-herlangga/pygeniu-z",
               "green", attrs=["blink"])    # mengambil dari library termcolor

select_menu = "y"
while select_menu != 0:
    print("============= MENU =============")
    print(title)
    print(descrip)
    print(link)
    print()
    menu = input(
        "A. Arimatika\nB. Segitiga (*)\nC. Penghitung luas\nD. Generate QR\nE. ???\n\n0. Keluar\nPilih Menu: ")

    if menu == "A" or menu == "a":
        def Penjumlahan():
            print("Penjumlahan")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            results = num1 + num2
            print(f"\nHasil dari {num1} + {num2} =", results)

        def Pengurangan():
            print("Pengurangan")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            results = num1 - num2
            print(f"\nHasil dari {num1} - {num2} =", results)

        def Perkalian():
            print("Perkalian")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            results = num1 * num2
            print(f"\nHasil dari {num1} * {num2} =", results)

        def Pembagian():
            print("Pembagian")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            results = num1 / num2
            print(f"\nHasil dari {num1} / {num2} =", results)

        def Modulus():
            print("Modulus")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            results = num1 % num2
            print(f"\nHasil dari {num1} % {num2} =", results)

        def Pangkatan():
            print("Pangkatan")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            results = num1 ** num2
            print(f"\nHasil dari {num1} ** {num2} =", results)

        def Pembagian_Bulatan():
            print("Pembagian Bulatan")
            num1 = float(input("\nMasukan bilangan awal: "))
            num2 = float(input("Masukan bilangan akhir: "))
            hasil = num1 // num2
            print(f"\nHasil dari {num1} // {num2} =", hasil)

        while True:
            print("\n*ARITMATIKA")
            choice = int(input(
                "1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Modulus \n6. Pangkat\n7. Pembagian Bulatan\n\n0. Keluar\n99. Kembali\n\nPilih: "))
            os.system("clear")
            os.system("cls")
            if choice == 1:
                Penjumlahan()
            elif choice == 2:
                Pengurangan()
            elif choice == 3:
                Perkalian()
            elif choice == 4:
                Pembagian()
            elif choice == 5:
                Modulus()
            elif choice == 6:
                Pangkatan()
            elif choice == 7:
                Pembagian_Bulatan()
            else:
                break
            continue
        print(exit_)
        os.system("clear")
        os.system("cls")

    elif menu == "B" or menu == "b":
        def sikuSiku():
            print("Siku-Siku")
            value = int(input("Masukan nilai: "))
            for i in range(0, value):
                for j in range(i + 1):
                    print("*", end="")
                print()

        def sikuSikuTerbalik():
            print("Siku-Siku (Reversed)")
            value = int(input("Masukan nilai: "))
            for i in reversed(range(0, value)):
                for j in range(i + 1):
                    print("*", end="")
                print()

        def segitigaSamaKaki():
            print("Sama Kaki")
            value = int(input("Masukan nilai: "))
            for i in range(0, value):
                print(('*' * (1 + 2 * i)).center(1+2*10))

        def segitigaSamaKakiTerbalik():
            print("Sama Kaki (Reversed)")
            value = int(input("Masukan nilai: "))
            for i in reversed(range(0, value)):
                print(('*' * (1 + 2 * i)).center(1+2*10))
        while True:
            print("\n*Segitiga")
            choice = int(input(
                "1. Siku-Siku\n2. Siku-Siku (Reversed)\n3. Segitiga Sama Kaki\n4. Segitiga Sama Kaki (Reversed)\n\n0. Keluar\n99. Kembali\n\nPilih: "))
            print()
            os.system("clear")
            os.system("cls")
            if choice == 1:
                sikuSiku()
            elif choice == 2:
                sikuSikuTerbalik()
            elif choice == 3:
                segitigaSamaKaki()
            elif choice == 4:
                segitigaSamaKakiTerbalik()
            else:
                break
            continue
        print(exit_)
        os.system("clear")
        os.system("cls")

    elif menu == "C" or menu == "c":
        def luasSegitiga():
            print("Luas segitiga")
            base = float(input("Masukan alas: "))
            tall = float(input("Masukan tinggi: "))
            results = 0.5 * base * tall
            print(f"Alas {base} dan tinggi {tall} Hasil = {results}")

        def luasLingkaran():
            print("Luas lingkaran")
            phi = 3.14
            r = float(input("Masukan panjang jari-jari lingkaran: "))

            broad = phi * r * r
            print(f"Luas lingkaran adalah = {broad}")

        def luasKelilingPersegi():
            print("Luas keliling persegi")
            s = float(input("Masukan panjang sisi: "))
            broad = s**2
            around = 4 * s
            print(f"Luas {broad} keliling {around} ")
        while True:
            print("\n*Penghitung luas")
            pilihan = int(input(
                "1. Luas segitiga\n2. Luas lingkaran\n3. Luas keliling persegi\n\n0. Keluar\n99. Kembali\n\nMasukan pilihan: "))
            print()
            os.system("clear")
            os.system("cls")
            if pilihan == 1:
                luasSegitiga()
            elif pilihan == 2:
                luasLingkaran()
            elif pilihan == 3:
                luasKelilingPersegi()
            else:
                break
            continue
        print(exit_)
        os.system("clear")
        os.system("cls")

    elif menu == "D" or menu == "d":
        def create_folder(folder_name):
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

        def QR():
            print("\n*Generate QR")
            make_qr = input("Buat nama file dengan (.png): ")
            text = input("Buat link QR: ")

            # Memanggil fungsi untuk membuat folder 'hasil QR'
            create_folder('hasil QR')

            # Menggabungkan nama file dengan path ke folder 'hasil QR'
            file_path = os.path.join('hasil QR', make_qr)

            qrcode = segno.make_qr(text)
            qrcode.save(file_path, scale=5)
            print(f"QR Code telah disimpan di '{file_path}'")
        while True:
            os.system("clear")
            os.system("cls")
            QR()
            break
        # Untuk membersihkan layar, Anda dapat menggunakan perintah berikut
        os.system("clear")  # Untuk sistem Linux / MacOS
        os.system("cls")    # Untuk sistem Windows
        continue

    elif menu == "E" or menu == "e":
        print(info)
        continue

    else:
        print(exit_)
        exit()
