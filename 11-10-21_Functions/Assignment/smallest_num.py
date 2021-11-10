def main():
    number1, number2, number3 = int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: "))
    print("Smallest:", smallest_num(number1, number2, number3))

def smallest_num(x, y, z): return min(x, y, z)
main()