t = (1, 2, 3, 4, 5)                                                      #1
print("1 is in t")if 1 in t else print("1 is Not in t")                  #2
print(f"First 2 Elements: {t[:2]} ")                                     #3
for i in range(len(t)):print(f"5 is at Index {i}")if t[i] == 5 else None #4
print(f"Tuple Length: {len(t)}")                                         #5