# -------------------------------------------------
# File Name: 46_mapping_replace_basics.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Duplicates, mapping, replace, and index rename.
# -------------------------------------------------

import pandas as pd

# Create a DataFrame
data = pd.DataFrame(
    {
        "item": ["ball", "pencil", "pencil", "ashtray"],
        "status": [1, 1, 1, 2],
    }
)

# Print the DataFrame
print("=== ORIGINAL DATA ===")
print(data)

# 1. Remove duplicates (DataFrame)
clean_data = data.drop_duplicates()
print("\n=== DROP DUPLICATES ===")
print(clean_data)

# 2. Mapping dictionary into a new column (DataFrame)
prices = {"ball": 10, "pencil": 5, "ashtray": 20}
data["price"] = data["item"].map(prices)

# 3. Replace values and rename index labels (DataFrame)
data["status"] = data["status"].replace({1: "active", 2: "old"})
data = data.rename(index={0: "first", 1: "second"})

print("\n=== TRANSFORMED DATA ===")
print(data)
