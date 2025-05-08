
# Hari 6 - List

# Membuat list
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
angka = [1, 2, 3, 4, 5]
campuran = ["Apel", 1, True, 3.14]

print("List buah:", buah)
print("List angka:", angka)
print("List campuran:", campuran)

# Mengakses item list
print("\nMengakses item list:")
print("Item pertama:", buah[0])        # Apel
print("Item ketiga:", buah[2])         # Mangga
print("Item terakhir:", buah[-1])      # Pisang
print("Item 2-3:", buah[1:3])          # ['Jeruk', 'Mangga']

# Mengubah nilai item
print("\nMengubah nilai item:")
buah[1] = "Anggur"
print("Setelah diubah:", buah)         # ['Apel', 'Anggur', 'Mangga', 'Pisang']

# Panjang list
print("\nPanjang list:", len(buah))    # 4

# Menambah item
print("\nMenambah item:")
buah.append("Durian")                   # Menambah di akhir
print("Setelah append:", buah)
buah.insert(2, "Jambu")                 # Menambah di posisi tertentu
print("Setelah insert:", buah)

# Menghapus item
print("\nMenghapus item:")
buah.remove("Mangga")                   # Menghapus item tertentu
print("Setelah remove:", buah)
buah.pop()                              # Menghapus item terakhir
print("Setelah pop:", buah)
buah.pop(1)                             # Menghapus item di indeks tertentu
print("Setelah pop(1):", buah)

# Metode list lainnya
print("\nMetode list lainnya:")
angka.sort()                            # Mengurutkan list
print("Sort:", angka)
angka.reverse()                         # Membalik urutan list
print("Reverse:", angka)
angka_copy = angka.copy()               # Membuat salinan list
print("Copy:", angka_copy)
angka.clear()                           # Menghapus semua item
print("Clear:", angka)

# List comprehension
print("\nList comprehension:")
kuadrat = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]
print("Kuadrat 1-5:", kuadrat)
