# تابع بررسی برنده
def check_winner(row1, row2, row3):
    # بررسی ردیف‌ها
    for row in [row1, row2, row3]:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return row[0]
    # بررسی ستون‌ها
    for col in range(3):
        if row1[col] == row2[col] == row3[col] and row1[col] != '_':
            return row1[col]
    return None

# نمونه بازی
row1 = input().split(" ")
row2 = input().split(" ")
row3 = input().split(" ")

winner = check_winner(row1, row2, row3)
if winner:
    print(f"winner: {winner}")
else:
    print("draw")
