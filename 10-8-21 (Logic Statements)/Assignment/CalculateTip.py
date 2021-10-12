bill = eval(input("Enter your Bill: $"))
sL = eval(input("Enter your Satisfaction Level: "))

if sL == 3:
    tip = bill * .20
elif sL == 2:
    tip = bill * .15
elif sL == 1:
    tip = bill * .10

print("-------------------")
print("Bill:", '${:,.2f}'.format(bill))
print("Satisfaction Level:", sL)
print("-------------------")
print("Tip:", '${:,.2f}'.format(tip))
print("-------------------")