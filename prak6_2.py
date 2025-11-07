def cek_kabisat(tahun):
    """Fungsi untuk mengecek apakah suatu tahun kabisat atau tidak"""
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)


def jumlah_hari(bulan, tahun):
    """Fungsi untuk menentukan jumlah hari dalam bulan tertentu"""
    # Daftar bulan dengan jumlah hari normal
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:  # Februari, cek tahun kabisat
        if cek_kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return None


# --- Program utama ---
print("=== Program Jumlah Hari dalam Bulan ===")
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

hari = jumlah_hari(bulan, tahun)

if hari:
    print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari.")
else:
    print("Input bulan tidak valid! Harus antara 1 sampai 12.")
