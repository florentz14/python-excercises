import pandas as pd


df = pd.DataFrame(
    {
        "col1": [1, 4, 3, 4, 5],
        "col2": [4, 5, 6, 7, 8],
        "col3": [7, 8, 9, 0, 1],
    }
)

print("Rows for col1 value == 4")
print(df[df["col1"] == 4])
