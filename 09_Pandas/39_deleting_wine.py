# -------------------------------------------------
# File Name: 39_deleting_wine.py
# Author: Florentino Báez
# Date: Pandas
# Description: Delete Rows and Columns from Wine Quality Data. Practice advanced
#              deletion: filtering out outliers, removing columns by dtype, and
#              cleaning data with drop/dropna.
# -------------------------------------------------

import pandas as pd
import numpy as np
from pathlib import Path

# -------------------------------------------------
# Create Wine DataFrame: at least 15 rows, some NaN and some duplicate rows
# -------------------------------------------------
df = pd.read_csv(Path(__file__).parent / "wine_quality.csv")
print("Original Wine DataFrame:")
print(df)
print("Shape:", df.shape)
print()

# -------------------------------------------------
# Drop the wine_type column
# -------------------------------------------------
df1 = df.copy()
df1 = df1.drop(columns=["wine_type"])
print("Step 1 - After dropping 'wine_type':")
print("Shape:", df1.shape)
print(df1.head(3))
print()

# -------------------------------------------------
# Drop all columns with any NaN using dropna(axis=1)
# -------------------------------------------------
df2 = df.copy()
df2 = df2.dropna(axis=1)
print("Step 2 - After dropna(axis=1) (drop columns with any NaN):")
print("Shape:", df2.shape)
print("Columns left:", list(df2.columns))
print()

# -------------------------------------------------
# Drop columns by selecting only numeric columns (select_dtypes)
# -------------------------------------------------
df3 = df.copy()
numeric_only = df3.select_dtypes(include=[np.number])
print("Step 3 - Only numeric columns (select_dtypes):")
print("Shape:", numeric_only.shape)
print("Columns:", list(numeric_only.columns))
print()

# -------------------------------------------------
# Remove rows where quality < 5 (low quality wines)
# -------------------------------------------------
df4 = df.copy()
df4 = df4[df4["quality"] >= 5]
print("Step 4 - After removing rows where quality < 5:")
print("Shape:", df4.shape)
print(df4[["quality", "alcohol"]].head(5))
print()

# -------------------------------------------------
# Remove outliers: drop rows where alcohol > mean + 2*std
# -------------------------------------------------
df5 = df.copy()
alcohol_mean = df5["alcohol"].mean()
alcohol_std = df5["alcohol"].std()
threshold = alcohol_mean + 2 * alcohol_std
df5 = df5[df5["alcohol"] <= threshold]
print("Step 5 - After removing alcohol outliers (alcohol > mean + 2*std):")
print("Alcohol mean:", alcohol_mean, "std:", alcohol_std, "threshold:", threshold)
print("Shape:", df5.shape)
print()

# -------------------------------------------------
# Drop duplicate rows
# -------------------------------------------------
df6 = df.copy()
df6 = df6.drop_duplicates()
print("Step 6 - After drop_duplicates():")
print("Shape:", df6.shape)
print()

# -------------------------------------------------
# Use dropna(subset=['quality']) to drop only rows with NaN in quality
# -------------------------------------------------
df7 = df.copy()
df7 = df7.dropna(subset=["quality"])
print("Step 7 - After dropna(subset=['quality']):")
print("Shape:", df7.shape)
print(df7[["quality"]].head(10))
print()

# -------------------------------------------------
# fillna() vs dropna() comparison (fill NaN with median then show both approaches)
# -------------------------------------------------
df8 = df.copy()
median_quality = df8["quality"].median()
filled = df8.copy()
filled["quality"] = filled["quality"].fillna(median_quality)
dropped = df8.dropna(subset=["quality"])
print("Step 8 - fillna() vs dropna():")
print("Filled with median - rows:", len(filled), "quality sample:", filled["quality"].head(8).tolist())
print("Dropped NaN in quality - rows:", len(dropped))
print()

# -------------------------------------------------
# Chain multiple operations: drop NaN -> drop duplicates -> filter quality >= 5
# -------------------------------------------------
df9 = df.copy()
df9 = df9.dropna().drop_duplicates()
df9 = df9[df9["quality"] >= 5]
print("Step 9 - Chained: dropna() -> drop_duplicates() -> quality >= 5:")
print("Shape:", df9.shape)
print(df9.head(5))
print()

# -------------------------------------------------
# Reset index at the end
# -------------------------------------------------
df_final = df9.reset_index(drop=True)
print("Step 10 - After reset_index(drop=True):")
print("Shape:", df_final.shape)
print(df_final)
