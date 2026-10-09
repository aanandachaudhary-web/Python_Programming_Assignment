books = [
    {"title": "Python Basics", "author": "John Smith",
     "available": True},
    {"title": "Java Programming", "author": "James Gosling",
     "available": True},
    {"title": "Web Development", "author": "David Miller",
     "available": True},
    {"title": "Database Systems", "author": "Thomas Connolly",
     "available": True},
    {"title": "Computer Networks", "author": "Andrew Tanenbaum",
     "available": True}
]


def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book

    raise LookupError("Book does not exist.")


def borrow_book(title):
    book = search_book(title)

    if not book["available"]:
        print("Sorry, this book is already borrowed.")
        return

    book["available"] = False
    print("You borrowed:", book["title"])


def return_book(title):
    book = search_book(title)

    if book["available"]:
        print("This book has not been borrowed.")
        return

    book["available"] = True
    print("You returned:", book["title"])


def display_available_books():
    print("\n--- Available Books ---")

    for book in books:
        if book["available"]:
            print(book["title"], "-", book["author"])


while True:
    print("\n1. Search Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            title = input("Enter book title: ")
            book = search_book(title)

            status = "Available" if book["available"] else "Borrowed"
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", status)

        elif choice == "2":
            title = input("Enter book title to borrow: ")
            borrow_book(title)

        elif choice == "3":
            title = input("Enter book title to return: ")
            return_book(title)

        elif choice == "4":
            display_available_books()

        elif choice == "5":
            print("Thank you for using the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

    except LookupError as error:
        print("Error:", error)