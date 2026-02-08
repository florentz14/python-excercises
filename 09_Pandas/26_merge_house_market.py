# -------------------------------------------------
# File Name: 26_merge_house_market.py
# Author: Florentino Báez
# Date: Pandas
# Description: Merge House Market Datasets. Practice merging property listings
#              with neighborhood data and sales history using different join
#              strategies.
# -------------------------------------------------

import pandas as pd
import numpy as np
from pathlib import Path

df_listings = pd.read_csv(Path(__file__).parent / "house_listings.csv")
df_neighborhoods = pd.read_csv(Path(__file__).parent / "house_neighborhoods.csv")
df_sales = pd.read_csv(Path(__file__).parent / "house_sales.csv")

print("=" * 60)
print("DF_LISTINGS (with neighborhood)")
print("=" * 60)
print(df_listings)
print()
print("DF_NEIGHBORHOODS")
print("=" * 60)
print(df_neighborhoods)
print()
print("DF_SALES")
print("=" * 60)
print(df_sales)
print()

# Merge listings with neighborhoods on neighborhood column
listings_with_neighborhood = pd.merge(df_listings, df_neighborhoods, on="neighborhood", how="left")
print("Listings merged with neighborhoods (left):")
print(listings_with_neighborhood)
print()

# Merge with sales history on property_id (left merge to keep all listings)
# First aggregate sales to one row per property (e.g. latest sale) for a simple merge demo
listings_with_sales = pd.merge(df_listings, df_sales, on="property_id", how="left")
print("Listings merged with sales (left - all listings kept, multiple rows if multiple sales):")
print(listings_with_sales)
print()

# Left merge keeps all listings; those without sales have NaN in sale columns
print("Shape of listings_with_sales:", listings_with_sales.shape)
print()

# Calculate price difference (listing price vs sale price) where sale exists
listings_with_sales["price_difference"] = listings_with_sales["sale_price"] - listings_with_sales["price"]
print("Price difference (sale_price - listing price):")
print(listings_with_sales[["property_id", "address", "price", "sale_price", "price_difference"]])
print()

# Group merged data by neighborhood: merge listings with neighborhoods first, then aggregate
full = pd.merge(df_listings, df_neighborhoods, on="neighborhood", how="left")
avg_price_by_neighborhood = full.groupby("neighborhood")["price"].mean()
print("Average listing price by neighborhood:")
print(avg_price_by_neighborhood)
print()

# Find properties that have not sold (NaN in sale columns after left merge)
no_sale = listings_with_sales[listings_with_sales["sale_date"].isna()]
print("Properties that have not sold (NaN in sale columns):")
print(no_sale[["property_id", "address", "price"]])
