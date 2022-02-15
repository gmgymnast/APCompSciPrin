n = int(input("Enter A Number To Convert: "))

val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

i = 0
romanN = ""

while  n > 0:
    for _ in range(n // val[i]):
        romanN += sym[i]
        n -= val[i]
    i += 1
    
print(romanN)