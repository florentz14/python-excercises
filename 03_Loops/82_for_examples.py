# -------------------------------------------------
# File Name: 82_for_examples.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Basic examples collection.
# -------------------------------------------------

print("Example 1: Print numbers 1 to 5")
print("-" * 40)
for i in range(1, 6):
    print(i)

# Example 2: iterate list
print("\nExample 2: Print items in a list")
print("-" * 40)
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# Example 3: iterate string
print("\nExample 3: Print each character in a string")
print("-" * 40)
word = "Python"
for char in word:
    print(char)

# Example 4: multiplication table
print("\nExample 4: Multiplication table of 5")
print("-" * 40)
number = 5
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

# Example 5: sum with loop
print("\nExample 5: Sum of numbers 1 to 10")
print("-" * 40)
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")

# Example 6: nested loops star pattern
print("\nExample 6: Print a star pattern")
print("-" * 40)
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Example 7: enumerate()
print("\nExample 7: Print list items with index")
print("-" * 40)
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
