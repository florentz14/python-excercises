# -------------------------------------------------
# File Name: 06_explore.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Explores a DataFrame with head, tail, info, describe, dtypes, and value_counts.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame
df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary", "Peter", "Sara"],
    "age": [25, 30, 28, 35, 22],
    "city": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona"],
})

# print the first 3 rows of the DataFrame
print("First 3 rows (head):")
print(df.head(3))

# print the last 2 rows of the DataFrame
print("\nLast 2 rows (tail):")
print(df.tail(2))

# print the shape of the DataFrame
print("\nShape:", df.shape)

# print the column info of the DataFrame
print("\nColumn info:")
df.info()

# print the dtypes of the DataFrame
print("\nDtypes:")
print(df.dtypes)

# print the statistics of the DataFrame
print("\nStatistics (describe):")
print(df.describe())

# print the unique city values of the DataFrame
print("\nUnique city values:", df["city"].unique().tolist())

# print the count by city of the DataFrame
print("\nCount by city (value_counts):")
print(df["city"].value_counts())
