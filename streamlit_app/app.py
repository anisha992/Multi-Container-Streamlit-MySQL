import streamlit as st
import mysql.connector
import json

# Connect to MySQL
conn = mysql.connector.connect(
    host="mysql",
    user="testuser",
    password="testpass",
    database="testdb"
)

cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Convert to JSON
json_data = json.dumps(rows, indent=2)

# Display in Streamlit
st.title("Data from MySQL")
st.json(json_data)

cursor.close()
conn.close()
