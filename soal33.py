def baca_file(fileku):
    try:
        with open(fileku, 'r') as file:
            return file.read().lower().split()
    except FileNotFoundError:
        print(f"File '{fileku}' tidak ditemukan atau tidak bisa dibaca.")
        exit()

def main():
    tekspertama = input("Masukkan file teks 1: ")
    tekskedua = input("Masukkan file teks 2: ")
    
    katafile1 = set(baca_file(tekspertama))
    katafile2 = set(baca_file(tekskedua))
    
    katayangsama = katafile1.intersection(katafile2)
    
    if katayangsama:
        print("Kata-kata yang muncul di kedua file:")
        for kata in katayangsama:
            print(kata)
    else:
        print("Tidak ada kata yang muncul di kedua file.")

if __name__ == "__main__":
    main()
