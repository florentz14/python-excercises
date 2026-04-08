import pandas as pd


series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

q1 = series.quantile(0.25)
q2 = series.quantile(0.50)
q3 = series.quantile(0.75)
iqr = q3 - q1

print("Percentiles:")
print(f"25th Percentile (Q1) : {q1}")
print(f"50th Percentile (Q2) : {q2}")
print(f"75th Percentile (Q3) : {q3}")
print(f"IQR (Q3 - Q1)        : {iqr}")
