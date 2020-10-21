from deck_sources.deck_stats import extract_ids


def test_extract_id_from_url():
    url = 'https://deckstats.net/decks/62058/1299769-double-titan'
    ownerid, deckid = extract_ids(url)
    assert ownerid == '62058'
    assert deckid == '1299769'
    