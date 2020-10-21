# EDH-diff-checker-Python
![Python application](https://github.com/howardki625/EDH-diff-checker-Python/workflows/Python%20application/badge.svg)

same as the other, but in Python

currently only supports DeckStats because it has an API for getting deck data

```bash
python deckdiff.py https://deckstats.net/decks/62058/1299769-double-titan https://deckstats.net/decks/62058/808205-raza-frog
```

To run tests, do the following

```bash
pip install pytest

pytest
```

test coverage

```bash
pip install pytest-cov

pytest --cov=test/ --cov-report=html
```