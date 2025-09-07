import os
import sqlite3
import streamlit as st

# --- Placeholder functions for your chatbot logic ---
def process_query(user_input):
    # Example: rule-based simple responses
    if "savings" in user_input.lower():
        return "You should track your savings every month."
    elif "expenses" in user_input.lower():
        return "Try to reduce unnecessary expenses."
    else:
        return "I can help you plan your finances."

def ml_generate_response(user_input):
    # Example ML response (replace with actual ML model later)
    return "Future ML-based recommendation for your input."

# --- Database Setup ---
DB_PATH = "database.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_chat(user_input, bot_response):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO chat_history (user_input, bot_response) VALUES (?, ?)",
        (user_input, bot_response)
    )
    conn.commit()
    conn.close()

def fetch_history():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT user_input, bot_response FROM chat_history ORDER BY id DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    return rows

# --- Initialize DB on first run ---
if "db_inited" not in st.session_state:
    init_db()
    st.session_state["db_inited"] = True

# --- Streamlit UI ---
st.title("💰 Agentic Financial Planning Chatbot")
st.write("Ask me about your savings, expenses, or financial goals.")

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input.strip():
        response = process_query(user_input)
        ml_resp = ml_generate_response(user_input)
        final_response = f"{response}\n\n[ML Future Response: {ml_resp}]"
        st.write("🤖 Bot:", final_response)
        log_chat(user_input, final_response)
    else:
        st.warning("Please type something first.")

st.subheader("Chat History (latest 50)")
for user, bot in fetch_history():
    st.write(f"🧑 {user}")
    st.write(f"🤖 {bot}")
