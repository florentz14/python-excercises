import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(5, 4), columns=["A", "B", "C", "D"])
df.index = pd.date_range("2000-01-01", periods=5, freq="D")

print("DataFrame with datetime index:")
print(df)
