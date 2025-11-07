def konversi(huruf):
    mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
    return mapping.get(huruf.upper(), None)

def hitung_rata():
    nilai = []
    while True:
        huruf = input("Masukkan nilai atau ketik 'done': ").strip()
        if huruf.lower() == 'done':
            break
        angka = konversi(huruf)
        if angka is not None:
            nilai.append(angka)
        else:
            print("Input tidak valid, masukkan huruf A-E saja!")

    if nilai:
        rata = sum(nilai) / len(nilai)
        print(f"\nNilai angka: {nilai}")
        print(f"Rata-rata: {rata}")
    else:
        print("Tidak ada nilai yang dimasukkan.")

# Jalankan program
hitung_rata()
