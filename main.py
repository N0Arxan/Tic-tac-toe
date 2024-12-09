import os
import random
board = [i for i in range(9)]
l = 0
turn = True
def print_board():
    
    global board
    os.system("cls")
    print(f"{board[:3]} \n{board[3:6]} \n{board[6:]}")
    print("enter q any moment for quitting")
    


def move_x():
    move = int(input("Enter a num Between 1...9 for your move as X : "))
    global l
    while True:
        if board[move] != "x" and board[move] != "o":
            board[move] = "x"
            
            l += 1
            break
        else:
            move = int(input("Invalid Input Enter a num _: "))

def move_o():
    move = random.randint(0,8)
    global l
    while True:
        if board[move] != "x" and board[move] != "o":
            board[move] = "o"
            l += 1
            break
        else:
            move = random.randint(0,8)
while l <= 9:
    print_board()
    move_x()
    move_o()
    print(l)





