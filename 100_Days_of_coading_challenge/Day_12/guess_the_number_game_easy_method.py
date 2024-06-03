import random
from guess_the_number_art import logo
num = int(random.choice(range(1, 100)))
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    continue_the_game = True
    attempts_left = 10
    while continue_the_game:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        else:
            print("You win.")
            continue_the_game = False
        attempts_left -= 1
elif level == "hard":
    continue_the_game = True
    attempts_left = 5
    while continue_the_game:
        print(f"You have {attempts_left} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        else:
            print("You win.")
            continue_the_game = False
        attempts_left -= 1

print(f"The number is: {num}")




