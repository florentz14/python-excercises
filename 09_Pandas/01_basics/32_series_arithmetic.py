# -------------------------------------------------
# File Name: 32_series_arithmetic.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Performs arithmetic operations between two pandas Series.
# -------------------------------------------------

# import libraries
import pandas as pd

# create two Series (int)
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

# print the Series
print("=" * 40)
print("        SERIES ARITHMETIC")
print("=" * 40)
print(f"Series 1 : {series1.tolist()}")
print(f"Series 2 : {series2.tolist()}")
print("=" * 40)

# addition (Series1 + Series2)
add_result = series1 + series2
print("\n+ Addition (Series1 + Series2):")
print(add_result.to_string())

# subtraction (Series1 - Series2)
sub_result = series1 - series2
print("\n- Subtraction (Series1 - Series2):")
print(sub_result.to_string())

# multiplication (Series1 * Series2)
mul_result = series1 * series2
print("\n* Multiplication (Series1 * Series2):")
print(mul_result.to_string())

# division (Series1 / Series2)
div_result = series1 / series2
print("\n/ Division (Series1 / Series2):")
print(div_result.to_string())

# floor division (Series1 // Series2)
floor_result = series1 // series2
print("\n// Floor Division (Series1 // Series2):")
print(floor_result.to_string())

# modulus (Series1 % Series2)
mod_result = series1 % series2
print("\n% Modulus (Series1 % Series2):")
print(mod_result.to_string())

# power (Series1 ** Series2)
pow_result = series1**series2
print("\n** Power (Series1 ** Series2):")
print(pow_result.to_string())

# summary table (print the summary table)
print("\n" + "=" * 60)
print("                   SUMMARY TABLE")
print("=" * 60)
print(f"{'S1':>5} {'S2':>5} {'Add':>8} {'Sub':>8} {'Mul':>8} {'Div':>8} {'Mod':>5} {'Pow':>12}")
print("-" * 60)
# print the summary table
for i in range(len(series1)):
    s1 = series1[i]
    s2 = series2[i]
    print(
        f"{s1:>5} {s2:>5} {add_result[i]:>8} {sub_result[i]:>8} "
        f"{mul_result[i]:>8} {div_result[i]:>8.2f} {mod_result[i]:>5} {pow_result[i]:>12}"
    )
print("=" * 60)

# Using built-in Pandas methods (Series1.add(Series2), Series1.sub(Series2), Series1.mul(Series2), Series1.div(Series2), Series1.floordiv(Series2), Series1.mod(Series2), Series1.pow(Series2))
print("\n-- Using Pandas Built-in Methods --")
print(f"series1.add(series2)      : {series1.add(series2).tolist()}")
print(f"series1.sub(series2)      : {series1.sub(series2).tolist()}")
print(f"series1.mul(series2)      : {series1.mul(series2).tolist()}")
print(f"series1.div(series2)      : {[round(x, 2) for x in series1.div(series2).tolist()]}")
print(f"series1.floordiv(series2) : {series1.floordiv(series2).tolist()}")
print(f"series1.mod(series2)      : {series1.mod(series2).tolist()}")
print(f"series1.pow(series2)      : {series1.pow(series2).tolist()}")
