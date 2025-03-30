import sqlite3
conn = sqlite3.connect('library.db')
conn.execute("PRAGMA foreign_keys = ON;")
cur = conn.cursor()


def findBook():
    while True:
        print("What would you like to search by?")
        print("1 - Title")
        print("2 - Author")
        print("3 - Publisher")
        print("4 - ISBN")
        print("0 - Go Back")
        search = (input("Enter a number: "))

        if search == '0':
            return

        elif search == '1':
            # title
            title = str(input("Enter the title: "))

            query = """
                SELECT i.title, b.author, b.publisher, b.ISBN, b.pages
                FROM Item i JOIN Book b ON i.itemID = b.itemID
                WHERE i.type = 'Book' AND i.available = 1
                AND i.title = ?;
                """

            cur.execute(query, (title,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '2':
            # author
            author = str(input("Enter name of author: "))

            query = """
                SELECT i.title, b.author, b.publisher, b.ISBN, b.pages
                FROM Item i JOIN Book b ON i.itemID = b.itemID
                WHERE i.type = 'Book' AND i.available = 1
                AND b.author = ?;
                """

            cur.execute(query, (author,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        elif search == '3':
            # publisher
            publisher = input("Enter name of publisher: ")

            query = """
                SELECT i.title, b.author, b.publisher, b.ISBN, b.pages
                FROM Item i JOIN Book b ON i.itemID = b.itemID
                WHERE i.type = 'Book' AND i.available = 1
                AND b.publisher = ?;
                """

            cur.execute(query, (publisher,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        elif search == '4':
            # ISBN
            isbn = input("Enter name of ISBN: ")
            query = """
                SELECT i.title, b.author, b.publisher, b.ISBN, b.pages
                FROM Item i JOIN Book b ON i.itemID = b.itemID
                WHERE i.type = 'Book' AND i.available = 1
                AND b.ISBN = ?;
                """

            cur.execute(query, (isbn,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        else:
            continue


def findMegazine():
    while True:
        print("What would you like to search by?")
        print("1 - Title")
        print("2 - Publisher")
        print("3 - ISSN")
        print("0 - Go Back")
        search = (input("Enter a number: "))

        if search == '0':
            return

        elif search == '1':
            # title
            title = str(input("Enter the title: "))

            query = """
                SELECT i.title, m.publisher, m.ISSN, m.pages
                FROM Item i JOIN Magazine m ON i.itemID = m.itemID
                WHERE i.type = 'Magazine' AND i.available = 1
                AND i.title = ?;
                """

            cur.execute(query, (title,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '2':
            # publisher
            publisher = input("Enter name of publisher: ")

            query = """
                SELECT i.title, m.publisher, m.ISSN, m.pages
                FROM Item i JOIN Magazine m ON i.itemID = m.itemID
                WHERE i.type = 'Magazine' AND i.available = 1
                AND m.publisher = ?;
                """

            cur.execute(query, (publisher,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '3':
            # ISSN
            issn = input("Enter name of ISSN: ")

            query = """
                SELECT i.title, m.publisher, m.ISSN, m.pages
                FROM Item i JOIN Magazine m ON i.itemID = m.itemID
                WHERE i.type = 'Magazine' AND i.available = 1
                AND m.ISSN = ?;
                """

            cur.execute(query, (issn,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        else:
            continue


def findJournal():
    while True:
        print("What would you like to search by?")
        print("1 - Title")
        print("2 - Author")
        print("3 - Publisher")
        print("4 - DOI")
        print("0 - Go Back")
        search = (input("Enter a number: "))

        if search == '0':
            return

        elif search == '1':
            # title
            title = str(input("Enter the title: "))

            query = """
                SELECT i.title, j.author, j.publisher, j.doi, j.pages
                FROM Item i JOIN Journal j ON i.itemID = j.itemID
                WHERE i.type = 'Journal' AND i.available = 1
                AND i.title = ?;
                """

            cur.execute(query, (title,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '2':
            # author
            author = str(input("Enter name of author: "))

            query = """
                SELECT i.title, j.author, j.publisher, j.doi, j.pages
                FROM Item i JOIN Journal j ON i.itemID = j.itemID
                WHERE i.type = 'Book' AND i.available = 1
                AND j.author = ?;
                """

            cur.execute(query, (author,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        elif search == '3':
            # publisher
            publisher = input("Enter name of publisher: ")

            query = """
                SELECT i.title, j.author, j.publisher, j.doi, j.pages
                FROM Item i JOIN Journal j ON i.itemID = j.itemID
                WHERE i.type = 'Journal' AND i.available = 1
                AND j.publisher = ?;
                """

            cur.execute(query, (publisher,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        elif search == '4':
            # DOI
            isbn = input("Enter name of DOI: ")
            query = """
                SELECT i.title, j.author, j.publisher, j.doi, j.pages
                FROM Item i JOIN Journal j ON i.itemID = j.itemID
                WHERE i.type = 'Journal' AND i.available = 1
                AND j.doi = ?;
                """

            cur.execute(query, (isbn,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        else:
            continue


def findCD():
    while True:
        print("What would you like to search by?")
        print("1 - Title")
        print("2 - Author")
        print("3 - Publisher")
        print("0 - Go Back")
        search = (input("Enter a number: "))

        if search == '0':
            return

        elif search == '1':
            # title
            title = str(input("Enter the title: "))

            query = """
                SELECT i.title, c.author, c.publisher, c.time
                FROM Item i JOIN CD c ON i.itemID = c.itemID
                WHERE i.type = 'CD' AND i.available = 1
                AND i.title = ?;
                """

            cur.execute(query, (title,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '2':
            # Author
            author = input("Enter name of author: ")

            query = """
                SELECT i.title, c.author, c.publisher, c.time
                FROM Item i JOIN CD c ON i.itemID = c.itemID
                WHERE i.type = 'CD' AND i.available = 1
                AND c.author = ?;
                """

            cur.execute(query, (author,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '3':
            # publisher
            publisher = input("Enter name of publisher: ")

            query = """
                SELECT i.title, c.author, c.publisher, c.time
                FROM Item i JOIN CD c ON i.itemID = c.itemID
                WHERE i.type = 'CD' AND i.available = 1
                AND c.publisher = ?;
                """

            cur.execute(query, (publisher,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        else:
            continue


def findRecord():
    while True:
        print("What would you like to search by?")
        print("1 - Title")
        print("2 - Author")
        print("3 - Publisher")
        print("0 - Go Back")
        search = (input("Enter a number: "))

        if search == '0':
            return

        elif search == '1':
            # title
            title = str(input("Enter the title: "))

            query = """
                SELECT i.title, r.author, r.publisher, r.time
                FROM Item i JOIN Record r ON i.itemID = r.itemID
                WHERE i.type = 'Record' AND i.available = 1
                AND i.title = ?;
                """

            cur.execute(query, (title,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '2':
            # Author
            author = input("Enter name of author: ")

            query = """
                SELECT i.title, r.author, r.publisher, r.time
                FROM Item i JOIN Record r ON i.itemID = r.itemID
                WHERE i.type = 'Record' AND i.available = 1
                AND r.author = ?;
                """

            cur.execute(query, (author,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

        elif search == '3':
            # publisher
            publisher = input("Enter name of publisher: ")

            query = """
                SELECT i.title, r.author, r.publisher, r.time
                FROM Item i JOIN Record r ON i.itemID = r.itemID
                WHERE i.type = 'Record' AND i.available = 1
                AND r.publisher = ?;
                """

            cur.execute(query, (publisher,))
            rows = cur.fetchall()

            for row in rows:
                print(row)
        else:
            continue


def findItem():

    while True:
        print("What type of item would you like to search for?")
        print("1 - Book")
        print("2 - Magazine")
        print("3 - Journal")
        print("4 - CD")
        print("5 - Record")
        print("0 - Go Back")
        type = int(input("Enter a number: "))

        if type == 0:
            return

        if type == 1:
            findBook()
        elif type == 2:
            findMegazine()
        elif type == 3:
            findJournal()
        elif type == 4:
            findCD()
        elif type == 5:
            findRecord()
        else:
            continue


"""
:TODO
def borrowItem():


def returnItem():


def donateItem():


def findEvent():


def registerEvent():


def volunteer():


def findLibrarian():
"""


def library():

    shouldExit = False

    while not shouldExit:
        print("What would you like to do?")
        print("1 - Search for an item")
        print("2 - Borrow an item")
        print("3 - Return an item")
        print("4 - Donate an item")
        print("5 - Find an event")
        print("6 - Register for an event")
        print("7 - Register as a volunteer")
        print("8 - Contact a librarian")
        print("0 - Exit")

        choice = input("Enter the number corresponding you your request: ")

        if choice == '0':
            shouldExit = True
            conn.close()
        elif choice == '1':
            findItem()
        elif choice == '2':
            borrowItem()
        elif choice == '3':
            returnItem()
        elif choice == '4':
            donateItem()
        elif choice == '5':
            findEvent()
        elif choice == '6':
            registerEvent()
        elif choice == '7':
            volunteer()
        elif choice == '8':
            findLibrarian()
        else:
            continue

        print(choice)
    return 0


if __name__ == "__main__":
    library()
