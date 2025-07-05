from art import logo, vs
from gamedata import data
import random


# format data
def format_data(account):
    account_name = account["name"]
    account_discription = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_discription}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    # Generate a random account from data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user to guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen & print the logo
    print("\n"* 40)
    print(logo)

    # Get follower count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # Check if user is correct
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, thats wrong. Final Score: {score}")
        game_should_continue = False


    # make the game repeatable

# making account at position B become the next account at position A.
