# -------------------------------------------------
# File Name: 28_simple_nested.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Simple Nested Dictionary.
# -------------------------------------------------

# Example 1: Simple Nested Dictionary
print("Example 1: Simple Nested Dictionary")
print("-" * 40)

# create a nested dictionary
#nested_dict = {"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "Anytown", "state": "CA"}} 

# create a nested dictionary of dictionaries
nested_dict = {
    "John": {
        "age": 30,
        "grade": "97",
        "address": {"street": "123 Main St", "city": "Anytown", "state": "CA"}
    },
    "Margarita": {
        "age": 28,
        "grade": "88",
        "address": {"street": "456 Oak St", "city": "Anytown", "state": "NY"}
    },
    "Alice": {
        "age": 25,
        "grade": "92",
        "address": {"street": "789 Pine St", "city": "Anytown", "state": "TX"}
    },
    "Dorian": {
        "age": 35,
        "grade": "78",
        "address": {"street": "101 Maple St", "city": "Anytown", "state": "FL"}
    }
}
print("Nested Dictionary:", nested_dict)
print("-" * 40)

# access the nested dictionary
print("Access the nested dictionary")
print("-" * 40)
print("Street:", nested_dict["John"]["address"]["street"])
print("City:", nested_dict["John"]["address"]["city"])
print("State:", nested_dict["John"]["address"]["state"])
print("-" * 40)

# display John' state
print("John's state:", nested_dict["John"]["address"]["state"])
print("-" * 40)

# display John's age
print("John's age:", nested_dict["John"]["age"])
print("-" * 40)


# add a new key-value pair to the nested dictionary