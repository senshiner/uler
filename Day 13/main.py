
# Program utama yang mengimpor modul

# Import seluruh modul
import kalkulator

print("Import seluruh modul:")
print(f"4 + 2 = {kalkulator.tambah(4, 2)}")
print(f"4 - 2 = {kalkulator.kurang(4, 2)}")
print(f"Nilai pi = {kalkulator.pi}")

# Import fungsi tertentu
from kalkulator import kali, bagi

print("\nImport fungsi tertentu:")
print(f"4 * 2 = {kali(4, 2)}")
print(f"4 / 2 = {bagi(4, 2)}")

# Import dengan alias
import kalkulator as calc

print("\nImport dengan alias:")
print(f"5 + 3 = {calc.tambah(5, 3)}")

# Import fungsi dengan alias
from kalkulator import tambah as add, kurang as subtract

print("\nImport fungsi dengan alias:")
print(f"5 + 3 = {add(5, 3)}")
print(f"5 - 3 = {subtract(5, 3)}")

# Import semua isi modul (tidak disarankan)
# from kalkulator import *

# Import dari modul bawaan Python
import math
import random
import datetime

print("\nImport dari modul bawaan:")
print(f"Akar kuadrat dari 16: {math.sqrt(16)}")
print(f"Angka acak antara 1-10: {random.randint(1, 10)}")
print(f"Waktu sekarang: {datetime.datetime.now()}")

# Import dari paket
# import nama_paket.nama_modul
# from nama_paket import nama_modul
# from nama_paket.nama_modul import nama_fungsi
