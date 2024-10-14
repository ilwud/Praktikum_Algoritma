angka = int(input("masukkan angka:"))

for i in range(angka,0, -1 ):
    for j in range(i,1, -1):
        print (i ,end='')
    print(i)