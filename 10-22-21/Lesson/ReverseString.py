# Read input from the user
inputStr = input("Enter a Word: ")

# Add each character to the beginning of the reversed String
reverse = ""

for ch in inputStr:
    reverse = ch + reverse

# Display the result
print(inputStr, "reversed string is:", reverse)