# Read input from the user
inputStr = input("Enter a string: ")

# Check Each character. If it is a vowel display an underscore instead of 
# The Character

for ch in inputStr:
    if ch in "aeiouAEIOU":
        print("_", end = "")
    else:
        print(ch, end = "")

print()