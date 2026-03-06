# -------------------------------------------------
# File Name: 07_loop_items.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Loop with items() Method.
#              items() returns (key, value) tuples, allowing
#              unpacking both in the for-loop header.
#              More readable than accessing values by key.
# -------------------------------------------------

# Example 7: Loop with items()
print("Example 7: Loop with items()")
print("-" * 40)

products = {"laptop": 1200, "phone": 800, "tablet": 400}
print("Products:", products)

# items() returns key-value pairs for unpacking
for product, price in products.items():
    print(f"{product}: ${price}")
