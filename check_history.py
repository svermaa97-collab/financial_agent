import sqlite3

# Connect to your database
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Fetch all chat history
c.execute("SELECT * FROM chat_history")
rows = c.fetchall()

# Print results
for row in rows:
    print(row)

conn.close()
