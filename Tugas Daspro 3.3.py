# Dictionary jadwal Daspro IF2
jadwal_if2 = {
    "Senin": "08.00 - 10.00",
    "Selasa": "10.00 - 12.00",
    "Rabu": "13.00 - 15.00",
    "Kamis": "08.00 - 10.00",
    "Jumat": "13.00 - 15.00"
}

# Dictionary jadwal Daspro IF3 (sebelum penggabungan)
jadwal_if3 = {
    "Senin": "07.00 - 09.00",
    "Selasa": "09.00 - 11.00",
    "Rabu": "12.00 - 14.00",
    "Kamis": "07.00 - 09.00",
    "Jumat": "12.00 - 14.00"
}

# Fungsi untuk menggabungkan dua dictionary
def gabung_jadwal(jadwal1, jadwal2):
    gabungan_jadwal = jadwal2.copy()  # Salin jadwal IF3 ke dictionary gabungan
    for hari, waktu in jadwal1.items():
        # Jika hari sudah ada di dictionary gabungan, gabungkan waktu
        if hari in gabungan_jadwal:
            gabungan_jadwal[hari] += ", " + waktu
        else:
            # Jika hari belum ada, tambahkan ke dictionary gabungan
            gabungan_jadwal[hari] = waktu
    return gabungan_jadwal

# Gabungkan jadwal IF2 ke jadwal IF3
jadwal_gabungan = gabung_jadwal(jadwal_if2, jadwal_if3)

# Cetak jadwal gabungan
print("Jadwal Gabungan Daspro IF2 dan IF3:")
for hari, waktu in jadwal_gabungan.items():
    print(f"{hari}: {waktu}")
