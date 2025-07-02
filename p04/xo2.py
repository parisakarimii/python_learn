# ایجاد یک صفحه 3x3 که خونه‌هاش با اعداد 1 تا 9 شماره‌گذاری شدن
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# تابع برای نمایش صفحه بازی
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# تابع برای بررسی اینکه آیا کسی برنده شده است
def check_winner():
    # حالت‌های برنده شدن (ردیف‌ها، ستون‌ها و قطرها)
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
    
    # بررسی هر حالت برای پیدا کردن برنده
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '-':
            return board[condition[0]]  # برنده پیدا شد
    return None  # هنوز برنده‌ای وجود ندارد

# تابع اصلی بازی
def play_game():
    for turn in range(9):  # 9 بار می‌تونیم بازی کنیم چون 9 تا خونه داریم
        print_board()  # نمایش صفحه بازی
        
        # گرفتن حرف (X یا O) از بازیکن
        char = input("X or O: ").upper()
        
        # گرفتن شماره خونه از بازیکن
        move = int(input("num: ")) - 1
        
        # اگر خونه خالی بود، حرف بازیکن رو داخل اون خونه قرار بده
        if board[move] != 'X' and board[move] != 'O':
            board[move] = char
        else:
            print("full")
            continue  # برگرد به شروع حلقه تا بازیکن دوباره تلاش کنه
        
        # بررسی برنده شدن
        winner = check_winner()
        if winner:
            print_board()
            print(f"winner: {winner}")
            return  # پایان بازی چون کسی برنده شده
        
    print_board()  # نمایش صفحه بازی
    print("draw")  # اگر 9 حرکت انجام شد و کسی برنده نشد، بازی مساوی است

# شروع بازی
play_game()