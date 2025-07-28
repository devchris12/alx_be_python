# robust_division_calculator.py

import sys

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats to handle non-numeric values
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
