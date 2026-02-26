# dictionaries simple loop
# -------------------------------------------------
# File Name: 27_simple_loop.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Simple Loop Through a Dictionary.
# -------------------------------------------------

# Example 1: Simple Loop Through a Dictionary
print("Example 1: Simple Loop Through a Dictionary")
print("-" * 40)

# create a dictionary of grades
grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92, "Eve": 88}

# loop through the dictionary of grades
for name, grade in grades.items():
    print(f"{name} has a grade of {grade}")
print("-" * 40)

'''
Why do we use dictionaries?
We use dictionaries because:
- we can store data in a key-value pair
- we can access the data by the key
- we can iterate over the dictionary
- we can add new data to the dictionary
- we can remove data from the dictionary
- we can update data in the dictionary
- we can check if a key exists in the dictionary
- we can get the value of a key in the dictionary
- we can get the keys of the dictionary
- we can get the values of the dictionary
'''