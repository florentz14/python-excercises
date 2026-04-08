# -------------------------------------------------
# File Name: 53_sales_analysis_miniproject.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Integrated sales mini-project for cleaning and reporting.
# -------------------------------------------------

import re

import numpy as np
import pandas as pd

# --- PHASE 1: PREPARATION (Loading & Assembling) ---
# Create a DataFrame with the sales data
sales_df = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104, 105, 106, 101],
        "product_id": ["ball", "pencil", "pen", "mug", "ashtray", "laptop", "ball"],
        "qty": [2, 5, 1, 3, 1, 10, 2],
        "customer_email": [
            "juan@mail.com",
            "ana@gmail.com",
            "PEDRO@OUTLOOK.COM",
            "luis@mail.net",
            "marta@mail.com",
            "error_mail",
            "juan@mail.com",
        ],
    }
)

# Create a DataFrame with the prices data
price_df = pd.DataFrame(
    {
        "product_id": ["ball", "pencil", "pen", "mug", "ashtray"],
        "price": [12.50, 1.20, 2.00, 15.00, 5.00],
    }
)

# Keep all sales rows, even if a product is missing from the catalog.
# Merge the sales and prices DataFrames on the product_id column
sales_full = pd.merge(sales_df, price_df, on="product_id", how="left")

# Fill missing prices with emergency defaults using combine_first.
# Create a Series with the emergency prices
fallback_prices = pd.Series(np.nan, index=sales_full.index)
fallback_prices.loc[sales_full["product_id"] == "laptop"] = 500.00
sales_full["price"] = sales_full["price"].fillna(fallback_prices)

# --- PHASE 2: TRANSFORMATION (Cleaning, Mapping & Strings) ---
# Drop the duplicate rows
sales_full = sales_full.drop_duplicates()
sales_full["customer_email"] = sales_full["customer_email"].str.lower().str.strip()

# Create a regex for the email
email_regex = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}")
sales_full["valid_email"] = sales_full["customer_email"].apply(
    lambda value: value if email_regex.fullmatch(value) else np.nan
)

# Create a dictionary with the category mapping
category_map = {
    "ball": "Sports",
    "pencil": "Stationery",
    "pen": "Stationery",
    "mug": "Home",
    "ashtray": "Home",
    "laptop": "Technology",
}
sales_full["category"] = sales_full["product_id"].apply(
    lambda value: category_map.get(str(value), "Other")
)

# Create a new column with the sales volume
sales_full["sales_volume"] = pd.cut(
    sales_full["qty"],
    bins=[0, 2, 5, 20],
    labels=["Low", "Medium", "High"],
)

# --- PHASE 3: AGGREGATION (Aggregation & Reshaping) ---
# Create a new column with the subtotal
sales_full["subtotal"] = sales_full["qty"] * sales_full["price"]
sales_full["category_total"] = sales_full.groupby("category")["subtotal"].transform("sum")
# Create a new column with the weight in category
sales_full["weight_in_category"] = (
    (sales_full["subtotal"] / sales_full["category_total"]) * 100
).round(2)

# Create a new DataFrame with the outlier sales
outlier_sales = sales_full[sales_full["qty"] > 8].copy()

# Create a pivot table with the summary
pivot_summary = (
    sales_full.pivot_table(
        index="category",
        columns="sales_volume",
        values="subtotal",
        aggfunc="sum",
        observed=False,
    )
    .fillna(0)
    .round(2)
)

print("=" * 64)
print("                 MINI-PROJECT: SALES ANALYSIS")
print("=" * 64)

print("\n--- CLEANED AND ENRICHED SALES DATA ---")
print(
    sales_full[
        [
            "order_id",
            "product_id",
            "category",
            "qty",
            "price",
            "sales_volume",
            "subtotal",
            "weight_in_category",
            "valid_email",
        ]
    ].to_string(index=False)
)

print("\n--- OUTLIER SALES (qty > 8) ---")
if outlier_sales.empty:
    print("No outlier sales were detected.")
else:
    outlier_display = pd.DataFrame(
        outlier_sales.loc[:, ["order_id", "product_id", "qty", "subtotal"]]
    )
    print(outlier_display.to_string(index=False))

print("\n--- PERFORMANCE MATRIX (PIVOT) ---")
print(pivot_summary.to_string())

print("\n--- QUICK METRICS ---")
print(f"Final rows: {len(sales_full)}")
print(f"Grand subtotal: ${sales_full['subtotal'].sum():.2f}")
print(f"Valid emails: {sales_full['valid_email'].notna().sum()} / {len(sales_full)}")
