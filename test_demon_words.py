from demon_words import *

word_list = ["foot", "feet", "hand", "head", "need", "kept", "knot", "than"]

def test_demon_check_guess():
    assert demon_check_guess(word_list, "o") == ["feet", "hand", "head", "need", "kept", "than"]
    assert demon_check_guess(word_list, "t") == ["foot", "feet", "kept", "knot"]
    assert demon_check_guess(word_list, "e") == ["foot", "hand", "knot", "than"]
