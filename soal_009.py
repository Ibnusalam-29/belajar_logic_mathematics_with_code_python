#cek bilangan prima

n = 29
is_prima = True

for i in range(2, n):
    if n % i == 0:
        is_prima = False

print(f"{n} adalah bilangan prima: {is_prima}")