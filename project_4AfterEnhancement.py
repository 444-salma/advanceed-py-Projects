import random


MIN_NUMBER = 1
MAX_NUMBER = 10


def get_player_name() -> str:
    """Ask for the player's name and return it."""
    return input("Enter your name: ").strip()


def ask_yes_no(prompt: str) -> bool:
    """Return True if the user answers yes, otherwise False."""
    return input(prompt).strip().lower() == "yes"


def get_guess(min_n: int, max_n: int) -> int:
    """Prompt the user until they enter a valid integer within [min_n, max_n]."""
    while True:
        raw = input(f"Guess a number ({min_n}–{max_n}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if min_n <= guess <= max_n:
            return guess

        print(f"Out of range. Please enter a number between {min_n} and {max_n}.")


def play_round(min_n: int, max_n: int) -> int:
    """
    Play one round of the guessing game.
    Returns the number of attempts taken to guess correctly.
    """
    secret = random.randint(min_n, max_n)
    attempts = 0
    print(f"\nI am thinking of a number between {min_n} and {max_n}.")

    while True:
        guess = get_guess(min_n, max_n)
        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return attempts

        print("Hint:", "higher" if guess < secret else "lower")


def main() -> None:
    """Run the game with replay support."""
    print("Welcome to the Number Guessing Game!")
    name = get_player_name()
    print(f"Hello, {name}!")

    while True:
        play_round(MIN_NUMBER, MAX_NUMBER)
        if not ask_yes_no("Play again? (yes/no): "):
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    main()
