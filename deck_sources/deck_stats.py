import re
import requests

def extract_ids(url):
    temp = re.findall(r'\d+', url)
    res = list(map(str, temp))
    return res[0], res[1]


def get_from_deck_stats(url):
    ownerid, deckid = extract_ids(url)
    api = 'https://deckstats.net/api.php?action=get_deck&id_type=saved&owner_id='+ownerid+'&id='+deckid+'&response_type=list'
    res = requests.get(api)
    decklist = res.json()['list']
    return decklist.split('\n')

