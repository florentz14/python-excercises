# -------------------------------------------------
# File Name: 07_inputs.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: input() for user input (returns str); conversion to
# -------------------------------------------------

name = input("Enter your name: ")
print(f"Hello, {name}!")

# For numbers, explicit conversion is required
age_str = input("\nHow old are you? ")
age = int(age_str)
print(f"In 10 years you will be {age + 10} years old.")

# Direct conversion on the same line
price = float(input("\nEnter a price: $"))
quantity = int(input("Enter the quantity: "))
total = price * quantity
print(f"Total: ${total:,.2f}")

# input() with empty or default message
response = input("\nContinue? (y/n): ").strip().lower()
if response == "y":
    print("Continuing...")
else:
    print("Finishing.")
