import os

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
    pilihan = int(input("1. Luas segitiga\n2. Luas lingkaran\n3. Luas keliling persegi\n\n0. Keluar\n99. Kembali\n\nMasukan pilihan: "))
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