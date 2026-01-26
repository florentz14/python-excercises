# Simple Dictionary Program
# This program demonstrates basic dictionary operations in Python
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Example 1: Create and display a dictionary
print("Example 1: Create and display a dictionary")
print("-" * 40)
student = {"name": "John", "age": 20, "grade": "A"}
print("Dictionary:", student)
print("Length:", len(student))
print("Type:", type(student))

# Example 2: Access dictionary values by key
print("\nExample 2: Access dictionary values by key")
print("-" * 40)
person = {"name": "Alice", "age": 25,
          "city": "New York", "profession": "Engineer"}
print("Dictionary:", person)
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Example 3: Use get() method
print("\nExample 3: Use get() method")
print("-" * 40)
user = {"username": "johndoe", "email": "john@example.com", "active": True}
print("Dictionary:", user)
print("Username:", user.get("username"))
print("Phone (not exists):", user.get("phone", "Not provided"))

# Example 4: Add and modify values
print("\nExample 4: Add and modify values")
print("-" * 40)
car = {"brand": "Toyota", "color": "red"}
print("Original:", car)
car["year"] = 2023  # Add new key-value pair
print("After adding year:", car)
car["color"] = "blue"  # Modify existing value
print("After modifying color:", car)

# Example 5: Remove items from dictionary
print("\nExample 5: Remove items from dictionary")
print("-" * 40)
inventory = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
print("Original:", inventory)
removed = inventory.pop("banana")  # Remove and return value
print(f"Removed banana: {removed}")
print("After pop:", inventory)
del inventory["grape"]  # Delete an item
print("After del grape:", inventory)

# Example 6: Loop through dictionary
print("\nExample 6: Loop through dictionary")
print("-" * 40)
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
print("Scores:", scores)
for key in scores:
    print(f"{key}: {scores[key]}")

# Example 7: Loop with items()
print("\nExample 7: Loop with items()")
print("-" * 40)
products = {"laptop": 1200, "phone": 800, "tablet": 400}
print("Products:", products)
for product, price in products.items():
    print(f"{product}: ${price}")

# Example 8: Get all keys and values
print("\nExample 8: Get all keys and values")
print("-" * 40)
courses = {"Math": "A", "Science": "B", "English": "A"}
print("Dictionary:", courses)
print("Keys:", list(courses.keys()))
print("Values:", list(courses.values()))

# Example 9: Check if key exists
print("\nExample 9: Check if key exists")
print("-" * 40)
settings = {"theme": "dark", "language": "English", "notifications": True}
print("Dictionary:", settings)
if "theme" in settings:
    print("'theme' is in the dictionary")
if "password" not in settings:
    print("'password' is not in the dictionary")

# Example 10: Update dictionary
print("\nExample 10: Update dictionary")
print("-" * 40)
config = {"host": "localhost", "port": 8000}
print("Original:", config)
new_config = {"port": 9000, "ssl": True}
config.update(new_config)
print("After update:", config)

# Example 11: Copy dictionary
print("\nExample 11: Copy dictionary")
print("-" * 40)
original = {"a": 1, "b": 2, "c": 3}
copy_dict = original.copy()
print("Original:", original)
print("Copy:", copy_dict)
copy_dict["a"] = 100
print("After modifying copy:")
print("Original:", original)
print("Copy:", copy_dict)

# Example 12: Clear dictionary
print("\nExample 12: Clear dictionary")
print("-" * 40)
temp_dict = {"x": 10, "y": 20, "z": 30}
print("Before clear:", temp_dict)
temp_dict.clear()
print("After clear:", temp_dict)

# Example 13: Dictionary with nested structures
print("\nExample 13: Dictionary with nested structures")
print("-" * 40)
nested = {
    "user1": {"name": "John", "age": 25},
    "user2": {"name": "Jane", "age": 23}
}
print("Nested dictionary:", nested)
print("User 1 name:", nested["user1"]["name"])
print("User 2 age:", nested["user2"]["age"])

# Example 14: Dictionary comprehension
print("\nExample 14: Dictionary comprehension")
print("-" * 40)
numbers = [1, 2, 3, 4, 5]
squared = {x: x**2 for x in numbers}
print("Numbers:", numbers)
print("Squared dictionary:", squared)
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print("Even squared dictionary:", even_squares)

# Example 15: Convert list of tuples to dictionary
print("\nExample 15: Convert list of tuples to dictionary")
print("-" * 40)
pairs = [("name", "Alice"), ("age", 30), ("city", "Boston")]
person_dict = dict(pairs)
print("List of tuples:", pairs)
print("Converted to dictionary:", person_dict)

# Example 16: Dictionary methods
print("\nExample 16: Dictionary methods")
print("-" * 40)
employee = {"id": 101, "name": "Bob", "department": "IT"}
print("Original:", employee)
print("setdefault('salary', 50000):", employee.setdefault("salary", 50000))
print("After setdefault:", employee)
print("setdefault('name', 'Unknown'):", employee.setdefault("name", "Unknown"))
print("Final dictionary:", employee)
