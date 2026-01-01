#Cek Palindrome, Palindrome adalah kata atau kalimat yang jika dibaca dari depan maupun belakang tetap sama.

angka = "123212"

if angka == angka[::-1]:
    print(f"{angka} adalah Palindrome")
else:
    print(f"{angka} bukan Palindrome")

kata = "katak"

if kata == kata[::-1]:
    print(f"{kata} adalah Palindrome")
else:
    print(f"{kata} bukan Palindrome")