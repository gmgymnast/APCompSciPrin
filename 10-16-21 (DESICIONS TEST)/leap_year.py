year = int(input("Enter the Test Year: "))

print(year, "is a Leap Year") if ((year % 400 == 0) or ((year % 4 == 0 ) and (year % 100 != 0))) else print(year, "is not a Leap Year")