import sqlite3
from pathlib import Path


class DbConnect:
    """
        Creates a context to work with database
    """

    def __init__(self):
        self.database = Path.resolve(Path.cwd() / 'database/database.db')

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

        if exc_val or exc_type or exc_tb:
            raise
