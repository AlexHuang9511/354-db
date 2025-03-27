import sqlite3
conn = sqlite3.connect('library.db')

"""
Utility script to drop all tables in library.db
"""

with conn:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_schema WHERE type='table';")
    tables = cur.fetchall()
    for t in tables:
        cur.execute("DROP TABLE %s" % t)

if conn:
    conn.close()
