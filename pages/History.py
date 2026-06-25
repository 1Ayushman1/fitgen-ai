import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 History")

# DATABASE
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# CREATE TABLE IF NOT EXISTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
name TEXT,
age INTEGER,
height REAL,
weight REAL,
goal TEXT,
bmi REAL,
calories INTEGER
)
""")

conn.commit()

# LOAD DATA
cursor.execute("""
SELECT
name,
age,
height,
weight,
goal,
bmi,
calories
FROM users
""")

rows = cursor.fetchall()

if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            "Name",
            "Age",
            "Height",
            "Weight",
            "Goal",
            "BMI",
            "Calories"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    selected = st.selectbox(
        "Select Saved User",
        df["Name"].tolist()
    )

    selected_data = (
        df[df["Name"] == selected]
        .iloc[0]
    )

    st.subheader("Selected User")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "BMI",
        round(selected_data["BMI"], 2)
    )

    c2.metric(
        "Goal",
        selected_data["Goal"]
    )

    c3.metric(
        "Calories",
        f'{selected_data["Calories"]} kcal'
    )

    c4.metric(
        "Weight",
        f'{selected_data["Weight"]} kg'
    )

    if st.button("🗑 Clear History"):

        cursor.execute(
            "DELETE FROM users"
        )

        conn.commit()

        st.success(
            "History Cleared"
        )

        st.rerun()

else:

    st.info(
        "No saved users yet"
    )

conn.close()
