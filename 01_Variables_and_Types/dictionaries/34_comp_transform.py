# -------------------------------------------------
# File Name: 34_comp_transform.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Transform existing dict with .items() and filter/transform.
# -------------------------------------------------

print("5. Transforming Existing Dictionary:")
print("-" * 60)
prices = {"apple": 1.5, "banana": 0.8, "orange": 2.0, "grape": 3.5}
print(f"Original prices: {prices}")

# Apply 10% discount - transform values while keeping same keys
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"10% discount: {discounted}")

# Filter expensive items (> $2) - keep only items matching condition
expensive = {item: price for item, price in prices.items() if price > 2}
print(f"Expensive items (>$2): {expensive}")
