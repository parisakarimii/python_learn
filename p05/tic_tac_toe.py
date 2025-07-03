import random


board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner():
    
    win_conditions = [
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8], 
        [0, 3, 6],
        [1, 4, 7], 
        [2, 5, 8], 
        [0, 4, 8], 
        [2, 4, 6]  
    ]
    
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '-':
            return board[condition[0]]  
    return None  


def player_move(char):
    while True:
        move = int(input("num: ")) - 1
        if board[move] != 'X' and board[move] != 'O':
            board[move] = char
            break
        else:
            print("full")


def computer_move(char):
    while True:
        move = random.randint(0, 8)
        if board[move] != 'X' and board[move] != 'O':
            board[move] = char
            break


def play_game():
    mode = input("Do you want to play with a friend or computer? (friend/computer): ").lower()
    for turn in range(9):  
        print_board()  
        
        if mode == "friend":
            char = 'X' 
            if turn % 2 == 0:
                char = 'X'
            else:
                char = 'O'

            print(f"Player {char}'s turn")
            player_move(char)
        elif mode == "computer":
            if turn % 2 == 0:
                char = 'X'
                print("Player X's turn")
                player_move(char)
            else:
                char = 'O'
                print("Computer's turn")
                computer_move(char)
        
        
        winner = check_winner()
        if winner:
            print_board()
            print(f"winner: {winner}")
            return  
        
    print_board()  
    print("draw")  

 
play_game()
