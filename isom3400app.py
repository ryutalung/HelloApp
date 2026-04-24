import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Database setup - KEEP THIS OPEN, DON'T CLOSE IT
@st.cache_resource
def get_connection():
    """Create and return database connection - KEEP OPEN"""
    conn = sqlite3.connect('submissions.db', check_same_thread=False)
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
    return conn  # Don't close this!

# Get the connection once at start
conn = get_connection()  # This stays open

# App UI
st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and enter the region.")

target = st.number_input("Enter monthly sales target (USD):", min_value=0, value=0)

if target > 100000:
    st.write("🎯 Great! You have entered an ambitious target!")

region = st.selectbox("Select region:", ["East", "South", "West", "North"])

# Submit button
if st.button("Submit"):
    try:
        # Use the existing open connection
        c = conn.cursor()
        c.execute(
            "INSERT INTO submissions (timestamp, target, region) VALUES (?, ?, ?)",
            (datetime.now().isoformat(), target, region)
        )
        conn.commit()
        st.write(f"✅ You submitted! Target: ${target:,}, Region: {region}.")
        st.success("Complete! Data saved to database.")
    except Exception as e:
        st.error(f"Error saving data: {e}")

# View submissions
if st.checkbox("Show past submissions"):
    try:
        # Use the existing open connection
        df = pd.read_sql_query("SELECT * FROM submissions ORDER BY id DESC", conn)
        
        if len(df) > 0:
            st.dataframe(df)
            st.metric("Total Submissions", len(df))
            st.metric("Average Target", f"${df['target'].mean():,.0f}")
        else:
            st.info("No submissions yet. Submit some data first!")
    except Exception as e:
        st.error(f"Error loading data: {e}")
