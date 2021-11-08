num = int(input("Enter a Number: "))
for i in range(2, num):
    for j in range(2, i): 
        if i % j == 0: i = i  
    else: print(i)