# -------------------------------------------------
# File Name: 14_control_flow.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Introduction to control flow: if, elif, else,
# -------------------------------------------------

age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")

# elif: multiple conditions
grade = 85
if grade >= 90:
    print("\nExcellent")
elif nota >= 70:
    print("Passed")
else:
    print("Failed")

# for: iterate sequence
print("\n--- for ---")
for i in range(3):
    print("Hello", i + 1)

for letter in "abc":
    print(letter, end=" ")
print()

# while: repeat while condition is true
print("\n--- while ---")
n = 0
while n < 3:
    print("n =", n)
    n += 1
