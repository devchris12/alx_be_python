# Function to display the menu options
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function that handles the shopping list functionality
def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")

        if choice == '1':  # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':  # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':  # View the current shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break

        else:  # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
