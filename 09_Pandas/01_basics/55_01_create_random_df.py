import numpy as np
import pandas as pd


np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 2))

print("Original DataFrame:")
print(df)
