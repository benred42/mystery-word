from demon_words import *

word_list = ["foot", "feet", "hand", "head", "need", "kept", "knot", "than"]
word_list2 = ["foot", "than", "feet", "then"]

def test_choose_best_list():
    assert choose_best_list(word_list, "o")[1] == ["feet", "hand", "head", "need", "kept", "than"]
    assert choose_best_list(word_list, "t")[1] == ["foot", "feet", "kept", "knot"]
    assert choose_best_list(word_list, "e")[1] == ["foot", "hand", "knot", "than"]
    assert choose_best_list(word_list2, "t")[1] == ["than", "then"]

def test_merge_words():
    assert merge_words("t...", "..e.") == "T _ E _"
    assert merge_words("t...", "..e.", "." , "." , "" ,False) == "t.e."
    assert merge_words("t...", "t...") == "T _ _ _"
    print("test", "halp")
    assert merge_words("test", "halp") == "H A L P"
