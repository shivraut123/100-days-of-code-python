def set_attempts(level):
    if level == "easy":
        return 10
    else:
        return 5

""""Function to check the guess"""
def check_guess(guess,secret_no):
    if guess == secret_no:
        return "correct"
    elif guess > secret_no:
        return "high"
    else:
        return "low"

import random
def play_game():
    print("Welcome to The Number Guessing Game")
    print("I am thinking of Number between 1 to 100")
    level=input("Choose difficulty level. Type 'easy' or 'hard' ")
    attempts = set_attempts(level)
    secret_no = random.randint(1,100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        try:
            guess = int(input("Make a guess:"))
        except ValueError:
            print("you have entered invalid no. Enter Numerical value")
            guess = int(input("Make a guess:"))
        result = check_guess(guess,secret_no)

        if result == "correct":
            print(f"You got it. The answer was {attempts}")

        elif result == "high":
            print("Too high")
        else:
            print("Too low")

        attempts -= 1
    print(f"You ran out of guesses. The number was {secret_no}")
play_game()


