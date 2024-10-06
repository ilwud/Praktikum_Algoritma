import math

sa = int(input("sisi a : "))
sb = int(input("sisi b : "))
sc = int(input("sisi c : "))

if sa + sb > sc and sa + sc > sb and sb + sc > sa:
    if sa==sb and sb==sc and sa==sc :
        print("segitiga sama sisi")
    elif sa==sb or sa==sc or sc==sb and sa != sc and sb!=sc :
        print("segitiga sama kaki")
    elif sa**2 + sb**2 ==sc**2 or sb**2 + sc**2 ==sa**2 or sa**2 + sc**2 ==sb**2 :
        print("segitiga siku siku")
    else:
        print("segitiga sembarang")
else:
    print("segitiga tidak valid")
