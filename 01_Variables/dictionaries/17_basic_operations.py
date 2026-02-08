# -------------------------------------------------
# File Name: 17_basic_operations.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Basic Dictionary Operations.
#              Demonstrates creating dictionaries, accessing values
#              by key and with get(), adding/modifying entries,
#              removing items with pop()/del, and checking key
#              existence using the 'in' operator.
# -------------------------------------------------

"""
Exercise 1: Basic Dictionary Operations
This exercise demonstrates fundamental dictionary creation, access, and modification.
Dictionaries store key-value pairs and provide fast lookups.
"""

def main():
    print("Exercise 1: Basic Dictionary Operations")
    print("=" * 60)
    
    # Creating a dictionary with student information
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "student_id": "CS2024001"
    }
    
    print("1. Creating and Displaying a Dictionary:")
    print("-" * 60)
    print(f"Student Information: {student}")
    print()
    
    # Accessing values by key
    print("2. Accessing Dictionary Values:")
    print("-" * 60)
    print(f"Name: {student['name']}")
    print(f"Major: {student['major']}")
    print(f"GPA: {student['gpa']}")
    print()
    
    # Using get() method (safer - returns None if key doesn't exist)
    # get() prevents KeyError exceptions when accessing non-existent keys
    print("3. Using get() Method (Safer Access):")
    print("-" * 60)
    print(f"Age: {student.get('age')}")
    # get() with default value: returns 'Not provided' if 'email' key doesn't exist
    print(f"Email: {student.get('email', 'Not provided')}")
    print()
    
    # Adding new key-value pairs
    print("4. Adding New Entries:")
    print("-" * 60)
    student["email"] = "alice.johnson@university.edu"
    student["year"] = "Junior"
    print(f"After adding email and year: {student}")
    print()
    
    # Modifying existing values
    print("5. Modifying Existing Values:")
    print("-" * 60)
    print(f"Old GPA: {student['gpa']}")
    student["gpa"] = 3.9
    print(f"New GPA: {student['gpa']}")
    print()
    
    # Removing items
    # pop() removes a key and returns its value, or raises KeyError if key doesn't exist
    print("6. Removing Dictionary Items:")
    print("-" * 60)
    removed_value = student.pop("student_id")
    print(f"Removed student_id: {removed_value}")
    print(f"Dictionary after removal: {student}")
    # Alternative: del student["student_id"] (doesn't return the value)
    print()
    
    # Checking if key exists
    # The 'in' operator checks for key existence (not value existence)
    print("7. Checking Key Existence:")
    print("-" * 60)
    print(f"Is 'name' in dictionary? {'name' in student}")
    print(f"Is 'phone' in dictionary? {'phone' in student}")
    
    print("\n" + "=" * 60)
    print("Summary:")
    print("  - Dictionaries use {key: value} syntax")
    print("  - Access values with dict[key] or dict.get(key)")
    print("  - Add/modify with dict[key] = value")
    print("  - Remove with pop() or del")
    print("  - Check existence with 'key in dict'")


if __name__ == "__main__":
    main()
