# -------------------------------------------------
# File Name: 15_hello_world_greet.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Basic print output, separators, and a simple
# -------------------------------------------------

print("Hello, World!")
print("*" * 30)  # Print a decorative separator line
print("This is a sample Python application.")

# Define a greeting function that takes a name parameter
def greet(name):
    """Return a personalized greeting message."""
    return f"Hello, {name}!"

# Call the greet function and display the result
print(greet("Alice"))
print("*" * 30)  # Print another decorative separator line