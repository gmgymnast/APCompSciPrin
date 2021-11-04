w = input("Enter a Word: ")
[print(w[pos:pos+length]) for length in range(1, len(w)+  1) for pos in range(0, len(w) - length + 1)]