# -------------------------------------------------
# File Name: 102_idxmax_idxmin.py
# Description: Index of max/min values
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"value": [10, 25, 15, 30, 5]}, index=["a", "b", "c", "d", "e"])
print("idxmax:", df["value"].idxmax())
print("idxmin:", df["value"].idxmin())
