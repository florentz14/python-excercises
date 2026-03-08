# -------------------------------------------------
# File Name: 110_crosstab.py
# Description: Cross-tabulation tables
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"A": ["X", "X", "Y", "Y"], "B": [1, 2, 1, 2], "count": [10, 20, 15, 25]})
ct = pd.crosstab(df["A"], df["B"], values=df["count"], aggfunc="sum")
print(ct)
