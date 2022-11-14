from app.components.basic.db_provider import get_chars_from_db


def test_should_get_data_from_db():
    data = get_chars_from_db()
    assert data
