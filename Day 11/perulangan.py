
# Hari 11 - Perulangan

# For loop dengan list
print("For loop dengan list:")
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
for item in buah:
    print(item)

# For loop dengan range
print("\nFor loop dengan range:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 6):  # 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(1, 10, 2):  # 1, 3, 5, 7, 9 (step = 2)
    print(i, end=" ")
print()

# For loop dengan string
print("\nFor loop dengan string:")
for char in "Python":
    print(char, end=" ")
print()

# For loop dengan dictionary
print("\nFor loop dengan dictionary:")
siswa = {"nama": "Budi", "umur": 20, "jurusan": "Informatika"}

for key in siswa:
    print(f"{key}: {siswa[key]}")

for key, value in siswa.items():
    print(f"{key}: {value}")

# While loop
print("\nWhile loop:")
counter = 1
while counter <= 5:
    print(f"Iterasi ke-{counter}")
    counter += 1

# Break statement
print("\nBreak statement:")
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print("\nLoop berhenti di angka 5")

# Continue statement
print("\nContinue statement:")
for i in range(1, 10):
    if i % 2 == 0:  # Jika genap, lewati
        continue
    print(i, end=" ")  # Hanya mencetak angka ganjil
print("\nHanya mencetak angka ganjil")

# Else dalam loop
print("\nElse dalam loop:")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop selesai tanpa break")

for i in range(5):
    print(i, end=" ")
    if i == 3:
        break
else:
    print("\nIni tidak akan dieksekusi karena ada break")
print()

# Nested loop (loop bersarang)
print("\nNested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# List comprehension (cara singkat membuat list dengan for)
print("\nList comprehension:")
kuadrat = [x**2 for x in range(1, 6)]
print("Kuadrat 1-5:", kuadrat)

genap = [x for x in range(1, 11) if x % 2 == 0]
print("Angka genap 1-10:", genap)
