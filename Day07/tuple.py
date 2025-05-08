
# Hari 7 - Tuple

# Membuat tuple
buah = ("Apel", "Jeruk", "Mangga", "Pisang")
angka = (1, 2, 3, 4, 5)
campuran = ("Apel", 1, True, 3.14)
tuple_tunggal = ("Python",)  # Tuple dengan satu item harus diakhiri koma

print("Tuple buah:", buah)
print("Tuple angka:", angka)
print("Tuple campuran:", campuran)
print("Tuple tunggal:", tuple_tunggal)

# Mengakses item tuple
print("\nMengakses item tuple:")
print("Item pertama:", buah[0])        # Apel
print("Item ketiga:", buah[2])         # Mangga
print("Item terakhir:", buah[-1])      # Pisang
print("Item 2-3:", buah[1:3])          # ('Jeruk', 'Mangga')

# Mencoba mengubah nilai (akan error, karena tuple immutable)
# buah[1] = "Anggur"  # TypeError: 'tuple' object does not support item assignment

# Panjang tuple
print("\nPanjang tuple:", len(buah))    # 4

# Tuple tidak bisa diubah, tapi bisa dikonversi ke list, diubah, lalu dikonversi kembali
print("\nMengubah tuple menjadi list:")
buah_list = list(buah)
buah_list[1] = "Anggur"
buah = tuple(buah_list)
print("Tuple setelah diubah:", buah)    # ('Apel', 'Anggur', 'Mangga', 'Pisang')

# Menggabungkan tuple
print("\nMenggabungkan tuple:")
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("Hasil penggabungan:", tuple3)    # ('a', 'b', 'c', 1, 2, 3)

# Mengulang tuple
print("\nMengulang tuple:")
tuple_ulang = tuple1 * 3
print("Tuple diulang 3x:", tuple_ulang) # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# Metode tuple
print("\nMetode tuple:")
angka_duplikat = (1, 2, 3, 2, 4, 2, 5)
print("Count 2:", angka_duplikat.count(2))  # Menghitung kemunculan nilai 2
print("Index 4:", angka_duplikat.index(4))  # Mencari indeks nilai 4
