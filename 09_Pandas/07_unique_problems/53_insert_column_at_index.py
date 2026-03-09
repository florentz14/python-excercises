# -------------------------------------------------
# File Name: 53_insert_column_at_index.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 53 insert column at index.
# -------------------------------------------------

"""Practice 53: Insert Column at Specific Index."""
import pandas as pd

df_practice_53 = pd.DataFrame({"col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]})
print("Original DataFrame")
print(df_practice_53)
col1 = pd.Series([1, 2, 3, 4, 7])
df_practice_53.insert(0, "col1", col1)
print("\nNew DataFrame")
print(df_practice_53)
