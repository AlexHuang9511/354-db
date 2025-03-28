import sqlite3
conn = sqlite3.connect('library.db')

conn.execute("PRAGMA foreign_keys = ON;")

"""
(Step 6)
Populate tables with sample tuples
"""

tuple_queries = (
    """
    INSERT INTO Item VALUES
    (0, 'Book', 1, '2024-03-10', 25),
    (1, 'Book', 1, '2024-02-15', 25),
    (2, 'Book', 1, '2024-01-20', 30),
    (3, 'Book', 1, '2024-03-05', 20),
    (4, 'Book', 1, '2024-01-30', 20),
    (5, 'Book', 1, '2024-02-25', 20),
    (6, 'Book', 1, '2024-03-12', 20),
    (7, 'Book', 1, '2024-02-18', 25),
    (8, 'Book', 1, '2024-03-08', 20),
    (9, 'Book', 1, '2024-01-22', 30),

    (10, 'Magazine', 1, '2024-03-01', 25.50),
    (11, 'Magazine', 1, '2024-02-15', 22.75),
    (12, 'Magazine', 1, '2024-03-10', 28.00),
    (13, 'Magazine', 1, '2024-02-20', 24.30),
    (14, 'Magazine', 1, '2024-03-05', 27.60),
    (15, 'Magazine', 1, '2024-02-25', 21.85),
    (16, 'Magazine', 1, '2024-03-12', 29.40),
    (17, 'Magazine', 1, '2024-02-18', 23.25),
    (18, 'Magazine', 1, '2024-03-08', 26.70),
    (19, 'Magazine', 1, '2024-01-22', 20.95),

    (20, 'Journal', 1, '2024-03-01', 24.50),
    (21, 'Journal', 1, '2024-02-15', 21.75),
    (22, 'Journal', 1, '2024-03-10', 29.00),
    (23, 'Journal', 1, '2024-02-20', 25.30),
    (24, 'Journal', 1, '2024-03-05', 27.60),
    (25, 'Journal', 1, '2024-02-25', 22.85),
    (26, 'Journal', 1, '2024-03-12', 28.40),
    (27, 'Journal', 1, '2024-02-18', 23.25),
    (28, 'Journal', 1, '2024-03-08', 26.70),
    (29, 'Journal', 1, '2024-01-22', 20.95),

    (30, 'CD', 1, '2024-03-01', 24.50),
    (31, 'CD', 1, '2024-02-15', 21.75),
    (32, 'CD', 1, '2024-03-10', 29.00),
    (33, 'CD', 1, '2024-02-20', 25.30),
    (34, 'CD', 1, '2024-03-05', 27.60),
    (35, 'CD', 1, '2024-02-25', 22.85),
    (36, 'CD', 1, '2024-03-12', 28.40),
    (37, 'CD', 1, '2024-02-18', 23.25),
    (38, 'CD', 1, '2024-03-08', 26.70),
    (39, 'CD', 1, '2024-01-22', 20.95),

    (40, 'Record', 1, '2024-03-01', 24.50),
    (41, 'Record', 1, '2024-02-15', 21.75),
    (42, 'Record', 1, '2024-03-10', 29.00),
    (43, 'Record', 1, '2024-02-20', 25.30),
    (44, 'Record', 1, '2024-03-05', 27.60),
    (45, 'Record', 1, '2024-02-25', 22.85),
    (46, 'Record', 1, '2024-03-12', 28.40),
    (47, 'Record', 1, '2024-02-18', 23.25),
    (48, 'Record', 1, '2024-03-08', 26.70),
    (49, 'Record', 1, '2024-01-22', 20.95);
    """,

    """
    INSERT INTO Book VALUES
    (0, 'George Orwell', 'Secker & Warburg', '1949-06-08', 328, '978-0451524935'),
    (1, 'J.K. Rowling', 'Bloomsbury', '1997-06-26', 223, '978-0747532699'),
    (2, 'J.R.R. Tolkien', 'Allen & Unwin', '1954-07-29', 423, '978-0618640157'),
    (3, 'Harper Lee', 'J.B. Lippincott & Co.', '1960-07-11', 281, '978-0061120084'),
    (4, 'F. Scott Fitzgerald', 'Charles Scribner’s Sons', '1925-04-10', 180, '978-0743273565'),
    (5, 'Leo Tolstoy', 'The Russian Messenger', '1869-01-01', 1225, '978-1420953297'),
    (6, 'Gabriel García Márquez', 'Editorial Sudamericana', '1967-05-30', 417, '978-0060883287'),
    (7, 'Mark Twain', 'American Publishing Company', '1885-02-18', 366, '978-0486280615'),
    (8, 'Mary Shelley', 'Lackington, Hughes, Harding, Mavor & Jones', '1818-01-01', 280, '978-0486282114'),
    (9, 'Jane Austen', 'T. Egerton', '1813-01-28', 279, '978-1503290563');
    """,

    """
    INSERT INTO Magazine VALUES
    (10, 'National Geographic', '2024-03-01', 98, '0027-9358'),
    (11, 'TIME', '2024-02-15', 76, '0040-781X'),
    (12, 'Scientific American', '2024-03-10', 88, '0036-8733'),
    (13, 'Forbes', '2024-02-20', 100, '0015-6914'),
    (14, 'The New Yorker', '2024-03-05', 120, '0028-792X'),
    (15, 'Wired', '2024-02-25', 110, '1059-1028'),
    (16, 'Popular Science', '2024-03-12', 90, '0161-7370'),
    (17, 'Smithsonian', '2024-02-18', 85, '0037-7333'),
    (18, 'Harvard Business Review', '2024-03-08', 95, '0017-8012'),
    (19, 'Nature', '2024-01-22', 150, '0028-0836');
    """,

    """
    INSERT INTO Journal VALUES
    (20, 'John Doe', 'Springer', '2024-03-01', 25, '10.1000/j.journal1'),
    (21, 'Jane Smith', 'Elsevier', '2024-02-15', 30, '10.1000/j.journal2'),
    (22, 'Alice Johnson', 'Wiley', '2024-03-10', 28, '10.1000/j.journal3'),
    (23, 'Robert Brown', 'Nature Publishing Group', '2024-02-20', 32, '10.1000/j.journal4'),
    (24, 'Emily White', 'Oxford University Press', '2024-03-05', 27, '10.1000/j.journal5'),
    (25, 'David Miller', 'Cambridge University Press', '2024-02-25', 35, '10.1000/j.journal6'),
    (26, 'Sarah Wilson', 'IEEE', '2024-03-12', 22, '10.1000/j.journal7'),
    (27, 'Michael Clark', 'ACM', '2024-02-18', 29, '10.1000/j.journal8'),
    (28, 'Laura Martinez', 'SAGE Publications', '2024-03-08', 31, '10.1000/j.journal9'),
    (29, 'Daniel Lewis', 'Taylor & Francis', '2024-01-22', 26, '10.1000/j.journal10');
    """,

    """
    INSERT INTO CD VALUES
    (30, 'The Beatles', 'Apple Records', '1969-09-26', 47),
    (31, 'Pink Floyd', 'Harvest Records', '1973-03-01', 43),
    (32, 'Michael Jackson', 'Epic Records', '1982-11-30', 42),
    (33, 'Queen', 'EMI', '1975-11-21', 40),
    (34, 'Nirvana', 'DGC Records', '1991-09-24', 49),
    (35, 'Adele', 'Columbia Records', '2011-11-18', 45),
    (36, 'Taylor Swift', 'Republic Records', '2022-10-21', 61),
    (37, 'Eminem', 'Aftermath Entertainment', '2000-05-23', 50),
    (38, 'Daft Punk', 'Virgin Records', '2013-05-17', 74),
    (39, 'The Weeknd', 'XO Records', '2020-03-20', 56);
    """,

    """
    INSERT INTO Record VALUES
    (40, 'The Rolling Stones', 'Decca Records', '1972-05-12', 46),
    (41, 'The Beatles', 'Parlophone', '1967-05-26', 40),
    (42, 'Fleetwood Mac', 'Warner Bros.', '1977-02-04', 45),
    (43, 'David Bowie', 'RCA Records', '1972-06-16', 39),
    (44, 'Led Zeppelin', 'Atlantic Records', '1971-11-08', 42),
    (45, 'Bob Dylan', 'Columbia Records', '1965-03-22', 50),
    (46, 'Elvis Presley', 'RCA Victor', '1956-03-23', 29),
    (47, 'Prince', 'Paisley Park Records', '1984-06-25', 44),
    (48, 'The Doors', 'Elektra Records', '1967-01-04', 43),
    (49, 'U2', 'Island Records', '1987-03-09', 51);
    """
)

with conn:
    cur = conn.cursor()

    for q in tuple_queries:
        cur.execute(q)

    print("Tuples added to database")

if conn:
    conn.close()
