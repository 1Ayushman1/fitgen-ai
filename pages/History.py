import streamlit as st
import sqlite3
import pandas as pd


st.title("📜 History")


conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
goal TEXT,
bmi REAL,
category TEXT,
calories INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


if st.button("🗑 Clear History"):

    cursor.execute(
        "DELETE FROM users"
    )

    conn.commit()

    st.success(
        "History Cleared"
    )



cursor.execute("""
SELECT
name,
age,
goal,
bmi,
category,
calories,
created_at
FROM users
ORDER BY created_at DESC
""")


rows = cursor.fetchall()


if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            "Name",
            "Age",
            "Goal",
            "BMI",
            "Category",
            "Calories",
            "Created"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "No history yet"
    )


conn.close()
