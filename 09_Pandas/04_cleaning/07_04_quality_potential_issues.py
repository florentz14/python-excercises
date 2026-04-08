from pathlib import Path

import numpy as np
import pandas as pd


data_dir = Path(__file__).parent.parent / "data"
df = pd.read_csv(data_dir / "store_sales.csv")

print("Potential issues in numeric columns:")
for col in df.select_dtypes(include=[np.number]).columns:
    zeros = (df[col] == 0).sum()
    negatives = (df[col] < 0).sum()
    if zeros > 0:
        print(f"{col}: {zeros} zeros")
    if negatives > 0:
        print(f"{col}: {negatives} negative values")
