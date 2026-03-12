# -------------------------------------------------
# File Name: 12_statistics.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Computes basic statistics on DataFrames.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the value and other columns
df = pd.DataFrame({"value": [10, 20, 30, 40, 50], "other": [1, 2, 3, 4, 5]})

# print the mean of the value column
print("Mean:", df["value"].mean())
# print the median of the value column
print("Median:", df["value"].median())
# print the standard deviation of the value column
print("Std dev:", df["value"].std())
# print the minimum value of the value column
print("Min:", df["value"].min())
# print the maximum value of the value column
print("Max:", df["value"].max())
# print the quantile 0.5 (median) of the value column
print("Quantile 0.5 (median):", df["value"].quantile(0.5))

# print the correlation matrix
print("\nCorrelation matrix:\n", df.corr())
