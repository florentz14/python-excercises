# -------------------------------------------------
# File Name: 100_astype_and_conversion.py
# Description: Convert column data types safely
# -------------------------------------------------

import pandas as pd

# Create a DataFrame with the a, b, and c data
df = pd.DataFrame({"a": [1, 2, 3], "b": ["4", "5", "6"], "c": [1.1, 2.2, 3.3]})
# Print the original dtypes
print("Original dtypes:", df.dtypes.to_dict())
# Convert the b column to int
df["b"] = df["b"].astype(int)
# Convert the c column to int
df["c"] = df["c"].astype(int)
# Print the dtypes after the conversion
print("After astype:", df.dtypes.to_dict())
