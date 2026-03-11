# -------------------------------------------------
# File Name: 21_series_comparison.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Compares two pandas Series with relational operators and methods.
# -------------------------------------------------

import pandas as pd

# Create two Pandas Series (int)
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

# Print the Series
print("=" * 45)
print("        SERIES COMPARISON")
print("=" * 45)
print(f"Series 1 : {series1.tolist()}")
print(f"Series 2 : {series2.tolist()}")
print("=" * 45)

# Equal To (Series1 == Series2)
eq_result = series1 == series2
print("\n== Equal To (Series1 == Series2):")
print(eq_result.to_string())

# Not Equal To (Series1 != Series2)
neq_result = series1 != series2
print("\n!= Not Equal To (Series1 != Series2):")
print(neq_result.to_string())

# Greater Than (Series1 > Series2)
gt_result = series1 > series2
print("\n>  Greater Than (Series1 > Series2):")
print(gt_result.to_string())

# Less Than (Series1 < Series2)
lt_result = series1 < series2
print("\n<  Less Than (Series1 < Series2):")
print(lt_result.to_string())

# Greater Than or Equal To (Series1 >= Series2)
gte_result = series1 >= series2
print("\n>= Greater Than or Equal To (Series1 >= Series2):")
print(gte_result.to_string())

# Less Than or Equal To (Series1 <= Series2)
lte_result = series1 <= series2
print("\n<= Less Than or Equal To (Series1 <= Series2):")
print(lte_result.to_string())

# Using Pandas Built-in Methods (Series1.eq(Series2), Series1.ne(Series2), Series1.gt(Series2), Series1.lt(Series2), Series1.ge(Series2), Series1.le(Series2))
print("\n" + "=" * 45)
print("   Using Pandas Built-in Methods")
print("=" * 45)
print(f"series1.eq(series2)  : {series1.eq(series2).tolist()}")
print(f"series1.ne(series2)  : {series1.ne(series2).tolist()}")
print(f"series1.gt(series2)  : {series1.gt(series2).tolist()}")
print(f"series1.lt(series2)  : {series1.lt(series2).tolist()}")
print(f"series1.ge(series2)  : {series1.ge(series2).tolist()}")
print(f"series1.le(series2)  : {series1.le(series2).tolist()}")

# Summary Table (print the summary table)
print("\n" + "=" * 65)
print("                     SUMMARY TABLE")
print("=" * 65)
print(
    f"{'S1':>4} {'S2':>4} {'S1==S2':>8} {'S1!=S2':>8} "
    f"{'S1>S2':>7} {'S1<S2':>7} {'S1>=S2':>8} {'S1<=S2':>8}"
)
print("-" * 65)
# Print the summary table
for i in range(len(series1)):
    s1 = series1[i]
    s2 = series2[i]
    print(
        f"{s1:>4} {s2:>4} "
        f"{str(eq_result[i]):>8} "
        f"{str(neq_result[i]):>8} "
        f"{str(gt_result[i]):>7} "
        f"{str(lt_result[i]):>7} "
        f"{str(gte_result[i]):>8} "
        f"{str(lte_result[i]):>8}"
    )
print("=" * 65)

# Filtered Values Based on Comparison (Series1[eq_result], Series1[gt_result], Series1[lt_result], Series1[gte_result], Series1[lte_result])
print("\n-- Filtered Values Based on Comparison --")
print(f"Elements where S1 == S2 : {series1[eq_result].tolist()}")
print(f"Elements where S1 >  S2 : {series1[gt_result].tolist()}")
print(f"Elements where S1 <  S2 : {series1[lt_result].tolist()}")
print(f"Elements where S1 >= S2 : {series1[gte_result].tolist()}")
print(f"Elements where S1 <= S2 : {series1[lte_result].tolist()}")
