# -------------------------------------------------
# File Name: 101_elementwise_transform.py
# Description: Elementwise transformations with apply and map
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
df["sum"] = df.apply(lambda row: row["x"] + row["y"], axis=1)
df["x_squared"] = df["x"].map(lambda v: v * v)
print(df)
