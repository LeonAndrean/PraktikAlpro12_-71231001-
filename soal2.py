#Buatlah sebuah program yang mendemonstrasikan konversi dari:
# • List menjadi Set
# • Set menjadi List
# • Tuple menjadi Set
# • Set menjadi Tuple
# Tampilkan isi data sebelum dan sesudah konversi.
data = input("Masukkan kalimat kamu: ")
data_list = list(data)

print("List ke Set")
print("Sebelum : ", data_list)
data_set_from_list = set(data_list)
print("Sesudah : ", data_set_from_list)
print()

print("Set ke List")
print("Sebelum : ", data_set_from_list)
data_list_from_set = list(data_set_from_list)
print("Sesudah : ", data_list_from_set)
print()

data_tuple = tuple(data)
print("Tuple ke Set")
print("Sebelum : ", data_tuple)
data_set_from_tuple = set(data_tuple)
print("Sesudah : ", data_set_from_tuple)
print()

print("Set ke Tuple")
print("Sebelum : ", data_set_from_tuple)
data_tuple_from_set = tuple(data_set_from_tuple)
print("Sesudah : ", data_tuple_from_set)
