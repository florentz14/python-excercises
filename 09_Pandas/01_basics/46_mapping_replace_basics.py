# -------------------------------------------------
# File Name: 46_mapping_replace_basics.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Duplicates, mapping, replace, and index rename.
# -------------------------------------------------

# Import pandas library
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({"item": ["ball", "pencil", "pencil", "ashtray"], "status": [1, 1, 1, 2]})

# Print the original DataFrame
print("=== ORIGINAL DATA ===")
print(df)

# Remove duplicates from the DataFrame
clean_df = df.drop_duplicates()
print("\n=== DROP DUPLICATES ===")
print(clean_df)

# Mapping dictionary into a new column
prices = {"ball": 10, "pencil": 5, "ashtray": 20}
df["price"] = df["item"].map(prices)

# Replace values and rename index labels
df["status"] = df["status"].replace({1: "active", 2: "old"})
df = df.rename(index={0: "first", 1: "second"})

# Print the transformed DataFrame
print("\n=== TRANSFORMED DATA ===")
print(df)