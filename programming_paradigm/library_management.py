class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    return f"Successfully checked out '{title}'."
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' is not available in the library."

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return f"Successfully returned '{title}'."
                else:
                    return f"Error returning '{title}'."
        return f"'{title}' is not checked out or not available in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

