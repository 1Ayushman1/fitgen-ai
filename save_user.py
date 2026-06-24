import sqlite3


def save_user(
    name,
    age,
    height,
    weight,
    goal
):

    conn = sqlite3.connect(
        "users.db"
    )

    cursor = conn.cursor()


    cursor.execute(
"""
CREATE TABLE IF NOT EXISTS users(

name TEXT,
age INTEGER,
height REAL,
weight REAL,
goal TEXT

)
"""
    )


    cursor.execute(

"""
INSERT INTO users
VALUES(
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
height,
weight,
goal
)

    )


    conn.commit()

    conn.close()
