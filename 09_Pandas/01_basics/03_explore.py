# -------------------------------------------------
# File Name: 03_explore.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Explores a DataFrame with head, tail, info, describe, dtypes, and value_counts.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary", "Peter", "Sara"],
    "age": [25, 30, 28, 35, 22],
    "city": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona"],
})

# Print the first 3 rows of the DataFrame
print("First 3 rows (head):")
print(df.head(3))

# Print the last 2 rows of the DataFrame
print("\nLast 2 rows (tail):")
print(df.tail(2))

# Print the shape of the DataFrame
print("\nShape:", df.shape)

# Print the column info of the DataFrame
print("\nColumn info:")
df.info()

# Print the dtypes of the DataFrame
print("\nDtypes:")
print(df.dtypes)

# Print the statistics of the DataFrame
print("\nStatistics (describe):")
print(df.describe())

# Print the unique city values of the DataFrame
print("\nUnique city values:", df["city"].unique().tolist())

# Print the count by city of the DataFrame
print("\nCount by city (value_counts):")
print(df["city"].value_counts())
