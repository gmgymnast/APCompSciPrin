def main(a, b, c, d, e, f, g, h): print(prob1(a, b, c), prob2(d, e, f), prob3(g), prob3(h))
def prob1(x, y, z): return "Problem 1: " + smallest(x, y, z) + average(x, y, z)
def prob2(x, y, z): return "\nProblem 2: " + same(x, y, z) + different(x, y, z) + order(x, y, z)
def prob3(a): return "\nProblem 3: " + first(a) + last(a) + length(a) + mid(a)
def smallest(x, y, z): return "\n   Smallest Num: " + str(min(x, y, z))
def average(x, y, z): return "\n   Average Num: " + str((x + y + z) /  3)
def same(x, y, z): return "\n   All Same: " + str(x == y == z)
def different(x, y, z): return "\n   All Different: " + str(x != y != z)
def order(x, y, z): return "\n   Sorted: " + str(x <= y <= z)
def first(a): return "\n   First Digit: " + a[0]
def last(a): return "\n   Last Digit: " + a[-1]
def length(a): return "\n   Number of Digits: " + str(len(a))
def mid(a): return "\n   Middle Digit(s): " + a[(len(a)-1)//2:(len(a)+2)//2]
main(int(input("Prob 1 Info 1: ")), int(input("Prob 1 Info 2: ")), int(input("Prob 1 Info 3: ")),\
    int(input("Prob 2 Info 1: ")), int(input("Prob 2 Info 2: ")), int(input("Prob 2 Info 3: ")),\
    input("Prob 3 Info 1: "), input("Prob 3 Info 2: "))