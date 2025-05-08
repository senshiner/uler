
# Hari 15 - Penanganan Exception

# Contoh error tanpa exception handling
print("Contoh error tanpa exception handling:")
# Uncomment untuk melihat error
# hasil = 10 / 0  # ZeroDivisionError
# print(hasil)
print("Program akan berhenti jika terjadi error")

# Penanganan exception dasar dengan try-except
print("\nPenanganan exception dasar:")
try:
    hasil = 10 / 0
    print(f"Hasil: {hasil}")
except:
    print("Terjadi error")

print("Program tetap berlanjut")

# Penanganan exception spesifik
print("\nPenanganan exception spesifik:")
try:
    angka = int("abc")  # ValueError
    hasil = 10 / 0      # ZeroDivisionError
    print(f"Hasil: {hasil}")
except ValueError:
    print("Error: Input bukan angka")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol")

# Multiple exceptions
print("\nMultiple exceptions:")
try:
    # Coba beberapa operasi berbeda
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    list_angka = [1, 2, 3]
    print(list_angka[angka])
except ValueError:
    print("Error: Input bukan angka")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol")
except IndexError:
    print("Error: Indeks tidak valid")

# Exception dengan else clause
print("\nException dengan else clause:")
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
except ValueError:
    print("Error: Input bukan angka")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol")
else:
    # Dieksekusi jika tidak ada exception
    print(f"Hasil: {hasil}")

# Exception dengan finally clause
print("\nException dengan finally clause:")
try:
    file = open("data_test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File tidak ditemukan")
finally:
    # Selalu dieksekusi, baik ada exception atau tidak
    print("Operasi file selesai")
    # Menutup file jika berhasil dibuka
    if 'file' in locals() and not file.closed:
        file.close()
        print("File ditutup")

# Menangkap exception message
print("\nMenangkap exception message:")
try:
    angka = int("abc")
except ValueError as e:
    print(f"Error: {e}")

# Menangkap semua jenis exception
print("\nMenangkap semua jenis exception:")
try:
    hasil = 10 / 0
except Exception as e:
    print(f"Terjadi error: {e}")
    print(f"Tipe error: {type(e).__name__}")

# Raise exception sendiri
print("\nRaise exception sendiri:")
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    if umur < 18:
        raise Exception("Umur minimal 18 tahun")
    return "Umur valid"

try:
    hasil = cek_umur(15)
    print(hasil)
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"Exception: {e}")

# Membuat custom exception
print("\nMembuat custom exception:")
class UmurError(Exception):
    def __init__(self, umur, pesan="Umur tidak valid"):
        self.umur = umur
        self.pesan = pesan
        super().__init__(self.pesan)
    
    def __str__(self):
        return f"{self.pesan} -> {self.umur}"

try:
    umur = -5
    if umur < 0:
        raise UmurError(umur, "Umur tidak boleh negatif")
except UmurError as e:
    print(f"UmurError: {e}")
