import random


# Words with hints
words = {
    "python": "A popular programming language",
    "internet": "A global network connecting computers",
    "database": "Used to store and manage data",
    "keyboard": "An input device used for typing",
    "software": "Programs and applications used on a computer",
    "developer": "A person who creates software",
    "network": "A group of connected computers",
    "algorithm": "A step-by-step procedure to solve a problem"
}


# Hangman visual stages
hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """
]


def play_hangman():

    # Select random word and hint
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n==============================")
    print("        HANGMAN GAME")
    print("==============================")

    print("\nHint:", hint)

    while wrong_guesses < max_wrong_guesses:

        # Display current progress
        display_word = ""

        for letter in word:

            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(hangman_stages[wrong_guesses])

        print("Word:", display_word)

        print(
            "Guessed letters:",
            " ".join(guessed_letters)
            if guessed_letters
            else "None"
        )

        print(
            "Remaining attempts:",
            max_wrong_guesses - wrong_guesses
        )


        # Check if word is completed
        if all(letter in guessed_letters for letter in word):

            print("\nCongratulations!")
            print("You guessed the word:", word)
            return


        # Ask user for a guess
        guess = input(
            "\nEnter a letter: "
        ).lower().strip()


        # Input validation
        if len(guess) != 1 or not guess.isalpha():

            print(
                "Please enter only one alphabet letter."
            )
            continue


        # Check repeated guess
        if guess in guessed_letters:

            print(
                "You already guessed that letter."
            )
            continue


        guessed_letters.append(guess)


        # Check correct or incorrect guess
        if guess in word:

            print("Correct guess!")

        else:

            print("Wrong guess!")
            wrong_guesses += 1


    # Game lost
    print(hangman_stages[max_wrong_guesses])

    print("\nGame Over!")

    print(
        "The correct word was:",
        word
    )


# Main program
while True:

    play_hangman()

    again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower().strip()

    if again not in ["yes", "y"]:

        print("\nThanks for playing Hangman!")
        break