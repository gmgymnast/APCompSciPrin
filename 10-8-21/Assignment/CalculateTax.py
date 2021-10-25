person1 = eval(input("Enter Income for Person 1: "))
person2 = eval(input("Enter Income for Person 2: "))
income = person1 + person2

if income <= 50000:
    tax = income * 0.01
elif income >= 50001 and income <= 75000:
    leftIncome = income - 50000
    tax = (50000 * 0.01) + leftIncome * 0.02
elif income >= 75001 and income <= 100000:
    leftIncome = income - 75000
    tax = (50000 * 0.01) + (25000 * 0.02) + leftIncome * 0.03
elif income >= 100001 and income <= 250000:
    leftIncome = income - 100000
    tax = (50000 * 0.01) + (25000 * 0.02) + (25000 * 0.03) + leftIncome * 0.04
elif income >= 250001 and income <= 500000:
    leftIncome = income - 250000
    tax = (50000 * 0.01) + (25000 * 0.02) + (25000 * 0.03) + (150000 * 0.04) + leftIncome * 0.05
elif income >= 500001:
    leftIncome = income - 500000
    tax = (50000 * 0.01) + (25000 * 0.02) + (25000 * 0.03) + (150000 * 0.04) + (250000 * 0.05) + leftIncome * 0.06

print("-----------------------------")
print("Income of Person 1: $" + str(person1))
print("Income of Person 2: $" + str(person2))
print("-----------------------------")
print("Total Income: $" + str(income))
print("Total Tax $" + str(tax))
print("-----------------------------")

