# -------------------------------------------------
# File Name: 38_iris_delete.py
# Author: Florentino Báez
# Date: Pandas
# Description: Delete Rows and Columns from the Iris Dataset. Practice drop(),
#              dropna(), del, pop(), and conditional deletion on the classic
#              Iris flower dataset.
# -------------------------------------------------

import pandas as pd
import numpy as np
from pathlib import Path

# -------------------------------------------------
# Create Iris DataFrame with at least 15 rows, 3 species, some NaN values
# -------------------------------------------------
df = pd.read_csv(Path(__file__).parent / "iris.csv")
print("Original Iris DataFrame:")
print(df)
print("Shape before any deletion:", df.shape)
print()

# -------------------------------------------------
# Drop a single column using drop(columns=...)
# -------------------------------------------------
df1 = df.copy()
df1 = df1.drop(columns=["sepal_width"])
print("After dropping column 'sepal_width':")
print(df1.head(3))
print("Shape:", df1.shape)
print()

# -------------------------------------------------
# Drop multiple columns
# -------------------------------------------------
df2 = df.copy()
df2 = df2.drop(columns=["sepal_width", "petal_width"])
print("After dropping 'sepal_width' and 'petal_width':")
print(df2.head(3))
print("Shape:", df2.shape)
print()

# -------------------------------------------------
# Delete a column using del df['col']
# -------------------------------------------------
df3 = df.copy()
del df3["sepal_width"]
print("After del df['sepal_width']:")
print(df3.head(3))
print("Shape:", df3.shape)
print()

# -------------------------------------------------
# Remove a column using pop() and capture it
# -------------------------------------------------
df4 = df.copy()
popped = df4.pop("petal_width")
print("Popped column (first 5 values):", list(popped.head()))
print("DataFrame after pop (first 3 rows):")
print(df4.head(3))
print("Shape:", df4.shape)
print()

# -------------------------------------------------
# Drop rows by index using drop(index=...)
# -------------------------------------------------
df5 = df.copy()
df5 = df5.drop(index=[0, 2, 4])
print("After dropping rows with index 0, 2, 4:")
print(df5.head(5))
print("Shape:", df5.shape)
print()

# -------------------------------------------------
# Drop rows where species == 'setosa'
# -------------------------------------------------
df6 = df.copy()
df6 = df6[df6["species"] != "setosa"]
print("After dropping rows where species == 'setosa':")
print(df6)
print("Shape:", df6.shape)
print()

# -------------------------------------------------
# Use dropna() to remove rows with any NaN
# -------------------------------------------------
df7 = df.copy()
before_na = df7.shape[0]
df7 = df7.dropna()
print("After dropna() (remove rows with any NaN):")
print("Rows before:", before_na, "Rows after:", len(df7))
print(df7)
print("Shape:", df7.shape)
print()

# -------------------------------------------------
# Use dropna(thresh=...) to keep rows with at least N non-null values
# -------------------------------------------------
df8 = df.copy()
df8 = df8.dropna(thresh=4)
print("After dropna(thresh=4) (keep rows with at least 4 non-null):")
print(df8)
print("Shape:", df8.shape)
print()

# -------------------------------------------------
# Drop duplicate rows using drop_duplicates()
# -------------------------------------------------
df9 = df.copy()
df9 = df9.drop_duplicates()
print("After drop_duplicates():")
print("Shape:", df9.shape)
print()

# -------------------------------------------------
# Drop rows based on condition (e.g., petal_length < 1.0)
# -------------------------------------------------
df10 = df.copy()
df10 = df10[df10["petal_length"] >= 1.0]
print("After dropping rows where petal_length < 1.0:")
print(df10)
print("Shape:", df10.shape)
print()

# -------------------------------------------------
# Reset index after dropping rows
# -------------------------------------------------
df_reset = df6.reset_index(drop=True)
print("After reset_index(drop=True) on filtered DataFrame:")
print(df_reset.head(5))
print("Shape:", df_reset.shape)
