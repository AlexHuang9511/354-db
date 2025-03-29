import sqlite3


def findItem():


def borrowItem():


def returnItem():


def donateItem():


def findEvent():


def registerEvent():


def volunteer():


def findLibrarian():


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
