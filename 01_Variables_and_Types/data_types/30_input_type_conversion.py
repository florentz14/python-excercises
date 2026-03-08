# -------------------------------------------------
# File Name: 30_input_type_conversion.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Read input as string and convert to int/float
# -------------------------------------------------

x = input("Enter a value: ")
print("You entered:", x)
# Convert to int for integer arithmetic
y = int(x) + 10
print("Value after adding 10:", y)
# Convert to float for decimal arithmetic
z = float(x) * 2.5
print("Value after multiplying by 2.5:", z)
print(f"x: {x}, y: {y}, z: {z}")
