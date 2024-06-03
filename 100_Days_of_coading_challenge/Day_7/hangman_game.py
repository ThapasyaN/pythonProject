# A: TODO-1 - Randomly choose a word from the word_list and assign it to a
#  variable called chosen_word.
import random

# E: TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)

# D: TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# E: TODO-3: - Import the logo from hangman_art.py and print it at the start
#  of the game.
from hangman_art import logo
print(logo)

# test coding
# print(f'Pssst, the solution is {chosen_word}.')

# B: TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
# with 5 "_" representing each letter to guess.
# create blanks
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"

# C: TODO-1: - Use a while loop to let the user guess again. The loop should only
#  stop once the user has guessed all the letters in the chosen_word and 'display'
#  has no more blanks ("_"). Then you can tell the user they've won.

# A: TODO-2 - Ask the user to guess a letter and assign their answer to a variable
#  called guess.Make guess lowercase

# B: TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the
# display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display
# should be ["_", "p", "p", "_", "_"].

# A: TODO-3 - Check if the letter the user guessed (guess) is one of the letters
#  in the chosen_word.

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()

    # E: TODO-4: - If the user has entered a letter they've already guessed,
    #  print the letter and let them know.
    if guess in display:
        print(f"you have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n
        # Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # D: TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    # Join all the elements in the list and turn it into a String.
    if guess not in chosen_word:
        # E: TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's
        #  not in the word.
        print(f"you have guessed {guess}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    # print(f"{' '.join(display)}")

    # B: TODO-3: - Print 'display' and you should see the guessed letter in the
    #  correct
    #  position and every other letter replace with "_".
    # Hint - Don't worry about getting the user to guess the next letter. We'll tackle
    # that in step 3.
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

    # E: TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages

    # D: TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    #  remaining
    print(stages[lives])
print(f"the word is: {chosen_word}")
