from random import randint
from art import logo

print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5


def compare_num(number, guess, turns):
    if guess > number:
        print("Too high.")
        return turns -1
    elif guess < number:
        print("Too Low.")  
        return turns -1     
    else:
        print(f"You got it! The answer is: {guess} ") 
        


def guess_difficulty():
    level = input("Choose a difficulty. Type 'easy or 'hard: ").lower()
    if level == "easy":
        return EASY_LEVEL   
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 200")
    number = randint(1, 100)
    # print(f"random number is: {number}")

    turns = guess_difficulty()
    
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = compare_num(number, guess, turns)
        if turns == 0:
            print("You've ran out of gusses you lose.")
            return
        elif guess != number:
            print("Guess again.")

game()