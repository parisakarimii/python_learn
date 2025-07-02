board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner():
 
    win_conditions = [
        [0, 1, 2], # ردیف اول
        [3, 4, 5], # ردیف دوم
        [6, 7, 8], # ردیف سوم
        [0, 3, 6], # ستون اول
        [1, 4, 7], # ستون دوم
        [2, 5, 8], # ستون سوم
        [0, 4, 8], # قطر اول
        [2, 4, 6]  # قطر دوم
    ]
    
 
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '-':
            return board[condition[0]] 
    return None  


def play_game():
    for turn in range(9): 
        print_board()  
        
       
        char = input("X or O: ").upper()
        
        move = int(input("num: ")) - 1
        
        if board[move] != 'X' and board[move] != 'O':
            board[move] = char
        else:
            print("full")
            continue 
        
    
        winner = check_winner()
        if winner:
            print_board()
            print(f"winner: {winner}")
            return  
        
    print_board() 
    print("draw") 


play_game()
