
# Hari 12 - Fungsi

# Fungsi sederhana
def sapa():
    print("Halo, selamat datang!")

print("Memanggil fungsi sederhana:")
sapa()

# Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

print("\nFungsi dengan parameter:")
sapa_nama("Budi")
sapa_nama("Andi")

# Fungsi dengan nilai default parameter
def sapa_lengkap(nama, pesan="Selamat datang"):
    print(f"Halo, {nama}! {pesan}")

print("\nFungsi dengan nilai default parameter:")
sapa_lengkap("Budi")
sapa_lengkap("Andi", "Apa kabar?")

# Fungsi dengan return value
def tambah(a, b):
    return a + b

print("\nFungsi dengan return value:")
hasil = tambah(5, 3)
print(f"5 + 3 = {hasil}")
print(f"10 + 7 = {tambah(10, 7)}")

# Fungsi dengan multiple return values
def operasi_matematika(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah, kurang, kali, bagi

print("\nFungsi dengan multiple return values:")
t, k, kl, b = operasi_matematika(10, 5)
print(f"10 + 5 = {t}")
print(f"10 - 5 = {k}")
print(f"10 * 5 = {kl}")
print(f"10 / 5 = {b}")

# Fungsi dengan parameter posisional dan keyword
def cetak_info(nama, umur, jurusan):
    print(f"Nama: {nama}, Umur: {umur}, Jurusan: {jurusan}")

print("\nParameter posisional dan keyword:")
cetak_info("Budi", 20, "Informatika")  # Posisional
cetak_info(nama="Andi", umur=19, jurusan="Teknik Elektro")  # Keyword
cetak_info("Citra", jurusan="Manajemen", umur=21)  # Campuran

# Fungsi dengan jumlah parameter tidak terbatas (*args)
def jumlahkan(*angka):
    total = 0
    for num in angka:
        total += num
    return total

print("\nFungsi dengan *args:")
print(f"Jumlah dari 1, 2, 3 = {jumlahkan(1, 2, 3)}")
print(f"Jumlah dari 5, 10, 15, 20 = {jumlahkan(5, 10, 15, 20)}")

# Fungsi dengan parameter keyword tidak terbatas (**kwargs)
def cetak_data_diri(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print("\nFungsi dengan **kwargs:")
cetak_data_diri(nama="Budi", umur=20, jurusan="Informatika", hobi="Membaca")

# Fungsi lambda (anonymous function)
print("\nFungsi lambda:")
kali = lambda a, b: a * b
print(f"5 x 3 = {kali(5, 3)}")

# Fungsi sebagai parameter fungsi lain
def operasi(a, b, fungsi):
    return fungsi(a, b)

print("\nFungsi sebagai parameter:")
print(f"5 + 3 = {operasi(5, 3, lambda a, b: a + b)}")
print(f"5 x 3 = {operasi(5, 3, lambda a, b: a * b)}")

# Fungsi rekursif
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

print("\nFungsi rekursif:")
print(f"Faktorial 5 = {faktorial(5)}")  # 5 * 4 * 3 * 2 * 1 = 120
