"""
Exercise 2: Dictionary Methods
This exercise explores the most useful built-in dictionary methods.
Understanding these methods is crucial for efficient dictionary manipulation.
"""

def main():
    print("Exercise 2: Dictionary Methods")
    print("=" * 60)
    
    # Sample dictionary
    inventory = {
        "apples": 50,
        "bananas": 30,
        "oranges": 25,
        "grapes": 40
    }
    
    print("Original Inventory:")
    print(inventory)
    print()
    
    # 1. keys() - Get all keys
    print("1. keys() - Getting All Keys:")
    print("-" * 60)
    keys = inventory.keys()
    print(f"All products: {list(keys)}")
    print()
    
    # 2. values() - Get all values
    print("2. values() - Getting All Values:")
    print("-" * 60)
    values = inventory.values()
    print(f"All quantities: {list(values)}")
    print(f"Total items: {sum(values)}")
    print()
    
    # 3. items() - Get key-value pairs
    print("3. items() - Getting Key-Value Pairs:")
    print("-" * 60)
    for product, quantity in inventory.items():
        print(f"  {product.capitalize()}: {quantity} units")
    print()
    
    # 4. update() - Merge dictionaries
    print("4. update() - Merging Dictionaries:")
    print("-" * 60)
    new_items = {"mangoes": 15, "pineapples": 10}
    print(f"Adding new items: {new_items}")
    inventory.update(new_items)
    print(f"Updated inventory: {inventory}")
    print()
    
    # 5. setdefault() - Get value or set default
    print("5. setdefault() - Get or Set Default:")
    print("-" * 60)
    watermelon_qty = inventory.setdefault("watermelons", 20)
    print(f"Watermelons quantity (new): {watermelon_qty}")
    apple_qty = inventory.setdefault("apples", 100)
    print(f"Apples quantity (existing): {apple_qty}")
    print(f"Inventory: {inventory}")
    print()
    
    # 6. clear() - Remove all items
    print("6. clear() - Removing All Items:")
    print("-" * 60)
    temp_dict = {"a": 1, "b": 2}
    print(f"Before clear: {temp_dict}")
    temp_dict.clear()
    print(f"After clear: {temp_dict}")
    print()
    
    # 7. copy() - Create a shallow copy
    print("7. copy() - Creating a Copy:")
    print("-" * 60)
    inventory_backup = inventory.copy()
    print(f"Backup created: {len(inventory_backup)} items")
    print()
    
    # 8. fromkeys() - Create dictionary with same value
    print("8. fromkeys() - Create Dictionary from Keys:")
    print("-" * 60)
    products = ["eggs", "milk", "bread"]
    stock_check = dict.fromkeys(products, "In Stock")
    print(f"Stock status: {stock_check}")
    
    print("\n" + "=" * 60)
    print("Key Methods Summary:")
    print("  keys()      → Get all keys")
    print("  values()    → Get all values")
    print("  items()     → Get (key, value) pairs")
    print("  update()    → Merge dictionaries")
    print("  setdefault()→ Get or set default value")
    print("  clear()     → Remove all items")
    print("  copy()      → Create shallow copy")
    print("  fromkeys()  → Create dict from keys")


if __name__ == "__main__":
    main()
