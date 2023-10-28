import os
import segno

# Fungsi untuk membuat folder jika belum ada


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def QR():
    print("\nGenerate QR")
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
    QR()
    break

# Untuk membersihkan layar, Anda dapat menggunakan perintah berikut
os.system("clear")  # Untuk sistem Linux / MacOS
os.system("cls")    # Untuk sistem Windows
