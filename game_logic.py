import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """ Display the snowman stage for the current number of mistakes and checks for win """
    print("\n" + "=" * 50)
    print("🌨️  SNOWMAN MELTDOWN 🌨️".center(50))
    print("=" * 50)
    
    # Display the snowman ASCII art
    print(STAGES[mistakes])
    
    # Display the word with better formatting
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\n" + "-" * 50)
    print(f"  Word:  {display_word}")
    print("-" * 50)
    
    # Display guessed letters
    if guessed_letters:
        guessed_display = ", ".join(sorted(guessed_letters))
        print(f"\n  📝 Guessed Letters: {guessed_display}")
    else:
        print(f"\n  📝 Guessed Letters: (none yet)")
    
    print(f"  ❄️  Mistakes: {mistakes} / 3")
    print("=" * 50 + "\n")
    
    check_for_win(display_word, secret_word)

def check_for_win(display_word, secret_word):
    """ Checks whether all letters have been guessed """
    if display_word.replace(" ", "") == secret_word:
        print("\n" + "*" * 50)
        print("🎉 🎉 🎉  CONGRATULATIONS!  🎉 🎉 🎉".center(50))
        print("*" * 50)
        print(f"\n  ✅ You won! The word was: {secret_word.upper()}")
        print("  ❄️  The snowman survived another day!\n")
        play_again()

def input_validation(guess):
    return len(guess) == 1 and guess.isalpha()

def play_again():
    while True:
        print("=" * 50)
        play_again_input = input("🔄 Would you like to play again? (y/n): ")
        if play_again_input.lower() in ["y", "yes"]:
            print("\n" * 2)  # Add some spacing before new game
            play_game()
        elif play_again_input.lower() in ["n", "no"]:
            print("\n" + "=" * 50)
            print("👋 Thanks for playing! See you next time!".center(50))
            print("=" * 50 + "\n")
            exit()
        else:
            print("\n  ⚠️  Please enter 'y' or 'n'.\n")

def play_game():
    """ Main-function with game-loop """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    
    # Welcome banner
    print("\n" + "=" * 50)
    print("🌨️  WELCOME TO SNOWMAN MELTDOWN! 🌨️".center(50))
    print("=" * 50)
    print("\n  Can you guess the word before the snowman melts?")
    print("  You have 3 chances. Good luck!\n")
    
    while True:
        try:
            display_game_state(mistakes, secret_word, guessed_letters)
        except IndexError:
            print("\n" + "*" * 50)
            print("💧 💧 💧  GAME OVER  💧 💧 💧".center(50))
            print("*" * 50)
            print(f"\n  ❌ You lost! The word was: {secret_word.upper()}")
            print("  ☀️  Unfortunately, the snowman has melted.\n")
            play_again()
        guess = input("💭 Guess a letter: ").lower()
        if not input_validation(guess):
            print("\n  ⚠️  Please enter exactly one letter!\n")
            continue
        
        if guess in guessed_letters:
            print(f"\n  ⚠️  You already guessed '{guess}'! Try a different letter.\n")
            continue
            
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"\n  ✅ Great! '{guess.upper()}' is in the word!\n")
        else:
            mistakes += 1
            print(f"\n  ❌ Sorry! '{guess.upper()}' is not in the word.\n")