"""
Task 1: Hangman Game
A simple text-based Hangman game played in the console.

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

# A small list of 5 predefined words (no file or API needed)
WORDS =WORDS = [
    "python", "program", "computer", "keyboard", "developer",
    "variable", "function", "network", "database", "software",
    "internet", "algorithm", "monitor", "browser", "library",
]

MAX_INCORRECT = 6  # Limit of incorrect guesses

# ASCII art for each stage of the hangman (0 to 6 wrong guesses)
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_guess(guessed_letters):
    """Ask the player for a valid single-letter guess."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly ONE letter.")
        elif not guess.isalpha():
            print("Please enter a letter (a-z) only.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_game():
    """Run a single round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("\n=== WELCOME TO HANGMAN ===")
    print(f"The word has {len(word)} letters. You can make {MAX_INCORRECT} wrong guesses.")

    while incorrect_guesses < MAX_INCORRECT:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "none")
        print(f"Wrong guesses left: {MAX_INCORRECT - incorrect_guesses}\n")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition: every letter of the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nWord:", display_word(word, guessed_letters))
            print(f"\n🎉 Congratulations! You guessed the word: {word.upper()}")
            return

    # Loop ended -> player ran out of guesses
    print(HANGMAN_STAGES[MAX_INCORRECT])
    print(f"\n💀 Game over! The word was: {word.upper()}")


def main():
    """Main loop that lets the player play again."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
