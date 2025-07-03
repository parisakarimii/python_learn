import random


symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔']


def spin_slot_machine():
    results = []  
    for _ in range(3): 
        symbol = random.choice(symbols) 
        results.append(symbol)  
    return results  

while True:
    result = spin_slot_machine()
    print(result[0],result[1],result[2])

    if result[0] == result[1] == result[2]:
        print("jackpot")
        break

    continue_playing = input("continue? ").strip().lower()
    if continue_playing == "no":
        print("finish")
        break