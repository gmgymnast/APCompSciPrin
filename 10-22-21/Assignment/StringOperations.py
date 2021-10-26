s, uppercase, skipping, _, index_vowel = input("Enter a String: "), "Uppercase: ", "Skipping: ", "Replace Vowel: ", "Pos of Vowel: "
for i in range(len(s)):
    if s[i].isupper(): uppercase += s[i]
    if i % 2 == 0: skipping += s[i]
    _ += "_" if s[i] in "aeiouAEIOU" else s[i]
    if s[i] in "aeiouAEIOU": index_vowel += str(i) + " "
print(uppercase, "\n" + skipping, "\n" + _, "\n# Digits:", len(s), "\n" + index_vowel)