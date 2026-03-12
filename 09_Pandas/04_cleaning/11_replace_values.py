# -------------------------------------------------
# File Name: 105_replace_values.py
# Description: Replace values with scalars, dicts, regex
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3, 2], "y": ["a", "b", "a", "c"]})
print("Replace scalar:", df["x"].replace(2, 99).tolist())
print("Replace dict:", df["y"].replace({"a": "A", "b": "B"}).tolist())
