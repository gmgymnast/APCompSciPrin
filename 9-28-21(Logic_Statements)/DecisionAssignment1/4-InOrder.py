n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

if (n1 < n2 < n3) or (n3 < n2 < n1):
    print("The Numbers are in Order")
else:
    print("The Numbers are not in Order")