message = "This is a program to explain reverse cipher"
translated = ''
l = len(message) - 1

def encrypt_ceaser_cipher(message, key):
    encryption_str = ""
    for l in message:
        if l.isupper():
            temp = 65 + ((ord(l) - 65 + key) % 26)
            encryption_str += chr(temp)
        elif l.islower():
            temp = 97 + ((ord(l) - 97 + key) % 26)
            encryption_str += chr(temp)
        else:
            encryption_str += l
    return encryption_str

def decrypt_ceaser_cipher(message, key):
    decryption_str = ""
    for l in message:
        if l.isupper():
            temp = 65 + ((ord(l) - 65 - key) % 26)
            decryption_str += chr(temp)
        elif l.islower():
            temp = 97 + ((ord(l) - 97 - key) % 26)
            decryption_str += chr(temp)
        else:
            decryption_str += l
    return decryption_str

key = int(input("Enter the key: "))
print(f"The Cipher Text Is: {encrypt_ceaser_cipher(message, key)}")
print(f"The Regular Text Is: {decrypt_ceaser_cipher(encrypt_ceaser_cipher(message, key), key)}")

