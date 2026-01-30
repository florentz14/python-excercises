# Simple Set Program
# This program demonstrates basic set operations in Python

# Example 1: Create and display a set
print("Example 1: Create and display a set")
print("-" * 40)
numbers = {10, 20, 30, 40, 50}
print("Set:", numbers)
print("Length:", len(numbers))
print("Type:", type(numbers))

# Example 2: Create an empty set
print("\nExample 2: Create an empty set")
print("-" * 40)
empty_set = set()  # Must use set() for empty set
print("Empty set:", empty_set)
print("Type:", type(empty_set))
not_a_set = {}  # This creates an empty dictionary, not a set
print("Empty dict:", not_a_set)
print("Type:", type(not_a_set))

# Example 3: Create set from list
print("\nExample 3: Create set from list")
print("-" * 40)
list_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("List with duplicates:", list_data)
unique_set = set(list_data)
print("Converted to set (removes duplicates):", unique_set)

# Example 4: Add and remove elements
print("\nExample 4: Add and remove elements")
print("-" * 40)
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)
fruits.add("date")
print("After add('date'):", fruits)
fruits.remove("banana")
print("After remove('banana'):", fruits)
fruits.discard("grape")  # No error if element doesn't exist
print("After discard('grape'):", fruits)

# Example 5: Check membership
print("\nExample 5: Check membership")
print("-" * 40)
colors = {"red", "green", "blue", "yellow"}
print("Set:", colors)
if "red" in colors:
    print("'red' is in the set")
if "purple" not in colors:
    print("'purple' is not in the set")

# Example 6: Loop through a set
print("\nExample 6: Loop through a set")
print("-" * 40)
animals = {"cat", "dog", "bird", "fish"}
print("Set:", animals)
for animal in animals:
    print(animal)

# Example 7: Set union
print("\nExample 7: Set union (combine sets)")
print("-" * 40)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set 1:", set1)
print("Set 2:", set2)
union = set1 | set2  # or set1.union(set2)
print("Union (set1 | set2):", union)

# Example 8: Set intersection
print("\nExample 8: Set intersection (common elements)")
print("-" * 40)
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "elderberry"}
print("Set A:", set_a)
print("Set B:", set_b)
intersection = set_a & set_b  # or set_a.intersection(set_b)
print("Intersection (set_a & set_b):", intersection)

# Example 9: Set difference
print("\nExample 9: Set difference (elements in first but not second)")
print("-" * 40)
set_x = {1, 2, 3, 4, 5}
set_y = {4, 5, 6, 7}
print("Set X:", set_x)
print("Set Y:", set_y)
difference = set_x - set_y  # or set_x.difference(set_y)
print("Difference (set_x - set_y):", difference)

# Example 10: Set symmetric difference
print("\nExample 10: Set symmetric difference (elements in either but not both)")
print("-" * 40)
set_m = {1, 2, 3, 4}
set_n = {3, 4, 5, 6}
print("Set M:", set_m)
print("Set N:", set_n)
sym_diff = set_m ^ set_n  # or set_m.symmetric_difference(set_n)
print("Symmetric Difference (set_m ^ set_n):", sym_diff)

# Example 11: Set comparison (subset, superset)
print("\nExample 11: Set comparison")
print("-" * 40)
parent_set = {1, 2, 3, 4, 5}
child_set = {2, 4}
print("Parent set:", parent_set)
print("Child set:", child_set)
print("Is child_set a subset of parent_set?", child_set.issubset(parent_set))
print("Is parent_set a superset of child_set?",
      parent_set.issuperset(child_set))
print("Are they disjoint?", child_set.isdisjoint(parent_set))

# Example 12: Clear a set
print("\nExample 12: Clear a set")
print("-" * 40)
temp_set = {10, 20, 30}
print("Original set:", temp_set)
temp_set.clear()
print("After clear:", temp_set)

# Example 13: Copy a set
print("\nExample 13: Copy a set")
print("-" * 40)
original_set = {1, 2, 3}
copied_set = original_set.copy()
print("Original:", original_set)
print("Copied:", copied_set)
copied_set.add(4)
print("After adding 4 to copy:")
print("Original:", original_set)
print("Copied:", copied_set)

# Example 14: Set operations with methods
print("\nExample 14: Set operations with methods")
print("-" * 40)
set_p = {1, 2, 3}
set_q = {3, 4, 5}
print("Set P:", set_p)
print("Set Q:", set_q)
set_p.update(set_q)  # Add all elements from set_q
print("After P.update(Q):", set_p)

# Example 15: Find and remove minimum/maximum
print("\nExample 15: Find and remove elements")
print("-" * 40)
num_set = {50, 10, 40, 20, 30}
print("Original set:", num_set)
print("Max element:", max(num_set))
print("Min element:", min(num_set))
popped = num_set.pop()  # Remove and return an arbitrary element
print(f"Popped element: {popped}")
print("After pop:", num_set)

# Example 16: Set comprehension
print("\nExample 16: Set comprehension")
print("-" * 40)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
squared_set = {x**2 for x in numbers_list}
print("Original numbers:", numbers_list)
print("Squared set (removes duplicates):", squared_set)
even_squared = {x**2 for x in numbers_list if x % 2 == 0}
print("Even squared set:", even_squared)

# Example 17: Practical example - Find unique elements
print("\nExample 17: Practical example - Find unique elements")
print("-" * 40)
votes = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print("Votes:", votes)
unique_votes = set(votes)
print("Unique votes:", unique_votes)
print(f"Total votes: {len(votes)}")
print(f"Unique votes: {len(unique_votes)}")

# Example 18: Practical example - Common hobbies
print("\nExample 18: Practical example - Common hobbies")
print("-" * 40)
alice_hobbies = {"reading", "hiking", "coding", "gaming"}
bob_hobbies = {"gaming", "music", "hiking", "cooking"}
print("Alice's hobbies:", alice_hobbies)
print("Bob's hobbies:", bob_hobbies)
common = alice_hobbies & bob_hobbies
print("Common hobbies:", common)
all_hobbies = alice_hobbies | bob_hobbies
print("All hobbies:", all_hobbies)
