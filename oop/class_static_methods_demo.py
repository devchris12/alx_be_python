import os
import sys
import inspect
import unittest
import io

# ==============================
# Calculator Implementation
# ==============================
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# ==============================
# Main Program
# ==============================
def main():
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


# ==============================
# Tests
# ==============================
class TestCalculator(unittest.TestCase):

    def test_file_exists_and_not_empty(self):
        """Check file exists and is not empty"""
        file_path = os.path.abspath(__file__)
        self.assertTrue(os.path.exists(file_path), "File does not exist")
        self.assertTrue(os.path.getsize(file_path) > 0, "File is empty")

    def test_class_implementation(self):
        """Check if Calculator class exists"""
        self.assertTrue(inspect.isclass(Calculator), "Calculator class is not implemented")

    def test_static_method_implementation(self):
        """Check if add is a static method"""
        self.assertTrue(hasattr(Calculator, 'add'), "add method missing")
        self.assertIsInstance(Calculator.__dict__['add'], staticmethod, "add is not a staticmethod")

    def test_class_method_implementation(self):
        """Check if multiply is a class method"""
        self.assertTrue(hasattr(Calculator, 'multiply'), "multiply method missing")
        self.assertIsInstance(Calculator.__dict__['multiply'], classmethod, "multiply is not a classmethod")

    def test_correct_output(self):
        """Check if output is correct"""
        captured = io.StringIO()
        sys.stdout = captured
        main()
        sys.stdout = sys.__stdout__

        expected_output = (
            "The sum is: 15\n"
            "Calculation type: Arithmetic Operations\n"
            "The product is: 50\n"
        )
        self.assertEqual(captured.getvalue(), expected_output)


# Run program and tests when executed directly
if __name__ == "__main__":
    main()
    print("\n--- Running Tests ---")
    unittest.main(argv=[''], exit=False)
