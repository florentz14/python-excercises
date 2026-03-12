# -------------------------------------------------
# File Name: 104_sampling.py
# Description: Random sampling from DataFrame
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"id": range(10), "value": range(10, 20)})
print("Sample n=3:")
print(df.sample(n=3))
print("\nSample frac=0.3:")
print(df.sample(frac=0.3, random_state=42))
