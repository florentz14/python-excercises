# Simple Tuple Program
# This program demonstrates basic tuple operations in Python

# Example 1: Create and display a tuple
print("Example 1: Create and display a tuple")
print("-" * 40)
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)
print("Length of tuple:", len(numbers))
print("Type:", type(numbers))

# Example 2: Access tuple elements by index
print("\nExample 2: Access tuple elements by index")
print("-" * 40)
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Third element:", fruits[2])

# Example 3: Negative indexing
print("\nExample 3: Negative indexing")
print("-" * 40)
colors = ("red", "green", "blue", "yellow")
print("Tuple:", colors)
print("Second to last element:", colors[-2])
print("Third from end:", colors[-3])

# Example 4: Slice a tuple
print("\nExample 4: Slice a tuple")
print("-" * 40)
letters = ("a", "b", "c", "d", "e", "f")
print("Original tuple:", letters)
print("First 3 elements:", letters[0:3])
print("Elements from index 2 to 4:", letters[2:5])
print("Every second element:", letters[::2])
print("Reverse tuple:", letters[::-1])

# Example 5: Loop through a tuple
print("\nExample 5: Loop through a tuple")
print("-" * 40)
scores = (85, 92, 78, 95, 88)
print("Scores:", scores)
for score in scores:
    print(f"Score: {score}")

# Example 6: Find element and check membership
print("\nExample 6: Find element and check membership")
print("-" * 40)
items = ("pen", "pencil", "eraser", "ruler", "notebook")
print("Tuple:", items)
if "pen" in items:
    print("'pen' is in the tuple")
    print("Index of 'pen':", items.index("pen"))
if "marker" not in items:
    print("'marker' is not in the tuple")

# Example 7: Count occurrences
print("\nExample 7: Count occurrences")
print("-" * 40)
repeated_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
print("Tuple:", repeated_tuple)
print("Count of 2:", repeated_tuple.count(2))
print("Count of 4:", repeated_tuple.count(4))

# Example 8: Tuple concatenation and repetition
print("\nExample 8: Tuple concatenation and repetition")
print("-" * 40)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Combined (tuple1 + tuple2):", combined)
repeated = tuple1 * 3
print("Repeated (tuple1 * 3):", repeated)

# Example 9: Tuple unpacking
print("\nExample 9: Tuple unpacking")
print("-" * 40)
person = ("John", 25, "Engineer")
name, age, profession = person
print("Original tuple:", person)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# Example 10: Single element tuple
print("\nExample 10: Single element tuple")
print("-" * 40)
single = (42,)  # Note the comma is required
print("Single element tuple:", single)
print("Type:", type(single))
not_tuple = (42)  # Without comma, it's just an integer
print("Without comma:", not_tuple)
print("Type:", type(not_tuple))

# Example 11: Tuple immutability
print("\nExample 11: Tuple immutability")
print("-" * 40)
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print(f"Error: Tuples are immutable! - {e}")

# Example 12: Tuple with mixed data types
print("\nExample 12: Tuple with mixed data types")
print("-" * 40)
mixed = (10, "hello", 3.14, True, None)
print("Mixed tuple:", mixed)
for index, item in enumerate(mixed):
    print(f"Index {index}: {item} (type: {type(item).__name__})")

# Example 13: Nested tuples
print("\nExample 13: Nested tuples")
print("-" * 40)
nested = ((1, 2), ("a", "b"), (True, False))
print("Nested tuple:", nested)
print("First inner tuple:", nested[0])
print("First element of first inner tuple:", nested[0][0])

# Example 14: Convert list to tuple and vice versa
print("\nExample 14: Convert list to tuple and vice versa")
print("-" * 40)
list_data = [10, 20, 30, 40]
tuple_data = tuple(list_data)
print("Original list:", list_data)
print("Converted to tuple:", tuple_data)
back_to_list = list(tuple_data)
print("Converted back to list:", back_to_list)
