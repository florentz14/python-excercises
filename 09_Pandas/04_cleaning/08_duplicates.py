# -------------------------------------------------
# File Name: 99_duplicates.py
# Description: Detect and remove duplicates
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"a": [1, 2, 2, 3, 3, 3], "b": [10, 20, 20, 30, 30, 30]})
print("Duplicated rows:")
print(df.duplicated())
print("\nKeep first, drop duplicates:")
print(df.drop_duplicates())
print("\nDrop duplicates based on column 'a':")
print(df.drop_duplicates(subset=["a"]))
