# ---------------------------------------------------------------------------
# Tuplas - 01: Python Tuples (Crear y Propiedades)
# ---------------------------------------------------------------------------
# Description: A tuple is an ordered, immutable collection of elements.
#              Defined with parentheses (). Elements cannot be changed,
#              added, or removed after creation. Tuples allow duplicates.
# Syntax:      my_tuple = (item1, item2, item3)
# ---------------------------------------------------------------------------

# --- Create a tuple ---
fruits = ("apple", "banana", "cherry", "pineapple", "grape")
print("Fruits tuple:", fruits)
# Output: ('apple', 'banana', 'cherry', 'pineapple', 'grape')

# --- Tuples allow duplicate values ---
numbers = (1, 5, 3, 5, 7, 5)
print("With duplicates:", numbers)
# Output: (1, 5, 3, 5, 7, 5)

# --- Tuple length with len() ---
print("Length:", len(fruits))
# Output: 5

# --- Check data type with type() ---
print("Type:", type(fruits))
# Output: <class 'tuple'>

# ---------------------------------------------------------------------------
# Different ways to create tuples
# ---------------------------------------------------------------------------

# Tuple with mixed data types
mixed = ("apple", 42, 3.14, True, None)
print("\nMixed types:", mixed)

# Tuple with one item (MUST include a trailing comma)
one_item = ("apple",)
print("One item tuple:", one_item, "-> type:", type(one_item))
# Output: ('apple',) -> type: <class 'tuple'>

# Without the comma, it's just a string in parentheses
not_a_tuple = ("apple")
print("NOT a tuple:", not_a_tuple, "-> type:", type(not_a_tuple))
# Output: apple -> type: <class 'str'>

# Empty tuple
empty = ()
print("Empty tuple:", empty, "-> length:", len(empty))

# Create tuple using the tuple() constructor
from_list = tuple(["red", "green", "blue"])
print("From list:", from_list)

from_string = tuple("Python")
print("From string:", from_string)
# Output: ('P', 'y', 't', 'h', 'o', 'n')

from_range = tuple(range(1, 6))
print("From range:", from_range)
# Output: (1, 2, 3, 4, 5)

# Tuple without parentheses (packing)
packed = "apple", "banana", "cherry"
print("\nPacked (no parentheses):", packed, "-> type:", type(packed))
# Output: ('apple', 'banana', 'cherry') -> type: <class 'tuple'>

# ---------------------------------------------------------------------------
# Key properties of tuples:
# 1. ORDERED     - Elements have a defined order (index 0, 1, 2...)
# 2. IMMUTABLE   - Cannot change, add, or remove items after creation
# 3. ALLOW DUPES - Can contain duplicate values
# 4. INDEXED     - Can access elements by index
# ---------------------------------------------------------------------------
