from demon_words import *

word_list = ["foot", "feet", "hand", "head", "need", "kept", "knot", "than"]
word_list2 = ["foot", "than", "feet", "then"]

def test_choose_best_list():
    assert choose_best_list(word_list, "o") == ["feet", "hand", "head", "need", "kept", "than"]
    assert choose_best_list(word_list, "t") == ["foot", "feet", "kept", "knot"]
    assert choose_best_list(word_list, "e") == ["foot", "hand", "knot", "than"]
    assert choose_best_list(word_list2, "t") == ["than", "then"]

def test_demon_display_word():
    assert demon_display_word("t...", "..e.") == "T _ E _"
