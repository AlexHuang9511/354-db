import sqlite3
conn = sqlite3.connect('library.db')

conn.execute("PRAGMA foreign_keys = ON;")

"""
(Step 5)
This is the initial setup script to create the schema.
It should only be run once at the beginning to put the tables into the database.
"""

setup_queries = (
    """
    CREATE TABLE Item(
    itemID INTEGER,
    type TEXT,
    available INTEGER,
    arrivalDate TEXT,
    fine REAL,
    PRIMARY KEY (itemID),
    CHECK (type IN ('Book', 'Magazine', 'Journal', 'CD', 'Record')),
    CHECK (available IN (True, False)),
    CHECK (fine >= 0));
    """,

    """
    CREATE TABLE Book(
    itemID INTEGER,
    author TEXT,
    publisher TEXT,
    releaseDate TEXT,
    pages INTEGER,
    ISBN TEXT,
    FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE,
    CHECK (pages > 0));
    """,

    """
    CREATE TABLE Magazine(
    itemID INTEGER,
    publisher TEXT,
    releaseDate TEXT,
    pages INTEGER,
    ISSN TEXT,
    FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE,
    CHECK (pages > 0));
    """,

    """
    CREATE TABLE Journal(
    itemID INTEGER,
    author TEXT,
    publisher TEXT,
    releaseDate TEXT,
    pages INTEGER,
    doi TEXT,
    FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE,
    CHECK (pages > 0));
    """,

    """
    CREATE TABLE CD(
    itemID INTEGER,
    author TEXT,
    publisher TEXT,
    releaseDate TEXT,
    time INTEGER,
    FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE,
    CHECK (time > 0));
    """,

    """
    CREATE TABLE Record(
    itemID INTEGER,
    author TEXT,
    publisher TEXT,
    releaseDate TEXT,
    time INTEGER,
    FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE,
    CHECK (time > 0));
    """,

    """
    CREATE TABLE Borrower(
    borrowerID INTEGER,
    name TEXT,
    email TEXT,
    phone INTEGER,
    balanceOwed REAL,
    PRIMARY KEY (borrowerID),
    CHECK (balanceOwed >= 0));
    """,

    """
    CREATE TABLE Borrows(
    borrowerID INTEGER,
    itemID INTEGER,
    borrowDate TEXT,
    returnDate TEXT,
    dueDate TEXT,
    FOREIGN KEY (borrowerID) REFERENCES Borrower(borrowerID) ON DELETE CASCADE,
    FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE,
    PRIMARY KEY (borrowerID, itemID, borrowDate),
    CHECK (dueDate >= borrowDate),
    CHECK (returnDate >= borrowDate));
    """,

    """
    CREATE TABLE Event(
    eventID INTEGER,
    name TEXT,
    date TEXT,
    audience TEXT,
    room TEXT,
    PRIMARY KEY (eventID));
    """,

    """
    CREATE TABLE Attendee(
    attendeeID INTEGER,
    name TEXT,
    email TEXT,
    phone INTEGER,
    PRIMARY KEY (attendeeID));
    """,

    """
    CREATE TABLE Attends(
    attendeeID INTEGER,
    eventID INTEGER,
    phone INTEGER,
    FOREIGN KEY (attendeeID) REFERENCES Attendee(attendeeID) ON DELETE CASCADE,
    FOREIGN KEY (eventID) REFERENCES Event(eventID) ON DELETE CASCADE,
    PRIMARY KEY (attendeeID));
    """,

    """
    CREATE TABLE Personnel(
    PID INTEGER,
    name TEXT,
    email TEXT,
    phone INTEGER,
    position TEXT,
    PRIMARY KEY (PID));
    """,
)

with conn:
    cur = conn.cursor()

    for q in setup_queries:
        cur.execute(q)

    print("Tables added to database")

if conn:
    conn.close()
