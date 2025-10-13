# Multiplication Table Generator
# This program generates and prints a multiplication table for a given number

# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
