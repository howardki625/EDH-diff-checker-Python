import sys
import re
import requests
import numpy as np

def ExtractIds(url):
    temp = re.findall(r'\d+', url)
    res = list(map(int, temp))
    return str(res[0]), str(res[1])

def GetFromDeckStats(url):
    ownerid, deckid = ExtractIds(url)
    api = 'https://deckstats.net/api.php?action=get_deck&id_type=saved&owner_id='+ownerid+'&id='+deckid+'&response_type=list'
    res = requests.get(api)
    decklist = res.json()['list']
    return decklist.split('\n')

# grabs url from console
url1 = sys.argv[1]
url2 = sys.argv[2]

# retrieve decklists
deck1 = GetFromDeckStats(url1)
deck2 = GetFromDeckStats(url2)

# for each deck, get the cards that are not in the other
diff1 = []
diff2 = []
for card in deck1:
    if card not in deck2:
        diff1.append(card)
for card in deck2:
    if card not in deck1:
        diff2.append(card)

# match the array lengths
delta = len(diff1) - len(diff2)
if delta != 0:
    if delta > 0:
        diff2.extend(['.'] * delta)
    else:
        diff1.extend(['.'] * abs(delta))

# print result to console
table = []
for x, y in zip(diff1, diff2):
    table.append([x, y])
table = np.array(table)

frmt = ("{:<35}"+"{:<35}")
for row in table:
    print(frmt.format(*row))


#https://deckstats.net/decks/62058/1299769-double-titan
#https://deckstats.net/decks/62058/808205-raza-frog
