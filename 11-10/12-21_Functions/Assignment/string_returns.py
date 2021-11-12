def main(a): print(first(a), last(a), length(a), mid(a))
def first(a): return "First Digit: " + a[0]
def last(a): return "\nLast Digit: " + a[-1]
def length(a): return "\nNumber of Digits: " + str(len(a))
def mid(a): return "\nMiddle Digit(s): " + a[(len(a)-1)//2:(len(a)+2)//2]
main(input("Enter Argument: "))