def main(): 
    print(f"A: {swap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"B: {shift([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"C: {replace_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"D: {remove_middle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"E: {extreme([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"F: {order([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"G: {duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
def swap(a): 
    a[0], a[-1] = a[-1], a[0]
    return a
def shift(a): 
    a.insert(0, a.pop())
    return a
def replace_even(a):
    for i, p in enumerate(a): 
        if p % 2 == 0: a[i] = 0
    return a
def remove_middle(a):
    if len(a) % 2 == 0: 
        for i in range(2): a.pop(len(a)//2)
    else: a.pop(len(a)//2)
    return a
def extreme(a): return f'Largest: {max(a)}, Smallest: {min(a)}'
def order(a): return a == sorted(a)
def duplicate(a): return len(a) != len(set(a))
print(main())