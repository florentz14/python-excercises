# Example 7: Loop with items()
print("Example 7: Loop with items()")
print("-" * 40)
products = {"laptop": 1200, "phone": 800, "tablet": 400}
print("Products:", products)
for product, price in products.items():
    print(f"{product}: ${price}")
