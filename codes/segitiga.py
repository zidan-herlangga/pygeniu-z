import os


def sikuSiku():
    nilai = int(input("Masukan pilihan: "))
    for i in range(0, nilai):
        for j in range(i + 1):
            print("*", end="")
        print()


def sikuSikuTerbalik():
    nilai = int(input("Masukan pilihan: "))
    for i in reversed(range(0, nilai)):
        for j in range(i + 1):
            print("*", end="")
        print()


def segitigaSamaKaki():
    nilai = int(input("Masukan pilihan: "))
    for i in range(0, nilai):
        print(('*' * (1 + 2 * i)).center(1+2*10))

def segitigaSamaKakiTerbalik():
    nilai = int(input("Masukan pilihan: "))
    for i in reversed(range(0, nilai)):
        print(('*' * (1 + 2 * i)).center(1+2*10))


while True:
    pilihan = int(input(
        "\n1. Siku-Siku\n2. Siku-Siku (Reversed)\n3. Segitiga Sama Kaki\n4. Segitiga Sama Kaki (Reversed)\n\n0. Keluar\n\nMasukan nilai: "))
    print()
    os.system("clear")
    if pilihan == 1:
        sikuSiku()
    elif pilihan == 2:
        sikuSikuTerbalik()
    elif pilihan == 3:
        segitigaSamaKaki()
    elif pilihan == 4:
        segitigaSamaKakiTerbalik()
    else:
        print("Good Bye...")
        break
