import mystery_word
import os


###############################################################################

def clean_text(text):
    """Takes a string line by line, strips leading and trailing whitespace
    characters, and lowercases.  Returns a list of the lines.

    Keyword Arguments:
    text -- the string to be processed
    """
    return [line.strip().lower() for line in text]

###############################################################################

def import_words(filepath):
    """Opens a file and places each line from that file in a list, then
    calls clean_text(text) to remove whitespace and lowercase.  Returns a list.

    Keyword Arguments:
    filepath -- the path to the file you wish to read
    """

    with open(filepath) as file:
        text = file.readlines()

        return clean_text(text)
        #clean_text only really works for files with one word per line.

###############################################################################

def choose_difficulty():
    """From a default imported library of words, filters by word length based
    on user input and returns a list of the filtered words.
    """

    words = import_words('/usr/share/dict/words')
    difficulty = input("What difficulty would you like? [E]asy, [M]edium, or [H]ard? ").lower()

    if difficulty == 'e':
        return mystery_word.easy_words(words)
    elif difficulty == 'm':
        return mystery_word.medium_words(words)
    elif difficulty == 'h':
        return mystery_word.hard_words(words)
    else:
        print("That is not a valid choice. Please choose again.")
        return choose_difficulty()

###############################################################################

def guess(word_choice):
    """Takes a string and intitializes two empty lists. Asks the user
    to guess a letter in the string. If the guess is 'quit' the function breaks.
    If the guess is in the string it adds that letter to a list of correct
    guesses and if it is not in the string it adds the letter to another list.
    The function will continue to loop and ask for user input until either the
    list of correct guesses contains all the letters in the string or the list
    of incorrect guesses reaches a length of 8, in which case the function will
    return a win or loss message (dependent on outcome).

    Keyword Arguments:
    word_choice -- the string the user will try to guess
    """

    word = word_choice
    incorrect_guesses = []
    correct_guesses = []

    while win_lose(word, correct_guesses, incorrect_guesses):
        guess = guess_input((correct_guesses + incorrect_guesses))
               #^handles user input

        if guess != 'quit':
            if check_guess(word, guess):
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
        else:
            os.system('clear')
            print("Goodbye!  Thanks for Playing!")
            break

        os.system('clear')
        guess_display(word, correct_guesses, incorrect_guesses)

###############################################################################

def guess_input(guess_list):
    """Takes a list.  Checks to see if input from user is:
        >equal to the string 'quit'
        >comprised of alphabet characters and is no longer
        than a single character (if not 'quit')
        >Not already in the given list.
    If input passes the given conditions, return the input.  Otherwise, print
    a message and rerun the function.

    Keyword Arguments:
    guess_list --  the list of guesses to check input against.
    """

    guess = input("(Type \"quit\" to exit) Please guess a letter >>> ").lower()

    if guess == 'quit' or (guess.isalpha() and len(guess) < 2):
        if guess not in guess_list:
            return guess
        else:
            print("You already guessed that letter!")
            return guess_input(guess_list)
    else:
        print("Invalid guess.  Please try again.")
        return guess_input(guess_list)

###############################################################################

def check_guess(word, guess):
    """Takes two strings.  Checks if 2nd string is in the 1st string and returns
    True if it is, False if it is not.

    Keyword Arguments:
    word -- string to be checked against
    guess -- string must be in the 'word' argument for function to return True
    """

    if guess in word:
        return True
    else:
        return False

###############################################################################

def guess_display(word, correct_guesses, incorrect_guesses):
    """Takes a string and two lists. Prints a user-friendly output based on
    the length of the lists and how the contents of the first list matches the
    characters in the string.

    Keyword Arguments:
    word --  string that correct_guesses is checked against
    correct_guesses -- list that is checked against "word"
    incorrect_guesses -- list whose length and contents is used in first line
    of output
    """

    number_incorrect = str(len(incorrect_guesses))
    incorrect = " ".join(incorrect_guesses)
    print("Incorrect guesses({}/8): [{}]\n".format(number_incorrect, incorrect.upper()))

    print(mystery_word.display_word(word, correct_guesses) + "\n")

###############################################################################

def win_lose(word, correct_guesses, incorrect_guesses):
    """Checks if the user has won or lost the game.  If the
    list of correct guesses contains all the letters in the string or the list
    of incorrect guesses reaches a length of 8 the function will
    return a win or loss message (dependent on outcome) which will in turn
    return False. If neither of condition is met, the function returns True.

    Keyword Arguments:
    word -- the string correct_guesses is compared to.
    correct_guesses -- list of characters compared to 'word' to determine if
    user has won.
    incorrect_guesses -- list of characters.  If length of list exceeds 7, user
    has lost.
    """

    if mystery_word.is_word_complete(word, correct_guesses):
        return you_win(word)
    elif len(incorrect_guesses) > 7:
        return you_lose(word)
    else:
        return True

###############################################################################

def you_win(word):
    """Clears the screen and informs the user they have won, shows them the
    full word they guessed, and returns False.

    Keyword Arguments:
    word -- the string the user was trying to guess
    """

    os.system('clear')
    print("Congratulations!  You Won!!")
    print("You correctly guessed the Word!")
    print("It was {}".format(word.upper()))
    return False

###############################################################################

def you_lose(word):
    """Clears the screen and informs the user they have lost, shows them the
    full word they failed to guess, and returns False.

    Keyword Arguments:
    word -- the string the user was trying to guess
    """

    os.system('clear')
    print("I'm sorry, but you've run out of guesses!")
    print("The word was {}".format(word.upper()))
    return False

###############################################################################

def welcome_rules():
    """Clears the screen and prints a welcome message"""

    os.system('clear')
    print("Welcome to the Mystery Word Game!")
    print("Guess the word one letter at a time.")

###############################################################################

def word_length(word):
    """Takes a string.  Determines the length of string and prints a statement
    informing user of the length.

    Keyword Arguments:
    word -- string whose length is determined
    """

    length = str(len(word))
    print("Your word is {} letters long.".format(length))

###############################################################################

def play_again():
    """Asks the user for input and, if input is valid, returns True or False
    depending on the input.  If input invalid, reruns function.
    """

    yes_no = input("Would you like to play again (y/n)? ").lower()

    if yes_no not in "yn" or len(yes_no) > 1:
        return play_again()
    elif yes_no == "y":
        return True
    else:
        return False

###############################################################################

def main():
    """Initializes game and controls game flow."""

    welcome_rules()
    words = choose_difficulty()
    word = mystery_word.random_word(words)
    word_length(word)

    guess(word)

    if play_again():
        return main()
    else:
        os.system('clear')
        return

###############################################################################

if __name__ == '__main__':
    main()
