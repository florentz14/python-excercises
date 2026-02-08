# -------------------------------------------------
# File Name: 01_python_sets.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Create Sets and Understand Their Properties.
#              A set is an unordered, unindexed collection of
#              unique items. Elements must be immutable (hashable).
#              Duplicates are automatically removed on creation.
#              Covers set(), {}, mixed types, and bool/int overlap.
# -------------------------------------------------

# --- Create a set using curly braces ---
fruits = {"apple", "banana", "cherry", "pineapple", "grape"}
print("Fruits set:", fruits)
# Note: Order may vary each time (sets are UNORDERED)

# --- Sets automatically remove duplicates ---
numbers = {1, 5, 3, 5, 7, 1, 3}
print("\nWith duplicates: {1, 5, 3, 5, 7, 1, 3}")
print("Result:", numbers)
# Output: {1, 3, 5, 7}  (duplicates removed)

# --- Length with len() ---
print(f"\nLength of fruits: {len(fruits)}")
# Output: 5

# --- Type check ---
print(f"Type: {type(fruits)}")
# Output: <class 'set'>

# -------------------------------------------------
# Different ways to create sets
# -------------------------------------------------

# Empty set (MUST use set(), NOT {} which creates a dict)
empty_set = set()
empty_dict = {}
print(f"\nset() type: {type(empty_set)}")    # <class 'set'>
print(f"{{}} type: {type(empty_dict)}")       # <class 'dict'>

# Set from a list (removes duplicates automatically)
colors_list = ["red", "blue", "red", "green", "blue"]
colors_set = set(colors_list)
print(f"\nFrom list: {colors_set}")
# Output: {'red', 'blue', 'green'}

# Set from a string (each character becomes an element)
char_set = set("hello")
print(f"From string 'hello': {char_set}")
# Output: {'h', 'e', 'l', 'o'}  (duplicate 'l' removed)

# Set from a tuple
from_tuple = set((10, 20, 30))
print(f"From tuple: {from_tuple}")

# Set from range
from_range = set(range(1, 6))
print(f"From range: {from_range}")
# Output: {1, 2, 3, 4, 5}

# --- Mixed data types (elements must be immutable/hashable) ---
mixed = {42, "hello", 3.14, True, (1, 2)}
print(f"\nMixed types: {mixed}")
# Note: True and 1 are considered the same value in a set
# Note: You CANNOT add lists or dicts to a set (they are mutable)

# -------------------------------------------------
# Key properties of sets:
# 1. UNORDERED    - No defined order, no index access
# 2. NO DUPLICATES - Each element is unique
# 3. MUTABLE      - Can add/remove items (but items must be immutable)
# 4. NO INDEXING   - Cannot access by set[0] (use 'in' to check)
# -------------------------------------------------

# Boolean and integer overlap: True==1, False==0
test = {True, 1, False, 0}
print(f"\n{{True, 1, False, 0}} = {test}")
# Output: {True, False} (True==1 and False==0, considered duplicates)
