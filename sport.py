import random

def sports_guessing_game():
    sports = ["football", "basketball", "tennis", "soccer", "baseball", "golf", "hockey", "volleyball", "cricket", "rugby"]
    
    # Choose a random sport
    secret_sport = random.choice(sports)
    
    print("Welcome to the Sports Guessing Game!")
    print("I've picked a sport. Can you guess which one it is?")
    
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        # Get user input
        guess = input("Enter your guess: ").lower()
        
        # Increase the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_sport:
            print(f"Congratulations! You guessed the sport '{secret_sport}' correctly in {attempts} attempts.")
            break
        else:
            print("Incorrect. Try again.")
    
    else:
        print(f"Sorry, you've run out of attempts. The correct sport was '{secret_sport}'.")

if __name__ == "__main__":
    sports_guessing_game()
