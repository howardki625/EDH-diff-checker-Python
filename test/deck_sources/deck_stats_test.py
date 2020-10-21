import requests
from deck_sources.deck_stats import extract_ids, get_from_deck_stats


def test_extract_id_from_url():
    url = 'https://deckstats.net/decks/62058/1299769-double-titan'
    ownerid, deckid = extract_ids(url)
    assert ownerid == '62058'
    assert deckid == '1299769'


def test_get_from_deck_stats(requests_mock):
    url = 'https://deckstats.net/decks/62058/1299769-double-titan'
    api = 'https://deckstats.net/api.php?action=get_deck&id_type=saved&owner_id=62058&id=1299769&response_type=list'
    requests_mock.get(f'{api}', json = {'list': '1 something'})
    res = get_from_deck_stats(url)
    assert res == ['1 something']
    