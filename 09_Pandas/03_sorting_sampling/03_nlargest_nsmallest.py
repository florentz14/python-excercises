# -------------------------------------------------
# File Name: 103_nlargest_nsmallest.py
# Description: Top and bottom records
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"name": ["A", "B", "C", "D", "E"], "score": [85, 92, 78, 95, 88]})
print("Top 2 by score:")
print(df.nlargest(2, "score"))
print("\nBottom 2 by score:")
print(df.nsmallest(2, "score"))
