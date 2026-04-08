import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

eq_result = series1 == series2
neq_result = series1 != series2
gt_result = series1 > series2
lt_result = series1 < series2
gte_result = series1 >= series2
lte_result = series1 <= series2

print("Series 1:", series1.tolist())
print("Series 2:", series2.tolist())
print("\nEqual (==):")
print(eq_result.to_string())
print("\nNot equal (!=):")
print(neq_result.to_string())
print("\nGreater than (>):")
print(gt_result.to_string())
print("\nLess than (<):")
print(lt_result.to_string())
print("\nGreater or equal (>=):")
print(gte_result.to_string())
print("\nLess or equal (<=):")
print(lte_result.to_string())
