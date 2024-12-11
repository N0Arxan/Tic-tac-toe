import os
import random
board = [i for i in range(9)]
l = 0


def print_board():
    global board
    os.system("cls" if os.name == "nt" else "clear")


    for i in range(0, len(board), 3):
        
        row = " | ".join(board[i:i+3])
        
        formatted_board += row + "\n"


    print(formatted_board.strip())

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    


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

def res_check():
    if board[0] == board[1] == board[2]:
        if board[0] == "o":
            return "o"
        else:
            return "x"
    elif board[3] == board[4] == board[5]:
        if board[3] == "o":
            return "o"
        else:
            return "x"
    elif board[6] == board[7] == board[8]:
        if board[6] == "o":
            return "o"
        else:
            return "x"
    elif board[0] == board[3] == board[6]:
        if board[0] == "o":
            return "o"
        else:
            return "x"
    elif board[1] == board[4] == board[7]:
        if board[1] == "o":
            return "o"
        else:
            return "x"
    elif board[2] == board[5] == board[8]:
        if board[2] == "o":
            return "o"
        else:
            return "x"
    elif board[0] == board[4] == board[8]:
        if board[0] == "o":
            return "o"
        else:
            return "x"
    elif board[2] == board[4] == board[6]:
        if board[2] == "o":
            return "o"
        else:
            return "x"
    else:
        return False
            
while True:
    print_board()
    
    move_x()
    res = res_check()
    print_board()
    
    if res:
        break
    elif l==9:
        break
    
    move_o()
    res = res_check()
    print_board()
    if res:
        break
    
    
if res == False:
    print(f"no winner")
if res == "o":
    print("OOO WIIIIINNNNN")
if res == "x":
    print("XXXXX WIIIIIINNNN")



