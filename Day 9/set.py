
# Hari 9 - Set

# Membuat set
buah = {"Apel", "Jeruk", "Mangga", "Pisang"}
angka = {1, 2, 3, 4, 5}
campuran = {"Apel", 1, True, 3.14}

print("Set buah:", buah)
print("Set angka:", angka)
print("Set campuran:", campuran)

# Set tidak mengizinkan duplikat
print("\nSet tidak mengizinkan duplikat:")
angka_duplikat = {1, 2, 3, 2, 4, 3, 5}
print("Set dengan nilai duplikat:", angka_duplikat)  # Duplikat akan dihilangkan

# Set tidak berurutan dan tidak bisa diakses dengan indeks
# print(buah[0])  # TypeError: 'set' object is not subscriptable

# Mengecek keberadaan item
print("\nMengecek keberadaan item:")
print("Apakah 'Apel' ada di set buah?", "Apel" in buah)  # True
print("Apakah 'Durian' ada di set buah?", "Durian" in buah)  # False

# Menambah item
print("\nMenambah item:")
buah.add("Durian")
print("Setelah add:", buah)
buah.update(["Nanas", "Semangka"])
print("Setelah update:", buah)

# Menghapus item
print("\nMenghapus item:")
buah.remove("Apel")  # Error jika item tidak ada
print("Setelah remove:", buah)
buah.discard("Jeruk")  # Tidak error jika item tidak ada
print("Setelah discard:", buah)
item = buah.pop()  # Menghapus item acak
print("Item yang di-pop:", item)
print("Setelah pop:", buah)

# Metode set
print("\nMetode set:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (gabungan)
print("Union:", set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}
print("Union dengan |:", set1 | set2)

# Intersection (irisan)
print("Intersection:", set1.intersection(set2))  # {4, 5}
print("Intersection dengan &:", set1 & set2)

# Difference (selisih)
print("Difference (set1 - set2):", set1.difference(set2))  # {1, 2, 3}
print("Difference dengan -:", set1 - set2)

# Symmetric difference (gabungan kecuali irisan)
print("Symmetric difference:", set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}
print("Symmetric difference dengan ^:", set1 ^ set2)

# Set comprehension
print("\nSet comprehension:")
kuadrat = {x**2 for x in range(1, 6)}
print("Kuadrat 1-5:", kuadrat)
