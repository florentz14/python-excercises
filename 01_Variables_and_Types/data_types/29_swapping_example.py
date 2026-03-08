# -------------------------------------------------
# File Name: 29_swapping_example.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Practical example of swapping two variable values
# -------------------------------------------------

print("Another Example with Swapping Variables")
# Initial quantities
shoes = 50
hats = 30
print(f"Initial values - Shoes: {shoes}, Hats: {hats}")
# Swap using tuple unpacking (no temporary variable needed)
shoes, hats = hats, shoes
print(f"After swapping - Shoes: {shoes}, Hats: {hats}")
print("*" * 30)
