import random
import os
import re
import interface


###############################################################################


def choose_best_list(word_list, current, guess):
    """Takes a list and two strings. Creates a dictionary where the keys are
    maps of where the guessed letter could appear in a word and the values are
    lists of the subset of words from the input list where the letter appears
    in those locations (example: {"...e":["fate", "lone"], ".ee.":["need"]}).
    It will return the value list of the greatest length, choosing randomly in
    case of ties and choosing the option that does not contain the guess if
    the dictionary only has two keys. It will also return the corresponding key
    after it has merged the key with the current state of the game (e.g if the
    game was currently restricted to words that met the condition ".n.rt" and
    the choose_best_list function determined the best subset to be those meeting
    the condition "i...." the function would return "in.rt").

    Keyword Arguments:
    word_list -- the current list of possible words

    current -- the current state of the game (".n.rt" in the example above)

    guess -- the user-input guess (a single letter string)
    """

    families = choice_types(word_list, guess)

    length = 0
    largest_group = []
    largest_group_name = ""
    if len(families) == 2:
        largest_group_name, largest_group = tie_breaker(families)
    else:
        for member in families:
            if len(families[member]) > length:
                length = len(families[member])
                largest_group = families[member]
                largest_group_name = member

    largest_group_name = merge_words(current, largest_group_name,
                                     filler=".", joiner="", capital=False)

    return largest_group_name, largest_group


###############################################################################


def choice_types(word_list, guess):
    """Take a list and a string(intended to be a single letter). Copies the list
    and iterates through it. For each word, it checks each letter and if that
    letter does not match the input "guess" string that letter is replaced with
    the string ".". Each word thus treated is appended to a new list, which the
    function returns when complete.

    Keyword Arguments:
    word_list -- the current list of possible words

    guess -- the user-input guess (a single letter string)
    """

    families = {}
    words = word_list[:]
    search = r'[^' + guess + ']'

    for word in words:
        blanked_word = re.sub(search, ".", word)

        families[blanked_word] = families.get(blanked_word, [])
        families[blanked_word].append(word)

    return families



###############################################################################


def tie_breaker(dictionary):
    """Takes a dictionary. For each key, checks the number of characters in that
    key that are the string ".". Returns the key with the highest number along
    with its corresponding value.

    Keyword Arguments:
    dictionary -- the dictionary that the function iterates through.
    """

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
    """Takes a list of strings.  Picks a number at random between 6 and 25 and
    returns as a list the subset of strings from the input list that are that
    length.

    Keyword Arguments:
    a_list -- the list of strings to be filtered.
    """

    random_length = random.choice(range(6,25))

    demon_list = [word for word in a_list if len(word) == random_length]
    return demon_list, random_length


###############################################################################


def merge_words(word, guess, to_replace=".", filler="_", joiner=" ", capital=True):
    """Takes a maximum of 5 strings and 1 boolean (minimum 2 strings).  The
    first 2 strings ("word" and "guess") must be the same length.  Essentially,
    the function creates a new string list using the "filler" connected by the
    "joiner". Each "filler" will be replaced by the character with the
    corresponding index from both "word" and "guess" if the character at that
    index in either of those strings is not equal to "to_replace".  The "capital"
    argument controls uppercasing of the resulting string.

    Examples:
    merge_words("t...", "..e.", "." , "." , "" ,False) == "t.e."
    merge_words("t...", "..e.") == "T _ E _"
    assert merge_words("t...", "....") == "T _ _ _"

    Keyword Arguments:
    word -- The first string to be used in the merge

    guess -- The second string to be used in the merge

    to_replace -- The character in "word" and "guess" to be found and replaced
    by the "filler" argument. Default "."

    filler -- The character to replace "to_replace" the resulting merged string.
    Default "_"

    joiner -- The character(s) to be used to join the resulting string

    capital -- Boolean controlling if the merged string will be uppercased or not
    (True for upper, False for not). Default True
    """

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
    """Takes a list and an int. Intitializes two empty lists, a variable equal
    to the list, and a variable equal to a string == ("." * input int). Asks
    the user to guess a letter in the string. If the guess is 'quit' the function
    breaks. If the guess returns a new state of game different than the current
    state of game, it adds that letter to a list of correct guesses and if
    not it adds the letter to a list of incorrect guesses. The function will
    continue to loop and ask for user input until either the list of
    correct guesses contains all the letters in the current state of game
    (including blanked out letters) or the list of incorrect guesses reaches a
    length of 8, in which case the function will return a win or loss
    message (dependent on outcome).

    Keyword Arguments:
    word_list -- the list of possibile words the function will use to try and
    dodge the user's guess

    length -- the length that all possible words are equal to (used to initialize
    current state of game)
    """

    words = word_list
    incorrect_guesses = []
    correct_guesses = []
    current_state = ("." * length)

    while interface.win_lose(current_state, correct_guesses, incorrect_guesses, words):

        guess = interface.guess_input((correct_guesses + incorrect_guesses))
        # ^handles user input

        if guess != 'quit':
            new_states = choose_best_list(words, current_state, guess)
            if new_states[0] != current_state:
                correct_guesses.append(guess)
                current_state = new_states[0]
            else:
                incorrect_guesses.append(guess)
        else:
            os.system('clear')
            print("Goodbye!  Thanks for Playing!")
            break

        words = new_states[1]

        os.system('clear')
        print(
            "   (_(\n  ('')\n_  \"\ )>,_     .-->\n_>--w/((_ >,_.'\n       ///\n       \"`\"")
        interface.guess_display(
            current_state, correct_guesses, incorrect_guesses)



###############################################################################


def main():
    """Initializes "demon" mode and controls game flow."""

    words, length = choose_length(
        interface.import_words('/usr/share/dict/words'))

    interface.word_length(words[0])

    demon_guess(words, length)

    if interface.play_again():
        return interface.main()
    else:
        os.system('clear')
        return


###############################################################################


if __name__ == '__main__':
    main()
