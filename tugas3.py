import math

A = int(input("Nilai A: "))
B = int(input("Nilai B: "))
C = int(input("Nilai C: "))
print(f"Persamaan kuadrat: {A}X² + {B}X + {C}")

D = B**2 - 4*A*C
print(f"Diskriminan: {D}")

if D > 0:
    akar1 = (-B+math.sqrt(D)) / (2*A)
    akar2 = (-B-math.sqrt(D)) / (2*A)
    print(f"Akar yang berbeda")
    print(f" X1 = {akar1}")
    print(f" X2 = {akar2}")
elif D == 0:
    akar = -B / (2*A)
    print(f"Akar yang kembar")
    print(f"akar = {akar}")
elif D < 0:
    print("akar imajiner")
    print(f"X1 = -{B}+√{D} / 2*{A}")
    print(f"X2 = -{B}-√{D} / 2*{A}")
else:
    print("Persamaan tidak memiliki akar real")
