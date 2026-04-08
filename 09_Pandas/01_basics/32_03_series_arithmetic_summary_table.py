import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

add_result = series1 + series2
sub_result = series1 - series2
mul_result = series1 * series2
div_result = series1 / series2
mod_result = series1 % series2
pow_result = series1 ** series2

print(f"{'S1':>5} {'S2':>5} {'Add':>8} {'Sub':>8} {'Mul':>8} {'Div':>8} {'Mod':>5} {'Pow':>12}")
print("-" * 60)
for i in range(len(series1)):
    s1 = series1[i]
    s2 = series2[i]
    print(
        f"{s1:>5} {s2:>5} {add_result[i]:>8} {sub_result[i]:>8} "
        f"{mul_result[i]:>8} {div_result[i]:>8.2f} {mod_result[i]:>5} {pow_result[i]:>12}"
    )
