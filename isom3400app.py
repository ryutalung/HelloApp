import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Initialize database
@st.cache_resource
def init_db():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            target REAL,
            region TEXT
        )
    ''')
    conn.commit()
    return conn

# Your existing UI
st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and enter the region.")

target = st.number_input("Enter monthly sales target (USD):", min_value=0, value=0)

if target > 100000:
    st.write("Great! You have entered an ambitious target!")

region = st.selectbox("Select region:", ["East", "South", "West", "North"])

if st.button("Submit"):
    # Save to database
    conn = init_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO submissions (timestamp, target, region) VALUES (?, ?, ?)",
        (datetime.now().isoformat(), target, region)
    )
    conn.commit()
    conn.close()
    
    st.write(f"You submitted! target: {target}, region: {region}.")
    st.success("Complete! Data saved to database.")

# Optional: Display past submissions
if st.checkbox("Show past submissions"):
    conn = init_db()
    df = pd.read_sql_query("SELECT * FROM submissions", conn)
    conn.close()
    st.dataframe(df)
