import random
import os

import interface
import mystery_word

def demon_check_guess(word_list, guess):
    not_in_list = [word for word in word_list if guess not in word]
    is_in_list = [word for word in word_list if guess in word]
    letter_count = {}

    for word in is_in_list:
        count = word.count(guess)
        letter_count[count] = letter_count.get(count, [])
        letter_count[count] = letter_count[count] + [word]


    if len(not_in_list) > len(letter_count[max(letter_count)]):
        return not_in_list
    else:
        return letter_count[max(letter_count)]

def choice_types(word_list, guess):
    words = word_list[:]
    word_groups = []

    for word in words:
        blanked_word = ["-" for letter in word if letter != guess]
        word_groups.append("".join(blanked_word))
