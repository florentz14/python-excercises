# -------------------------------------------------
# File Name: 27_fruits.py
# Author: Florentino Báez
# Date: 19/02/2026
# Description: Sets Example with fruits.
#              Shows how to create a set, add elements,
#              remove elements, loop through a set, and
#              perform mathematical operations on sets.
#              Also shows how to check if an element is
#              in a set, clear a set, and convert a set
#              to a list.
# -------------------------------------------------

print("Sets Example")
print("-" * 40)

# create a set
fruits = {"apple", "kiwi", "orange", "banana", "pineapple", "strawberry", "watermelon"}
print("Original fruits:", fruits)

# duplicates are removed automatically
numbers = {1, 2, 3, 4, 5, 6, 6, 6}
print("Numbers (duplicates removed):", numbers)

# ---------------------------------------
# ADD ELEMENT
# ---------------------------------------
fruits.add("mango")
print("After add:", fruits)

# ---------------------------------------
# REMOVE ELEMENT (throws error if not exists)
# ---------------------------------------
fruits.remove("apple")
print("After remove:", fruits)

# ---------------------------------------
# DISCARD (safe remove, no error)
# ---------------------------------------
fruits.discard("banana")  # no error if not found
print("After discard banana:", fruits)

# ---------------------------------------
# LOOP THROUGH SET
# ---------------------------------------
print("\nLooping through fruits:")
for fruit in fruits:
    print(fruit)

# ---------------------------------------
# MATHEMATICAL OPERATIONS
# ---------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# UNION (all unique values)
print("\nUnion:", set1.union(set2))
print("Union using | :", set1 | set2)

# INTERSECTION (common values)
print("Intersection:", set1.intersection(set2))
print("Intersection using & :", set1 & set2)

# DIFFERENCE (values in set1 but not in set2)
print("Difference:", set1.difference(set2))
print("Difference using - :", set1 - set2)

# SYMMETRIC DIFFERENCE (not common values)
print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Using ^ :", set1 ^ set2)

# ---------------------------------------
# CHECK MEMBERSHIP
# ---------------------------------------
if 2 in set1:
    print("\n2 exists in set1")

# ---------------------------------------
# CLEAR SET
# ---------------------------------------
temp = {10, 20, 30}
temp.clear()
print("After clear:", temp)
