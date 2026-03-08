# -------------------------------------------------
# File Name: 07_loop_items.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Loop with items() for (key, value) tuple unpacking.
# -------------------------------------------------

print("Example 7: Loop with items()")
print("-" * 40)

products = {"laptop": 1200, "phone": 800, "tablet": 400}
print("Products:", products)

# items() returns key-value pairs for unpacking
for product, price in products.items():
    print(f"{product}: ${price}")
