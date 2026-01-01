#Jumlah bilangan Genap dari 1 sampai 10

jumlah = 0

for i in range(1, 11):
    if i % 2 == 0:
        jumlah += i
print(f"Jumlah bilangan genap dari 1 sampai 10 adalah {jumlah}")