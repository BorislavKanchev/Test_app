import sqlite3

conn = sqlite3.connect('users.db')  # Създаване на или свързване със SQLite база данни
cursor = conn.cursor()

# Създаване на таблицата
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    )
''')

conn.commit()  # Запазване на промените
conn.close()   # Затваряне на връзката с базата данни