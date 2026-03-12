# -------------------------------------------------
# File Name: 114_rank.py
# Description: Ranking values
# -------------------------------------------------

import pandas as pd

s = pd.Series([3, 1, 4, 1, 5])
print("Default (average for ties):", s.rank().tolist())
print("min:", s.rank(method="min").tolist())
print("dense:", s.rank(method="dense").tolist())
