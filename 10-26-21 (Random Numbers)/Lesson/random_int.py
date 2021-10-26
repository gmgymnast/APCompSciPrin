from random import *

for i in range(5):
    num = randint(1, 2)
    print(num, "- Heads") if num == 1 else print(num, "- Tails")