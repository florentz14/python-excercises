import pandas as pd


df = pd.DataFrame(
    {
        "a": [1, 2, 2, 3],
        "b": [4, 5, 5, 6],
        "c": [7, 8, 9, 10],
    }
)

df_no_b = df.drop(columns=["b"])

print("Without column 'b':")
print(df_no_b)
