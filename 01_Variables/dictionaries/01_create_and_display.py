# -------------------------------------------------
# File Name: 01_create_and_display.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Create and Display a Dictionary.
#              Shows how to create a dictionary with key-value
#              pairs using curly braces {}, and how to check
#              its length with len() and type with type().
# -------------------------------------------------

# Example 1: Create and display a dictionary
print("Example 1: Create and display a dictionary")
print("-" * 40)

# Create a dictionary with string keys and mixed-type values
student = {"name": "John", "age": 20, "grade": "A"}

print("Dictionary:", student)
print("Length:", len(student))      # Number of key-value pairs
print("Type:", type(student))       # <class 'dict'>
