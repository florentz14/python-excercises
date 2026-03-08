# -------------------------------------------------
# File Name: 11_statistics.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Computes basic statistics on DataFrames.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"value": [10, 20, 30, 40, 50], "other": [1, 2, 3, 4, 5]})

print("Mean:", df["value"].mean())
print("Median:", df["value"].median())
print("Std dev:", df["value"].std())
print("Min:", df["value"].min())
print("Max:", df["value"].max())
print("Quantile 0.5 (median):", df["value"].quantile(0.5))

print("\nCorrelation matrix:\n", df.corr())
