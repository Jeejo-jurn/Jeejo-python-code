import random

def test_random():
    random_number = random.randint(1, 10)
    print(random_number)
    
test_random()

def guess_the_number():
    target = random.randint(1, 10)
    print("Random number 1 to 10! Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < target:
                print("Too low! Try a higher number.")
            elif guess > target:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it right. The number was {target}.")
                break
        except ValueError:
            print("Please enter a valid number.")
#เรียกฟังก์ชัน
guess_the_number()
