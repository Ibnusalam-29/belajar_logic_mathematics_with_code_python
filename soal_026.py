#Menghitung Diskon

hargaAsli = 150000
diskon = 20  # dalam persen
hargaSetelahDiskon = hargaAsli - (diskon / 100 * hargaAsli)

print(f"harga seteleh diskon adalah {hargaSetelahDiskon}")

#Menetukan Diskon Berdasarkan Harga
hargaAsli = 150000
if hargaAsli > 100000:
    diskon = 10
elif hargaAsli <= 200000:
    diskon = 20
else:
    diskon = 5

hargaSetelahDiskon = hargaAsli - (diskon / 100 * hargaAsli)
print(f"Harga setelah diskon adalah {hargaSetelahDiskon} dengan diskon {diskon}%")
