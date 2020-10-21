from utilities import get_deck_differences, extend_lists_for_printing


def test_deck_commonalities():
    deck1 = [1, 3, 5, 7]
    deck2 = [1, 3, 5, 8]
    diff1, diff2 = get_deck_differences(deck1, deck2)
    assert diff1 == [7]
    assert diff2 == [8]


def test_list_extender_both_list_same_length():
    list1 = [1, 3, 5]
    list2 = [1, 3, 5]
    extend_lists_for_printing(list1, list2)
    assert list1 == [1, 3, 5]
    assert list2 == [1, 3, 5]


def test_list_extender_list1_is_longer():
    list1 = [1, 3, 5, 7]
    list2 = [1, 3, 5]
    extend_lists_for_printing(list1, list2)
    assert list1 == [1, 3, 5, 7]
    assert list2 == [1, 3, 5, '.']


def test_list_extender_list2_is_longer():
    list1 = [1, 3, 5]
    list2 = [1, 3, 5, 7]
    extend_lists_for_printing(list1, list2)
    assert list1 == [1, 3, 5, '.']
    assert list2 == [1, 3, 5, 7]
