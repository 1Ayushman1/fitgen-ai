import streamlit as st
import sqlite3

conn=sqlite3.connect(
"fitness.db",
check_same_thread=False
)

cursor=conn.cursor()

st.title(
"📜 History"
)


if st.button(
"🗑️ Clear History"
):

    cursor.execute(
"""
DELETE FROM users
"""
    )

    conn.commit()

    st.success(
"History Cleared"
    )



rows=list(
cursor.execute(
"""
SELECT * FROM users
"""
)
)


if rows:

    selected=st.selectbox(

"Select User",

[
r[0]

for r in rows

]

    )



    for r in rows:

        if r[0]==selected:

            st.write(
f"""
Age:
{r[1]}

Height:
{r[2]}

Weight:
{r[3]}

Goal:
{r[4]}
"""
            )

            if st.button(
"Use This Plan"
):

                st.session_state[
"name"
]=r[0]

                st.session_state[
"age"
]=r[1]

                st.session_state[
"height"
]=r[2]

                st.session_state[
"weight"
]=r[3]

                st.session_state[
"goal"
]=r[4]

                st.success(
"Open Planner"
)
