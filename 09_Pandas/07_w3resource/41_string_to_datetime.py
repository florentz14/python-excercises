"""W3Resource 41: String to Datetime."""
import pandas as pd

s = pd.Series(["3/11/2000", "3/12/2000", "3/13/2000"])
print("String Date:")
print(s)
df = pd.DataFrame(pd.to_datetime(s))
print("\nOriginal DataFrame (string to datetime):")
print(df)
