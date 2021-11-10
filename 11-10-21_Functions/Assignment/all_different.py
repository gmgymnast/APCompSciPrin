def main():
    number1, number2, number3 = int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: "))
    print("All Different:", all_different(number1, number2, number3))

def all_different(x, y, z): return x != y != z
main()