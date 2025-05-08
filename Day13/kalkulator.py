
# Modul kalkulator

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol"
    return a / b

# Variabel dalam modul
pi = 3.14159

# Fungsi yang hanya dijalankan jika file ini dieksekusi langsung
if __name__ == "__main__":
    print("Ini adalah modul kalkulator")
    print(f"4 + 2 = {tambah(4, 2)}")
    print(f"4 - 2 = {kurang(4, 2)}")
    print(f"4 * 2 = {kali(4, 2)}")
    print(f"4 / 2 = {bagi(4, 2)}")
