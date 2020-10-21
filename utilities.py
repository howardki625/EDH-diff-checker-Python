def get_deck_differences(deck1, deck2):
    # for each deck, get the cards that are not in the other
    diff1 = [i for i in deck1 if i not in deck2]
    diff2 = [i for i in deck2 if i not in deck1]
    return diff1, diff2

def extend_lists_for_printing(diff1, diff2):
    # match the list lengths for print formatting
    delta = len(diff1) - len(diff2)
    if delta > 0:
        diff2.extend(['.'] * delta)
    else:
        diff1.extend(['.'] * abs(delta))