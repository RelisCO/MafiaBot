import sqlite3
from config import database_name


sql_database_create = """CREATE TABLE Players(
id TEXT PRIMARY KEY,
chat TEXT NOT NULL,
role TEXT,
CONSTRAINT check_role CHECK (role in ('Mafia', 'Don', 'Civilian', 'Sheriff')));"""


if __name__ == '__main__':
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(sql_database_create)
    conn.commit()
    conn.close()
