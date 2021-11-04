from math import *

n = 1
t = 0

while n <= 100:
    rt = sqrt(n)
    if int(rt + 0.5) ** 2 == n:
        t += n
    n += 1

print(t)