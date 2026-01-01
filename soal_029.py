#Jumlah huruf dalam sebuah kata
kata = "Pemrograman"
jumlahHuruf = len(kata)

print(f"Jumlah huruf dalam kata '{kata}' adalah {jumlahHuruf}")

#Jumlah kata dalam sebuah kalimat
kalimat = "Saya sedang belajar pemrograman Python"
jumlahKata = len(kalimat.split())

print(f"Jumlah kata dalam kalimat adalah {jumlahKata}")

#Menentukan huruf vokal dalam sebuah kata
vokal = "aeiouAEIOU"
jumlahVokal = sum(1 for char in kata if char in vokal)
print(f"Jumlah huruf vokal dalam kata '{kata}' adalah {jumlahVokal}")

#Menentukan huruf konsonan dalam sebuah kata
konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
jumlahKonsonan = sum(1 for char in kata if char in konsonan)
print(f"Jumlah huruf konsonan dalam kata '{kata}' adalah {jumlahKonsonan}")