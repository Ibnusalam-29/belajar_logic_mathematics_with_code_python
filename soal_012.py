#Jumlah bilangan Ganjil dari 1 sampai 10

count = 0
for i in range(1, 21):
    if i % 2 != 0:
        count += i
print(f"Jumlah bilangan ganjil dari 1 sampai 10 adalah {count}")