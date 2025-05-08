
# 100 Hari Belajar Python
# File index untuk menjelajahi materi

def list_materi():
    materi = [
        "Day 1: Hello World - Pengenalan dasar Python dengan program Hello World",
        "Day 2: Tipe Data - Berbagai tipe data dalam Python (string, integer, float, boolean, dll)",
        "Day 3: Variabel - Cara membuat dan menggunakan variabel dalam Python",
        "Day 4: Operator - Operator aritmatika, perbandingan, logika, dan assignment",
        "Day 5: String - Manipulasi dan operasi pada string",
        "Day 6: List - Pembuatan dan manipulasi list (array) dalam Python",
        "Day 7: Tuple - Penggunaan tuple (array yang tidak dapat diubah) dalam Python",
        "Day 8: Dictionary - Struktur data key-value dalam Python",
        "Day 9: Set - Koleksi unik dan tidak berurutan dalam Python",
        "Day 10: Kondisi - Penggunaan if, elif, else untuk pengambilan keputusan",
        "Day 11: Perulangan - Penggunaan for loop dan while loop",
        "Day 12: Function - Membuat dan menggunakan fungsi",
        "Day 13: Modul - Mengorganisasi kode dalam modul dan mengimpornya",
        "Day 14: File I/O - Operasi baca dan tulis file",
        "Day 15: Exception - Penanganan kesalahan (error handling)",
        "Day 16: Class - Object-Oriented Programming (OOP) dengan class dan object",
        "Day 17: Date and Time - Manipulasi tanggal dan waktu",
        "Day 18: Regular Expressions - Pencocokan dan manipulasi pola teks",
        "Day 19: JSON - Bekerja dengan format data JSON",
        "Day 20: API dan Requests - Melakukan HTTP request ke API"
    ]
    
    print("Daftar Materi 100 Hari Belajar Python (20 hari pertama):")
    print("=" * 80)
    for materi_item in materi:
        print(materi_item)
    print("=" * 80)
    print("\nUntuk menjalankan contoh program, masuk ke folder tiap hari dan jalankan file Python di dalamnya.")
    print("Contoh: cd 'Day 1' && python hello.py")

if __name__ == "__main__":
    list_materi()
