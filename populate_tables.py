import sqlite3
conn = sqlite3.connect('library.db')

conn.execute("PRAGMA foreign_keys = ON;")

"""
(Step 6)
Populate tables with sample tuples
"""

tuple_queries = (
    """"""
)

with conn:
    cur = conn.cursor()

    for q in tuple_queries:
        cur.execute(q)

    print("Tuples added to database")

if conn:
    conn.close()
