# -------------------------------------------------
# File Name: 15_list_tuples_to_dict.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Convert a List of Tuples to a Dictionary.
#              The dict() constructor accepts an iterable of
#              (key, value) pairs, making conversion from a
#              list of 2-element tuples straightforward.
# -------------------------------------------------

# Example 15: Convert list of tuples to dictionary
print("Example 15: Convert list of tuples to dictionary")
print("-" * 40)

# Each tuple is a (key, value) pair
pairs = [("name", "Alice"), ("age", 30), ("city", "Boston")]

# dict() converts the list of tuples into a dictionary
person_dict = dict(pairs)

print("List of tuples:", pairs)
print("Converted to dictionary:", person_dict)
