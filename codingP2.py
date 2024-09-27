import math

a = int(input("Masukkan nilai a= "))
b = int(input("Masukkan nilai b= "))

jumlah = a+b
kurang = b-a
kali = a*b
persen = a%b
bagi = a/b
log = math.log(a)
pangkat = a**b

print(f'''
Jumlah a ditambah b adalah {jumlah} 
Selisih antara a dan b adalah {kurang}
Jumlah a dikali b adalah {kali}
Jumlah sisa pembagian dari hasil a dibagi b adalah {persen}
Jumlah a dibagi b adalah {bagi}
Hasil dari log(a) adalah {log} 
Hasil a pangkat b adalah {pangkat} 
    ''')