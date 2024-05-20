#Dari contoh kasus kategori kasus di Play Store, tambahkan kemampuan-kemampuan berikut ini:
# • Tampilkan nama-nama aplikasi yang hanya muncul di satu kategori saja.
# • Untuk input n>2, tampilkan nama-nama aplikasi yang muncul tepat di dua kategori sekaligus

inkategori = int(input("Masukkan Jumlah Kategori: "))
data_apk = {}

for i in range(inkategori):
    nama_kategori = input("Masukkan Nama Kategori: ")
    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)
    apk = list()

    for j in range(5):
        nama_apk = input("Masukkan Nama Aplikasi: ")
        apk.append(nama_apk)
    data_apk[nama_kategori] = apk
print(data_apk)
print()

daftar_apk_lst = list()
for apk in data_apk.values():
    daftar_apk_lst.append(set(apk))
print(daftar_apk_lst)
print()

hasil = daftar_apk_lst
for x in range(1,inkategori):
    unik = daftar_apk_lst[i] ^ daftar_apk_lst[i-1]
else:
    unik = daftar_apk_lst[0] ^ daftar_apk_lst[i]
print()
print("Aplikasi Yang Hanya Muncul Di Satu Kategori Saja: ", unik)

print()
if inkategori > 2:
    for y in range(1,inkategori):
        inter = daftar_apk_lst[i] and daftar_apk_lst[i-1]
    else:
        inter = daftar_apk_lst[0] and daftar_apk_lst[i]       
    print("Aplikasi Yang Muncul Di Dua Kategori Sekaligus: ", inter)