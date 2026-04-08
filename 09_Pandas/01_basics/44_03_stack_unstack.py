import numpy as np
import pandas as pd


df1 = pd.DataFrame({"a": [1, np.nan, 5, np.nan], "b": [np.nan, 2, np.nan, 6]})
stacked = df1.stack()
unstacked = stacked.unstack()

print("STACKED:")
print(stacked)
print("\nUNSTACKED:")
print(unstacked)
