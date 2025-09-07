import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Chat history
c.execute('''
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT,
    bot_response TEXT
)
''')

# User profile (optional)
c.execute('''
CREATE TABLE IF NOT EXISTS user_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    income REAL,
    expenses REAL,
    goal_amount REAL,
    goal_months INTEGER
)
''')

conn.commit()
conn.close()
print("SQLite database ready ✅")
