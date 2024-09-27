import math
lintang1 = math.radians(float(input("Lintang Kota 1;")))
bujur1 = math.radians(float(input("Bujur Kota 1;")))
lintang2 = math.radians(float(input("Lintang kota 2;")))
bujur2 = math.radians(float(input("Bujur kota 2;")))

jarijaribumi = 6371
Lintangkota = lintang2 - lintang1
Bujurkota = bujur2 - bujur1
A = math.sin(Lintangkota/2)*2+math.cos(lintang1)*math.cos(lintang2)*math.sin(Bujurkota/2)*2
C = 2*math.atan2(math.sqrt(A), math.sqrt(1 - A))
final = jarijaribumi*C

print(f"jarak antara dua titik tersebut adalah {final}kilometer")
