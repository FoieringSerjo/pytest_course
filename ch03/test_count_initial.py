from pathlib import Path
from tempfile import TemporaryDirectory
import cards


def test_empty():
    with TemporaryDirectory() as db_dir:
        # Arrange
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)

        #  Act
        count = db.count()
        # Teardown
        db.close()

        # Assert
        assert count == 0
