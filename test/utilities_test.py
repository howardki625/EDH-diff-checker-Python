import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from utilities import get_deck_differences

def test_deck_commonalities():
    deck1 = [1, 3, 5, 7]
    deck2 = [1, 3, 5, 8]
    diff1, diff2 = get_deck_differences(deck1, deck2)
    assert diff1 == [7]
    assert diff2 == [8]