from os import system, name
from graphics import stages, logo
import random


def clear():
    """Clears the screen according to the os."""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


end_of_game = False
word_list = ["aardvark", "baboon", "camel", "banana", "strawberry", "grape", "apple", "watermelon",
             "orange", "blueberry", "lemon", "peach", "avocado", "cherry",
             "cantaloupe", "raspberry", "pear", "lime", "blackberry", "clementine",
             "mango", "plum"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You are hanged 💀, you lose.")
            print(f"The word was {chosen_word}.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
    if not end_of_game:
        if lives == 1:
            print(f"You have 1 life remaining.")
        else:
            print(f"You have {lives} lives remaining.")
