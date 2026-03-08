"""W3Resource 78: Replace Value Based on Last Largest Value."""
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({"rnum": np.random.randint(15, 36, 15)})
print("Original DataFrame:")
print(df)
cummax = df["rnum"].cummax()
df["rnum"] = np.where(df["rnum"] >= cummax, df["rnum"], 0)
print("\nReplace current value in a dataframe column based on last largest value:")
print(df)
