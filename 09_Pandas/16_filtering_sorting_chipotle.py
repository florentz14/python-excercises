# -------------------------------------------------
# File Name: 16_filtering_sorting_chipotle.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter and Sort Chipotle Orders. Practice boolean indexing,
#              query(), sort_values(), and loc/iloc to filter orders by
#              price, item, and quantity.
# -------------------------------------------------

import pandas as pd

# Create sample Chipotle order data inline (no external CSV)
orders_data = {
    "order_id": [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12],
    "quantity": [1, 2, 1, 1, 1, 3, 1, 1, 2, 1, 1, 2, 1, 1, 1],
    "item_name": [
        "Chicken Bowl",
        "Steak Burrito",
        "Chicken Bowl",
        "Chips and Guacamole",
        "Veggie Bowl",
        "Chicken Bowl",
        "Barbacoa Bowl",
        "Carnitas Burrito",
        "Chicken Bowl",
        "Steak Bowl",
        "Chips",
        "Chicken Bowl",
        "Chicken Salad",
        "Steak Burrito",
        "Coca-Cola",
    ],
    "item_price": [
        8.49,
        11.75,
        8.49,
        4.45,
        8.49,
        8.49,
        9.25,
        10.98,
        8.49,
        11.25,
        2.15,
        8.49,
        8.99,
        11.75,
        2.25,
    ],
}

df = pd.DataFrame(orders_data)

# Filter items with price > 10
print("=== FILTER: item_price > 10 ===")
high_price = df[df["item_price"] > 10]
print(high_price)
print()

# Filter only "Chicken Bowl" items
print("=== FILTER: Chicken Bowl only ===")
chicken_bowl = df[df["item_name"] == "Chicken Bowl"]
print(chicken_bowl)
print()

# Sort by item_price descending
print("=== SORT BY item_price (descending) ===")
sorted_price = df.sort_values(by="item_price", ascending=False)
print(sorted_price)
print()

# Sort by quantity ascending, then item_price descending
print("=== SORT BY quantity (asc), then item_price (desc) ===")
sorted_multi = df.sort_values(by=["quantity", "item_price"], ascending=[True, False])
print(sorted_multi)
print()

# Use .query() method for filtering (e.g., price > 9)
print("=== QUERY: item_price > 9 ===")
query_result = df.query("item_price > 9")
print(query_result)
print()

# Use .loc to select specific rows and columns (e.g., rows 0-4, columns item_name and item_price)
print("=== LOC: rows 0-4, columns item_name and item_price ===")
loc_result = df.loc[0:4, ["item_name", "item_price"]]
print(loc_result)
print()

# Use .iloc for positional selection (e.g., first 5 rows, first 3 columns)
print("=== ILOC: first 5 rows, first 3 columns ===")
iloc_result = df.iloc[0:5, 0:3]
print(iloc_result)
print()

# Find items ordered more than once (quantity > 1)
print("=== ROWS WHERE quantity > 1 ===")
multi_quantity = df[df["quantity"] > 1]
print(multi_quantity)
