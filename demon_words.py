import random
import os

import interface
import mystery_word

def choose_best_list(word_list, guess):
    families = {}
    words = word_list[:]
    word_groups = choice_types(word_list, guess)

    for word in words:
        location = words.index(word)
        choice = word_groups[location]

        families[choice] = families.get(choice, [])
        families[choice] = families[choice]+ [words[location]]

    length = 0
    largest_group = []
    largest_group_name = ""
    for member in families:
        if len(families[member]) > length:
            length = len(families[member])
            largest_group = families[member]
            largest_group_name = member


    return largest_group

###############################################################################

def choice_types(word_list, guess):
    words = word_list[:]
    word_groups = []

    for word in words:
        blanked_word = []
        for letter in word:
            if letter != guess:
                blanked_word.append(".")
            else:
                blanked_word.append(letter)
        word_groups.append("".join(blanked_word))

    return word_groups

###############################################################################

def choose_length(a_list):
    random_length = random.choice(range(8,25))

    demon_list = [word for word in a_list if len(word) == random_length]
    return demon_list

###############################################################################

def demon_display_word(word, guess):

    display_list = ["_" for letter in word]
    for index in range(len(display_list)):
        if word[index] != ".":
            display_list[index] = word[index].upper()

        elif guess[index] != ".":
            display_list[index] = guess[index].upper()

    return " ".join(display_list)
###############################################################################

def demon_guess(word_list):

    words = word_list
    incorrect_guesses = []
    correct_guesses = []

    while win_lose(word, correct_guesses, incorrect_guesses):
        guess = guess_input((correct_guesses + incorrect_guesses))
               #^handles user input

        if guess != 'quit':
            if demon_check_guess(word, guess):
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
        else:
            os.system('clear')
            print("Goodbye!  Thanks for Playing!")
            break

        os.system('clear')
        guess_display(word, correct_guesses, incorrect_guesses)
