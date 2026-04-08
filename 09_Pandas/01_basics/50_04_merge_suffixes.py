import pandas as pd


left_df = pd.DataFrame({"id": [1, 2, 3], "value": [10, 20, 30]})
right_df = pd.DataFrame({"id": [1, 2, 4], "value": [100, 200, 400]})

merged_suffix = pd.merge(left_df, right_df, on="id", suffixes=("_left", "_right"))

print("Merge with suffixes:")
print(merged_suffix)
