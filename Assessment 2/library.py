# Stores book details and whether the book is available.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_book(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")


# Stores a member and the books they borrow.
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def display_member(self):
        print(f"Member: {self.name}")
        print("Borrowed Books:")

        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title}")


# Manages books, members, borrowing, and returns.
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def borrow_book(self, book, member):
        if book not in self.books:
            print("Book is not in the library.")
        elif member not in self.members:
            print("Member is not registered.")
        elif book.available:
            book.available = False
            member.borrow_book(book)
            print(f"'{book.title}' has been borrowed by {member.name}.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.return_book(book)
            print(f"'{book.title}' has been returned.")
        else:
            print(f"{member.name} did not borrow this book.")

    def display_books(self):
        print("\n--- Library Books ---")

        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                book.display_book()
                print()


# Create a library
library = Library()

# Create books
book1 = Book("Python Programming", "John Smith")
book2 = Book("Introduction to Networking", "David Brown")
book3 = Book("Object-Oriented Programming", "Sarah Jones")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create members
member1 = Member("Ali")
member2 = Member("Maria")

# Add members
library.add_member(member1)
library.add_member(member2)

# Display books
library.display_books()

# Borrow a book
print("--- Borrow Book ---")
library.borrow_book(book1, member1)

# Display books after borrowing
library.display_books()

# Display member information
print("--- Member Information ---")
member1.display_member()

# Return the book
print("\n--- Return Book ---")
library.return_book(book1, member1)

# Display books after returning
library.display_books()

# Display member information again
print("--- Member Information ---")
member1.display_member()