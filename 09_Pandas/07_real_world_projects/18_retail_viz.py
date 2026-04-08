# -------------------------------------------------
# File Name: 40_retail_viz.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Sales trends, top products, country pie chart for retail data.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create retail DataFrame: InvoiceNo, InvoiceDate, Description, Quantity, UnitPrice, CustomerID, Country
# At least 15 rows with dates
csv_path = Path(__file__).parent.parent / "data" / "online_retail.csv"
df = pd.read_csv(csv_path)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Calculate TotalPrice = Quantity * UnitPrice
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print("Online retail data (sample):")
print(df.head())

# --- Line chart: daily total sales (group by date) ---
daily_sales = (
    df.assign(InvoiceDay=df["InvoiceDate"].dt.date)
    .groupby("InvoiceDay", as_index=False)
    .agg(total_sales=("TotalPrice", "sum"))
)
daily_labels = [str(value) for value in daily_sales["InvoiceDay"]]
daily_values = [float(value) for value in daily_sales["total_sales"]]

plt.figure(figsize=(8, 5))
plt.plot(daily_labels, daily_values, marker="o", linestyle="-")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("retail_daily_sales.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Bar chart: top 5 products by quantity sold ---
quantity_by_product = df.groupby("Description", as_index=False).agg(
    quantity=("Quantity", "sum")
)
top5_rows = sorted(
    quantity_by_product.itertuples(index=False),
    key=lambda row: float(row[1]),
    reverse=True,
)[:5]
top5_products = pd.DataFrame(top5_rows, columns=["Description", "quantity"])
top5_labels = [str(value) for value in top5_products["Description"]]
top5_values = [float(value) for value in top5_products["quantity"]]

plt.figure(figsize=(8, 5))
plt.bar(top5_labels, top5_values, color="steelblue", edgecolor="black")
plt.title("Top 5 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("retail_top5_products.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Pie chart: sales by country ---
sales_by_country = df.groupby("Country", as_index=False).agg(
    total_sales=("TotalPrice", "sum")
)
country_values = [float(value) for value in sales_by_country["total_sales"]]
country_labels = [str(value) for value in sales_by_country["Country"]]

plt.figure(figsize=(6, 6))
plt.pie(country_values, labels=country_labels, autopct="%1.1f%%", startangle=90)
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
