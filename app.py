from random_word import RandomWords

# Step 1: Generate a random word using the external library
r = RandomWords()

# Step 2: Display the state of the word
def show_word(random_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in random_word])

# Step 3: Main Hangman logic
def hangman_game():
    random_word = r.get_random_word()  # Generate a random word
    if not random_word:  # Handle case where the API doesn't return a word
        print("Error: Could not fetch a random word. Please try again later.")
        return

    length_of_word = len(random_word)
    guessed_letters = set()
    max_attempts = 6

    print("Welcome to Hangman!")
    print(f'CLUE: The word has {length_of_word} letters.')

    while max_attempts > 0:
        print("\nWord to guess: " + show_word(random_word, guessed_letters))
        print("Guessed letters: " + ", ".join(sorted(guessed_letters)))
        print(f"You have {max_attempts} attempts left.")

        # Get input from the user
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single valid letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed this letter. Try again.")
            continue

        # Add the guessed letter to the set
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in random_word:
            print("Correct guess!")
        else:
            max_attempts -= 1
            print(f"Wrong guess. You lost an attempt.")

        # Check if all letters are guessed
        if all(letter in guessed_letters for letter in random_word):
            print("\nCongratulations! You guessed the word: " + random_word)
            break
    else:
        print("\nGame over! The word was: " + random_word)

# Step 4: Start the game
if __name__ == "__main__":
    hangman_game()
