from utilities import get_deck_differences

def test_deck_commonalities():
    deck1 = [1, 3, 5, 7]
    deck2 = [1, 3, 5, 8]
    diff1, diff2 = get_deck_differences(deck1, deck2)
    assert diff1 == [7]
    assert diff2 == [8]