tahun = int(input("Masukkan tahun: "))

while True:
    bulan = int(input("Masukkan nomor bulan (1-12): "))
    if bulan < 1 or bulan > 12:
        print("bye bye :3")
        break
    elif bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            print("bulan", bulan, "tahun", tahun, "ada 29 hari")
        else:
            print("bulan", bulan, "tahun", tahun, "ada 28 hari")
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        print("bulan", bulan, "ada 31 hari")
    else:
        print("bulan", bulan, "ada 30 hari")