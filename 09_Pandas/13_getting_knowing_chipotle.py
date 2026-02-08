# -------------------------------------------------
# File Name: 13_getting_knowing_chipotle.py
# Author: Florentino Báez
# Date: Pandas
# Description: Explore the Chipotle Orders Dataset. Load order data,
#              inspect structure with info(), shape, columns, dtypes,
#              head(), tail(). Count observations, columns, and print
#              dataset summary including most ordered items and revenue.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

# Load Chipotle order data from the CSV file (same folder as this script)
csv_path = Path(__file__).parent / "chipotle_orders.csv"
df = pd.read_csv(csv_path)

# Print dataset shape (rows, columns)
print("=== SHAPE ===")
print(df.shape)
print()

# Print column names
print("=== COLUMNS ===")
print(df.columns.tolist())
print()

# Print data types for each column
print("=== DTYPES ===")
print(df.dtypes)
print()

# Full info summary (index, columns, dtypes, non-null counts, memory)
print("=== INFO SUMMARY ===")
df.info()
print()

# First 5 rows
print("=== HEAD (first 5 rows) ===")
print(df.head())
print()

# Last 5 rows
print("=== TAIL (last 5 rows) ===")
print(df.tail())
print()

# Count observations and columns
print("=== OBSERVATIONS & COLUMNS ===")
print(f"Number of observations (rows): {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print()

# Most ordered items (value_counts on item_name)
print("=== MOST ORDERED ITEMS (value_counts) ===")
print(df["item_name"].value_counts())
print()

# Total revenue: item_price is string with $, convert to float and multiply by quantity
df["item_price_float"] = df["item_price"].str.replace("$", "").astype(float)
df["line_total"] = df["quantity"] * df["item_price_float"]
total_revenue = df["line_total"].sum()
print("=== TOTAL REVENUE ===")
print(f"Total revenue: ${total_revenue:.2f}")
print()

# Most expensive items (by unit price)
print("=== MOST EXPENSIVE ITEMS (by unit price) ===")
price_by_item = df.groupby("item_name")["item_price_float"].max().sort_values(ascending=False)
print(price_by_item)
print()

# Alternative: show top 5 most expensive unique item prices
print("Top 5 highest unit prices:")
print(df[["item_name", "item_price_float"]].drop_duplicates().nlargest(5, "item_price_float"))
