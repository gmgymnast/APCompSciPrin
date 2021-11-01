w, sCounter = input("Enter a Word: "), 1 
for n, i in enumerate(w): sCounter += 0 if w[n - 1] in "aeiouAEIOU" else + 1 if w[n] in "aeiouAEIOU" and n != len(w) - 1 else 0 
print("Number of Syllables:", sCounter)
