import os
import sys
import unittest
import io
import inspect

# ==============================
# Library System Implementation
# ==============================

# Base Class
class Book:
    def __init__(self, title: str, author: str):
        self.title = str(title)
        self.author = str(author)

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)


# ==============================
# Main Program
# ==============================
def main():
    my_library = Library()
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


# ==============================
# Test Cases
# ==============================
class TestLibrarySystem(unittest.TestCase):

    def test_file_exists_and_not_empty(self):
        file_path = os.path.abspath(__file__)
        self.assertTrue(os.path.exists(file_path), "File does not exist")
        self.assertTrue(os.path.getsize(file_path) > 0, "File is empty")

    def test_class_implementations(self):
        self.assertTrue(inspect.isclass(Book), "Book class not implemented")
        self.assertTrue(inspect.isclass(EBook), "EBook class not implemented")
        self.assertTrue(inspect.isclass(PrintBook), "PrintBook class not implemented")
        self.assertTrue(inspect.isclass(Library), "Library class not implemented")

    def test_inheritance(self):
        self.assertTrue(issubclass(EBook, Book), "EBook does not inherit from Book")
        self.assertTrue(issubclass(PrintBook, Book), "PrintBook does not inherit from Book")

    def test_library_methods(self):
        lib = Library()
        self.assertTrue(hasattr(lib, 'add_book'), "Library missing add_book method")
        self.assertTrue(hasattr(lib, 'list_books'), "Library missing list_books method")

    def test_correct_output(self):
        captured = io.StringIO()
        sys.stdout = captured
        main()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Book: Pride and Prejudice by Jane Austen\n"
            "EBook: Snow Crash by Neal Stephenson, File Size: 500KB\n"
            "PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234\n"
        )
        self.assertEqual(captured.getvalue(), expected_output)


# Run tests when executed directly
if __name__ == "__main__":
    main()  # Run main function
    print("\n--- Running Tests ---")
    unittest.main(argv=[''], exit=False)
