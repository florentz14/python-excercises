# -------------------------------------------------
# File Name: 09_merge_concat.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Merges and concatenates DataFrames.
# -------------------------------------------------

import pandas as pd

# Merge (join)
df1 = pd.DataFrame({"id": [1, 2], "name": ["Anna", "Louis"]})
    
# Create a DataFrame with the city data
df2 = pd.DataFrame({"id": [1, 2], "city": ["Madrid", "Barcelona"]})

# Merge the df1 and df2 DataFrames on the id column
merged = pd.merge(df1, df2, on="id")
print("Merge (inner join):\n", merged)

# Concat vertical (concatenate the rows of the two DataFrames)
# Create a DataFrame with the x data
df_a = pd.DataFrame({"x": [1, 2]})
# Create a DataFrame with the x data
df_b = pd.DataFrame({"x": [3, 4]})
# Concatenate the rows of the two DataFrames
concat_v = pd.concat([df_a, df_b], ignore_index=True)
print("\nConcat vertical:\n", concat_v)

# Concat horizontal (concatenate the columns of the two DataFrames)
# Create a DataFrame with the a data
df_c = pd.DataFrame({"a": [1, 2]})
# Create a DataFrame with the b data
df_d = pd.DataFrame({"b": [10, 20]})
# Concatenate the columns of the two DataFrames
concat_h = pd.concat([df_c, df_d], axis=1)
print("\nConcat horizontal:\n", concat_h)
