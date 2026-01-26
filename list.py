# Simple List Program
# This program demonstrates basic list operations in Python

# Example 1: Create and display a list
print("Example 1: Create and display a list")
print("-" * 40)
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("Length of list:", len(numbers))

# Example 2: Access list elements by index
print("\nExample 2: Access list elements by index")
print("-" * 40)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Third element:", fruits[2])

# Example 3: Add elements to a list
print("\nExample 3: Add elements to a list")
print("-" * 40)
colors = ["red", "blue"]
print("Original list:", colors)
colors.append("green")  # Add one element
print("After append:", colors)
colors.extend(["yellow", "purple"])  # Add multiple elements
print("After extend:", colors)

# Example 4: Remove elements from a list
print("\nExample 4: Remove elements from a list")
print("-" * 40)
animals = ["cat", "dog", "bird", "fish", "dog"]
print("Original list:", animals)
animals.remove("dog")  # Remove first occurrence
print("After remove 'dog':", animals)
removed_item = animals.pop()  # Remove and return last element
print("Popped item:", removed_item)
print("After pop:", animals)

# Example 5: Slice a list
print("\nExample 5: Slice a list")
print("-" * 40)
letters = ["a", "b", "c", "d", "e", "f"]
print("Original list:", letters)
print("First 3 elements:", letters[0:3])
print("Elements from index 2 to 4:", letters[2:5])
print("Every second element:", letters[::2])
print("Reverse list:", letters[::-1])

# Example 6: Loop through a list
print("\nExample 6: Loop through a list")
print("-" * 40)
scores = [85, 92, 78, 95, 88]
print("Scores:", scores)
for score in scores:
    print(f"Score: {score}")

# Example 7: List comprehension
print("\nExample 7: List comprehension")
print("-" * 40)
numbers_list = [1, 2, 3, 4, 5]
print("Original numbers:", numbers_list)
squared = [x ** 2 for x in numbers_list]
print("Squared numbers:", squared)
even_numbers = [x for x in numbers_list if x % 2 == 0]
print("Even numbers:", even_numbers)

# Example 8: Sort and reverse
print("\nExample 8: Sort and reverse")
print("-" * 40)
unsorted = [50, 10, 40, 20, 30]
print("Original list:", unsorted)
unsorted.sort()
print("Sorted list:", unsorted)
unsorted.reverse()
print("Reversed list:", unsorted)

# Example 9: Find element and check membership
print("\nExample 9: Find element and check membership")
print("-" * 40)
items = ["pen", "pencil", "eraser", "ruler", "notebook"]
print("List:", items)
if "pen" in items:
    print("'pen' is in the list")
    print("Index of 'pen':", items.index("pen"))
if "marker" not in items:
    print("'marker' is not in the list")

# Example 10: List operations
print("\nExample 10: List operations")
print("-" * 40)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("List 1:", list1)
print("List 2:", list2)
print("Combined (list1 + list2):", combined)
repeated = list1 * 3
print("Repeated (list1 * 3):", repeated)
