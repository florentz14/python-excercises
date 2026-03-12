# -------------------------------------------------
# File Name: 109_where_mask.py
# Description: Conditional replacement with where/mask
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"x": [1, -2, 3, -4, 5]})
print("where: keep where cond True, else replace:")
print(df["x"].where(df["x"] > 0, 0))
print("\nmask: replace where cond True:")
print(df["x"].mask(df["x"] < 0, -df["x"]))
