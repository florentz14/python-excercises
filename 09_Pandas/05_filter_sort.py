# -------------------------------------------------
# File Name: 05_filter_sort.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Filters rows by condition, sorts by column, and uses nlargest.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary", "Peter"],
    "age": [25, 30, 28, 35],
    "city": ["Madrid", "Barcelona", "Madrid", "Valencia"],
})

# Filter by condition
print("Age >= 28:")
print(df[df["age"] >= 28])

# Multiple conditions (AND)
print("\nAge >= 28 AND city Madrid:")
print(df[(df["age"] >= 28) & (df["city"] == "Madrid")])

# Sort by column
print("\nSorted by age (ascending):")
print(df.sort_values("age"))

# Sort descending
print("\nSorted by age (descending):")
print(df.sort_values("age", ascending=False))

# Top N by value
print("\nTop 2 by age:")
print(df.nlargest(2, "age"))
