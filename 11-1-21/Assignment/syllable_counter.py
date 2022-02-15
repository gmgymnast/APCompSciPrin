w, sCount, noW = input("Enter a Word: "), 1, "aeiouyAEIOUY"
for n, i in enumerate(w): sCount += 0 if w[n - 1] in noW else + 1 if i in noW and (i in "aiouyAIOUY" and n == len(w) - 1) else 0 
print("Number of Syllables:", sCount)