# -------------------------------------------------
# File Name: 29_visualization_chipotle.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Chipotle Order Data. Create bar charts of most popular
#              items, histogram of prices, and pie chart of item categories
#              using matplotlib.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create Chipotle order DataFrame with item_name, quantity, item_price, item_category
# Approximately 15 rows
csv_path = Path(__file__).parent / "chipotle_viz.csv"
df = pd.read_csv(csv_path)

# Ensure item_price is numeric (in case stored as string in real data)
df["item_price"] = pd.to_numeric(df["item_price"], errors="coerce")

print("Chipotle order data (sample):")
print(df.head())

# --- Plot 1: Bar chart - top 5 most ordered items ---
# Aggregate by item name and sum quantity, then take top 5
top5_items = df.groupby("item_name")["quantity"].sum().nlargest(5)

plt.figure(figsize=(8, 5))
plt.bar(top5_items.index, top5_items.values, color="steelblue", edgecolor="black")
plt.title("Top 5 Most Ordered Items at Chipotle")
plt.xlabel("Item Name")
plt.ylabel("Total Quantity Ordered")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("chipotle_top5_items.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Plot 2: Histogram - distribution of item prices ---
plt.figure(figsize=(8, 5))
plt.hist(df["item_price"], bins=8, color="coral", edgecolor="black")
plt.title("Distribution of Item Prices")
plt.xlabel("Item Price ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("chipotle_price_histogram.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Plot 3: Pie chart - orders by category (Bowls, Burritos, Tacos, etc.) ---
orders_by_category = df.groupby("item_category")["quantity"].sum()

plt.figure(figsize=(7, 7))
plt.pie(orders_by_category.values, labels=orders_by_category.index, autopct="%1.1f%%", startangle=90)
plt.title("Orders by Category")
plt.tight_layout()
plt.savefig("chipotle_pie_category.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Plot 4: Horizontal bar chart - total revenue per item ---
# Revenue = quantity * item_price per row; then sum by item
df["revenue"] = df["quantity"] * df["item_price"]
revenue_per_item = df.groupby("item_name")["revenue"].sum().sort_values(ascending=True)

plt.figure(figsize=(8, 6))
plt.barh(revenue_per_item.index, revenue_per_item.values, color="seagreen", edgecolor="black")
plt.title("Total Revenue per Item")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Item Name")
plt.tight_layout()
plt.savefig("chipotle_revenue_per_item.png", dpi=100, bbox_inches="tight")
plt.show()

print("Plots saved: chipotle_top5_items.png, chipotle_price_histogram.png, chipotle_pie_category.png, chipotle_revenue_per_item.png")
