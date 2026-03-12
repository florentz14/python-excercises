# -------------------------------------------------
# File Name: 39_series_statistics.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Computes descriptive statistics for a pandas Series.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a pandas Series (int)
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print the Series
print("=" * 45)
print("         SERIES STATISTICS")
print("=" * 45)
print(f"Series Data : {series.tolist()}")
print("=" * 45)

# mean (series.mean())
mean = series.mean()
print(f"\nMean                 : {mean}")

# standard deviation (series.std())
std = series.std()
print(f"Standard Deviation   : {std:.6f}")

# variance (series.var())
variance = series.var()
print(f"Variance             : {variance:.6f}")

# median (series.median())
median = series.median()
print(f"Median               : {median}")

# mode (series.mode())
mode = series.mode()
print(f"Mode                 : {mode.tolist()}")

# min & max (series.min(), series.max())
print(f"Minimum              : {series.min()}")
print(f"Maximum              : {series.max()}")

# sum & product (series.sum(), series.prod())
print(f"Sum                  : {series.sum()}")
print(f"Product              : {series.prod()}")

# count & size (series.count(), series.size)
print(f"Count                : {series.count()}")
print(f"Size                 : {series.size}")

# percentiles (series.quantile(0.25), series.quantile(0.50), series.quantile(0.75))
print("\n-- Percentiles ----------------------------")
print(f"  25th Percentile (Q1) : {series.quantile(0.25)}")
print(f"  50th Percentile (Q2) : {series.quantile(0.50)}")
print(f"  75th Percentile (Q3) : {series.quantile(0.75)}")
iqr = series.quantile(0.75) - series.quantile(0.25)
print(f"  IQR (Q3 - Q1)        : {iqr}")

# skewness & kurtosis (series.skew(), series.kurt())
print("\n-- Distribution Shape ---------------------")
print(f"  Skewness             : {series.skew():.6f}")
print(f"  Kurtosis             : {series.kurt():.6f}")

# describe() summary
print("\n-- describe() Full Statistical Summary ----")
print(series.describe())

# mean vs std interpretation
print("\n-- Mean and Std Interpretation ------------")
print(f"  Mean                 : {mean:.4f}")
print(f"  Std Dev              : {std:.4f}")
print(f"  Mean - 1xStd         : {mean - std:.4f}")
print(f"  Mean + 1xStd         : {mean + std:.4f}")
print(f"  Mean - 2xStd         : {mean - 2 * std:.4f}")
print(f"  Mean + 2xStd         : {mean + 2 * std:.4f}")

# values within 1 std and 2 std (series[(series >= mean - std) & (series <= mean + std)], series[(series >= mean - 2 * std) & (series <= mean + 2 * std)])
within_1std = series[(series >= mean - std) & (series <= mean + std)]
# values within 2 std (series[(series >= mean - 2 * std) & (series <= mean + 2 * std)])
within_2std = series[(series >= mean - 2 * std) & (series <= mean + 2 * std)]
# print the values within 1 std and 2 std
print(f"\n  Values within 1 Std  : {within_1std.tolist()}")
print(f"  Values within 2 Std  : {within_2std.tolist()}")
# print the percentage of values within 1 std and 2 std
print(f"  % within 1 Std       : {len(within_1std) / len(series) * 100:.1f}%")
print(f"  % within 2 Std       : {len(within_2std) / len(series) * 100:.1f}%")
print("=" * 45)
