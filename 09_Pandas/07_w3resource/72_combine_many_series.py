"""W3Resource 72: Combine Many Series to Create a DataFrame."""
import pandas as pd

s1 = pd.Series(["php", "python", "java", "c#", "c++"])
s2 = pd.Series([1, 2, 3, 4, 5])
print("Original Series:")
print(s1)
print(s2)
print("\nCombine above series to a dataframe:")
df = pd.concat([s1, s2], axis=1)
print(df)
print("\nUsing pandas concat:")
df2 = pd.concat([s1, s2], axis=1)
print(df2)
print("\nUsing pandas DataFrame with a dictionary, gives a specific name to the columns:")
df3 = pd.DataFrame({"col1": s1, "col2": s2})
print(df3)
