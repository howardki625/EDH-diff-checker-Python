import sys
from deck_sources.deck_stats import get_from_deck_stats
from utilities import get_deck_differences, extend_lists_for_printing

# grabs url from console
url1 = sys.argv[1]
url2 = sys.argv[2]

# retrieve decklists
deck1 = get_from_deck_stats(url1)
deck2 = get_from_deck_stats(url2)

diff1, diff2 = get_deck_differences(deck1, deck2)
extend_lists_for_printing(diff1, diff2)

# print result to console
frmt = ("{:<35}"+"{:<35}")
for x, y in zip(diff1, diff2):
    print(frmt.format(x, y))
