# ------------------------------------------------------------
# Basic case: Create and modify columns
# ------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C"],
    "price": [10, 20, 15],
    "quantity": [2, 3, 1],
})

# Computed column
df["total"] = df["price"] * df["quantity"]
print("With total column:")
print(df)

# apply: apply function per row
df["double_price"] = df["price"].apply(lambda x: x * 2)
print("\nWith apply:")
print(df)

# map: replace values
mapping = {"A": "High", "B": "Medium", "C": "Low"}
df["level"] = df["product"].map(mapping)
print("\nWith map:")
print(df)

# Rename columns
df = df.rename(columns={"total": "subtotal"})
print("\nRenamed:")
print(df)
