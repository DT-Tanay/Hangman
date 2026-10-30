"""
CodeAlpha Python Programming Internship
Task 1: Hangman Game

A simple text-based Hangman game. The computer picks a random word from a
small predefined list and the player guesses it one letter at a time.
The player loses after 6 incorrect guesses.

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "internship", "developer", "keyboard", "algorithm"]
MAX_WRONG_GUESSES = 6

# One drawing per number of wrong guesses (0 to 6).
HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def choose_word(words=WORDS):
    """Return a random word from the given list."""
    return random.choice(words)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden, e.g. 'p _ t h _ n'."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_guess(guessed_letters):
    """Keep asking until the player enters a valid, new single letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_round(word):
    """Play one full game of Hangman. Returns True if the player wins."""
    guessed_letters = []
    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("        WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"I'm thinking of a word with {len(word)} letters.")
    print(f"You can make up to {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or '-'}")
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations, you won! The word was '{word}'.")
                return True
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    print(HANGMAN_STAGES[MAX_WRONG_GUESSES])
    print(f"\nGame over! The word was '{word}'.")
    return False


def main():
    """Run the game and let the player play again."""
    wins = 0
    games = 0

    while True:
        won = play_round(choose_word())
        games += 1
        wins += int(won)
        print(f"Score: {wins} win(s) out of {games} game(s).")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
