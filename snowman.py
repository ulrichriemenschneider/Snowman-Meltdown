import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """ Display the snowman stage for the current number of mistakes and checks for win """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")
    check_for_win(display_word, secret_word)

def check_for_win(display_word, secret_word):
    """ Checks whether all letters have been guessed """
    if display_word.replace(" ", "") == secret_word:
        print("You won! Congratulation!")
        exit()

def play_game():
    """ Main-function with game-loop """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    while True:
        try:
            display_game_state(mistakes, secret_word, guessed_letters)
        except IndexError:
            print("You loose!")
            exit()
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if not guess in secret_word:
            mistakes += 1
            print(f"{guess} is not in the word you are looking for")
   
if __name__ == "__main__":
    play_game()