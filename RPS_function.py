import random


def get_player_choice():
    user_choice = input("Please select a choice betwen rock, paper or scissors!").lower()
    return user_choice


def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        return "user"
    else:
        print("Computer wins!")
        return "computer"


while True:
    user_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break