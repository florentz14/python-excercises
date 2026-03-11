# -------------------------------------------------
# File Name: 98_value_counts.py
# Description: Frequency counts and percentages
# -------------------------------------------------

import pandas as pd

# Create a DataFrame with the color data
df = pd.DataFrame({"color": ["red", "blue", "red", "green", "blue", "red"]})
# Print the counts of the color column
print("Counts:")
# Print the counts of the color column with normalize=True (percentages)
print(df["color"].value_counts())
print("\nWith normalize (percentages):")
print(df["color"].value_counts(normalize=True))
print("\nWith dropna=False:")
print(df["color"].value_counts(dropna=False))
