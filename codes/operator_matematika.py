# # PENGHITUNG MATEMATIKA
# # https://github.com/zidan-herlangga/

# import os

# def Penjumlahan():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 + num2
#     print(f"\nHasil dari {num1} + {num2} =", hasil)

# def Pengurangan():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 - num2
#     print(f"\nHasil dari {num1} - {num2} =", hasil)

# def Perkalian():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 * num2
#     print(f"\nHasil dari {num1} * {num2} =", hasil)


# def Pembagian():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 / num2
#     print(f"\nHasil dari {num1} / {num2} =", hasil)


# def Modulus():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 % num2
#     print(f"\nHasil dari {num1} % {num2} =", hasil)

# def Pangkatan():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 ** num2
#     print(f"\nHasil dari {num1} ** {num2} =", hasil)

# def Pembagian_Bulatan():
#     num1 = float(input("\nMasukan bilangan awal: "))
#     num2 = float(input("Masukan bilangan akhir: "))
#     hasil = num1 // num2
#     print(f"\nHasil dari {num1} // {num2} =", hasil)


# while True:
#     pilihan = int(input(
#         "1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Modulus \n6. Pangkat \n7. Pembagian pembulatan\n\n0. Keluar\n\nPilih: "))
#     os.system("clear")
#     if pilihan == 1:
#         Penjumlahan()
#     elif pilihan == 2:
#         Pengurangan()
#     elif pilihan == 3:
#         Perkalian()
#     elif pilihan == 4:
#         Pembagian()
#     elif pilihan == 5:
#         Modulus()
#     elif pilihan == 6:
#         Pangkatan()
#     elif pilihan == 7:
#         Pembagian_Bulatan()
#     else:
#         print("Good Bye..")
#         break

with open("output.txt", "a") as f:
    print("Hello stackoverflow!", file=f)
    print("I have a question.", file=f)