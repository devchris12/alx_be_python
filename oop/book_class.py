import os
import sys
import io
import unittest
import inspect
import importlib.util

# === Define the Book class in this same file for testing ===
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year})"


class TestBookClass(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "George Orwell", 1949)

    def test_file_exists_and_not_empty(self):
        """Check if this script file exists and is not empty."""
        file_path = os.path.abspath(__file__)
        self.assertTrue(os.path.exists(file_path), "File does not exist.")
        self.assertTrue(os.path.getsize(file_path) > 0, "File is empty.")

    def test_class_exists(self):
        """Check if the Book class exists."""
        self.assertTrue('Book' in globals(), "Book class is not defined.")
        self.assertTrue(inspect.isclass(Book), "Book is not a class.")

    def test_python_library_import(self):
        """Check if standard libraries can be imported successfully."""
        try:
            import os, sys, io
        except ImportError as e:
            self.fail(f"Library import failed: {e}")

    def test_magic_methods_exist(self):
        """Check if required magic methods are implemented."""
        for method in ['__init__', '__del__', '__str__', '__repr__']:
            self.assertTrue(hasattr(Book, method), f"{method} not implemented.")

    def test_str_output(self):
        """Check __str__ output."""
        self.assertEqual(str(self.book), "1984 by George Orwell, published in 1949")

    def test_repr_output(self):
        """Check __repr__ output."""
        self.assertEqual(repr(self.book), "Book('1984', 'George Orwell', 1949)")

    def test_del_output(self):
        """Check __del__ output."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        b = Book("Temp", "Author", 2024)
        del b
        sys.stdout = sys.__stdout__
        self.assertIn("Deleting Temp", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
