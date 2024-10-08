import os
import random

board_num = [i for i in range(9)]
l = 0
def print_board ():
    os.system('cls')
    global board_num
    print(f"{board_num[:3]}\n{board_num[3:6]}\n{board_num[6:]}",sep="|" )
    
def move_o ():
    move = int(input("enter your move "))
    global l 
    while True:
        if board_num[move] != "X" or board_num[move] != "O" :
            board_num[move] = "O"
            l =+ 1
            break
        else:
            print("invalid input")
            continue
def move_x ():
    global l 
    
    while True:
        xo = [i for i in range(9)]
        move = random.choice(xo)
        if board_num[move] != "X" or board_num[move] != "O" :
            board_num[move] = "X"
            l =+ 1
            break
        else:
            print("invalid input")
            continue

def main ():
    while l != 9 :
        print_board()
        move_o()
        move_x()

main()