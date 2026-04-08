from pathlib import Path

import pandas as pd


data_dir = Path(__file__).parent.parent / "data"
df = pd.read_csv(data_dir / "store_sales.csv")

nulls = df.isna().sum()
dup_rows = df.duplicated().sum()

print("Null counts:")
print(nulls[nulls > 0] if nulls.any() else "No nulls")
print("\nDuplicate rows:")
print(dup_rows)
