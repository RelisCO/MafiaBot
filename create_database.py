import sqlite3
from config import database_name


sql_database_create = f"""CREATE TABLE Players(
id TEXT,
chat TEXT,
CONSTRAINT pk PRIMARY KEY (id));"""


if __name__ == '__main__':
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(sql_database_create)
    conn.commit()
    conn.close()
