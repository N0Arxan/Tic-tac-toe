import os
import random
import time

num_moves = 0

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
m_board = [i for i in range(0,9)]


def print_board():
    global board
    os.system("cls" if os.name == "nt" else "clear")
    formatted_board = ""
    for i in range(0, len(board), 3):
        
        row = " | ".join(board[i:i+3])
        
        formatted_board += row + "\n"

    print(formatted_board)

def move_x():
    move = int(input("Enter a index num for your move as X : "))
    global num_moves
    while True:
        if board[move] != "x" and board[move] != "o":
            board[move] = "x"
            m_board.pop(move)
            num_moves += 1
            return board[move] 
        else:
            move = int(input("Invalid Input Enter a num _: "))

def move_o():
    move = random.choice(m_board)
    global num_moves
    while True:
        if board[move] != "x" and board[move] != "o":
            board[move] = "o"
            num_moves += 1
            return board[move]
        else:
            move = random.randint(0,8)

def res_check(move_x):
    global num_moves
    win_comb = [(0,1,2),(3,4,5),(6,7,8), #Horizental
                (0,3,6),(1,4,7),(2,5,8), #Vertical
                (2,4,6),(0,4,8)]         #Diagonal
    for comb in win_comb:
        if board[comb[0]] == board[comb[1]] == board[comb[2]]:
            if board[comb[0]] == move_x:
                return "You(X) Won"
            else:
                return "Machine(O) Won"
    
    if num_moves < 9:
        return False  
    
    return "Its a Tie"
      
            
def Run():
    
    print_board()
    
    while True : 
        
        mx = move_x()
        result = res_check(mx)
        print_board()
        if result:
            return result
        
        os.system("cls" if os.name == "nt" else "clear")
        print("Thinking ...")
        time.sleep(1)

        move_o()
        print_board()
        result = res_check(mx)
        if result:
            return result

def main():
    final = Run()
    print(final)


if __name__ == "__main__":
    main()



