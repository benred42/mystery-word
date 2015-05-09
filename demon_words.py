import random
import os

import interface
import mystery_word

def choose_best_list(word_list, current, guess):
    families = {}
    words = word_list[:]
    word_groups = choice_types(word_list, guess)
    count = 0

    print("Thinking")
    for word in words:
        if count%1000 == 0:
            print(".")
        location = words.index(word)
        choice = word_groups[location]

        families[choice] = families.get(choice, [])
        families[choice] = families[choice]+ [words[location]]
        count += 1

    length = 0
    largest_group = []
    largest_group_name = ""
    if len(families) == 2:
        largest_group_name, largest_group = tie_breaker(families)
        return largest_group_name, largest_group
    else:
        for member in families:
            if len(families[member]) > length:
                length = len(families[member])
                largest_group = families[member]
                largest_group_name = member

    largest_group_name = merge_words(current, largest_group_name, filler = ".", joiner = "", capital = False)

    return largest_group_name, largest_group

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

def tie_breaker(dictionary):
    number_blanks = 0
    choice = ""

    for key in dictionary:
        count = 0
        for letter in key:
            if letter == ".":
                count += 1
        if count > number_blanks:
            number_blanks = count
            choice = key
    return choice, dictionary[choice]


###############################################################################

def choose_length(a_list):
    random_length = random.choice(range(8,25))

    demon_list = [word for word in a_list if len(word) == random_length]
    return demon_list, random_length

###############################################################################

def merge_words(word, guess, to_replace = ".", filler = "_", joiner = " ", capital = True):

    display_list = [filler for letter in word]
    for index in range(len(display_list)):
        if word[index] != to_replace:
            display_list[index] = word[index]

        elif guess[index] != to_replace:
            display_list[index] = guess[index]
    if capital:
        return joiner.join(display_list).upper()
    else:
        return joiner.join(display_list)

###############################################################################


def demon_guess(word_list, length):

    words = word_list
    incorrect_guesses = []
    correct_guesses = []
    current_state = ("." * length)

    while interface.win_lose(current_state, correct_guesses, incorrect_guesses, words):
        guess = interface.guess_input((correct_guesses + incorrect_guesses))
               #^handles user input

        if guess != 'quit':
            new_states = choose_best_list(words, current_state, guess)
            if  new_states[0] != current_state:
                correct_guesses.append(guess)
                current_state = merge_words(current_state, new_states[0], to_replace = ".", filler = ".", joiner = "", capital = False)
            else:
                incorrect_guesses.append(guess)
        else:
            os.system('clear')
            print("Goodbye!  Thanks for Playing!")
            break

        words = new_states[1]

        os.system('clear')
        print("   (_(\n  ('')\n_  \"\ )>,_     .-->\n_>--w/((_ >,_.'\n       ///\n       \"`\"")
        interface.guess_display(current_state, correct_guesses, incorrect_guesses)

###############################################################################

def main():
    words, length = choose_length(interface.import_words('/usr/share/dict/words'))
    interface.word_length(words[0])

    demon_guess(words, length)

    if interface.play_again():
        return interface.main()
    else:
        os.system('clear')
        return
