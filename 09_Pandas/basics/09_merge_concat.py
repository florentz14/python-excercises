# ------------------------------------------------------------
# Basic case: Combine DataFrames (merge and concat)
# ------------------------------------------------------------

import pandas as pd

# Merge (join)
df1 = pd.DataFrame({"id": [1, 2], "name": ["Anna", "Louis"]})
df2 = pd.DataFrame({"id": [1, 2], "city": ["Madrid", "Barcelona"]})
merged = pd.merge(df1, df2, on="id")
print("Merge (inner join):\n", merged)

# Concat vertical
df_a = pd.DataFrame({"x": [1, 2]})
df_b = pd.DataFrame({"x": [3, 4]})
concat_v = pd.concat([df_a, df_b], ignore_index=True)
print("\nConcat vertical:\n", concat_v)

# Concat horizontal
df_c = pd.DataFrame({"a": [1, 2]})
df_d = pd.DataFrame({"b": [10, 20]})
concat_h = pd.concat([df_c, df_d], axis=1)
print("\nConcat horizontal:\n", concat_h)
