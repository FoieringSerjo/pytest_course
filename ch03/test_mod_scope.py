from pathlib import Path
from tempfile import TemporaryDirectory
import cards

import pytest


@pytest.fixture(scope="module")
def cards_db():
    print("\ncards_db() setup")
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        print("\ncards_db() teardown")
        db.close()


def test_empty(cards_db):
    print("test_empty()")
    assert cards_db.count() == 0


def test_two(cards_db):
    print("test_two()")
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2