
# ---------------- FUNCTIONS ---------------- #
import random
from game_data import data
from art import logo,vs
print(logo)

def get_random_account():
    """Return a random account from the data."""
    return random.choice(data)

def format_account(account, label):
    """Format account data for display."""
    return f"Compare {label}: {account['name']}, a {account['description']}, from {account['country']}."

def check_answer(guess, a_followers, b_followers):
    """Check if user's guess is correct."""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

# ---------------- GAME LOGIC ---------------- #

score = 0
game_should_continue = True

account_a = get_random_account()
account_b = get_random_account()

while account_a == account_b:
    account_b = get_random_account()

while game_should_continue:

    print(format_account(account_a, "A"))
    print(vs)
    print(format_account(account_b, "B"))

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"✅ You're right! Current score: {score}.\n")
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
    else:
        game_should_continue = False
        print(f"❌ Sorry, that's wrong. Final score: {score}")