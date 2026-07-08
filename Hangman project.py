import random

# ─────────────────────────────────────────
#  Word list  (5 predefined words)
# ─────────────────────────────────────────
WORDS = ["python", "bioinformatics", "hangman", "coding", "internship"]

# ─────────────────────────────────────────
#  Hangman ASCII art  (0 = safe … 6 = dead)
# ─────────────────────────────────────────
HANGMAN_STAGES = [
    # 0 wrong guesses
    """
   -----
   |   |
       |
       |
       |
       |
=========
""",
    # 1 wrong guess
    """
   -----
   |   |
   O   |
       |
       |
       |
=========
""",
    # 2 wrong guesses
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========
""",
    # 3 wrong guesses
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
""",
    # 4 wrong guesses
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========
""",
    # 5 wrong guesses
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
""",
    # 6 wrong guesses  →  game over
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
""",
]

MAX_WRONG = 6  # maximum allowed incorrect guesses


def display_state(wrong_count: int, guessed: set, word: str) -> None:
    """Print the current hangman drawing, guessed letters, and word progress."""
    print(HANGMAN_STAGES[wrong_count])
    print(f"  Wrong guesses left : {MAX_WRONG - wrong_count}")
    print(f"  Letters guessed    : {' '.join(sorted(guessed)) or '-'}")

    # Show the word with blanks for unguessed letters
    display_word = "  " + " ".join(
        letter if letter in guessed else "_" for letter in word
    )
    print(display_word)
    print()


def get_valid_input(guessed: set) -> str:
    """Prompt the player until they enter a single, previously-unused letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("  ⚠  Please enter exactly one letter.\n")
        elif not guess.isalpha():
            print("  ⚠  Only letters are allowed.\n")
        elif guess in guessed:
            print(f"  ⚠  You already guessed '{guess}'. Try another.\n")
        else:
            return guess


def play_game() -> None:
    """Run a single round of Hangman."""
    word          = random.choice(WORDS)
    guessed       = set()      # all letters the player has tried
    wrong_letters = set()      # only the incorrect ones
    wrong_count   = 0

    print("\n" + "=" * 40)
    print("       W E L C O M E   T O")
    print("           H A N G M A N")
    print("=" * 40)
    print(f"\n  A word has been chosen ({len(word)} letters).")
    print(f"  You have {MAX_WRONG} incorrect guesses before the man hangs!\n")

    # ── Main game loop ──────────────────────
    while wrong_count < MAX_WRONG:
        display_state(wrong_count, guessed, word)

        # Check win condition BEFORE asking for a new guess
        if all(letter in guessed for letter in word):
            print(f"  🎉  You won! The word was: {word.upper()}\n")
            return

        guess = get_valid_input(guessed)
        guessed.add(guess)

        if guess in word:
            print(f"\n  ✔  '{guess}' is in the word!\n")
        else:
            wrong_count += 1
            wrong_letters.add(guess)
            print(f"\n  ✘  '{guess}' is NOT in the word.  "
                  f"({MAX_WRONG - wrong_count} guesses left)\n")

    # ── Reached here → player lost ──────────
    display_state(wrong_count, guessed, word)
    print(f"  💀  Game over! The word was: {word.upper()}\n")


def main() -> None:
    """Entry point – supports replay."""
    while True:
        play_game()
        again = input("  Play again? (y / n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Keep coding in Python. 🐍\n")
            break


if __name__ == "__main__":
    main()
