from termcolor import colored


def konversi_KB():
    print("\n*Konversi KB")
    size_KB = float(input("Masukan size KB: "))

    kb_to_mb = 1 / 1024
    mb_to_gb = 1 / 1024
    gb_to_tb = 1 / 1024

    size_mb = size_KB * kb_to_mb
    size_gb = size_mb * mb_to_gb
    size_tb = size_gb * gb_to_tb

    print()
    print(colored(f"{size_KB} KB = {size_mb:.6f} MB",
                  "green", attrs=["blink"]))
    print(colored(f"{size_KB} MB = {size_gb:.6f} GB",
                  "green", attrs=["blink"]))
    print(colored(f"{size_KB} GB = {size_tb:.6f} TB",
                  "green", attrs=["blink"]))

    out_in = "y"
    while out_in != "n":
        konversi_KB()
        out_in = input("\nMengulang kembali (Y/n)? ")
        continue
