from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "chipotle_orders.csv"
df = pd.read_csv(csv_path)
df["item_price"] = df["item_price"].str.replace("$", "", regex=False).astype(float)

print("Query: item_price > 9")
print(df.query("item_price > 9"))
print("\nloc rows 0-4, columns item_name/item_price:")
print(df.loc[0:4, ["item_name", "item_price"]])
print("\niloc first 5 rows, first 3 columns:")
print(df.iloc[0:5, 0:3])
