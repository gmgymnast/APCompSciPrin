q = 0
d = 0
n = 0

while q <= 2:
    if (n * 0.05) + (d * 0.1) + (q * 0.25) == 0.50:
        print(q, "Quarters", d, "Dimes", n, "Nickels == 50 Cents")   
    n += 1

    if 0.50 / 0.05 == n - 1:
        d += 1
        n = 0
    if 0.50 / 0.1 == d - 1:
        q += 1
        d = 0
        n = 0
