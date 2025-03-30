import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('library.db')
conn.execute("PRAGMA foreign_keys = ON;")
cur = conn.cursor()


def findItem():
    # option:(type, search attribute, search query)
    options = {'1': ("Book", ("Title", "Author", "Publisher", "ISBN"),
                     """
                  SELECT i.itemID, i.title, b.author, b.publisher, b.ISBN, b.pages
                  FROM Item i JOIN Book b ON i.itemID = b.itemID
                  WHERE i.type = 'Book' AND i.available = 1
                  AND """),
               '2': ("Magazine", ("Title", "Publisher", "ISSN"),
                     """
                  SELECT i.itemID, i.title, m.publisher, m.ISSN, m.pages
                  FROM Item i JOIN Magazine m ON i.itemID = m.itemID
                  WHERE i.type = 'Magazine' AND i.available = 1
                  AND """),
               '3': ("Journal", ("Title", "Author", "Publisher", "DOI"),
                     """
                  SELECT i.itemID, i.title, j.author, j.publisher, j.doi, j.pages
                  FROM Item i JOIN Journal j ON i.itemID = j.itemID
                  WHERE i.type = 'Journal' AND i.available = 1
                  AND """),
               '4': ("CD", ("Title", "Author", "Publisher"),
                     """
                  SELECT i.itemID, i.title, c.author, c.publisher, c.time
                  FROM Item i JOIN CD c ON i.itemID = c.itemID
                  WHERE i.type = 'CD' AND i.available = 1
                  AND """),
               '5': ("Record", ("Title", "Author", "Publisher"),
                     """
                  SELECT i.itemID, i.title, r.author, r.publisher, r.time
                  FROM Item i JOIN Record r ON i.itemID = r.itemID
                  WHERE i.type = 'Record' AND i.available = 1
                  AND """)}

    while True:
        print("What type of item would you like to search for?")
        for o in options:
            print(o, "-", options[o][0])
        print("0 - Go back")

        type = input("Enter a number: ")

        if type == '0':
            return

        if type in options:
            search = None
            while search != 0:
                print("What would you like to search by?")
                for i in range(1, len(options[type][1]) + 1):
                    print(i, "-", options[type][1][i-1])
                print("0 - Go back")

                try:
                    search = int(input("Enter a number: "))
                except:
                    continue

                if 1 <= search <= len(options[type][1]):
                    # Construct query
                    query = options[type][2]
                    if search == 1:  # Title
                        query += "i."  # Search in Item
                    else:  # Not title, search in subtype
                        query += options[type][0][0] + "."
                    query += options[type][1][search-1] + " = ?;"

                    param = str(
                        input("Enter " + options[type][1][search-1] + ": "))

                    cur.execute(query, (param,))
                    rows = cur.fetchall()

                    for row in rows:
                        print(row)


def borrowItem():
    borrowerID = input("Enter your ID: ")
    itemID = input("Enter the itemID of the item you want to borrow: ")

    date = datetime.today()
    dueDate = date + timedelta(days=30)

    date = date.strftime("%y-%m-%d")
    dueDate = dueDate.strftime("%y-%m-%d")

    # put item into Borrows
    query = """
        INSERT INTO Borrows VALUES
        (?, ?, ?, NULL, ?)
    """

    cur.execute(query, (borrowerID, itemID, date, dueDate,))

    # make item unavailable
    query = """
        UPDATE Item
        SET available=0
        WHERE Item.itemID = ?
    """

    cur.execute(query, (itemID,))

    conn.commit()
    return


def returnItem():
    borrowerID = input("Enter your ID: ")
    itemID = input("Enter the itemID of the item you want to return: ")

    # make item available
    # trigger in db checks if item is over due
    #   sets returnDate to not NULL if item is overdue
    query = """
        UPDATE Item
        SET available = 1
        WHERE Item.itemID = ?
    """

    cur.execute(query, (itemID,))

    # remove from Borrows only if the returnDate is NULL
    # returnDate = NULL -> not overdue
    query = """
        DELETE FROM Borrows
        WHERE Borrows.itemID = ? AND Borrows.borrowerID = ?
        AND Borrows.returnDate IS NULL
    """

    cur.execute(query, (itemID, borrowerID))
    conn.commit()
    return


def donateItem():
    # itemID - get largest, existing itemID and add 1
    # type - input
    # title - input
    # avail = 1
    # arrivalDate = today
    # fine = 20
    # item specific fields

    # option:(type, input attribute, insert query)
    options = {'1': ("Book", ("Title", "Author", "Publisher", "ISBN"),
                     """
                  SELECT i.itemID, i.title, b.author, b.publisher, b.ISBN, b.pages
                  FROM Item i JOIN Book b ON i.itemID = b.itemID
                  WHERE i.type = 'Book' AND i.available = 1
                  AND """),
               '2': ("Magazine", ("Title", "Publisher", "ISSN"),
                     """
                  SELECT i.itemID, i.title, m.publisher, m.ISSN, m.pages
                  FROM Item i JOIN Magazine m ON i.itemID = m.itemID
                  WHERE i.type = 'Magazine' AND i.available = 1
                  AND """),
               '3': ("Journal", ("Title", "Author", "Publisher", "DOI"),
                     """
                  SELECT i.itemID, i.title, j.author, j.publisher, j.doi, j.pages
                  FROM Item i JOIN Journal j ON i.itemID = j.itemID
                  WHERE i.type = 'Journal' AND i.available = 1
                  AND """),
               '4': ("CD", ("Title", "Author", "Publisher"),
                     """
                  SELECT i.itemID, i.title, c.author, c.publisher, c.time
                  FROM Item i JOIN CD c ON i.itemID = c.itemID
                  WHERE i.type = 'CD' AND i.available = 1
                  AND """),
               '5': ("Record", ("Title", "Author", "Publisher"),
                     """
                  SELECT i.itemID, i.title, r.author, r.publisher, r.time
                  FROM Item i JOIN Record r ON i.itemID = r.itemID
                  WHERE i.type = 'Record' AND i.available = 1
                  AND """)}

    type = input("What type of item are you donating: ")
    title = input("What is the title of the item you are donating: ")
    date = datetime.today()
    fine = 20

    query = """
        SELECT MAX(itemID) FROM Item;
    """
    cur.execute(query)
    maxID = cur.fetchone()
    itemID = int(maxID) + 1

    return


"""
:TODO
def findEvent():
    # search by:
    # name
    # date

    # returns:
    # *
"""


def registerEvent():
    # eventID
    # attendeeID
    # insert into attends

    eventID = int(input("Enter eventID: "))
    attendeeID = int(input("Enter your attendeeID: "))

    query = """
        INSERT INTO Attends VALUES
        (?, ?)
    """
    cur.execute(query, (attendeeID, eventID))
    conn.commit()

    return


"""
def volunteer():
    # needs:
    # PID - same as donate
    # name
    # email
    # phone
    # position = volunteer
    # insert into personnel


def findLibrarian():
    # all info (except PID, position)
    # WHERE position = 'Librarian'
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
