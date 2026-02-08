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

# Create first DataFrame: property listings (10 rows)
df_listings = pd.DataFrame({
    "property_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "address": [
        "100 Oak St", "200 Pine Ave", "300 Elm Rd", "400 Maple Dr", "500 Cedar Ln",
        "600 Birch St", "700 Spruce Ave", "800 Willow Rd", "900 Ash Dr", "1000 Oak St",
    ],
    "bedrooms": [3, 4, 2, 5, 3, 4, 2, 4, 3, 5],
    "bathrooms": [2, 3, 1, 4, 2, 3, 2, 3, 2, 4],
    "sqft": [1800, 2400, 1200, 3200, 1600, 2200, 1100, 2500, 1900, 3000],
    "price": [350000, 480000, 220000, 620000, 310000, 445000, 195000, 510000, 380000, 590000],
})

# Add neighborhood column to df_listings for merging
df_listings["neighborhood"] = ["Downtown", "Riverside", "Downtown", "Hillside", "Riverside", "Downtown", "Uptown", "Hillside", "Uptown", "Riverside"]

# Create second DataFrame: neighborhood info (6 neighborhoods)
df_neighborhoods = pd.DataFrame({
    "neighborhood": ["Downtown", "Riverside", "Hillside", "Uptown", "Midtown", "Lakeside"],
    "city": ["Springfield", "Springfield", "Springfield", "Springfield", "Springfield", "Springfield"],
    "median_income": [55000, 62000, 85000, 48000, 72000, 78000],
    "crime_rate": [4.2, 2.8, 1.1, 5.0, 2.5, 1.8],
    "school_rating": [7, 8, 9, 6, 8, 9],
})

# Create third DataFrame: sales history (8 rows, some properties sold multiple times)
df_sales = pd.DataFrame({
    "property_id": [101, 102, 103, 105, 106, 107, 108, 108],
    "sale_date": ["2023-01-15", "2023-02-20", "2023-03-10", "2023-04-05", "2023-05-12", "2023-06-01", "2023-07-18", "2022-08-01"],
    "sale_price": [340000, 475000, 215000, 305000, 438000, 190000, 505000, 495000],
    "buyer_type": ["first_time", "investor", "first_time", "first_time", "investor", "first_time", "investor", "investor"],
})

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
