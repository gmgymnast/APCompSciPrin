def main():
    inputStr = input("Enter a String: ")
    count = int(input("How Many Representations: "))
    delimiter = input("Seperated By: ")

    print(repeat(inputStr, count, delimiter))

def repeat(string, n, delim):
    retval = string
    for i in range(1, n): retval += delim + string
    return retval

main()