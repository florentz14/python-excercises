# -------------------------------------------------
# File Name: 100_astype_and_conversion.py
# Description: Convert column data types safely
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": ["4", "5", "6"], "c": [1.1, 2.2, 3.3]})
print("Original dtypes:", df.dtypes.to_dict())
df["b"] = df["b"].astype(int)
df["c"] = df["c"].astype(int)
print("After astype:", df.dtypes.to_dict())
