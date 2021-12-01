def main(table): 
    print(f"The Average at (0, 0) is {neighborAverage(table, 0, 0)}")
    print(f"The Average at (1, 2) is {neighborAverage(table, 1, 2)}")
    print(f"The Average at (3, 2) is {neighborAverage(table, 3, 2)}")

def neighborAverage(table, row, col):
    total, count = 0, 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < len(table) and j >= 0 and j < len(table[i]):
                total += table[i][j]
                count += 1
    return total / count

main([ [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])