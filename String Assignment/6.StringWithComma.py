n = input("Please enter your number without a comma: ")

last3 = n[len(n) - 3] + n[len(n) - 2] + n[len(n) - 1]
first = n - last3
print(first + "," + last)