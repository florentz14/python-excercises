# -------------------------------------------------
# File Name: 24_series_statistics.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Computes descriptive statistics for a pandas Series.
# -------------------------------------------------

import pandas as pd

# Create a Pandas Series (int)
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the Series
print("=" * 45)
print("         SERIES STATISTICS")
print("=" * 45)
print(f"Series Data : {series.tolist()}")
print("=" * 45)

# Mean (series.mean())
mean = series.mean()
print(f"\nMean                 : {mean}")

# Standard Deviation (series.std())
std = series.std()
print(f"Standard Deviation   : {std:.6f}")

# Variance (series.var())
variance = series.var()
print(f"Variance             : {variance:.6f}")

# Median (series.median())
median = series.median()
print(f"Median               : {median}")

# Mode (series.mode())
mode = series.mode()
print(f"Mode                 : {mode.tolist()}")

# Min & Max (series.min(), series.max())
print(f"Minimum              : {series.min()}")
print(f"Maximum              : {series.max()}")

# Sum & Product (series.sum(), series.prod())
print(f"Sum                  : {series.sum()}")
print(f"Product              : {series.prod()}")

# Count & Size (series.count(), series.size)
print(f"Count                : {series.count()}")
print(f"Size                 : {series.size}")

# Percentiles (series.quantile(0.25), series.quantile(0.50), series.quantile(0.75))
print("\n-- Percentiles ----------------------------")
print(f"  25th Percentile (Q1) : {series.quantile(0.25)}")
print(f"  50th Percentile (Q2) : {series.quantile(0.50)}")
print(f"  75th Percentile (Q3) : {series.quantile(0.75)}")
iqr = series.quantile(0.75) - series.quantile(0.25)
print(f"  IQR (Q3 - Q1)        : {iqr}")

# Skewness & Kurtosis (series.skew(), series.kurt())
print("\n-- Distribution Shape ---------------------")
print(f"  Skewness             : {series.skew():.6f}")
print(f"  Kurtosis             : {series.kurt():.6f}")

# describe() Summary
print("\n-- describe() Full Statistical Summary ----")
print(series.describe())

# Mean vs Std Interpretation
print("\n-- Mean and Std Interpretation ------------")
print(f"  Mean                 : {mean:.4f}")
print(f"  Std Dev              : {std:.4f}")
print(f"  Mean - 1xStd         : {mean - std:.4f}")
print(f"  Mean + 1xStd         : {mean + std:.4f}")
print(f"  Mean - 2xStd         : {mean - 2 * std:.4f}")
print(f"  Mean + 2xStd         : {mean + 2 * std:.4f}")

# Values within 1 Std and 2 Std (series[(series >= mean - std) & (series <= mean + std)], series[(series >= mean - 2 * std) & (series <= mean + 2 * std)])
within_1std = series[(series >= mean - std) & (series <= mean + std)]
# Values within 2 Std (series[(series >= mean - 2 * std) & (series <= mean + 2 * std)])
within_2std = series[(series >= mean - 2 * std) & (series <= mean + 2 * std)]
# Print the values within 1 Std and 2 Std
print(f"\n  Values within 1 Std  : {within_1std.tolist()}")
print(f"  Values within 2 Std  : {within_2std.tolist()}")
# Print the percentage of values within 1 Std and 2 Std
print(f"  % within 1 Std       : {len(within_1std) / len(series) * 100:.1f}%")
print(f"  % within 2 Std       : {len(within_2std) / len(series) * 100:.1f}%")
print("=" * 45)
