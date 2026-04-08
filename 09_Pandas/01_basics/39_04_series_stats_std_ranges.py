import pandas as pd


series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean = series.mean()
std = series.std()

within_1std = series[(series >= mean - std) & (series <= mean + std)]
within_2std = series[(series >= mean - 2 * std) & (series <= mean + 2 * std)]

print("Mean and Std interpretation:")
print(f"Mean         : {mean:.4f}")
print(f"Std Dev      : {std:.4f}")
print(f"Mean - 1xStd : {mean - std:.4f}")
print(f"Mean + 1xStd : {mean + std:.4f}")
print(f"Mean - 2xStd : {mean - 2 * std:.4f}")
print(f"Mean + 2xStd : {mean + 2 * std:.4f}")
print()
print(f"Values within 1 Std : {within_1std.tolist()}")
print(f"Values within 2 Std : {within_2std.tolist()}")
print(f"% within 1 Std      : {len(within_1std) / len(series) * 100:.1f}%")
print(f"% within 2 Std      : {len(within_2std) / len(series) * 100:.1f}%")
