import random

def get_user_choice():
    choices = ['rock','scissors','paper']
    while True:
        user_input = input("your choice: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("invalid input!")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user, computer):
    if user == computer:
        return "draw!"
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return "you win!"
    else:
        return "computer win!"


def play_game(rounds):
    user_wins = 0
    computer_wins = 0

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nyour choice: {user_choice}")
        print(f"computer choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "you win" in result:
            user_wins += 1
        elif "computer win" in result:
            computer_wins += 1

    print(f"final result \n you: {user_wins} computer: {computer_wins} ")


rounds = int(input("round: "))
play_game(rounds)
