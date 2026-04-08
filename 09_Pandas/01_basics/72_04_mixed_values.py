import pandas as pd


df = pd.DataFrame(
    {
        "A": [0, 1, 2, 3, 4],
        "B": [0, 1, 0, 1, 0],
        "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
        "D": pd.date_range("2009-01-01", periods=5, freq="D"),
    }
)

print("DataFrame with mixed values:")
print(df)
