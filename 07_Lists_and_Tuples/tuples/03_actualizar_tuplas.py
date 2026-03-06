# ---------------------------------------------------------------------------
# Tuplas - 03: Update Tuples (Modificar Tuplas)
# ---------------------------------------------------------------------------
# Description: Tuples are IMMUTABLE - you cannot directly change, add, or
#              remove items. However, there are workarounds by converting
#              the tuple to a list, making changes, and converting back.
# ---------------------------------------------------------------------------

fruits = ("apple", "banana", "cherry")
print("Original tuple:", fruits)

# --- You CANNOT change a tuple directly ---
try:
    fruits[1] = "kiwi"  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: 'tuple' object does not support item assignment

# =========================================================================
# WORKAROUND: Convert to list -> modify -> convert back to tuple
# =========================================================================

# --- Change a value ---
temp_list = list(fruits)       # Convert to list
temp_list[1] = "kiwi"         # Change "banana" to "kiwi"
fruits = tuple(temp_list)      # Convert back to tuple
print("\nAfter changing index 1:", fruits)
# Output: ('apple', 'kiwi', 'cherry')

# --- Add an item ---
temp_list = list(fruits)
temp_list.append("mango")     # Add "mango" at the end
fruits = tuple(temp_list)
print("After append:", fruits)
# Output: ('apple', 'kiwi', 'cherry', 'mango')

# --- Insert an item at a specific position ---
temp_list = list(fruits)
temp_list.insert(1, "banana")  # Insert "banana" at index 1
fruits = tuple(temp_list)
print("After insert at 1:", fruits)
# Output: ('apple', 'banana', 'kiwi', 'cherry', 'mango')

# --- Remove an item ---
temp_list = list(fruits)
temp_list.remove("kiwi")      # Remove "kiwi"
fruits = tuple(temp_list)
print("After removing 'kiwi':", fruits)
# Output: ('apple', 'banana', 'cherry', 'mango')

# =========================================================================
# ALTERNATIVE: Add tuples using concatenation (+)
# =========================================================================

# Add items by concatenating tuples (no list conversion needed)
original = ("apple", "banana", "cherry")
added = original + ("orange",)  # Note the comma to make it a tuple
print("\nConcatenation:", added)
# Output: ('apple', 'banana', 'cherry', 'orange')

# =========================================================================
# DELETE a tuple entirely
# =========================================================================

temp_tuple = ("apple", "banana")
del temp_tuple  # Deletes the variable completely

try:
    print(temp_tuple)
except NameError as e:
    print(f"\nError: {e}")
# Output: Error: name 'temp_tuple' is not defined

# ---------------------------------------------------------------------------
# Summary of workarounds:
# - Change value: list() -> modify -> tuple()
# - Add item:     list() -> append/insert -> tuple()  OR  tuple1 + tuple2
# - Remove item:  list() -> remove/pop -> tuple()
# - Delete tuple: del tuple_name
# ---------------------------------------------------------------------------
