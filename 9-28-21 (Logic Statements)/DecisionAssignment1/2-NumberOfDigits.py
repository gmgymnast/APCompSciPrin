number = int(input("Enter a Number: "))

if number < 0:
    number *= -1

if number < 10:
    print("1 Digit")
elif number < 100:
    print("2 Digits")
elif number < 1000:
    print("3 Digits")
elif number < 10000:
    print("4 Digits")
elif number < 100000:
    print("5 Digits")
elif number < 1000000:
    print("6 Digits")
elif number < 10000000:
    print("7 Digits")
elif number < 100000000:
    print("8 Digits")
elif number < 1000000000:
    print("9 Digits")
elif number < 10000000000:
    print("10 Digits")