# -------------------------------------------------
# File Name: 98_value_counts.py
# Description: Frequency counts and percentages
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"color": ["red", "blue", "red", "green", "blue", "red"]})
print("Counts:")
print(df["color"].value_counts())
print("\nWith normalize (percentages):")
print(df["color"].value_counts(normalize=True))
print("\nWith dropna=False:")
print(df["color"].value_counts(dropna=False))
