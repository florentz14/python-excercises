# -------------------------------------------------
# File Name: 107_to_numeric.py
# Description: Convert object columns to numeric
# -------------------------------------------------

import pandas as pd

s = pd.Series(["1", "2", "invalid", "4"])
print("to_numeric with errors='coerce':")
print(pd.to_numeric(s, errors="coerce"))
