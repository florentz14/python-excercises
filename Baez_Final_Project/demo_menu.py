# menu2.py - Menu with while choice != 4
# Florentino & LaAngel
# course: ITSE-1002 Python Programming
# professor: Mauricio Quiroga
# description: Menu with while choice != 4


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 50)
    print("MAIN MENU")
    print("=" * 50)
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Show me your Name")
    print("4. Quit")

def say_hello():
    """Option 1: Say Hello."""
    print("Hello! Welcome to Python for DS")

def add_two_numbers():
    """Option 2: Add two numbers."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print("The sum is:", total)

def show_name():
    """Option 3: Show your name."""
    name = input("Enter your name: ")
    print("Your name is:", name)

def quit_menu():
    """Option 4: Quit."""
    print("Goodbye ! ! !")

def main():
    """Main function."""
    choice = 0
    # Loop: Print the menu until the user chooses to quit
    while choice != 4:
        print_menu() # Print the menu
        
        # Get the user's choice
        choice = int(input("Enter your choice (1-4): ")) 
        
        # Decisions
        if choice == 1:
            say_hello()
        elif choice == 2:
            add_two_numbers()
        elif choice == 3:
            show_name()
        elif choice == 4:
            quit_menu() 
        else:
            print("Invalid choice. Please select 1 to 4")


# Call the main function
main()
print("End of program! ! !")