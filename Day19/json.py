
# Hari 19 - JSON (JavaScript Object Notation)

import json

# JSON adalah format pertukaran data yang populer
# JSON mendukung tipe data: string, number, boolean, null, object, dan array
# Python memiliki modul json untuk mengolah data JSON

# Dictionary Python ke JSON
print("Dictionary Python ke JSON:")
data = {
    "nama": "Budi",
    "umur": 25,
    "aktif": True,
    "hobi": ["membaca", "coding", "traveling"],
    "alamat": {
        "jalan": "Jl. Python No. 123",
        "kota": "Jakarta",
        "kode_pos": "12345"
    }
}

# Konversi dictionary ke JSON string
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

# Konversi dictionary ke JSON string dengan formatting
json_formatted = json.dumps(data, indent=4, sort_keys=True)
print(f"\nJSON string dengan formatting:")
print(json_formatted)

# Mengatur separators dan mengganti non-ASCII
json_compact = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
print(f"\nJSON compact: {json_compact}")

# JSON string ke Dictionary Python
print("\nJSON string ke Dictionary Python:")
json_data = '{"nama":"Andi","umur":30,"aktif":true,"hobi":["coding","gaming"]}'
python_dict = json.loads(json_data)
print(f"Dictionary Python: {python_dict}")
print(f"Nama: {python_dict['nama']}")
print(f"Umur: {python_dict['umur']}")
print(f"Hobi: {python_dict['hobi']}")

# Menulis JSON ke file
print("\nMenulis JSON ke file:")
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
print("Data berhasil ditulis ke file 'data.json'")

# Membaca JSON dari file
print("\nMembaca JSON dari file:")
try:
    with open("data.json", "r") as f:
        data_from_file = json.load(f)
        print(f"Data dari file: {data_from_file}")
except FileNotFoundError:
    print("File tidak ditemukan")

# Mengolah array JSON
print("\nMengolah array JSON:")
json_array = '''
[
    {"id": 1, "nama": "Budi", "nilai": 85},
    {"id": 2, "nama": "Andi", "nilai": 90},
    {"id": 3, "nama": "Citra", "nilai": 78}
]
'''

data_array = json.loads(json_array)
print("Data array:")
for item in data_array:
    print(f"ID: {item['id']}, Nama: {item['nama']}, Nilai: {item['nilai']}")

# Menghitung rata-rata nilai
total_nilai = sum(item["nilai"] for item in data_array)
rata_rata = total_nilai / len(data_array)
print(f"Rata-rata nilai: {rata_rata}")

# Menemukan nilai tertinggi
nilai_tertinggi = max(data_array, key=lambda x: x["nilai"])
print(f"Nilai tertinggi: {nilai_tertinggi['nama']} dengan nilai {nilai_tertinggi['nilai']}")

# JSON Schema validation
# Untuk validasi JSON schema, biasanya menggunakan library tambahan seperti jsonschema

# JSON dan web API
print("\nContoh penggunaan JSON dengan API (simulasi):")
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "username": "user1", "email": "user1@example.com"},
            {"id": 2, "username": "user2", "email": "user2@example.com"}
        ],
        "total": 2,
        "page": 1,
        "per_page": 10
    }
}
'''

response_data = json.loads(api_response)
if response_data["status"] == "success":
    users = response_data["data"]["users"]
    print(f"Total users: {response_data['data']['total']}")
    print("Daftar users:")
    for user in users:
        print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")
else:
    print("Error fetching data")

# Nested JSON parsing
print("\nParsing JSON bersarang:")
nested_json = '''
{
    "perusahaan": {
        "nama": "PT Example",
        "tahun_berdiri": 2010,
        "kantor": {
            "pusat": {
                "alamat": "Jl. Utama No. 1",
                "kota": "Jakarta",
                "telepon": "021-1234567"
            },
            "cabang": [
                {
                    "alamat": "Jl. Cabang No. 10",
                    "kota": "Bandung",
                    "telepon": "022-7654321"
                },
                {
                    "alamat": "Jl. Cabang No. 20",
                    "kota": "Surabaya",
                    "telepon": "031-9876543"
                }
            ]
        },
        "karyawan": [
            {"id": 1, "nama": "Budi", "posisi": "Manager"},
            {"id": 2, "nama": "Andi", "posisi": "Developer"},
            {"id": 3, "nama": "Citra", "posisi": "Designer"}
        ]
    }
}
'''

data_nested = json.loads(nested_json)
# Akses data bersarang
perusahaan = data_nested["perusahaan"]
print(f"Nama perusahaan: {perusahaan['nama']}")
print(f"Alamat kantor pusat: {perusahaan['kantor']['pusat']['alamat']}, {perusahaan['kantor']['pusat']['kota']}")
print(f"Jumlah kantor cabang: {len(perusahaan['kantor']['cabang'])}")
print(f"Jumlah karyawan: {len(perusahaan['karyawan'])}")

# Menampilkan semua kantor cabang
print("\nDaftar kantor cabang:")
for i, cabang in enumerate(perusahaan["kantor"]["cabang"], 1):
    print(f"Cabang {i}: {cabang['alamat']}, {cabang['kota']}, Tel: {cabang['telepon']}")

# Menampilkan semua karyawan
print("\nDaftar karyawan:")
for karyawan in perusahaan["karyawan"]:
    print(f"ID: {karyawan['id']}, Nama: {karyawan['nama']}, Posisi: {karyawan['posisi']}")
