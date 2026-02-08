# -------------------------------------------------
# File Name: 32_retail_viz.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Online Retail Data. Create sales trend lines, product
#              category charts, and customer analysis visualizations using
#              matplotlib.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create retail DataFrame: InvoiceNo, InvoiceDate, Description, Quantity, UnitPrice, CustomerID, Country
# At least 15 rows with dates
csv_path = Path(__file__).parent / "online_retail.csv"
df = pd.read_csv(csv_path)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Calculate TotalPrice = Quantity * UnitPrice
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print("Online retail data (sample):")
print(df.head())

# --- Line chart: daily total sales (group by date) ---
daily_sales = df.groupby(df["InvoiceDate"].dt.date)["TotalPrice"].sum()

plt.figure(figsize=(8, 5))
plt.plot(daily_sales.index.astype(str), daily_sales.values, marker="o", linestyle="-")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("retail_daily_sales.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Bar chart: top 5 products by quantity sold ---
top5_products = df.groupby("Description")["Quantity"].sum().nlargest(5)

plt.figure(figsize=(8, 5))
plt.bar(top5_products.index, top5_products.values, color="steelblue", edgecolor="black")
plt.title("Top 5 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("retail_top5_products.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Pie chart: sales by country ---
sales_by_country = df.groupby("Country")["TotalPrice"].sum()

plt.figure(figsize=(6, 6))
plt.pie(sales_by_country.values, labels=sales_by_country.index, autopct="%1.1f%%", startangle=90)
plt.title("Sales by Country")
plt.tight_layout()
plt.savefig("retail_pie_country.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Histogram: unit price distribution ---
plt.figure(figsize=(7, 5))
plt.hist(df["UnitPrice"], bins=8, color="coral", edgecolor="black")
plt.title("Unit Price Distribution")
plt.xlabel("Unit Price ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("retail_unitprice_histogram.png", dpi=100, bbox_inches="tight")
plt.show()

print("Plots saved: retail_daily_sales.png, retail_top5_products.png, retail_pie_country.png, retail_unitprice_histogram.png")
