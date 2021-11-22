upper_count, lower_count = 0, 0
def main(s): 
    for i in s: Check_Case(i) 
    return (f"Upper Case: {upper_count}\nLower Case: {lower_count}")
    
def Check_Case(s): 
    global upper_count, lower_count
    if s.isupper(): upper_count += 1
    elif s.islower(): lower_count += 1
print(main(input("Enter a string: ")))