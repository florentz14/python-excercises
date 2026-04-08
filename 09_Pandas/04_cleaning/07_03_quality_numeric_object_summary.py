from pathlib import Path

import numpy as np
import pandas as pd


data_dir = Path(__file__).parent.parent / "data"
df = pd.read_csv(data_dir / "store_sales.csv")

print("Numeric summary:")
print(df.select_dtypes(include=[np.number]).describe())

obj_cols = df.select_dtypes(include="object").columns
if len(obj_cols) > 0:
    print("\nUnique counts (object columns):")
    for col in obj_cols:
        print(f"{col}: {df[col].nunique()} unique")
