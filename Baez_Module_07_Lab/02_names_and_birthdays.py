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
            choice = int(input("Enter your choice: ")) # Get the user's menu choice
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
    # str: Name to look up
    name: str = input("Enter a name to look up: ")

    # Check if name exists in dictionary
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.") # Display the birthday
    else:
        print(f"Sorry, {name} is not found in the dictionary.") # Display an error message


# Function: Add a new birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
def add(birthdays: dict[str, str]) -> None:
    # str: Name to add
    name: str = input("Enter a name: ")

    # Check if name already exists
    if name in birthdays:
        print(f"{name} already exists in the dictionary.") # Display a message that the name already exists
        print(f"Current birthday: {birthdays[name]}") # Display the current birthday
        response = input("Do you want to change it? (yes/no): ").lower() # Get the user's response
        if response == 'yes':
            birthday = input("Enter the birthday: ") # Get the new birthday
            birthdays[name] = birthday # Update the birthday in the dictionary
            print(f"{name}'s birthday has been updated to {birthday}.") # Display the updated birthday
    else:
        birthday = input("Enter the birthday: ") # Get the new birthday
        birthdays[name] = birthday  # Add new entry to dictionary
        print(f"{name}'s birthday ({birthday}) has been added to the dictionary.") # Display the new birthday


# Function: Change a birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values the types is optional
def change(birthdays: dict[str, str]) -> None:
    # str: Name to change
    name: str = input("Enter a name: ")

    # Check if name exists in dictionary
    if name in birthdays:
        print(f"Current birthday for {name}: {birthdays[name]}") # Display the current birthday
        new_birthday = input("Enter the new birthday: ")
        birthdays[name] = new_birthday  # Update birthday in dictionary
        print(f"{name}'s birthday has been changed to {new_birthday}.") # Display the updated birthday
    else:
        print(f"Sorry, {name} is not found in the dictionary.") # Display an error message


# Function: Delete a birthday
# dict[str, str]: Dictionary with names as keys and birthdays as values
def delete(birthdays: dict[str, str]) -> None:
    # str: Name to delete
    name: str = input("Enter a name: ")

    # Check if name exists in dictionary
    if name in birthdays:
        print(f"{name}'s birthday ({birthdays[name]}) will be deleted.") # Display the birthday to be deleted
        response = input("Are you sure? (yes/no): ").lower()
        if response == 'yes':
            del birthdays[name]  # Delete entry from dictionary
            print(f"{name}'s birthday has been deleted from the dictionary.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.") # Display an error message


# Function: Main function to run the names and birthdays program
# None: No return value
def main_birthdays() -> None:
    print("=" * 60)
    print("EXERCISE 2: Names and Birthdays Program")
    print("=" * 60)

    # Initialize empty dictionary
    birthdays = {} # Initialize an empty dictionary

    # Loop (while True): Continuously display menu until user chooses to quit
    while True:
        choice = get_menu_choice() # Get the user's menu choice

        # Process user's choice
        if choice == LOOK_UP:
            look_up(birthdays) # Look up a birthday
        elif choice == ADD:
            add(birthdays) # Add a new birthday
        elif choice == CHANGE:
            change(birthdays) # Change a birthday
        elif choice == DELETE:
            delete(birthdays) # Delete a birthday
        elif choice == QUIT:
            print("\nThank you for using the Birthday Dictionary program!")
            print(f"Total entries in dictionary: {len(birthdays)}")
            if birthdays:
                print("\nFinal dictionary contents:")
                for name, birthday in birthdays.items(): # Loop (for): Iterate through each name and birthday in the dictionary and display them
                    print(f"  {name}: {birthday}")
            break  # Exit the loop


# Run the main function to run the names and birthdays program
# None: No return value
main_birthdays()

print()
print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)
