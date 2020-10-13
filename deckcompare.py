import sys
import re
import requests

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

def GetDiff(deck1, deck2):
    diff = []
    for card in deck1 + deck2:
        if card not in deck1 or card not in deck2:
            diff.append(card)
    return diff

def CompareLists(url1, url2):
    deck1 = GetFromDeckStats(url1)
    deck2 = GetFromDeckStats(url2)
    return GetDiff(deck1, deck2)


res = CompareLists(sys.argv[1], sys.argv[2])
#print(deck1, '\n', deck2)
print(res)
#https://deckstats.net/decks/62058/1299769-double-titan
