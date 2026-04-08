import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

eq_result = series1 == series2
gt_result = series1 > series2
lt_result = series1 < series2
gte_result = series1 >= series2
lte_result = series1 <= series2

print("Filtered values based on comparison:")
print(f"Elements where S1 == S2 : {series1[eq_result].tolist()}")
print(f"Elements where S1 >  S2 : {series1[gt_result].tolist()}")
print(f"Elements where S1 <  S2 : {series1[lt_result].tolist()}")
print(f"Elements where S1 >= S2 : {series1[gte_result].tolist()}")
print(f"Elements where S1 <= S2 : {series1[lte_result].tolist()}")
