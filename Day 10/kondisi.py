
# Hari 10 - Kondisi (if-else)

# If sederhana
umur = 18
if umur >= 18:
    print("Anda sudah dewasa")

# If-else
nilai = 75
print("\nIf-else:")
if nilai >= 60:
    print("Anda lulus")
else:
    print("Anda tidak lulus")

# If-elif-else
print("\nIf-elif-else:")
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai: {nilai}, Grade: {grade}")

# If bersarang (nested if)
print("\nIf bersarang:")
umur = 20
punya_sim = True

if umur >= 17:
    print("Usia mencukupi untuk mengemudi")
    if punya_sim:
        print("Anda boleh mengemudi")
    else:
        print("Anda harus membuat SIM terlebih dahulu")
else:
    print("Anda belum cukup umur untuk mengemudi")

# Operator logika dalam kondisi
print("\nOperator logika dalam kondisi:")
nilai_uts = 80
nilai_uas = 75

if nilai_uts >= 70 and nilai_uas >= 70:
    print("Lulus kedua ujian")
elif nilai_uts >= 70 or nilai_uas >= 70:
    print("Lulus salah satu ujian")
else:
    print("Tidak lulus kedua ujian")

# Kondisi singkat (ternary operator)
print("\nTernary operator:")
umur = 20
status = "dewasa" if umur >= 18 else "belum dewasa"
print(f"Status: {status}")

# In operator dalam kondisi
print("\nIn operator:")
buah = ["Apel", "Jeruk", "Mangga"]
if "Apel" in buah:
    print("Apel tersedia")
if "Pisang" not in buah:
    print("Pisang tidak tersedia")
