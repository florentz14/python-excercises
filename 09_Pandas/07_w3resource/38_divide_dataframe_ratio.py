"""W3Resource 38: Divide DataFrame by Ratio."""
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 2))
print("Original DataFrame:")
print(df)
n = len(df)
train_size = int(0.7 * n)
train_df = df.sample(n=train_size, random_state=42)
test_df = df.drop(train_df.index)
print("\n70% of the said DataFrame:")
print(train_df)
print("\n30% of the said DataFrame:")
print(test_df)
