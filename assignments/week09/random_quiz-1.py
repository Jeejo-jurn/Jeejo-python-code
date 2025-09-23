"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

def number_guessing_game():
    print("=== SIMPLE GUESSING GAME ===")
    print("Guess my number between 1 and 20!")
    print("You have 6 attempts.\n")

    target = random.randint(1, 20)
    max_attempts = 6

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))

            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.\n")
                continue

            if guess < target:
                print("Too low! Try a higher number.\n")
            elif guess > target:
                print("Too high! Try a lower number.\n")
            else:
                print(f"Congratulations! You guessed it right. The number was {target}.")
                break
        except ValueError:
            print("Please enter a valid number.\n")
    else:
        print(f"Game over! The correct number was {target}.\n")

# เรียกใช้ฟังก์ชัน
number_guessing_game()

