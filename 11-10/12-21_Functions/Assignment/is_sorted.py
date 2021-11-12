def main(x, y, z): print("Sorted:", sorted(x, y, z))
def sorted(x, y, z): return x <= y <= z
main(int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: ")))