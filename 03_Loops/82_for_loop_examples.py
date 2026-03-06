# Simple For Loop Program
# This program demonstrates basic for loop examples

# Example 1: Loop through numbers using range()
print("Example 1: Print numbers 1 to 5")
print("-" * 40)
for i in range(1, 6):
    print(i)

# Example 2: Loop through a list
print("\nExample 2: Print items in a list")
print("-" * 40)
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# Example 3: Loop through a string
print("\nExample 3: Print each character in a string")
print("-" * 40)
word = "Python"
for char in word:
    print(char)

# Example 4: Print multiplication table
print("\nExample 4: Multiplication table of 5")
print("-" * 40)
number = 5
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

# Example 5: Sum numbers using a loop
print("\nExample 5: Sum of numbers 1 to 10")
print("-" * 40)
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")

# Example 6: Print pattern using nested loops
print("\nExample 6: Print a star pattern")
print("-" * 40)
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Example 7: Loop with index using enumerate()
print("\nExample 7: Print list items with index")
print("-" * 40)
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
