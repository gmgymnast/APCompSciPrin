from random import *
playerC, compC = input("Enter Your Choice: ").lower(), choice(["rock", "paper", "scissors"])
print("Comptuer Picked:", compC)
if playerC == "rock": playerC = "a"
if compC == "rock": compC = "a"

if playerC == compC: print("Tie") 
elif playerC == "a" and compC == "scissors": print("Player Won")
elif playerC == "scissors" and CompC == "a": print("Computer Won")
else: print("Player Won") if(compC < playerC) else print("Computer Won") 