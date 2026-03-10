# -------------------------------------------------
# File Name: 07_inputs.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: input() for user input (returns str); conversion to
# -------------------------------------------------

# Define a variable for user input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Define a variable for user input
age_str = input("\nHow old are you? ")
# Print the result of the user input
age = int(age_str)
print(f"In 10 years you will be {age + 10} years old.")

# Define two variables for user input
price = float(input("\nEnter a price: $"))
# Print the result of the user input
quantity = int(input("Enter the quantity: "))
# Print the result of the user input
total = price * quantity
# Print the result of the calculation
print(f"Total: ${total:,.2f}")

# Define a variable for user input
response = input("\nContinue? (y/n): ").strip().lower()
# Print the result of the user input
if response == "y":
    # Print the result of the condition
    print("Continuing...")
else:
    print("Finishing.")
