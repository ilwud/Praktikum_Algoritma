nilai_total = 0
nilai_jumlah = 0

while True:
    nilai = input("masukkan nilai : ")
    if nilai == "" :
        break
    nilai = nilai.upper()

    if nilai == 'A':
        angka = 4.00
    elif nilai == 'A-':
        angka = 3.75
    elif nilai == 'B+':
        angka = 3.50
    elif nilai == 'B':
        angka = 3.00
    elif nilai == 'B-':
        angka = 2.75
    elif nilai == 'C+':
        angka = 2.50
    elif nilai == 'C':
        angka = 2.00
    elif nilai == 'C-':
        angka = 1.75
    elif nilai == 'D':
        angka = 1.50
    elif nilai == 'E':
        angka = 1.25
    else:
        print("Nilai tidak valid, masukkan nilai yang benar.")
        continue
    nilai_total += angka
    nilai_jumlah += 1

if nilai_jumlah > 0:
    rata_rata = nilai_total / nilai_jumlah
    print(f"Rata-rata nilai: {rata_rata:.2f}")
else:
    print("Tidak ada nilai yang dimasukkan.")