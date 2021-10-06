n = eval(input("Enter A Number To Convert: "))

val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

rn = ""
i = 0
while  n > 0:
    for _ in range(n // val[i]):
        rn += syb[i]
        n -= val[i]
    i += 1
print(rn)