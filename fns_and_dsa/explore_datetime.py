from datetime import datetime, timedelta

# Part 1: Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Format the current date and time in "YYYY-MM-DD HH:MM:SS"
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print(f"Current date and time: {current_date}")

# Part 2: Function to calculate the future date after adding specified days
def calculate_future_date():
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_datetime + timedelta(days=days_to_add)
    
    # Format the future date as "YYYY-MM-DD"
    future_date_str = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future date: {future_date_str}")

# Main function to run both parts
def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
