"""W3Resource 74: Fill Missing Values in Time Series Data."""
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {"c1": [120, 130, 140, 150, np.nan, 170], "c2": [7, np.nan, 10, np.nan, 5.5, 16.5]},
    index=pd.DatetimeIndex(["2000-01-03", "2000-01-04", "2000-01-05", "2000-01-06", "2000-01-07", "2000-01-10"]),
)
print("Original DataFrame:")
print(df)
df = df.interpolate(method="linear")
print("\nDataFrame after interpolate:")
print(df)
