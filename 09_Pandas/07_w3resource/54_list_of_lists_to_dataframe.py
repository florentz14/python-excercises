"""W3Resource 54: Convert List of Lists into DataFrame."""
import pandas as pd

data = [[2, 4], [1, 3]]
print("Original list of lists:")
print(data)
df = pd.DataFrame(data, columns=["col1", "col2"])
print("\nNew DataFrame")
print(df)
