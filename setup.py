import sqlite3
conn = sqlite3.connect('library.db')

"""
(Step 5)
This is just the initial setup script to create the schema.
It should only ever be run once at the very beginning.
It is written out here for convenience.
"""

setup_queries = (
    ("CREATE TABLE Item("
     "itemID INTEGER,"
     "type TEXT,"
     "available INTEGER,"
     "arrivalDate TEXT,"
     "fine REAL,"
     "PRIMARY KEY(itemID));"),

    ("CREATE TABLE Book("
     "itemID INTEGER,"
     "author TEXT,"
     "publisher TEXT,"
     "releaseDate TEXT,"
     "pages INTEGER,"
     "ISBN TEXT,"
     "FOREIGN KEY(itemID) REFERENCES Item(itemID) ON DELETE CASCADE);"),

    ("CREATE TABLE Magazine("
     "itemID INTEGER,"
     "publisher TEXT,"
     "releaseDate TEXT,"
     "pages INTEGER,"
     "ISSN TEXT,"
     "FOREIGN KEY(itemID) REFERENCES Item(itemID) ON DELETE CASCADE);"),

    ("CREATE TABLE Journal("
     "itemID INTEGER,"
     "author TEXT,"
     "publisher TEXT,"
     "releaseDate TEXT,"
     "pages INTEGER,"
     "doi TEXT,"
     "FOREIGN KEY(itemID) REFERENCES Item(itemID) ON DELETE CASCADE);"),

    ("CREATE TABLE CD("
     "itemID INTEGER,"
     "author TEXT,"
     "publisher TEXT,"
     "releaseDate TEXT,"
     "time INTEGER,"
     "FOREIGN KEY(itemID) REFERENCES Item(itemID) ON DELETE CASCADE);"),

    ("CREATE TABLE Record("
     "itemID INTEGER,"
     "author TEXT,"
     "publisher TEXT,"
     "releaseDate TEXT,"
     "time INTEGER,"
     "FOREIGN KEY(itemID) REFERENCES Item(itemID) ON DELETE CASCADE);")
)

with conn:
    cur = conn.cursor()

    for q in setup_queries:
        cur.execute(q)

if conn:
    conn.close()
