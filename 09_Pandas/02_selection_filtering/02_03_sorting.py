from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "chipotle_orders.csv"
df = pd.read_csv(csv_path)
df["item_price"] = df["item_price"].str.replace("$", "", regex=False).astype(float)

print("Sort by item_price (descending):")
print(df.sort_values(by="item_price", ascending=False))
print("\nSort by quantity (asc), then item_price (desc):")
print(df.sort_values(by=["quantity", "item_price"], ascending=[True, False]))
