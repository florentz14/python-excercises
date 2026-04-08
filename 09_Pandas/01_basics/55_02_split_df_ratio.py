import numpy as np
import pandas as pd


np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 2))

n = len(df)
train_size = int(0.7 * n)
train_df = df.sample(n=train_size, random_state=42)
test_df = df.drop(train_df.index)

print("70% of the DataFrame:")
print(train_df)
print("\n30% of the DataFrame:")
print(test_df)
