# -------------------------------------------------
# File Name: 07_columns.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Selects and creates columns in a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame
df = pd.DataFrame({
    "product": ["A", "B", "C"],
    "price": [10, 20, 15],
    "quantity": [2, 3, 1],
})

# create a computed column
df["total"] = df["price"] * df["quantity"]
print("With total column:")
print(df)

# create a new column using the apply function
df["double_price"] = df["price"].apply(lambda x: x * 2)
print("\nWith apply:")
print(df)

# create a new column using the map function
mapping = {"A": "High", "B": "Medium", "C": "Low"}

# create a new column using the map function
df["level"] = df["product"].map(mapping)

# print the DataFrame
print("\nWith map:")
print(df)

# rename the total column to subtotal
df = df.rename(columns={"total": "subtotal"})

# print the DataFrame
print("\nRenamed:")
print(df)
