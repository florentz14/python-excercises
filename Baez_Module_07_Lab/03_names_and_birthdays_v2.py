# -------------------------------------------------
# File Name: 03_names_and_birthdays_v2.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 07 Lab
# Description: Names and Birthdays Program (Version 2). Same as 02_names_and_birthdays
#              but displays the final dictionary contents.
# -------------------------------------------------

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Function: Print the birthdays dictionary in a tabular format
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
# str: Title of the dictionary
# None: No return value
def print_birthdays_table(birthdays: dict[str, str], title: str = "Current Dictionary") -> None:
    """Display the birthdays dictionary in a tabular format."""
    print(f"\n--- {title} ---")
    if not birthdays:
        print("  (empty)")
        return
    # Column widths: The width of the name and birthday columns
    name_width = max(len("Name"), max(len(n) for n in birthdays.keys()), 10)
    bday_width = max(len("Birthday"), max(len(b) for b in birthdays.values()), 12)
    # Header: The header of the table
    print(f"  {'Name':<{name_width}} | {'Birthday':<{bday_width}}")
    print("  " + "-" * (name_width + bday_width + 3))
    # Rows: The rows of the table
    for name, birthday in birthdays.items():
        print(f"  {name:<{name_width}} | {birthday:<{bday_width}}")
    print()


# Function: Get the user's menu choice
# int: User's menu choice
def get_menu_choice() -> int:
    print("\n" + "=" * 60)
    print("BIRTHDAY MENU")
    print("=" * 60)
    print(f"{LOOK_UP}. Look up a birthday")
    print(f"{ADD}. Add a new birthday")
    print(f"{CHANGE}. Change a birthday")
    print(f"{DELETE}. Delete a birthday")
    print(f"{QUIT}. Quit the program")
    print("=" * 60)

    # Loop (while True): Continuously prompts until valid input is provided
    # Try-except block: Handles exceptions that may occur during input conversion
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [LOOK_UP, ADD, CHANGE, DELETE, QUIT]: # Check if the choice is valid
                return choice
            else:
                print(f"Error: Please enter a number between {LOOK_UP} and {QUIT}.") # Display an error message
        except ValueError:
            # Handle invalid numeric input (e.g., non-numeric characters)
            print("Error: Please enter a valid integer.")


# Function: Look up a birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
def look_up(birthdays: dict[str, str]) -> None:
    print_birthdays_table(birthdays, "Before Look Up") # Display the dictionary before the look up operation
    name = input("Enter a name to look up: ").strip() # Get the name to look up

    if name in birthdays:
        print(f"\n>>> {name}'s birthday is {birthdays[name]}.") # Display the birthday
    else:
        print(f"\n>>> Sorry, {name} is not found in the dictionary.")
    print_birthdays_table(birthdays, "After Look Up")

# Function: Add a new birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
def add(birthdays: dict[str, str]) -> None:
    print_birthdays_table(birthdays, "Before Add") # Display the dictionary before the add operation
    name = input("Enter a name: ").strip()

    if name in birthdays:
        print(f"\n>>> {name} already exists in the dictionary.")
        print(f"    Current birthday: {birthdays[name]}")
        response = input("Do you want to change it? (yes/no): ").lower().strip() # Get the user's response
        if response == 'yes':
            birthday = input("Enter the birthday: ").strip() # Get the new birthday
            birthdays[name] = birthday # Update the birthday in the dictionary  
            print(f"\n>>> {name}'s birthday has been updated to {birthday}.") # Display the updated birthday
        else:
            print(">>> No changes made.") # Display a message that no changes were made
    else:
        birthday = input("Enter the birthday: ").strip() # Get the new birthday
        birthdays[name] = birthday # Add the new birthday to the dictionary
        print(f"\n>>> {name}'s birthday ({birthday}) has been added.") # Display the new birthday
    print_birthdays_table(birthdays, "After Add")


# Function: Change a birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
def change(birthdays: dict[str, str]) -> None:
    print_birthdays_table(birthdays, "Before Change") # Display the dictionary before the change operation
    name = input("Enter a name: ").strip() # Get the name to change

    if name in birthdays:
        print(f"\n>>> Current birthday for {name}: {birthdays[name]}")
        new_birthday = input("Enter the new birthday: ").strip() # Get the new birthday
        birthdays[name] = new_birthday # Update the birthday in the dictionary
        print(f">>> {name}'s birthday has been changed to {new_birthday}.") # Display the updated birthday
    else:
        print(f"\n>>> Sorry, {name} is not found in the dictionary.") # Display an error message
    print_birthdays_table(birthdays, "After Change")


# Function: Delete a birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
def delete(birthdays: dict[str, str]) -> None:
    print_birthdays_table(birthdays, "Before Delete") # Display the dictionary before the delete operation
    print_birthdays_table(birthdays, "Before Delete")
    name = input("Enter a name: ").strip()

    if name in birthdays:
        print(f"\n>>> {name}'s birthday ({birthdays[name]}) will be deleted.") # Display the birthday to be deleted
        response = input("Are you sure? (yes/no): ").lower().strip() # Get the user's response
        if response == 'yes':
            del birthdays[name] # Delete the birthday from the dictionary
            print(f">>> {name}'s birthday has been deleted.") # Display a message that the birthday has been deleted
        else:
            print(">>> Deletion cancelled.") # Display a message that the deletion was cancelled
    else:
        print(f"\n>>> Sorry, {name} is not found in the dictionary.")
    print_birthdays_table(birthdays, "After Delete")


# Function: Main function to run the names and birthdays program
# None: No return value
def main_birthdays() -> None:
    print("=" * 60)
    print("EXERCISE 3: Names and Birthdays Program (Version 2)")
    print("=" * 60)

    birthdays: dict[str, str] = {}

    while True:
        choice = get_menu_choice() # Get the user's menu choice

        if choice == LOOK_UP:
            look_up(birthdays) # Look up a birthday
        elif choice == ADD: # Add a new birthday
            add(birthdays) # Add a new birthday
        elif choice == CHANGE:
            change(birthdays) # Change a birthday
        elif choice == DELETE:
            delete(birthdays) # Delete a birthday
        elif choice == QUIT:
            print("\nThank you for using the Birthday Dictionary program!")
            print(f"Total entries in dictionary: {len(birthdays)}")
            print_birthdays_table(birthdays, "Final Dictionary Contents")
            break

# Main function to run the program
# None: No return value
main_birthdays()

print()
print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)