
# Hari 16 - Class dan Object-Oriented Programming (OOP)

# Mendefinisikan class sederhana
class Mobil:
    # Atribut class (shared oleh semua instance)
    jenis = "Kendaraan Darat"
    
    # Constructor/initializer method
    def __init__(self, merek, warna, tahun):
        # Atribut instance (unik untuk setiap instance)
        self.merek = merek
        self.warna = warna
        self.tahun = tahun
        self.kecepatan = 0
    
    # Method
    def akselerasi(self, tambah_kecepatan):
        self.kecepatan += tambah_kecepatan
        print(f"Kecepatan meningkat menjadi {self.kecepatan} km/jam")
    
    def rem(self, kurang_kecepatan):
        if self.kecepatan - kurang_kecepatan < 0:
            self.kecepatan = 0
        else:
            self.kecepatan -= kurang_kecepatan
        print(f"Kecepatan menurun menjadi {self.kecepatan} km/jam")
    
    def info(self):
        return f"Mobil {self.merek}, warna {self.warna}, tahun {self.tahun}"

# Membuat instance (objek) dari class Mobil
print("Membuat objek dari class:")
mobil1 = Mobil("Toyota", "Merah", 2020)
mobil2 = Mobil("Honda", "Hitam", 2021)

# Mengakses atribut
print("\nMengakses atribut:")
print(f"Mobil 1: {mobil1.merek}, {mobil1.warna}, {mobil1.tahun}")
print(f"Mobil 2: {mobil2.merek}, {mobil2.warna}, {mobil2.tahun}")
print(f"Jenis mobil 1: {mobil1.jenis}")
print(f"Jenis mobil 2: {mobil2.jenis}")

# Memanggil method
print("\nMemanggil method:")
print(mobil1.info())
mobil1.akselerasi(30)
mobil1.akselerasi(20)
mobil1.rem(15)

# Memodifikasi atribut
print("\nMeodifikasi atribut:")
mobil1.warna = "Biru"
print(f"Warna mobil 1 sekarang: {mobil1.warna}")

# Membuat class dengan private atribut
print("\nPrivate atribut dan method:")
class Rekening:
    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        # Atribut private (konvensi, bukan benar-benar private)
        self.__saldo = saldo
    
    # Getter method
    def get_saldo(self):
        return self.__saldo
    
    # Setter method
    def set_saldo(self, saldo):
        if saldo < 0:
            print("Saldo tidak boleh negatif")
        else:
            self.__saldo = saldo
    
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup")
        else:
            self.__saldo -= jumlah
            print(f"Tarik tunai Rp{jumlah} berhasil")
    
    def setor(self, jumlah):
        self.__saldo += jumlah
        print(f"Setor tunai Rp{jumlah} berhasil")
    
    def __str__(self):
        return f"Rekening {self.no_rekening} atas nama {self.nama} dengan saldo Rp{self.__saldo}"

# Membuat objek Rekening
rek1 = Rekening("12345", "Budi", 1000000)
print(rek1)

# Mencoba mengakses private atribut (tidak disarankan)
# print(rek1.__saldo)  # AttributeError

# Menggunakan getter dan setter
print(f"Saldo: Rp{rek1.get_saldo()}")
rek1.set_saldo(1500000)
print(f"Saldo baru: Rp{rek1.get_saldo()}")
rek1.tarik(500000)
rek1.setor(200000)
print(rek1)

# Inheritance (Pewarisan)
print("\nInheritance (Pewarisan):")
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        return f"Kendaraan {self.merek} tahun {self.tahun}"
    
    def bergerak(self):
        return "Kendaraan bergerak"

class Sepeda(Kendaraan):
    def __init__(self, merek, tahun, jenis):
        # Memanggil constructor class parent
        super().__init__(merek, tahun)
        self.jenis = jenis
    
    # Override method parent
    def info(self):
        return f"Sepeda {self.merek} jenis {self.jenis} tahun {self.tahun}"
    
    def bergerak(self):
        return "Sepeda dikayuh"

class Motor(Kendaraan):
    def __init__(self, merek, tahun, cc):
        super().__init__(merek, tahun)
        self.cc = cc
    
    def info(self):
        # Memanggil method parent
        info_parent = super().info()
        return f"{info_parent} dengan kapasitas mesin {self.cc}cc"
    
    def bergerak(self):
        return "Motor digas"

# Membuat objek dari class turunan
sepeda = Sepeda("Polygon", 2019, "Gunung")
motor = Motor("Yamaha", 2020, 150)

print(sepeda.info())
print(sepeda.bergerak())
print(motor.info())
print(motor.bergerak())

# Polymorphism
print("\nPolymorphism:")
def gerakkan_kendaraan(kendaraan):
    print(kendaraan.info())
    print(kendaraan.bergerak())

print("Polymorphism dengan fungsi:")
gerakkan_kendaraan(sepeda)
gerakkan_kendaraan(motor)

# Duck Typing
print("\nDuck Typing:")
class Bebek:
    def bersuara(self):
        return "Kwek kwek"
    
    def berenang(self):
        return "Bebek berenang"

class Manusia:
    def bersuara(self):
        return "Halo"
    
    def berenang(self):
        return "Manusia berenang"

def buat_suara(objek):
    print(objek.bersuara())

def buat_berenang(objek):
    print(objek.berenang())

bebek = Bebek()
manusia = Manusia()

buat_suara(bebek)
buat_suara(manusia)
buat_berenang(bebek)
buat_berenang(manusia)
