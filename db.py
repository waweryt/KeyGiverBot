import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    is_allowed INTEGER DEFAULT 0
)
''')

conn.commit()


def add_user(telegram_id: int):
    try:
        cursor.execute("INSERT INTO users (telegram_id) VALUES (?)", (telegram_id,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # exist


def get_user(telegram_id: int):
    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
    return cursor.fetchone()


def allow_user(telegram_id: int):
    cursor.execute("UPDATE users SET is_allowed = 1 WHERE telegram_id = ?", (telegram_id,))
    conn.commit()


def is_allowed_user(telegram_id: int) -> bool:
    cursor.execute("SELECT is_allowed FROM users WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()
    return row is not None and row[0] == 1
