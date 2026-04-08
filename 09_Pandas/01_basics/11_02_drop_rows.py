import pandas as pd


df = pd.DataFrame(
    {
        "a": [1, 2, 2, 3],
        "b": [4, 5, 5, 6],
        "c": [7, 8, 9, 10],
    }
)

df_no_rows = df.drop(index=[0, 1])

print("Without rows 0 and 1:")
print(df_no_rows)
