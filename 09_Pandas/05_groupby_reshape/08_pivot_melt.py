# -------------------------------------------------
# File Name: 59_pivot_melt.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: pivot_table, melt, unstack for wide vs long format reshaping.
# -------------------------------------------------

import pandas as pd

# Sample sales: region, product, quarter, sales
df = pd.DataFrame({
    "region": ["North", "North", "South", "South"] * 3,
    "product": ["A", "B", "C"] * 4,
    "quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2", "Q3", "Q3", "Q3", "Q4", "Q4", "Q4"],
    "sales": [100, 120, 90, 110, 130, 95, 105, 125, 88, 115, 135, 92],
})

print("=== ORIGINAL (long format) ===")
print(df)
print()

# pivot_table: rows=region, columns=product, values=sales, aggfunc=sum
pivot = df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")
print("=== PIVOT (wide: region x product) ===")
print(pivot)
print()

# melt: wide -> long (unnamed columns become variable/value)
wide = pd.DataFrame({
    "id": [1, 2],
    "temp_jan": [10, 15],
    "temp_feb": [12, 14],
    "temp_mar": [18, 20],
})
print("=== WIDE DATA (before melt) ===")
print(wide)
long = wide.melt(id_vars="id", var_name="month", value_name="temp")
long["month"] = long["month"].str.replace("temp_", "")
print("=== LONG (after melt) ===")
print(long)
print()

# Unstack equivalent via pivot_table (more type-checker friendly)
by_region_product = df.pivot_table(
    index="region", columns="product", values="sales", aggfunc="sum"
)
print("=== UNSTACK (MultiIndex -> columns) ===")
print(by_region_product)
