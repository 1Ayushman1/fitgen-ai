import sqlite3


def save_user(
        name,
        age,
        goal,
        bmi,
        category,
        calories
):

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


    cursor.execute("""
    INSERT INTO users(
        name,
        age,
        goal,
        bmi,
        category,
        calories
    )

    VALUES(
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
    )
    """,

    (
        name,
        age,
        goal,
        bmi,
        category,
        calories
    )

    )

    conn.commit()

    conn.close()
