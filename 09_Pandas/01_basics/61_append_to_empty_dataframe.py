# -------------------------------------------------
# File Name: 61_append_to_empty_dataframe.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 49 append to empty dataframe.
# -------------------------------------------------

"""Practice 49: Append Data to Empty DataFrame."""
import pandas as pd

df_practice_49 = pd.DataFrame()
print("Original DataFrame:")
print(df_practice_49)
df_practice_49 = pd.concat([df_practice_49, pd.DataFrame({"col1": [0, 1, 2], "col2": [0, 1, 2]})], ignore_index=True)
print("\nAfter appending some data:")
print(df_practice_49)
