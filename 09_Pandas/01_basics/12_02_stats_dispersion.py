import pandas as pd


df = pd.DataFrame({"value": [10, 20, 30, 40, 50], "other": [1, 2, 3, 4, 5]})

print("Std dev:", df["value"].std())
print("Min:", df["value"].min())
print("Max:", df["value"].max())
