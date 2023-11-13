import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ")
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ")
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to the classic game of rock, paper, scissors!")

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print("Player chose:", player_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(player_choice, computer_choice))

        play_again = input("Do you want to play again? (yes or no): ")
        if play_again.lower() != 'yes':
            break

if _name_ == "_main_":
    main()