import requests
import random
from hangman import *

# Get list of words
url = "https://bit.ly/3jK3V22"
myList = requests.get(url)
myList = myList.text.splitlines()

# Hang Man Logic
while True:
    # Choose a Random Word
    word = random.choice(myList)

    # Reinitialize all lists.
    rightGuesses = []
    wrongGuesses = []
    totalGuesses = []

    # Reset blank spaces
    numBlanks = 0
    for letter in word:
        numBlanks += 1
    blanks = ("_ " * numBlanks)
    # Clear screen and print start of Hang Man
    clear_screen()
    hangman()
    print(blanks)

    # Repeat guessing until you get the word or hangman.
    while len(wrongGuesses) <= 6 and len(rightGuesses) < numBlanks:

        # Reset the index
        index = 0
        # Ask for a guess
        print("Guesses so far: ", totalGuesses)
        guess = input("Guess a single letter: ")

        # Error Checking
        while guess == "" or len(guess) > 1 or not guess.isalpha():
            guess = input("Please type in a single letter: ")

        # If the guess is correct or not
        if guess in word and guess not in totalGuesses:
            # Store the guess into the appropriate lists.
            rightGuesses += guess
            totalGuesses += guess

            # Find all indexes of the guessed letter in the word and store that to blanks
            while index < len(word):
                index = word.find(guess, index)
                if index == -1:
                    break

                # Perform string splicing with the letter guessed
                blanks = blanks[:(index * 2)] + guess + blanks[(index * 2) + 1:]
                index += 1

            # Print out current progression on Hang Man
            clear_screen()
            hang(len(wrongGuesses))

            # Print the blanks and letters found
            print(blanks)

        # Guess is not in the word
        else:
            if guess in totalGuesses:
                print("You've already chosen this letter.")
            else:
                # Store the guess into the appropriate lists.
                wrongGuesses += guess
                totalGuesses += guess

                # Print out current progression on Hang Man
                clear_screen()
                hang(len(wrongGuesses))

                # Print the blanks and letters found
                print(blanks)

        # Check if all blanks have been filled
        if "_" not in blanks:
            print("Congratulations, you WIN!")
            break

    # After Game is finished print out the word and ask to play again
    print("The word was: " + word)
    again = input("Play again? [y/n]")

    # If yes
    if again.lower() == "y" or again.lower() == "yes":
        # Clear Screen to Play Again
        clear_screen()

    # If no
    else:
        clear_screen()
        break
# https://repl.it/@AlikanakelaKarw/hangman
