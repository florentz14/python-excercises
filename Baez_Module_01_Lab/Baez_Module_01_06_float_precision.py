# -------------------------------------------------
# File Name: Baez_Module_01_06_float_precision.py
# Author: Florentino Báez
# Date: Module 01 Lab - Exercise 6
# Description: Formatting Float Numbers with Precision.
#              Format floating-point numbers to 2 decimal places using
#              the :.2f format specifier in f-strings.
# -------------------------------------------------

print("Exercise 6: Formatting Float Numbers with Precision")
print("-" * 40)

# Variables for products with imprecise floating-point values
item1 = "Milk"
price1 = 2.45678  # Has many decimal places
item2 = "Bread"
price2 = 1.2  # Missing decimal places
item3 = "Cheese"
price3 = 4.789  # Has 3 decimal places

# Print table with price formatted to 2 decimal places
print(f"{'Item':<10}{'Price':<10}")
print("-" * 20)
print(f"{item1:<10}{price1:.2f}")
print(f"{item2:<10}{price2:.2f}")
print(f"{item3:<10}{price3:.2f}")
