# -------------------------------------------------
# File Name: 02_variables.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Introduces basic variables and types: integers, floats,
# -------------------------------------------------

x = 3
y = 5

# Perform a simple arithmetic operation
z = x + y  # Sum of x and y

# Display the result
print("Integer Example")
print("----------------")
print(f"x = {x}")
print(f"y = {y}")
print(f"The sum of x and y is: {z}")

# Check the data type
print(f"Type of x: {type(x)}")
print(f"Type of z: {type(z)}")
print()

# -------------------------------
# 2. Floating point numbers
# -------------------------------

# Price of a product
unit_price = 19.99

# Tax rate (7%)
tax_rate = 0.07

# Calculate the total price including tax
total_price = unit_price * (1 + tax_rate)

print("Float Example (Price Calculation)")
print("----------------------------------")
print(f"Unit price: ${unit_price}")
print(f"Tax rate: {tax_rate * 100}%")

# Format output with 2 decimal places
print(f"Total price after tax: ${total_price:.2f}")

# Check data types
print(f"Type of unit_price: {type(unit_price)}")
print(f"Type of total_price: {type(total_price)}")
print()

# -------------------------------
# 3. String formatting
# -------------------------------

# Create a message using string concatenation
message = "The sum of x and y is: " + str(z)

print("String Example")
print("--------------")
print(message)

# Create a formatted string using f-string (recommended in modern Python)
formatted_message = f"The total price is ${total_price:.2f}"
print(formatted_message)

# Check string type
print(f"Type of message: {type(message)}")