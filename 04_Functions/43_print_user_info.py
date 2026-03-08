# -------------------------------------------------
# File Name: 43_print_user_info.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Print user information (name, email).
# -------------------------------------------------

def print_user_info(first_name, email):
    """
    Prints user information on a single line.
    
    Args:
        first_name: The user's first name
        email: The user's email address
    """
    print(f"Name: {first_name}, Email: {email}")


# Example usage
if __name__ == "__main__":
    print("=== User Info Demo ===\n")
    
    print_user_info("John", "john@example.com")
    print()
    print_user_info("Maria", "maria@gmail.com")
