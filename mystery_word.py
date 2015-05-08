import random


def easy_words(a_list):
    easy_list = [word for word in a_list if len(word) in range(4,7)]
    return easy_list


def medium_words(a_list):
    medium_list = [word for word in a_list if len(word) in range(6,9)]
    return medium_list


def hard_words(a_list):
    return [word for word in a_list if len(word) > 7]


def random_word(a_list):
    return random.choice(a_list)


def display_word(word, guesses_list):
    display_list = [letter.upper() for letter in word]
    for index in range(len(display_list)):
        if word[index] not in guesses_list:
            display_list[index] = "_"
    return " ".join(display_list)


def is_word_complete(word, guesses_list):
    check_list = [letter for letter in word if letter not in guesses_list]
    return check_list == []
