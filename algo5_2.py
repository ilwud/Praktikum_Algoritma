print("Masukkan umur pengunjung atau ketik 'selesai' untuk berhenti.")

total_harga = 0

while True:
    umur = input("Masukkan umur pengunjung: ").strip()
    
    if umur.lower() == 'selesai': 
        break
    
    try:
        umur = int(umur)
        if umur <= 2:
            harga = 0
        elif 3 <= umur <= 12:
            harga = 14
        elif umur >= 65:
            harga = 18
        else:
            harga = 23
        
        total_harga += harga
        print(f"Harga tiket untuk umur {umur} adalah: ${harga}")
        
    except ValueError:
        print("Umur tidak valid, masukkan angka yang benar.")

print(f"Total keseluruhan harga tiket: ${total_harga}")