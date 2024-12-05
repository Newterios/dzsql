import sqlite3
from config import DB_path

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
    posts_id INTEGER  PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
"""

conection = sqlite3.connect(DB_path)
cursor = conection.cursor()

cursor.execute(create_posts_table)

conection.commit()
conection.close()

print("готово!")
