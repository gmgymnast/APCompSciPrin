def main():
    number1, number2, number3 = int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: "))
    print("Average:", average_num(number1, number2, number3))
    
def average_num(x, y, z): return (x + y + z) /  3
main()