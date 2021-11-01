word = 'rum'

for length in range(1, len(word)+1):
    for pos in range(0, len(word)-length+1):
        print(word[pos:pos+length])