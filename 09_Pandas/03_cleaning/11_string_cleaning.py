# -------------------------------------------------
# File Name: 106_string_cleaning.py
# Description: Clean text columns
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"text": ["  hello  ", "WORLD", "  mixed  CASE  "]})
df["cleaned"] = df["text"].str.strip().str.lower()
print(df)
