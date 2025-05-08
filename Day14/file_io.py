
# Hari 14 - Operasi File

# Menulis ke file
print("Menulis ke file:")
try:
    # Mode 'w' akan membuat file baru atau menimpa jika sudah ada
    with open("data.txt", "w") as file:
        file.write("Ini adalah baris pertama\n")
        file.write("Ini adalah baris kedua\n")
        file.write("Ini adalah baris ketiga\n")
    print("Data berhasil ditulis ke file")
except Exception as e:
    print(f"Error: {e}")

# Membaca file
print("\nMembaca seluruh file sekaligus:")
try:
    with open("data.txt", "r") as file:
        # Membaca seluruh isi file
        content = file.read()
        print(content)
except Exception as e:
    print(f"Error: {e}")

# Membaca file baris per baris
print("\nMembaca file baris per baris:")
try:
    with open("data.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() untuk menghilangkan \n di akhir
except Exception as e:
    print(f"Error: {e}")

# Membaca file sebagai list
print("\nMembaca file sebagai list:")
try:
    with open("data.txt", "r") as file:
        lines = file.readlines()
        print(lines)
except Exception as e:
    print(f"Error: {e}")

# Menambahkan data ke file yang sudah ada
print("\nMenambahkan data ke file:")
try:
    # Mode 'a' (append) untuk menambah tanpa menimpa data lama
    with open("data.txt", "a") as file:
        file.write("Ini adalah baris tambahan\n")
        file.write("Ini adalah baris terakhir\n")
    print("Data berhasil ditambahkan")
except Exception as e:
    print(f"Error: {e}")

# Membaca file setelah ditambahkan data
print("\nMembaca file setelah ditambahkan data:")
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Error: {e}")

# Menulis dan membaca data biner
print("\nMenulis dan membaca data biner:")
try:
    # Mode 'wb' untuk menulis file biner
    with open("data.bin", "wb") as file:
        file.write(b'\x00\x01\x02\x03\x04')
    
    # Mode 'rb' untuk membaca file biner
    with open("data.bin", "rb") as file:
        binary_data = file.read()
        print(binary_data)
except Exception as e:
    print(f"Error: {e}")

# Cek apakah file ada
import os
print("\nCek keberadaan file:")
print(f"data.txt ada? {os.path.exists('data.txt')}")
print(f"data.bin ada? {os.path.exists('data.bin')}")
print(f"tidak_ada.txt ada? {os.path.exists('tidak_ada.txt')}")

# Mendapatkan informasi file
print("\nInformasi file:")
if os.path.exists("data.txt"):
    print(f"Ukuran data.txt: {os.path.getsize('data.txt')} bytes")
    print(f"Waktu modifikasi terakhir: {os.path.getmtime('data.txt')}")

# Manipulasi path file
print("\nManipulasi path file:")
current_dir = os.getcwd()
print(f"Direktori saat ini: {current_dir}")

file_path = os.path.join(current_dir, "data", "test.txt")
print(f"Path lengkap: {file_path}")
print(f"Direktori: {os.path.dirname(file_path)}")
print(f"Nama file: {os.path.basename(file_path)}")
