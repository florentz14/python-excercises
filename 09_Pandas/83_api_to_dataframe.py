# -------------------------------------------------
# File Name: 83_api_to_dataframe.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: pd.json_normalize for nested JSON to DataFrame.
# -------------------------------------------------

import pandas as pd

# Nested JSON (typical API response)
data = [
    {
        "id": 1,
        "user": {"name": "Anna", "email": "anna@x.com"},
        "orders": [{"product": "A", "qty": 2}, {"product": "B", "qty": 1}],
    },
    {
        "id": 2,
        "user": {"name": "Bob", "email": "bob@x.com"},
        "orders": [{"product": "A", "qty": 5}],
    },
]

# Flatten top level
df = pd.json_normalize(data)
print("=== json_normalize (flatten nested) ===")
print(df)
print()

# Flatten with separator
df_sep = pd.json_normalize(data, sep="_")
print("=== sep='_' ===")
print(df_sep.columns.tolist())
print()

# Max depth
df_flat = pd.json_normalize(data, max_level=1)
print("=== max_level=1 ===")
print(df_flat)
print()

# Explode list column
df_base = pd.json_normalize(data)
df_exp = df_base.explode("orders").reset_index(drop=True)
orders_df = pd.json_normalize(df_exp["orders"].tolist())
df_exp = pd.concat([df_exp.drop("orders", axis=1).reset_index(drop=True), orders_df], axis=1)
print("=== Explode orders ===")
print(df_exp)
