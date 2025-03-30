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
    (0, 'Book', 'One Hundred Years of Solitude', 1, '2024-03-10', 20),
    (1, 'Book', 'War and Peace', 1, '2024-02-15', 20),
    (2, 'Book', 'The Lord of the Rings', 1, '2024-01-20', 30),
    (3, 'Book', 'To Kill a Mockingbird', 1, '2024-03-05', 20),
    (4, 'Book', 'The Great Gatsby', 1, '2024-01-30', 20),
    (5, 'Book', 'War and Peace', 0, '2024-02-25', 20),
    (6, 'Book', 'One Hundred Years of Solitude', 1, '2024-03-12', 20),
    (7, 'Book', 'Adventures of Huckleberry Finn', 0, '2024-02-18', 25),
    (8, 'Book', 'Frankenstein', 1, '2024-03-08', 20),
    (9, 'Book', 'Pride and Prejudice', 0, '2024-01-22', 30),

    (10, 'Magazine', 'National Geographic - March 2024', 1, '2024-03-01', 25.50),
    (11, 'Magazine', 'TIME - February 2024', 1, '2024-02-15', 22.75),
    (12, 'Magazine', 'Scientific American - March 2024', 0, '2024-03-10', 28.00),
    (13, 'Magazine', 'Scientific American - March 2024', 0, '2024-02-20', 28.00),
    (14, 'Magazine', 'The New Yorker - March 2024', 1, '2024-03-05', 27.60),
    (15, 'Magazine', 'Wired - February 2024', 0, '2024-02-25', 21.85),
    (16, 'Magazine', 'Popular Science - March 2024', 1, '2024-03-12', 29.40),
    (17, 'Magazine', 'Smithsonian - February 2024', 1, '2024-02-18', 23.25),
    (18, 'Magazine', 'Nature - January 2024', 1, '2024-03-08', 20.95),
    (19, 'Magazine', 'Nature - January 2024', 1, '2024-01-22', 20.95),

    (20, 'Journal', 'Social Sciences Review - March 2024', 1, '2024-03-01', 26.70),
    (21, 'Journal', 'Medical Innovations - February 2024', 1, '2024-02-15', 21.75),
    (22, 'Journal', 'Quantum Computing Review - March 2024', 0, '2024-03-10', 29.00),
    (23, 'Journal', 'Environmental Studies - February 2024', 1, '2024-02-20', 25.30),
    (24, 'Journal', 'Philosophy Today - March 2024', 1, '2024-03-05', 27.60),
    (25, 'Journal', 'Economic Trends - February 2024', 1, '2024-02-25', 22.85),
    (26, 'Journal', 'Neuroscience Frontiers - March 2024', 1, '2024-03-12', 28.40),
    (27, 'Journal', 'Cybersecurity & Privacy - February 2024', 0, '2024-02-18', 23.25),
    (28, 'Journal', 'Social Sciences Review - March 2024', 1, '2024-03-08', 26.70),
    (29, 'Journal', 'Machine Learning Digest - January 2024', 1, '2024-01-22', 20.95),

    (30, 'CD', 'Abbey Road', 0, '2024-03-01', 24.50),
    (31, 'CD', 'The Dark Side of the Moon', 1, '2024-02-15', 21.75),
    (32, 'CD', 'Thriller', 1, '2024-03-10', 29.00),
    (33, 'CD', 'A Night at the Opera', 1, '2024-02-20', 25.30),
    (34, 'CD', 'Nevermind', 1, '2024-03-05', 27.60),
    (35, 'CD', '21', 1, '2024-02-25', 22.85),
    (36, 'CD', 'The Marshall Mathers LP', 1, '2024-03-12', 23.25),
    (37, 'CD', 'The Marshall Mathers LP', 1, '2024-02-18', 23.25),
    (38, 'CD', 'Random Access Memories', 1, '2024-03-08', 26.70),
    (39, 'CD', 'After Hours', 1, '2024-01-22', 20.95),

    (40, 'Record', 'Exile on Main St.', 1, '2024-03-01', 24.50),
    (41, 'Record', 'Sgt. Pepper’s Lonely Hearts Club Band', 1, '2024-02-15', 21.75),
    (42, 'Record', 'Rumours', 1, '2024-03-10', 29.00),
    (43, 'Record', 'The Rise and Fall of Ziggy Stardust', 1, '2024-02-20', 25.30),
    (44, 'Record', 'Led Zeppelin IV', 0, '2024-03-05', 27.60),
    (45, 'Record', 'Bringing It All Back Home', 1, '2024-02-25', 22.85),
    (46, 'Record', 'Elvis Presley', 1, '2024-03-12', 28.40),
    (47, 'Record', 'Purple Rain', 1, '2024-02-18', 23.25),
    (48, 'Record', 'The Doors', 1, '2024-03-08', 26.70),
    (49, 'Record', 'The Joshua Tree', 1, '2024-01-22', 20.95);
    """,

    """
    INSERT INTO Book VALUES
    (0, 'Gabriel García Márquez', 'Editorial Sudamericana', '1967-05-30', 417, '978-0060883287'),
    (1, 'Leo Tolstoy', 'The Russian Messenger', '1869-01-01', 1225, '978-1420953297'),
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
    (13, 'Scientific American', '2024-03-10', 88, '0036-8733'),
    (14, 'The New Yorker', '2024-03-05', 120, '0028-792X'),
    (15, 'Wired', '2024-02-25', 110, '1059-1028'),
    (16, 'Popular Science', '2024-03-12', 90, '0161-7370'),
    (17, 'Smithsonian', '2024-02-18', 85, '0037-7333'),
    (18, 'Nature', '2024-01-22', 150, '0028-0836'),
    (19, 'Nature', '2024-01-22', 150, '0028-0836');
    """,

    """
    INSERT INTO Journal VALUES
    (20, 'Laura Martinez', 'SAGE Publications', '2024-03-08', 31, '10.1000/j.journal9'),
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
    (36, 'Eminem', 'Aftermath Entertainment', '2000-05-23', 50),
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
    """,

    """
    INSERT INTO Borrower VALUES
    (0, 'Alice Johnson', 'alice.johnson@gmail.com', 1234567890, 0),
    (1, 'Bob Smith', 'bob.smith@gmail.com', 2345678901, 0),
    (2, 'Charlie Davis', 'charlie.davis@gmail.com', 3456789012, 0),
    (3, 'David White', 'david.white@gmail.com', 4567890123, 0),
    (4, 'Emma Brown', 'emma.brown@gmail.com', 5678901234, 0),
    (5, 'Frank Miller', 'frank.miller@gmail.com', 6789012345, 0),
    (6, 'Grace Wilson', 'grace.wilson@gmail.com', 7890123456, 0),
    (7, 'Henry Adams', 'henry.adams@gmail.com', 8901234567, 0),
    (8, 'Isabella Martinez', 'isabella.martinez@gmail.com', 9012345678, 0),
    (9, 'Jack Taylor', 'jack.taylor@gmail.com', 9123456789, 0);
    """,

    """
    INSERT INTO Borrows VALUES
    (0, 12, '2025-03-01', NULL, '2025-04-01'),
    (1, 30, '2025-03-05', NULL, '2025-04-05'),
    (2, 15, '2025-03-10', NULL, '2025-04-10'),
    (3, 5, '2025-03-12', NULL, '2025-04-12'),
    (4, 13, '2025-03-15', NULL, '2025-04-15'),
    (5, 27, '2025-03-18', NULL, '2025-04-18'),
    (6, 44, '2025-03-20', NULL, '2025-04-20'),
    (7, 7, '2025-03-22', NULL, '2025-04-22'),
    (8, 22, '2025-03-25', NULL, '2025-04-25'),
    (9, 9, '2025-03-28', NULL, '2025-04-28');
    """,

    """
    INSERT INTO Event VALUES
    (100, 'Tech Conference 2025', '2025-05-10', 'Developers, Entrepreneurs', 'A302'),
    (101, 'AI Symposium', '2025-06-15', 'Researchers, Students', 'B320'),
    (102, 'Music Fest', '2025-07-20', 'Music Lovers, Artists', 'A203'),
    (103, 'Science Fair', '2025-08-05', 'Students, Scientists', 'C414'),
    (104, 'Business Summit', '2025-09-12', 'Executives, Entrepreneurs', 'A311'),
    (105, 'Art Exhibition', '2025-10-18', 'Artists, Collectors', 'A315'),
    (106, 'Sports Meetup', '2025-11-25', 'Athletes, Coaches', 'C337'),
    (107, 'Book Fair', '2025-12-02', 'Readers, Writers', 'B399'),
    (108, 'Film Festival', '2026-01-14', 'Filmmakers, Critics', 'B399'),
    (109, 'Health & Wellness Expo', '2026-02-22', 'Doctors, Fitness Enthusiasts', 'A302');
    """,

    """
    INSERT INTO Attendee VALUES
    (0, 'Oliver Scott', 'oliver.scott@gmail.com', 1234567890),
    (1, 'Sophia Lee', 'sophia.lee@gmail.com', 2345678901),
    (2, 'Liam Walker', 'liam.walker@gmail.com', 3456789012),
    (3, 'Mia Robinson', 'mia.robinson@gmail.com', 4567890123),
    (4, 'Ethan Harris', 'ethan.harris@gmail.com', 5678901234),
    (5, 'Ava Gonzalez', 'ava.gonzalez@gmail.com', 6789012345),
    (6, 'Mason Carter', 'mason.carter@gmail.com', 7890123456),
    (7, 'Isabella Wright', 'isabella.wright@gmail.com', 8901234567),
    (8, 'Lucas Adams', 'lucas.adams@gmail.com', 9012345678),
    (9, 'Charlotte Mitchell', 'charlotte.mitchell@gmail.com', 9123456789);
    """,

    """
    INSERT INTO Attends VALUES
    (0, 100),
    (0, 105),
    (1, 100),
    (7, 100),
    (2, 108),
    (0, 108),
    (3, 108),
    (8, 104),
    (9, 109),
    (9, 103);
    """,

    """
    INSERT INTO Personnel VALUES
    (19822, 'Oliver Scott', 'oliver.scott@gmail.com', 1234567890, 'Librarian'),
    (22033, 'Sophia Lee', 'sophia.lee@gmail.com', 2345678901, 'Archivist'),
    (28548, 'Liam Walker', 'liam.walker@gmail.com', 3456789012, 'Library Assistant'),
    (13562, 'Mia Robinson', 'mia.robinson@gmail.com', 4567890123, 'Reference Librarian'),
    (10739, 'Ethan Harris', 'ethan.harris@gmail.com', 5678901234, 'Librarian'),
    (27227, 'Emma Thompson', 'emma.thompson@gmail.com', 6789123456, 'Cataloger'),
    (39715, 'James Anderson', 'james.anderson@gmail.com', 7890234567, 'Volunteer'),
    (40290, 'Isabella Wright', 'isabella.wright@gmail.com', 8901234567, 'Volunteer'),
    (25222, 'Lucas Adams', 'lucas.adams@gmail.com', 9012345678, 'Digital Resources Librarian'),
    (24843, 'William Johnson', 'william.johnson@gmail.com', 9123345679, 'Library Director');
    """
)

with conn:
    cur = conn.cursor()

    for q in tuple_queries:
        cur.execute(q)

    print("Tuples added to database")

if conn:
    conn.close()
