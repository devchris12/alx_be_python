import os
import math
import sys
import inspect
import unittest
import io

# ==============================
# Polymorphism Demo Implementation
# ==============================
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# ==============================
# Main Program
# ==============================
def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
    for shape in shapes:
        area_val = shape.area()
        # Remove .0 if integer
        if area_val == int(area_val):
            area_val = int(area_val)
        print(f"The area of the {shape.__class__.__name__} is: {area_val}")

# ==============================
# Tests
# ==============================
class TestPolymorphismDemo(unittest.TestCase):

    def test_file_exists_and_not_empty(self):
        """Check if file exists and is not empty"""
        file_path = os.path.abspath(__file__)
        self.assertTrue(os.path.exists(file_path), "File does not exist")
        self.assertTrue(os.path.getsize(file_path) > 0, "File is empty")

    def test_math_import(self):
        """Check if math module is imported"""
        self.assertIn("math", sys.modules, "math module not imported")

    def test_class_implementation_and_initialization(self):
        """Check classes exist and can be instantiated"""
        self.assertTrue(inspect.isclass(Shape), "Shape class missing")
        self.assertTrue(inspect.isclass(Rectangle), "Rectangle class missing")
        self.assertTrue(inspect.isclass(Circle), "Circle class missing")
        self.assertIsInstance(Rectangle(10, 5), Rectangle)
        self.assertIsInstance(Circle(7), Circle)

    def test_methods_in_circle(self):
        """Check required methods in Circle"""
        self.assertTrue(hasattr(Circle, '__init__'), "Circle missing __init__")
        self.assertTrue(hasattr(Circle, 'area'), "Circle missing area method")

    def test_methods_in_rectangle(self):
        """Check required methods in Rectangle"""
        self.assertTrue(hasattr(Rectangle, '__init__'), "Rectangle missing __init__")
        self.assertTrue(hasattr(Rectangle, 'area'), "Rectangle missing area method")

    def test_correct_output(self):
        """Check if program output matches expected"""
        captured = io.StringIO()
        sys.stdout = captured
        main()
        sys.stdout = sys.__stdout__

        expected_output = (
            "The area of the Rectangle is: 50\n"
            "The area of the Circle is: 153.93804002589985\n"
        )
        self.assertEqual(captured.getvalue(), expected_output)

# ==============================
# Run
# ==============================
if __name__ == "__main__":
    main()
    print("\n--- Running Tests ---")
    unittest.main(argv=[''], exit=False)
