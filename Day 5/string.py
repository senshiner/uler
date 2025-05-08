
# Hari 5 - String

# Membuat string
str1 = "Hello"
str2 = 'World'

# Concatenation (penggabungan string)
print(str1 + " " + str2)  # Hello World

# String multiline
multiline_str = """Ini adalah string
yang terdiri dari
beberapa baris"""
print("\nString multiline:")
print(multiline_str)

# Mengakses karakter dalam string (indeks)
text = "Python"
print("\nMengakses karakter:")
print("Karakter pertama:", text[0])  # P
print("Karakter ketiga:", text[2])   # t

# Slicing string
print("\nSlicing string:")
print("text[0:3]:", text[0:3])    # Pyt
print("text[:4]:", text[:4])      # Pyth
print("text[2:]:", text[2:])      # thon
print("text[-3:]:", text[-3:])    # hon

# Panjang string
print("\nPanjang string:", len(text))  # 6

# Metode string
contoh = " Belajar Python "
print("\nMetode string:")
print("Upper:", contoh.upper())            # BELAJAR PYTHON
print("Lower:", contoh.lower())            # belajar python
print("Strip:", contoh.strip())            # Belajar Python
print("Replace:", contoh.replace("Python", "Java"))  # Belajar Java
print("Split:", "Apel,Jeruk,Mangga".split(","))  # ['Apel', 'Jeruk', 'Mangga']

# Format string
nama = "Andi"
umur = 25
print("\nFormat string:")
print("Halo, nama saya {} dan umur saya {} tahun".format(nama, umur))
print(f"Halo, nama saya {nama} dan umur saya {umur} tahun")  # f-string (Python 3.6+)
