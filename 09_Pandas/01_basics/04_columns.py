# -------------------------------------------------
# File Name: 06_columns.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Selects and creates columns in a DataFrame.
# -------------------------------------------------

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "product": ["A", "B", "C"],
    "price": [10, 20, 15],
    "quantity": [2, 3, 1],
})

# Create a computed column
df["total"] = df["price"] * df["quantity"]
print("With total column:")
print(df)

# Create a new column using the apply function
df["double_price"] = df["price"].apply(lambda x: x * 2)
print("\nWith apply:")
print(df)

# Create a new column using the map function
mapping = {"A": "High", "B": "Medium", "C": "Low"}
df["level"] = df["product"].map(mapping)
print("\nWith map:")
print(df)

# Rename the total column to subtotal
df = df.rename(columns={"total": "subtotal"})
print("\nRenamed:")
print(df)
