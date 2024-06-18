import random

def roll_dice():
    return random.randint(1, 6)

def play_round(player_name):
    input(f"{player_name}, press Enter to roll the dice...")
    roll = roll_dice()
    print(f"{player_name} rolled a {roll}")
    return roll

def main():
    print("Welcome to the Dice Rolling Simulator Game!")
    print("Each player will take turns rolling a dice.")
    print("The player who wins 2 out of 3 rounds first will be the winner.\n")

    player1_wins = 0
    player2_wins = 0
    rounds = 1

    while player1_wins < 2 and player2_wins < 2 and rounds <= 3:
        print(f"\nRound {rounds}:")
        player1_roll = play_round("Player 1")
        player2_roll = play_round("Player 2")
        
        if player1_roll > player2_roll:
            print("Player 1 wins this round!")
            player1_wins += 1
        elif player2_roll > player1_roll:
            print("Player 2 wins this round!")
            player2_wins += 1
        else:
            print("It's a tie! No one wins this round.")
        
        rounds += 1

    print("\nFinal Result:")
    if player1_wins > player2_wins:
        print("Player 1 is the overall winner!")
    elif player2_wins > player1_wins:
        print("Player 2 is the overall winner!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    main()
