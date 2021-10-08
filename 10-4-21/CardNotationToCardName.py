short = input("Enter The Card Notation: ")

if short[0] == "1" and short[1] == "0":
    first = short[0] + short[1] + " of"
elif short[0] == "A":
    first = "Ace of"
elif short[0] == "J":
    first = "Jack of"
elif short[0] == "Q":
    first = "Queen of"
elif short[0] == "K":
    first = "King of"
elif short[0] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
    first = short[0] + " of"

if short[1] == "0":
    if short[2] == "D":
        second = "Diamonds"
    elif short[2] == "H":
        second = "Hearts"
    elif short[2] == "S":
        second = "Spades"
    elif short[2] == "C":
        second = "Clubs"
else:
    if short[1] == "D":
        second = "Diamonds"
    elif short[1] == "H":
        second = "Hearts"
    elif short[1] == "S":
        second = "Spades"
    elif short[1] == "C":
        second = "Clubs"

print("The Card Entered is:", first, second)