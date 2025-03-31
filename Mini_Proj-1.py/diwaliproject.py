import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Game loop that allows replay
    while True:
        # The computer selects a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed_correctly = False
        
        print("I have selected a number between 1 and 100. Try to guess it!")
        
        # Game loop continues until the player guesses the correct number
        while not guessed_correctly:
            try:
                # Get user input and check if it's a valid integer
                player_guess = int(input("Enter your guess: "))
                attempts += 1
                
                # Check if the guess is too high, too low, or correct
                if player_guess < number_to_guess:
                    print("Too low! Try again.")
                elif player_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    guessed_correctly = True
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
            
            except ValueError:
                print("Please enter a valid number!")
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    number_guessing_game()


import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    # Game loop continues until the player guesses the correct number
    while not guessed_correctly:
        try:
            # Get user input and check if it's a valid integer
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is too high, too low, or correct
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
        
        except ValueError:
            print("Please enter a valid number!")
        
# Start the game
if __name__ == "__main__":
    number_guessing_game()
