import numpy as np
import pandas as pd


np.random.seed(7)
randframe = pd.DataFrame(np.random.randn(1000, 3), columns=["A", "B", "C"])
outliers = randframe[(np.abs(randframe) > 3).any(axis=1)]

print("Outlier count (|z| > 3 approx):")
print(len(outliers))
print("\nSample outliers:")
print(outliers.head().to_string(index=False))
