import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        guess = input("Enter your guess: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

number_guessing_game()