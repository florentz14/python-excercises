"""W3Resource 45: Row with Maximum Value."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
print("\nRow where col1 has maximum value:")
print(df["col1"].idxmax())
print("Row where col2 has maximum value:")
print(df["col2"].idxmax())
print("Row where col3 has maximum value:")
print(df["col3"].idxmax())
