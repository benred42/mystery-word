from mystery_word import *
import os

def main():
    welcome()
    words = import_words("/usr/share/dict/words")
    word_list = ask_difficulty(words)




###############################################################################

def import_words(filepath):
    with open(filepath) as file:
        text = file.readlines()

    return clean_text(text)

###############################################################################

def clean_text(text):
    return [line.strip().lower() for line in text]

###############################################################################

def ask_difficulty(words):
    user_input = input("Which difficulty would you like? \
    [E]asy [M]edium [H]ard [Q]uit? ")
    user_input = user_input.lower()
    word_list = []

    if user_input not in "emh":
        ask_difficulty()
    os.system('clear')

    elif user_input == "e":
        word_list = easy_words(words)
    elif user_input == "m":
        word_list = medium_words(words)
    else:
        word_list = hard_words(words)

    return word_list


###############################################################################

def number_of_letters(word):
    print("Your word has {} letters".format(str(len(word))))

def welcome_rules():
    print("Welcome to the Mystery Word Game!/nTry to guess the mystery word \
    one letter at a time.")

def guess_limit():

def win_lose():




if __name__ == '__main__':
    main()
