from helpers import DbConnect


def get_chars_from_db() -> dict[str, str]:
    """
        Allows getting necessary chars from database in common string representation
    """

    with DbConnect() as db:
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM chars''')

        column_headers = [(lambda desc: desc[0])(desc) for desc in cursor.description]
        data_rows = cursor.fetchone()

        # Database contains only lowercase letters, and it needs to add uppercase before making dict
        data = list(zip(column_headers, data_rows))
        data.insert(1, ('RuUpper', data[0][1].upper()))
        data.insert(3, ('EnUpper', data[2][1].upper()))

        return {x: y for x, y in data}
