import os
import random
board = [i for i in range(9)]
l = 0
def print_board():
    
    global board
    os.system("cls")
    print(f"{board[:3]} \n{board[3:6]} \n{board[6:]}")
    print("enter q any moment for quitting")
    
print_board()

def move_x():
    move = int(input("Enter a num Between 1...9 for your move as X"))
    
    board[move]="x"

for i in range(9):
    print_board()
    move_x()



