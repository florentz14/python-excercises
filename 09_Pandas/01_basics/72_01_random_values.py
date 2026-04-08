import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(5, 4), columns=["A", "B", "C", "D"])
df.index = ["".join(np.random.choice(list("abcdefghij"), 10)) for _ in range(5)]

print("DataFrame with random values:")
print(df)
