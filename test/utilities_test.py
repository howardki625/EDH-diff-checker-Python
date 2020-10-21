from utilities import *

def test_deck_commonalities():
    deck1 = [1, 3, 5, 7]
    deck2 = [1, 3, 5, 8]
    diff1, diff2 = get_deck_differences(deck1, deck2)
    assert diff1 == [7]
    assert diff2 == [8]


def test_list_extender():
    list1 = [1, 3, 5, 7]
    list2 = [1, 3, 5]
    extend_lists_for_printing(list1, list2)
    assert list1 == [1, 3, 5, 7]
    assert list2 == [1, 3, 5, '.']
