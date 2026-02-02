# -------------------------------------------------
# File Name: 02_names_and_birthdays.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 07 Lab
# Description: Names and Birthdays Program. Keeps friends' names and birthdays
#              in a dictionary (name as key, birthday as value). Menu options:
#              1. Look up a birthday
#              2. Add a new birthday
#              3. Change a birthday
#              4. Delete a birthday
#              5. Quit the program
#              Starts with an empty dictionary; add entries with option 2, then
#              look up (1), change (3), delete (4), or quit (5). Functions:
#              main_birthdays, get_menu_choice, look_up, add, change, delete.
# -------------------------------------------------

# =============================================================================
# EXERCISE 2: Names and Birthdays Program
# =============================================================================

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def get_menu_choice() -> int:
    """
    Display the menu and get the user's choice.

    Returns:
        int: User's menu choice
    """
    print("\n" + "=" * 60)
    print("BIRTHDAY MENU")
    print("=" * 60)
    print(f"{LOOK_UP}. Look up a birthday")
    print(f"{ADD}. Add a new birthday")
    print(f"{CHANGE}. Change a birthday")
    print(f"{DELETE}. Delete a birthday")
    print(f"{QUIT}. Quit the program")
    print("=" * 60)

    # Get user's choice
    # Try-except block: Handles exceptions that may occur during input conversion
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [LOOK_UP, ADD, CHANGE, DELETE, QUIT]:
                return choice
            else:
                print(f"Error: Please enter a number between {LOOK_UP} and {QUIT}.")
        except ValueError:
            # Handle invalid numeric input (e.g., non-numeric characters)
            print("Error: Please enter a valid integer.")


def look_up(birthdays: dict[str, str]) -> None:
    """
    Look up a birthday in the dictionary.

    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name to look up: ")

    # Check if name exists in dictionary
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.")


def add(birthdays: dict[str, str]) -> None:
    """
    Add a new birthday to the dictionary.

    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name: ")

    # Check if name already exists
    if name in birthdays:
        print(f"{name} already exists in the dictionary.")
        print(f"Current birthday: {birthdays[name]}")
        response = input("Do you want to change it? (yes/no): ").lower()
        if response == 'yes':
            birthday = input("Enter the birthday: ")
            birthdays[name] = birthday
            print(f"{name}'s birthday has been updated to {birthday}.")
    else:
        birthday = input("Enter the birthday: ")
        birthdays[name] = birthday  # Add new entry to dictionary
        print(f"{name}'s birthday ({birthday}) has been added to the dictionary.")


def change(birthdays: dict[str, str]) -> None:
    """
    Change an existing birthday in the dictionary.

    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name: ")

    # Check if name exists in dictionary
    if name in birthdays:
        print(f"Current birthday for {name}: {birthdays[name]}")
        new_birthday = input("Enter the new birthday: ")
        birthdays[name] = new_birthday  # Update birthday in dictionary
        print(f"{name}'s birthday has been changed to {new_birthday}.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.")


def delete(birthdays: dict[str, str]) -> None:
    """
    Delete a birthday from the dictionary.

    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name: ")

    # Check if name exists in dictionary
    if name in birthdays:
        print(f"{name}'s birthday ({birthdays[name]}) will be deleted.")
        response = input("Are you sure? (yes/no): ").lower()
        if response == 'yes':
            del birthdays[name]  # Delete entry from dictionary
            print(f"{name}'s birthday has been deleted from the dictionary.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.")


def main_birthdays() -> None:
    """
    Main function to run the names and birthdays program.
    """
    print("=" * 60)
    print("EXERCISE 2: Names and Birthdays Program")
    print("=" * 60)

    # Initialize empty dictionary
    birthdays = {}

    # Loop (while True): Continuously display menu until user chooses to quit
    while True:
        choice = get_menu_choice()

        # Process user's choice
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
        elif choice == QUIT:
            print("\nThank you for using the Birthday Dictionary program!")
            print(f"Total entries in dictionary: {len(birthdays)}")
            if birthdays:
                print("\nFinal dictionary contents:")
                for name, birthday in birthdays.items():
                    print(f"  {name}: {birthday}")
            break  # Exit the loop


# Run Exercise 2
main_birthdays()

print()
print("=" * 60)
print("All exercises completed!")
print("=" * 60)

# =============================================================================
# CITATIONS
# =============================================================================
print("\nCitations:")
print("1. Dictionary Operations in Python:")
print("   - Dictionary creation, access, update, and deletion")
print("   - Dictionary methods: keys(), values(), items()")
print("   Source: Python Documentation - Dictionaries")
print("   https://docs.python.org/3/tutorial/datastructures.html#dictionaries")
print()
print("2. Menu-Driven Programs:")
print("   - Design pattern for interactive programs with multiple options")
print("   Source: Common programming design pattern")
