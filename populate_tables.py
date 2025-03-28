import sqlite3
conn = sqlite3.connect('library.db')

conn.execute("PRAGMA foreign_keys = ON;")

"""
(Step 6)
Populate tables with sample tuples
"""

setup_queries = (
    """"""
)

with conn:
    cur = conn.cursor()

    for q in setup_queries:
        cur.execute(q)

    print("Tuples added to database")

if conn:
    conn.close()
