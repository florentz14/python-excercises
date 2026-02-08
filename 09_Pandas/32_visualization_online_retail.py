# -------------------------------------------------
# File Name: 32_visualization_online_retail.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Online Retail Data. Create sales trend lines, product
#              category charts, and customer analysis visualizations using
#              matplotlib.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Create retail DataFrame: InvoiceNo, InvoiceDate, Description, Quantity, UnitPrice, CustomerID, Country
# At least 15 rows with dates
data = {
    "InvoiceNo": ["1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010",
                  "1011", "1012", "1013", "1014", "1015", "1016"],
    "InvoiceDate": pd.to_datetime([
        "2024-01-02", "2024-01-02", "2024-01-03", "2024-01-03", "2024-01-05",
        "2024-01-05", "2024-01-07", "2024-01-07", "2024-01-08", "2024-01-10",
        "2024-01-10", "2024-01-12", "2024-01-12", "2024-01-14", "2024-01-14", "2024-01-15"
    ]),
    "Description": [
        "Whiteboard Markers", "Stapler", "Notebook A4", "Pen Pack", "Desk Lamp",
        "Whiteboard Markers", "Notebook A4", "Stapler", "Pen Pack", "Desk Lamp",
        "Notebook A4", "Whiteboard Markers", "Stapler", "Pen Pack", "Desk Lamp", "Notebook A4"
    ],
    "Quantity": [2, 1, 5, 3, 1, 4, 2, 2, 6, 1, 3, 2, 1, 4, 2, 2],
    "UnitPrice": [3.50, 12.00, 4.25, 8.00, 25.00, 3.50, 4.25, 12.00, 8.00, 25.00, 4.25, 3.50, 12.00, 8.00, 25.00, 4.25],
    "CustomerID": [101, 102, 101, 103, 104, 102, 105, 103, 101, 104, 106, 102, 103, 105, 104, 106],
    "Country": ["UK", "Germany", "UK", "France", "UK", "Germany", "France", "Germany", "UK", "UK", "France", "Germany", "France", "France", "UK", "Germany"]
}

df = pd.DataFrame(data)

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
