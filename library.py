import sqlite3
conn = sqlite3.connect('library.db')
conn.execute("PRAGMA foreign_keys = ON;")
cur = conn.cursor()


def findItem():
    def findBook():
        print("find book")
        while not doneSearch:
            print("What would you like to search by?")
            print("1 - Author")
            print("2 - Publisher")
            print("3 - ISBN")
            print("0 - Go Back")
            search = int((input("Enter a number: ")))

            if search == 0:
                return
            elif search == 1:
                author = str(input("Enter name of author: "))
                print("author: ", author)

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

            elif search == 2:
                publisher = input("Enter name of publisher: ")
            elif search == 3:
                isbn = input("Enter name of ISBN: ")

    shoudClose = False

    while not shoudClose:
        print("What type of item would you like to search for?")
        print("1 - Book")
        print("2 - Magazine")
        print("3 - Journal")
        print("4 - CD")
        print("5 - Record")
        print("0 - Go Back")
        type = int(input("Enter a number: "))

        if type == 0:
            shoudClose = True

        doneSearch = False

        if type == 1:
            findBook()
        elif type == 2:
            print("find Magazine")
        elif type == 3:
            print("find Journal")
        elif type == 4:
            print("find CD")
        elif type == 5:
            print("find Record")


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

        choice = int(
            input("Enter the number corresponding you your request: "))

        if choice == 0:
            shouldExit = True
            conn.close()
        elif choice == 1:
            findItem()
        elif choice == 2:
            borrowItem()
        elif choice == 3:
            returnItem()
        elif choice == 4:
            donateItem()
        elif choice == 5:
            findEvent()
        elif choice == 6:
            registerEvent()
        elif choice == 7:
            volunteer()
        elif choice == 8:
            findLibrarian()

        print(choice)
    return 0


if __name__ == "__main__":
    library()
