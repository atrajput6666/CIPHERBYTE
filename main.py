import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to stop playing: ").lower()
        if player_choice == "quit":
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
