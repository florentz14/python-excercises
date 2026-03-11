# -------------------------------------------------
# File Name: 11_statistics.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Computes basic statistics on DataFrames.
# -------------------------------------------------

import pandas as pd

# Create a DataFrame with the value and other columns
df = pd.DataFrame({"value": [10, 20, 30, 40, 50], "other": [1, 2, 3, 4, 5]})

# Print the mean of the value column
print("Mean:", df["value"].mean())
# Print the median of the value column
print("Median:", df["value"].median())
# Print the standard deviation of the value column
print("Std dev:", df["value"].std())
# Print the minimum value of the value column
print("Min:", df["value"].min())
# Print the maximum value of the value column
print("Max:", df["value"].max())
# Print the quantile 0.5 (median) of the value column
print("Quantile 0.5 (median):", df["value"].quantile(0.5))

# Print the correlation matrix
print("\nCorrelation matrix:\n", df.corr())
