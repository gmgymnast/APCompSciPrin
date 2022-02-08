message = "This is a program to explain reverse cipher"
translated = ''
l = len(message)

while l >= 0:
    translated += message[l]
    l -= 1
print(f"The Cipher Text Is {translated}")