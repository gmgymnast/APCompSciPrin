#TicTacToe
from random import randint
from math import *

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
turn  = randint(0,1)
game = True
won = 0

def main():
    global game, turn, board, taken, won
    while game:
        if turn == 0:
            print("Your Turn")
            for row in board: print("{: >2} {: >2} {: >2}".format(*row))
            selection = eval(input("Enter A Square (1-9): "))
            if checkAvalibility(str(selection)) == False: 
                print("Square was taken. Try Again")
                main()
            else: 
                if selection == 1: board[0][0] = 'O'
                elif selection == 2: board[0][1] = 'O'
                elif selection == 3: board[0][2] = 'O'
                elif selection == 4: board[1][0] = 'O'
                elif selection == 5: board[1][1] = 'O'
                elif selection == 6: board[1][2] = 'O'
                elif selection == 7: board[2][0] = 'O'
                elif selection == 8: board[2][1] = 'O'
                elif selection == 9: board[2][2] = 'O'
                turn = 1
        else:
            selection = randint(1,9)
            if checkAvalibility(str(selection)) == False: main()
            else: 
                if selection == 1: board[0][0] = 'X'
                elif selection == 2: board[0][1] = 'X'
                elif selection == 3: board[0][2] = 'X'
                elif selection == 4: board[1][0] = 'X'
                elif selection == 5: board[1][1] = 'X'
                elif selection == 6: board[1][2] = 'X'
                elif selection == 7: board[2][0] = 'X'
                elif selection == 8: board[2][1] = 'X'
                elif selection == 9: board[2][2] = 'X'
                print(f"Computer Just Played in Square {selection}")
                turn = 0

        if board[0][0] != "-" and board[0][1] != "-" and board[0][2] != "-" and board[1][0] != "-" and board[1][1] != "-" and board[1][2] != "-" and board[2][0] != "-"  \
            and board[2][1] != "-" and board[2][2] != "-": won = 3

        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": won = 2
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X": won = 2
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X": won = 2
        elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X": won = 2
        elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X": won = 2
        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X": won = 2
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": won = 2
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X": won = 2
        
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O": won = 1
        elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O": won = 1
        elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O": won = 1
        elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O": won = 1
        elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O": won = 1
        elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O": won = 1
        elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": won = 1
        elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O": won = 1
       
        if won == 1:
            print("Congratulations! You won!")
            game = False
            quit()
        elif won == 2:
            print("You lost!")
            game = False
            quit()
        elif won == 3:
            print("Tie Game")
            game = False
            quit()
        else:
            game = True

def checkAvalibility(selection):
    if selection == '1': return board[0][0] == '-'
    elif selection == '2': return board[0][1] == '-'
    elif selection == '3': return board[0][2] == '-'
    elif selection == '4': return board[1][0] == '-'
    elif selection == '5': return board[1][1] == '-'
    elif selection == '6': return board[1][2] == '-'
    elif selection == '7': return board[2][0] == '-'
    elif selection == '8': return board[2][1] == '-'
    elif selection == '9': return board[2][2] == '-'

print("Welcome to Tic Tac Toe!")
main()
