# Hangman Game

This is a simple Hangman game implemented in Python for the command-line interface (CLI). The game allows the player to guess a word letter by letter. The player has 6 lives to guess the word correctly. 

## Rules

1. The game randomly selects a word, and the player's task is to guess it letter by letter.
2. The player starts with 6 lives. Each incorrect guess will result in losing one life.
3. The game ends in two scenarios:
   - The player guesses the word correctly within 6 lives.
   - The player runs out of lives without guessing the word.
4. The player can only guess one letter at a time. Guessing more than one letter or a non-alphabetic character will result in an error.
5. The player is shown the current state of the word with underscores representing unguessed letters.
6. The player cannot guess the same letter again, whether it's correct or incorrect.
7. After each guess, the game will inform the player if the guessed letter is correct and reveal its position(s) in the word.

## Usage

1. Make sure you have Python installed on your system.
2. Clone the repository or download the files form the repo.
3. Open a terminal or command prompt and navigate to the directory containing `hangman-game.py`.
4. Run the script using the command:
    ```bash
    python hangman-game.py
    ```

## Example

Here's an example of how the game might look:

```bash
You are hanged, you lose.
The word was lime.
_ _ _ _
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.
I know this code is messed up. I was in a hurry. But hey, it still works 😉.
