"""W3Resource 44: DataFrame from NumPy Array."""
import pandas as pd
import numpy as np

arr = np.zeros((15, 3))
column_names = ["Column1", "Column2", "Column3"]
index_labels = [f"Index{i}" for i in range(1, 16)]
df = pd.DataFrame(arr, index=index_labels, columns=column_names)
print(df)
