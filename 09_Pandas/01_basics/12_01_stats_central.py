import pandas as pd


df = pd.DataFrame({"value": [10, 20, 30, 40, 50], "other": [1, 2, 3, 4, 5]})

print("Mean:", df["value"].mean())
print("Median:", df["value"].median())
