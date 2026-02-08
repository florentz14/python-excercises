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

# Create sample Chipotle order data inline (no external CSV)
orders_data = {
    "order_id": [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10],
    "quantity": [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 3, 1, 2, 1, 1],
    "item_name": [
        "Chicken Bowl",
        "Chips and Guacamole",
        "Chicken Bowl",
        "Steak Burrito",
        "Chips",
        "Chicken Bowl",
        "Coca-Cola",
        "Veggie Bowl",
        "Barbacoa Bowl",
        "Chips and Guacamole",
        "Chicken Bowl",
        "Carnitas Burrito",
        "Steak Bowl",
        "Chips",
        "Chicken Salad",
    ],
    "choice_description": [
        "[Tomatillo-Red Chili, Rice, Black Beans]",
        "[Fresh Tomato Salsa]",
        "[Tomatillo-Green Chili, Rice, Pinto Beans]",
        "[Tomatillo-Red Chili, Rice, Black Beans, Guacamole]",
        "[Fresh Tomato Salsa]",
        "[Tomatillo-Red Chili, Rice, Fajita Veggies]",
        "[N/A]",
        "[Tomatillo-Green Chili, Rice, Fajita Veggies]",
        "[Tomatillo-Red Chili, Rice, Black Beans]",
        "[Fresh Tomato Salsa]",
        "[Tomatillo-Red Chili, Rice, Black Beans]",
        "[Tomatillo-Red Chili, Rice, Black Beans, Guacamole]",
        "[Tomatillo-Green Chili, Rice, Fajita Veggies]",
        "[Fresh Tomato Salsa]",
        "[Tomatillo-Red Chili, Rice, Black Beans]",
    ],
    "item_price": [
        "$8.49",
        "$4.45",
        "$8.49",
        "$11.75",
        "$2.15",
        "$8.49",
        "$2.25",
        "$8.49",
        "$9.25",
        "$4.45",
        "$8.49",
        "$10.98",
        "$11.25",
        "$2.15",
        "$8.99",
    ],
}

df = pd.DataFrame(orders_data)

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
