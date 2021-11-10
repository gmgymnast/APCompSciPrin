def main():
    number1, number2, number3 = int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: "))
    print("Sorted:", sorted(number1, number2, number3))

def sorted(x, y, z): return x <= y <= z
main()