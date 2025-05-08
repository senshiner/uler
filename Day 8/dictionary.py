
# Hari 8 - Dictionary

# Membuat dictionary
siswa = {
    "nama": "Budi",
    "umur": 20,
    "nilai": 85.5,
    "lulus": True
}

print("Dictionary siswa:", siswa)

# Mengakses nilai dengan key
print("\nMengakses nilai:")
print("Nama:", siswa["nama"])       # Budi
print("Umur:", siswa["umur"])       # 20
print("Nilai:", siswa.get("nilai")) # 85.5
print("Status tidak ada:", siswa.get("status", "Tidak ada"))  # Nilai default jika key tidak ada

# Mengubah nilai
print("\nMengubah nilai:")
siswa["nama"] = "Andi"
siswa["nilai"] = 90
print("Setelah diubah:", siswa)

# Menambah item baru
print("\nMenambah item baru:")
siswa["jurusan"] = "Informatika"
print("Setelah ditambah:", siswa)

# Menghapus item
print("\nMenghapus item:")
del siswa["lulus"]
print("Setelah del:", siswa)
nilai = siswa.pop("nilai")  # Menghapus dan mengambil nilainya
print("Nilai yang di-pop:", nilai)
print("Setelah pop:", siswa)

# Metode dictionary
print("\nMetode dictionary:")
keys = siswa.keys()      # Mengambil semua key
values = siswa.values()  # Mengambil semua value
items = siswa.items()    # Mengambil pasangan key-value

print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Copy dictionary
print("\nCopy dictionary:")
siswa_copy = siswa.copy()
print("Copy:", siswa_copy)

# Dictionary bersarang (nested)
print("\nDictionary bersarang:")
mahasiswa = {
    "mhs1": {"nama": "Budi", "umur": 20, "jurusan": "Informatika"},
    "mhs2": {"nama": "Andi", "umur": 21, "jurusan": "Teknik Elektro"},
    "mhs3": {"nama": "Citra", "umur": 19, "jurusan": "Manajemen"}
}

print("Data mahasiswa:", mahasiswa)
print("Nama mhs2:", mahasiswa["mhs2"]["nama"])
print("Umur mhs3:", mahasiswa["mhs3"]["umur"])

# Dictionary comprehension
print("\nDictionary comprehension:")
kuadrat = {x: x**2 for x in range(1, 6)}
print("Kuadrat 1-5:", kuadrat)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
