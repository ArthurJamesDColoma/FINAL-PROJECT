import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_one_round():
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(player_choice, computer_choice)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return winner

def main_game():
    player_score = 0
    computer_score = 0
    
    while player_score < 2 and computer_score < 2:
        winner = play_one_round()
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"Current Score: Player {player_score} - Computer {computer_score}")
    
    if player_score == 2:
        print("Congratulations! You are the overall winner!")
    else:
        print("The computer wins the game! Better luck next time!")

if __name__ == "__main__":
    main_game()
