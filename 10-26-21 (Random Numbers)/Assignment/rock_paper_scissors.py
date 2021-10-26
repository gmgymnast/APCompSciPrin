from random import *

playerC = input("Enter Your Choice: ").lower()
compC = choice(["rock", "paper", "scissors"])

if playerC == "rock": playerC = "a"
if compC == "rock": compC = "a"

if playerC == compC: print("Tie") 
else: print("Player Won") if(compC < playerC) else print("Computer Won") 