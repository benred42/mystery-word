import random


def easy_words(a_list):
    """Takes a list of strings and creates a new list from it by selecting only
    the list items with a length in a given range.

    Keyword Arguments:
    a_list -- list of strings to be filtered
    """

    easy_list = [word for word in a_list if len(word) in range(4,7)]
    return easy_list

###############################################################################

def medium_words(a_list):
    """Takes a list of strings and creates a new list from it by selecting only
    the list items with a length in a given range.

    Keyword Arguments:
    a_list -- list of strings to be filtered
    """

    medium_list = [word for word in a_list if len(word) in range(6,9)]
    return medium_list

###############################################################################

def hard_words(a_list):
    """Takes a list of strings and creates a new list from it by selecting only
    the list items above a given length.

    Keyword Arguments:
    a_list -- list of strings to be filtered
    """

    return [word for word in a_list if len(word) > 7]

###############################################################################

def random_word(a_list):
    """Takes a list and returns a random element from that list.

    Keyword Arguments:
    a_list -- list to select from
    """

    return random.choice(a_list)

###############################################################################

def display_word(word, guesses_list):
    """Takes a string and a list.  Prints a string of underscores equal to the
    length of the string.  Replaces underscores with corresponding characters
    from the string based on whether or not those characters are in the list.

    Keyword Arguments:
    word -- the string whose length and characters are used in the print output
    guesses_list -- the list whose elements determine which characters from
    "word" are displayed
    """
    
    display_list = [letter.upper() for letter in word]
    for index in range(len(display_list)):
        if word[index] not in guesses_list:
            display_list[index] = "_"
    return " ".join(display_list)

###############################################################################

def is_word_complete(word, guesses_list):
    """Takes a string and a list.  Creates a new list containing only the
    items form the list that are not in the string and then returns if this new
    list is empty (Boolean value).

    Keyword Arguments:
    word -- string to compare list against
    guesses_list -- list whose elements are compared to "word" to create new
    list
    """

    check_list = [letter for letter in word if letter not in guesses_list]
    return check_list == []
