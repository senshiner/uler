
# Hari 18 - Regular Expressions

import re

# Pencocokan dasar
print("Pencocokan dasar:")
text = "Hello, world! Python is awesome."

# Mencari pola dalam string
match = re.search(r"Python", text)
if match:
    print(f"Ditemukan: {match.group()} pada posisi {match.start()}-{match.end()}")
else:
    print("Tidak ditemukan")

# Mencari semua kemunculan
print("\nMencari semua kemunculan:")
text = "Python adalah bahasa pemrograman. Python sangat mudah dipelajari."
matches = re.findall(r"Python", text)
print(f"Ditemukan {len(matches)} kemunculan: {matches}")

# Mengganti pola
print("\nMengganti pola:")
new_text = re.sub(r"Python", "Java", text)
print(f"Teks asli: {text}")
print(f"Teks baru: {new_text}")

# Membagi string berdasarkan pola
print("\nMembagi string berdasarkan pola:")
text = "apple,banana;orange,grape;pineapple"
fruits = re.split(r"[,;]", text)
print(f"Hasil split: {fruits}")

# Metacharacters
print("\nMetacharacters:")
# . (dot) - mencocokkan karakter apapun kecuali newline
text = "cat, bat, rat, mat, fat"
pattern = r".at"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# ^ (caret) - mencocokkan awal string
pattern = r"^cat"
match = re.search(pattern, text)
print(f"Pola '{pattern}': {'Cocok' if match else 'Tidak cocok'}")

# $ (dollar) - mencocokkan akhir string
pattern = r"fat$"
match = re.search(pattern, text)
print(f"Pola '{pattern}': {'Cocok' if match else 'Tidak cocok'}")

# * (asterisk) - mencocokkan 0 atau lebih kemunculan
text = "ca cat catch category"
pattern = r"cat*"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# + (plus) - mencocokkan 1 atau lebih kemunculan
pattern = r"cat+"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# ? (question mark) - mencocokkan 0 atau 1 kemunculan
text = "color, colour"
pattern = r"colou?r"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# {} (curly braces) - mencocokkan rentang kemunculan
text = "ha haa haaa haaaa"
pattern = r"ha{2,3}"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# Character classes
print("\nCharacter classes:")
# [] - mencocokkan salah satu karakter dalam kurung
text = "cat, bat, rat, mat, fat, hat, sat"
pattern = r"[bcr]at"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# [^] - mencocokkan karakter apapun kecuali yang dalam kurung
pattern = r"[^bcr]at"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# Range karakter
pattern = r"[a-f]at"
matches = re.findall(pattern, text)
print(f"Pola '{pattern}': {matches}")

# Shorthand character classes
print("\nShorthand character classes:")
# \d - digit [0-9]
# \D - bukan digit [^0-9]
# \w - karakter word [a-zA-Z0-9_]
# \W - bukan karakter word [^a-zA-Z0-9_]
# \s - whitespace [ \t\n\r\f\v]
# \S - bukan whitespace [^ \t\n\r\f\v]
text = "Hello 123 World!"

print(f"\\d (digit): {re.findall(r'\d', text)}")
print(f"\\D (non-digit): {re.findall(r'\D', text)}")
print(f"\\w (word char): {re.findall(r'\w', text)}")
print(f"\\W (non-word char): {re.findall(r'\W', text)}")
print(f"\\s (whitespace): {re.findall(r'\s', text)}")
print(f"\\S (non-whitespace): {re.findall(r'\S', text)}")

# Groups and capture
print("\nGroups dan capture:")
text = "2022-03-15, 2023-12-31, 1999-01-01"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
for match in re.finditer(pattern, text):
    print(f"Tanggal lengkap: {match.group(0)}")
    print(f"Tahun: {match.group(1)}")
    print(f"Bulan: {match.group(2)}")
    print(f"Hari: {match.group(3)}")
    print("---")

# Named groups
print("\nNamed groups:")
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "2023-12-31")
if match:
    print(f"Tahun: {match.group('year')}")
    print(f"Bulan: {match.group('month')}")
    print(f"Hari: {match.group('day')}")

# Lookahead dan lookbehind
print("\nLookahead dan lookbehind:")
# Positive lookahead (?=...)
text = "One price: $10, another price: $20"
pattern = r"\$\d+(?= price)"
matches = re.findall(pattern, text)
print(f"Positive lookahead: {matches}")

# Negative lookahead (?!...)
pattern = r"\$\d+(?! price)"
matches = re.findall(pattern, text)
print(f"Negative lookahead: {matches}")

# Contoh implementasi
print("\nContoh implementasi:")
# Validasi email
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

emails = ["user@example.com", "invalid.email", "user@domain", "user@example.co.id"]
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")

# Validasi nomor telepon
def is_valid_phone(phone):
    pattern = r"^(\+62|0)8[1-9][0-9]{7,11}$"
    return bool(re.match(pattern, phone))

phones = ["081234567890", "+6281234567890", "0812345", "0912345678901"]
for phone in phones:
    print(f"{phone}: {'Valid' if is_valid_phone(phone) else 'Invalid'}")
