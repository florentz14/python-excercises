import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

eq_result = series1 == series2
neq_result = series1 != series2
gt_result = series1 > series2
lt_result = series1 < series2
gte_result = series1 >= series2
lte_result = series1 <= series2

print(f"{'S1':>4} {'S2':>4} {'S1==S2':>8} {'S1!=S2':>8} {'S1>S2':>7} {'S1<S2':>7} {'S1>=S2':>8} {'S1<=S2':>8}")
print("-" * 65)
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
