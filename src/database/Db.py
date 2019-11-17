import psycopg2
import psycopg2.extras
import os

class Db:
    connection: None
    cursor: None

    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS')
        )
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor
            )

    def __del__(self):
        self.connection.close()
        self.cursor.close()
