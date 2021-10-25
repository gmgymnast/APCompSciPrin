import sys

i = input("Enter a List of Integer: ")

iArray = i.split(",")

small = sys.maxsize + 1
large = -sys.maxsize - 1

even = 0
odd = 0

for i in iArray:
    if small > int(i):
        small = int(i)
    if large < int(i):
        large = int(i)
        
    if int(i) % 2 == 0:
        even += 1  
    else: 
        odd += 1
    
print("smallest:", small)
print("largest:", large)
print("even:", even)
print("odd:", odd)