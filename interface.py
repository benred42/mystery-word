import mystery_word
import os

def clean_text(text):
    return [line.strip().lower() for line in text]


def import_words(filepath):
    with open(filepath) as file:
        text = file.readlines()

        return clean_text(text)


def choose_difficulty():
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


def choose_word(word_list):
    return mystery_word.random_word(word_list)


def guess(word_choice):
    word = word_choice
    incorrect_guesses = []
    correct_guesses = []

    while win_lose(word, correct_guesses, incorrect_guesses):
        guess = guess_input((correct_guesses + incorrect_guesses))

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


def guess_input(guess_list):
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


def check_guess(word, guess):
    if guess in word:
        return True
    else:
        return False


def guess_display(word, correct_guesses, incorrect_guesses):

    number_incorrect = str(len(incorrect_guesses))
    incorrect = " ".join(incorrect_guesses)
    print("Incorrect guesses({}/8): [{}]\n".format(number_incorrect, incorrect.upper()))

    print(mystery_word.display_word(word, correct_guesses) + "\n")


def win_lose(word, correct_guesses, incorrect_guesses):
    if mystery_word.is_word_complete(word, correct_guesses):
        return you_win(word)
    elif len(incorrect_guesses) > 7:
        return you_lose(word)
    else:
        return True


def you_win(word):
    os.system('clear')
    print("Congratulations!  You Won!!")
    print("You correctly guessed the Word!")
    print("It was {}".format(word.upper()))
    return False


def you_lose(word):
    os.system('clear')
    print("I'm sorry, but you've run out of guesses!")
    print("The word was {}".format(word.upper()))
    return False


def welcome_rules():
    os.system('clear')
    print("Welcome to the Mystery Word Game!")
    print("Guess the word one letter at a time.")


def word_length(word):
    length = str(len(word))
    print("Your word is {} letters long.".format(length))


def play_again():
    yes_no = input("Would you like to play again (y/n)? ").lower()

    if yes_no not in "yn" or len(yes_no) > 1:
        return play_again()
    elif yes_no == "y":
        return True
    else:
        return False


def main():
    welcome_rules()
    words = choose_difficulty()
    word = choose_word(words)
    word_length(word)

    guess(word)

    if play_again():
        return main()
    else:
        os.system('clear')
        return


if __name__ == '__main__':
    main()
