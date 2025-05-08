
# Hari 17 - Date and Time

import datetime
import time
import calendar
from datetime import timedelta

# Mendapatkan waktu saat ini
print("Waktu saat ini:")
waktu_sekarang = datetime.datetime.now()
print(f"Datetime now(): {waktu_sekarang}")
print(f"Tanggal: {waktu_sekarang.date()}")
print(f"Waktu: {waktu_sekarang.time()}")

# Komponen datetime
print("\nKomponen datetime:")
print(f"Tahun: {waktu_sekarang.year}")
print(f"Bulan: {waktu_sekarang.month}")
print(f"Hari: {waktu_sekarang.day}")
print(f"Jam: {waktu_sekarang.hour}")
print(f"Menit: {waktu_sekarang.minute}")
print(f"Detik: {waktu_sekarang.second}")
print(f"Mikrodetik: {waktu_sekarang.microsecond}")

# Membuat objek datetime
print("\nMembuat objek datetime:")
tanggal_tertentu = datetime.datetime(2023, 12, 31, 23, 59, 59)
print(f"Tanggal tertentu: {tanggal_tertentu}")

# Membuat objek date
print("\nMembuat objek date:")
tanggal = datetime.date(2023, 12, 31)
print(f"Tanggal: {tanggal}")

# Membuat objek time
print("\nMembuat objek time:")
waktu = datetime.time(23, 59, 59)
print(f"Waktu: {waktu}")

# Format datetime
print("\nFormat datetime:")
print(f"Format default: {waktu_sekarang}")
print(f"Format ISO: {waktu_sekarang.isoformat()}")
print(f"Format custom: {waktu_sekarang.strftime('%A, %d %B %Y %H:%M:%S')}")
print(f"Format lain: {waktu_sekarang.strftime('%d/%m/%Y %H:%M')}")

# Format code umum
print("\nFormat code umum:")
print(f"%Y: {waktu_sekarang.strftime('%Y')}")  # Tahun 4 digit
print(f"%m: {waktu_sekarang.strftime('%m')}")  # Bulan 2 digit
print(f"%d: {waktu_sekarang.strftime('%d')}")  # Hari 2 digit
print(f"%H: {waktu_sekarang.strftime('%H')}")  # Jam 24-jam
print(f"%I: {waktu_sekarang.strftime('%I')}")  # Jam 12-jam
print(f"%M: {waktu_sekarang.strftime('%M')}")  # Menit
print(f"%S: {waktu_sekarang.strftime('%S')}")  # Detik
print(f"%A: {waktu_sekarang.strftime('%A')}")  # Nama hari lengkap
print(f"%a: {waktu_sekarang.strftime('%a')}")  # Nama hari singkat
print(f"%B: {waktu_sekarang.strftime('%B')}")  # Nama bulan lengkap
print(f"%b: {waktu_sekarang.strftime('%b')}")  # Nama bulan singkat
print(f"%p: {waktu_sekarang.strftime('%p')}")  # AM/PM

# Parse string menjadi datetime
print("\nParse string menjadi datetime:")
string_tanggal = "31/12/2023 23:59:59"
parsed_date = datetime.datetime.strptime(string_tanggal, "%d/%m/%Y %H:%M:%S")
print(f"String asli: {string_tanggal}")
print(f"Parsed datetime: {parsed_date}")
print(f"Tahun: {parsed_date.year}")

# Operasi timedelta
print("\nOperasi timedelta:")
sekarang = datetime.datetime.now()
print(f"Waktu sekarang: {sekarang}")

# Menambah atau mengurangi waktu
besok = sekarang + timedelta(days=1)
print(f"Besok: {besok}")

kemarin = sekarang - timedelta(days=1)
print(f"Kemarin: {kemarin}")

sekarang_plus_1_jam = sekarang + timedelta(hours=1)
print(f"1 jam dari sekarang: {sekarang_plus_1_jam}")

next_week = sekarang + timedelta(weeks=1)
print(f"Minggu depan: {next_week}")

# Perbedaan dua waktu
print("\nPerbedaan dua waktu:")
waktu1 = datetime.datetime(2023, 1, 1, 0, 0, 0)
waktu2 = datetime.datetime(2023, 1, 2, 12, 30, 45)
selisih = waktu2 - waktu1
print(f"Waktu 1: {waktu1}")
print(f"Waktu 2: {waktu2}")
print(f"Selisih: {selisih}")
print(f"Selisih dalam detik: {selisih.total_seconds()}")
print(f"Selisih dalam jam: {selisih.total_seconds() / 3600}")

# Modul time
print("\nModul time:")
# Waktu saat ini dalam detik sejak epoch (1 Jan 1970)
epoch_time = time.time()
print(f"Waktu epoch: {epoch_time}")

# Konversi epoch time ke struct_time
struct_time = time.localtime(epoch_time)
print(f"Struct time: {struct_time}")
print(f"Tahun: {struct_time.tm_year}")
print(f"Bulan: {struct_time.tm_mon}")
print(f"Hari: {struct_time.tm_mday}")

# Format struct_time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(f"Formatted time: {formatted_time}")

# Modul calendar
print("\nModul calendar:")
# Menampilkan kalender bulan
cal = calendar.month(2023, 12)
print("Kalender Desember 2023:")
print(cal)

# Cek apakah tahun kabisat
print("\nCek tahun kabisat:")
print(f"2023 adalah tahun kabisat: {calendar.isleap(2023)}")
print(f"2024 adalah tahun kabisat: {calendar.isleap(2024)}")

# Jumlah hari dalam bulan
print("\nJumlah hari dalam bulan:")
print(f"Jumlah hari Februari 2023: {calendar.monthrange(2023, 2)[1]}")
print(f"Jumlah hari Februari 2024: {calendar.monthrange(2024, 2)[1]}")  # Kabisat
