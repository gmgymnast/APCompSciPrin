from math import *

n = eval(input("Enter a Number: ")) - 1

while n >= 0:
    rt = sqrt(n)
    if int(rt + 0.5) ** 2 == n:
        print(n)
    n -= 1