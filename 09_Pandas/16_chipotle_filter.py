# -------------------------------------------------
# File Name: 16_chipotle_filter.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter and Sort Chipotle Orders. Practice boolean indexing,
#              query(), sort_values(), and loc/iloc to filter orders by
#              price, item, and quantity.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

# Load Chipotle order data from the CSV file (same folder as this script)
csv_path = Path(__file__).parent / "chipotle_orders.csv"
df = pd.read_csv(csv_path)

# Convert item_price from string "$8.49" to float 8.49
df["item_price"] = df["item_price"].str.replace("$", "").astype(float)

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
