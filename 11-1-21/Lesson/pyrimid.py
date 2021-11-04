r = int(input("Enter the Number of Rows: "))

for i in range(0, r):
    for j in range(0, r - i): print(" ", end = "")
    for k in range(0, 2 * i + 1): print('*', end = "")
    print("")