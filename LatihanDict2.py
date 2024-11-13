import os
import random
import string

print(f"{'DATA MOTOR ':_^30}")
data = dict()
while True:
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range (3))
    print(f"keyFinal = {keyFinal}")
    nama = input("Enter Nama Motor\t:")
    merk = input("Enter Merk\t\t:")
    cc = input("Enter CC\t\t:")
    data[keyFinal] = {'namamotorkey' : nama, 'merkkey' : merk, 'cckey' : cc}
    opsi = input("input data Lagi (y/t) :").lower()
    if opsi == 't' :
        break

print(data)

print("-"*40)
print(F"Key\t Nama Motor\t Merk\t cc")
print("-"*40)

for key, value in data.items():
    print(f"{key}.\t{ data [key]['namamotorkey']}\t {data[key]['merkkey']}\t {data[key]['cckey']}")