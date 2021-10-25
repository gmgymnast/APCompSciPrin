s = input("Enter a String: ")

for i in range(len(s)):
    if s[i].isupper():
        print("Upper Case Letters:", s[i], end="")

    